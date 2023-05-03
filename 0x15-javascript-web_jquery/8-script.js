$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (res) {
  res.results.forEach(function (r) {
    $('UL#list_movies').append(`<li>${r.title}</li>`);
  });
});
