const elem = document.getElementById('list_movies');

async function fetchJSONdata () {
  console.log('hold please');
  const data = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
  const movies = await data.json();
  for (let i = 0; i < movies.count; i++) {
    const newListItem = document.createElement('li');
    newListItem.appendChild(document.createTextNode(movies.results[i].title));
    document.querySelector('ul').appendChild(newListItem);
    console.log(movies.results[i].title);
  }
}
elem.addEventListener('click', fetchJSONdata);
