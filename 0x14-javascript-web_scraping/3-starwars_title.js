#!/usr/bin/node
const request = require('request');
const starWarsUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(starWarsUrl, (_error, _response, body) => {
  body = JSON.parse(body);
  console.log(body.title);
});




