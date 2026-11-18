window.onload = fetchHTMLdata;
async function fetchHTMLdata () {
  console.log('hold please, fetching data');
  const data = await fetch('https://hellosalut.stefanbohacek.com/?lang=fr');
  const info = await data.json();
  for (const key in info) {
    if (key === 'hello') {
      const pass = info[key];
      const elem = document.getElementById('hello');
      elem.append(pass);
    }
  }
}
