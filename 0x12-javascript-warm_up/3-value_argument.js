#!/usr/bin/node

const process = require('process');

let arg;
if ((arg = process.argv[2]) !== undefined) {
  console.log(arg);
} else {
  console.log('No argument');
}
