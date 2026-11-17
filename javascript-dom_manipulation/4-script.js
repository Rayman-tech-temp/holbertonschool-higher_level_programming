const elem = document.getElementById('add_item');

function newItem () {
  const newListItem = document.createElement('li');
  newListItem.appendChild(document.createTextNode('Item'));
  document.querySelector('ul').appendChild(newListItem);
}
elem.addEventListener('click', newItem);
