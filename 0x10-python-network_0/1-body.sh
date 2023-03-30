#!/usr/bin/env bash
# Sends a GET request and display the body of response
curl -sG -w "%{http_code}" -o ./res http://"$1" | { read -r c ; if [ "$c" == 200 ]; then cat ./res ; fi } 