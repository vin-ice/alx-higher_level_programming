#!/usr/bin/node

const process = require('process');
const request = require('request');

request.get(process.argv[2], function (err, res) { if (!err) { console.log(`code: ${res.statusCode}`); } });
