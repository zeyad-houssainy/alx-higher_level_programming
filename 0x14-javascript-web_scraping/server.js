#!/usr/bin/node
const http = require("http");
const fs = require("fs");
const parser = require("url");

http
  .createServer(function (req, res) {
    const pathname = parser.parse(req.url, true).pathname;
    if (pathname === "/404") {
      res.writeHead(404, { "Content-Type": "text/plain" });
    } else if (pathname === "/301") {
      res.writeHead(301, { "Content-Type": "text/plain" });
    } else if (pathname === "/204") {
      res.writeHead(204, { "Content-Type": "text/plain" });
    } else {
      res.writeHead(200, { "Content-Type": "text/plain" });
    }
    res.end("OK");
  })
  .listen(5050);
