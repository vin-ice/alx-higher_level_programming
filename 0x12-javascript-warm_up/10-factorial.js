#!/usr/bin/node

const process = require('process');

console.log(factorial(Number.parseInt(process.argv[2])));

function factorial (num) {
  if (num <= 0 || Number.isNaN(num)) { return 1; }
  return (num * factorial(num - 1));
}
