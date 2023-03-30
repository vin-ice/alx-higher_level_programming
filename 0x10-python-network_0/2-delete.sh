#!/usr/bin/env bash
# sends a DELETE request to URL passed as arg and displays body

curl -s -X DELETE http://"$1"
