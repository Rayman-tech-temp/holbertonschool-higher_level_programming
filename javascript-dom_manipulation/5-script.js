const elem = document.getElementById('update_header');

function editHeader () {
  elem.textContent = 'New Header!!';
}
elem.addEventListener('click', editHeader);
