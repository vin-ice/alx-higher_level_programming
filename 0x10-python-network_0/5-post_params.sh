#!/usr/bin/env bash
# takes in URL, sends POST and displays body of response
curl -s -X POST -F "email=test@gmail.com;subject=\"I will always be here for PLD\""