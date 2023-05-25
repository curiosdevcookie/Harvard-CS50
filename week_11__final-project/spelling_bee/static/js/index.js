const APIurl = 'https://urban-dictionary7.p.rapidapi.com/v0/define?term=';

const controller = new AbortController();
const signal = controller.signal;

function abortFetching() {
  console.log('Now aborting');
  controller.abort();
}

function setInnerHTMLtextarea(id, APIValue) {
  const term = document.getElementById('input-word').value;
  fetchData(term);
  document.getElementById(id).innerHTML = APIValue;
  abortFetching();
}

async function fetchData(term) {
  const response = await fetch(APIurl + term, {
    method: 'get',
    signal: signal,
  });
  if (!response.ok) {
    console.log(response.status, response.statusText);
  } else {
    const { list } = await response.json();
    if (list.length > 0) {
      const { definition, example, permalink } = list[0];
      console.log(definition, example);
      setInnerHTMLtextarea('definition-area', definition);
      setInnerHTMLtextarea('example-area', example);
      setInnerHTMLtextarea('source', permalink);
    }
  }
}

const letters = ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7'];

letters.map((letter) => {
  const element = document.getElementById(letter);
  if (element) {
    element.addEventListener('click', letterValueInput);
  }
});

function letterValueInput() {
  const input = document.getElementById('input-word');
  const term = this.innerHTML;
  input.value += term;
  return term;
}

const deleteButton = document.getElementById('delete');
if (deleteButton) {
  deleteButton.addEventListener('click', deleteLetter);
}

function deleteLetter() {
  const input = document.getElementById('input-word');
  input.value = input.value.slice(0, -1);
}

const buttonSubmit = document.getElementById('submit');
if (buttonSubmit) {
  buttonSubmit.addEventListener('click', fetchAPI);
  buttonSubmit.addEventListener('click', appendWord);
}

function fetchAPI() {
  const term = document.getElementById('input-word').value;
  console.log(term);
  fetchData(term);
}

//wordlist
function appendWord() {
  const inputWordValue = document.getElementById('input-word').value;
  const wordList = document.getElementById('word-list');
  const liElement = document.createElement('li');
  liElement.textContent = inputWordValue;
  wordList.appendChild(liElement);
  console.log(inputWordValue);
  console.log(liElement);
}
