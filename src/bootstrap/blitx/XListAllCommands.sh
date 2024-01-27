#!/bin/bash
function ListAllCommands
{
    echo -n $PATH | xargs -d : -I {} find {} -maxdepth 1 \
        -executable -type f -printf '%P\n' | sort -u
}
ListAllCommands
