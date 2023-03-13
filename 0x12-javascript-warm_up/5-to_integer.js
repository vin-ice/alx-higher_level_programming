#!/usr/bin/node

const process = require('process');

let num;

if (!isNaN(num = Number.parseInt(process.argv[2]))) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
