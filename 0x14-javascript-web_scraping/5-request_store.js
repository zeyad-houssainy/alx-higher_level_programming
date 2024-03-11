#!/usr/bin/node
const fs = require("fs");
const request = require("request");
let url = process.argv[2];
let fileName = process.argv[3] !== undefined ? process.argv[3] : "";

request(url, (error, _response, content) => {
  if (error) {
    console.log(error);
  }
  fs.writeFile(fileName, content, utf - 8, (err) => {
    if (err) {
      console.log(err);
    }
  });
});
