#!/bin/bash
rm -rf certs
mkdir -p certs/ca
cd certs/ca
openssl genrsa -out ca.key 2048
openssl req -x509 -new -nodes \
      -key ca.key -subj "/CN=localhost/C=US/L=CALIFORNIA" \
      -days 1825 -out ca.crt
cd ..
openssl genrsa -out server.key 2048
cat > csr.conf <<EOF
[ req ]
default_bits = 2048
prompt = no
default_md = sha256
req_extensions = req_ext
distinguished_name = dn

[ dn ]
C = US
ST = California
L = San Fransisco
O = Scriptcrunch
OU = Scriptcrunch Dev
CN = localhost

[ req_ext ]
subjectAltName = @alt_names

[ alt_names ]
DNS.1 = localhost
IP.1 = 127.0.0.1

EOF
openssl req -new -key server.key -out server.csr -config csr.conf
openssl x509 -req -in server.csr -CA ca/ca.crt -CAkey ca/ca.key \
-CAcreateserial -out server.crt -days 10000 \
-extfile csr.conf

