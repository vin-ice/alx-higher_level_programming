#!/bin/bash
# Display all HTTP methods the server will accept
curl -s -i -X OPTIONS http://"$1" | grep Allow | cut -d " " -f 2-
