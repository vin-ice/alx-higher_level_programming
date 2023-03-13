#!/usr/bin/node

const process = require('process');

console.log(add(process.argv[2], process.argv[3]));

function add (op1, op2) {
  return Number.parseInt(op1) + Number.parseInt(op2);
}
