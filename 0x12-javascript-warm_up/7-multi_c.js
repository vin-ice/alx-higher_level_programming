#!/usr/bin/node

const process = require('process');

let count;
if (Number.isInteger(count = Number.parseInt(process.argv[2]))) { for (; count > 0; count--) { console.log('C is fun'); } } else { console.log('Missing number of occurences'); }
