#!/usr/bin/env bash
# Sends a GET request and display the body of response
curl -s -X GET -w "%{http_code}" -o /dev/null http://"$1" | grep -q 200 && curl http://"$1"
