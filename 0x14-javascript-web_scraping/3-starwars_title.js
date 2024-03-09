#!/usr/bin/node
const request = require('request');
const starWarsUrl = `https://swapi-api.alx-tools.com/api/films/:${process.argv[2]}`;
request(starWarsUrl, (_error, _response, body) => {
  if (error) {
    console.error(error);
  }
  const statWarsMovieData = JSON.parse(body);
  const statWarsMovieName = statWarsMovieData.title;
  console.log(statWarsMovieName);
});
