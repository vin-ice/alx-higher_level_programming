#!/usr/bin/env bash
# takes in URL, sends POST and displays body of response
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST http://"$1"