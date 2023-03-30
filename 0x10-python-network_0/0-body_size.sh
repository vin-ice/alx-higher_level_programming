#!/usr/bin/env bash
# takes a URL, sends a request to URL, and displays the size of the body of the response

curl -s -I "http://$1" | awk -F ': ' '{ if ($1 == "Content-Length") print $2  }'