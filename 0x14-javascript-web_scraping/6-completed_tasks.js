#!/usr/bin/node
const request = require("request");
let url = process.argv[2];
let userTotals = {};

request(url, (error, _response, content) => {
  if (error) {
    console.log(error);
  }
  let taskList = JSON.parse(content); //change json data to object in JS
  for (let task of taskList) {
    if (task.completed === true) {
      if (task.userId in userTotals) {
        userTotals[task.userId] += 1;
      } else {
        userTotals[`User: ${task.userId}`] = 1;
      }
    }
  }
  console.log(userTotals)
});
