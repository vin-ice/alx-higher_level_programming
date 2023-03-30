#!/usr/bin/env bash
# Display all HTTP methods the server will accept
curl -s -i -L -X OPTIONS http://"$1" | grep Allow | awk -F ': ' '{ print $2 }'