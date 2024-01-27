#!/bin/bash
sudo mkdir /usr/local/share/ca-certificates/extra
sudo cp certs/ca/ca.crt /usr/local/share/ca-certificates/extra/root.cert.crt
sudo update-ca-certificates
