#!/usr/bin/node

const list = require('./100-data').list;

const result = Array.from(list).map((ele, i) => { return ele * i; });

console.log(list);
console.log(result);
