#!/usr/bin/node

const process = require('process');

let size, l;

if (Number.isInteger(size = Number.parseInt(process.argv[2]))) {
  for (l = 0; l < size; l++) {
    console.log('X'.repeat(size));
  }
} else { console.log('Missing size'); }
