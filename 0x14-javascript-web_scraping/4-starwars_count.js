#!/usr/bin/node

const process = require('process');
const request = require('request');

const URL = process.argv[2];

request.get({ url: URL, json: true }, function (err, res, body) {
  if (!err) {
    console.log(Array.from(body.results).filter(function (film) {
      return film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/');
    }).length);
  } else { console.log(err); }
});
