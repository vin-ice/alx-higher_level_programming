#!/usr/bin/node

const process = require('process');
const request = require('request');
const URL = require('url').URL;

const BASEURL = 'https://swapi-api.alx-tools.com/';

request.get({ url: new URL(`/api/films/${process.argv[2]}`, BASEURL).href, json: true }, function (err, res, body) {
  if (!err) {
    body.characters.forEach(function (userUrl) {
      request.get({ url: userUrl, json: true }, function (err, res, body) {
        if (res.statusCode === 200) { console.log(body.name); } else { console.log(err); }
      });
    });
  } else { console.log(err); }
});
