const request = require("request");
const baseUrl = "https://swapi-api.alx-tools.com/api/films/";
const userId = 18;

const temp = 0;
request(`${baseUrl}`, (error, _response, body) => {
  if (error) {
    console.error(error);
  }
  const films = JSON.parse(body).results;
  for (let film of films){
    for (let url of film.characters){
      if (url.includes(`/api/people/${userId}/`)) {
        console.log("OK");
      }
  }
  }
});

