#!/bin/bash
# sends a DELETE request to URL passed as arg and displays body
curl -sX DELETE http://"$1"
