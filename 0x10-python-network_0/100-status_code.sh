#!/usr/bin/env bash
# Sends a request URL passed as an argument and displays status code of res
curl -sI -w "%{http_code}\n" -o /dev/null http://"$1"
