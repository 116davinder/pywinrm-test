#!/bin/bash

echo "Running Test without credentials and GET Request only"
curl -v "$1"/wsman

echo "Running Test with credentials and POST Request + NTLM AUTH"
curl -X POST -k -v --ntlm -d "whoami" -u "$2":"$3" "$1"/wsman
