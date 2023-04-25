#!/usr/bin/node

const process = require('process');
const request = require('request');

const URL = process.argv[2];

request.get({ url: URL, json: true }, function (err, res, body) {
  if (!err) {
    tasks = Array.from(body).filter(function (todo) { return todo.completed; })
      .reduce(function (acc, curr) {
        if (!acc[curr.userId]) { acc[curr.userId] = 1; } else { acc[curr.userId]++; }
        return acc;
      }, {});
    console.log(tasks);
  } else { console.log(err); }
});
