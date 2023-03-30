#!/usr/bin/env bash
# Display all HTTP methods the server will accept
curl -s -X OPTIONS http://"$1"