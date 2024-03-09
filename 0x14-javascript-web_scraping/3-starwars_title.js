#!/usr/bin/node
const request = require('request');
const starWarsUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(starWarsUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(response.statusCode);
    return;
  }

  try {
    body = JSON.parse(body);
    console.log(body.title);
  } catch (error) {
    console.log(error);
  }
});
