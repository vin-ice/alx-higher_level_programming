#!/usr/bin/env bash
# Sends json POST to url and displays body of res
curl -X POST -H "Content-Type: application/json" -d @"$2" -s http://"$1"