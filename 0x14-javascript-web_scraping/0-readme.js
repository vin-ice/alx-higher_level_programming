#!/usr/bin/node

const fs = require('fs');
const process = require('process');

fs.readFile(process.argv[2], { encoding: 'utf-8' }, function (err, data) {
  if (!err) { console.log(data); } else { console.log(err); }
});
