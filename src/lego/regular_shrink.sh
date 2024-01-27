#!/bin/bash
# fuck! store it later.
# will you store working script somewhere?
cat judger.log | python3 shrink.py > judger_shrink.log
mv judger_shrink.log judger.log
