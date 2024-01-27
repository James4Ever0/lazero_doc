#!/bin/bash
ls | grep cpp | grep -Eo "^[^\.]+" | xargs -I % gcc %.cpp -o % 
