#!/usr/bin/node

const { argv } = require('process');
const process = require('process');

const size = process.argv.length;

if (size <= 2) { console.log(0); } else if (size <= 3) { console.log(0); } else {
  console.log(argv.slice(2).map(x => Number.parseInt(x)).sort(function (a, b) { return b - a; })[1]);
}
