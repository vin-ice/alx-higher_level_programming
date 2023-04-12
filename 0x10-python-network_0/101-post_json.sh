#!/bin/bash
# Sends json POST to url and displays body of res
curl -s -X POST -H "Content-Type: application/json" -d @"$2" http://"$1"
