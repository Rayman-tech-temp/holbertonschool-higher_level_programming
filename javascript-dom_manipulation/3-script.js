const header = document.getElementById('toggle_header');
header.className = 'red';

function classToggle () {
  if (header.classList.contains('green')) {
    header.className = 'red';
  } else if (header.classList.contains('red')) {
    header.className = 'green';
  }
  return null;
}
header.addEventListener('click', classToggle);
