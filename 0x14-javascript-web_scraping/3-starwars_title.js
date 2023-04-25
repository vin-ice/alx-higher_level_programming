#!/usr/bin/node

const process = require('process');
const request = require('request');
const URL = require('url').URL

const BASEURL = "https://swapi-api.alx-tools.com/";

request.get({url: new URL(`/api/films/${process.argv[2]}`, BASEURL).href, json: true}, function (err, res, body) {
    if (!err) { console.log(body.title); } else { console.log(err) }
});
