#!/bin/bash
#curl -k "https://localhost:5001/s/s"
#not to trust all.
curl "https://localhost:5001/s/s"
echo
echo "___spilter___"
echo
wget -q -O - "https://localhost:5001/s/s"
# what if do it in system level?
