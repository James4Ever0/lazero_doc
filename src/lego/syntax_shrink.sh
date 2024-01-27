#!/bin/bash
# fuck! store it later.
# will you store working script somewhere?
cat syntax.log | python3 shrink.py > syntax_shrink.log
mv syntax_shrink.log syntax.log
