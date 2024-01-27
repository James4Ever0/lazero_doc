#!/bin/bash
#curl -k "https://localhost:5001/s/s"
#not to trust all.
curl --cacert certs/ca/ca.crt "https://localhost:5001/s/s"
echo
echo "___spilter___"
echo
#wget -q -O - "https://localhost:5001/s/s" --no-check-certificate
wget -q -O - "https://localhost:5001/s/s" --ca-certificate=certs/ca/ca.crt
# what if do it in system level?
