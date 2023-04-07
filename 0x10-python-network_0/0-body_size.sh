#!/bin/bash
# takes a URL, sends a request to URL, and displays the size of the body of the response
curl -s -I http://"$1" | grep Content-Length | cut -d " " -f 2-
