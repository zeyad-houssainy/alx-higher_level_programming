#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, (_error, response) => {
  console.log(`code: ${response.statusCode}`);
});
