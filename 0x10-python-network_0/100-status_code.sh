#!/bin/bash
# Sends a request URL passed as an argument and displays status code of res
curl -s -w "%{http_code}" -o /dev/null http://"$1"
