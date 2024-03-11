const url = "https://swapi-api.alx-tools.com/api/films/?format=json";
$.getJSON(url, (content) => {
  const results = content.results;
  $.each(results, (index, film) => {
    $("UL#list_movies").append(`<li>${film.title}</li>`);
  });
});
