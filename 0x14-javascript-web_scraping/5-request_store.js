#!/usr/bin/node

const fs = require('fs');
const process = require('process');
const request = require('request');

const URL = process.argv[2];
const file = process.argv[3];

request
  .get(URL)
  .on('error', function (err) {
    console.log(err);
  })
  .pipe(fs.createWriteStream(file, { encoding: 'utf-8' }));
