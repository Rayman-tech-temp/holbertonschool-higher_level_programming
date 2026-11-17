const elem = document.getElementById('character');

async function fetchJSONdata () {
  console.log('hold please');
  const data = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
  const character = await data.json();
  elem.textContent = character.name;
}
elem.addEventListener('click', fetchJSONdata);
