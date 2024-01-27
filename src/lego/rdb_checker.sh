#!/bin/bash
cx=$(date +%s -r dump.rdb)
cy=$(date +%s)
echo $(($cy - $cx))
# so white space is still some great element here, at least used by bash.
# what do you mean by that? human can make mistakes.
