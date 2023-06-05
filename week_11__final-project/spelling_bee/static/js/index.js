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


// STYLE

(function resizeTextareas() {
  const textareas = document.querySelectorAll('textarea');
  console.log(textareas);
  textareas.forEach((textarea) => {
    /* Add event listener to each textarea */
    textarea.addEventListener('input', (event) => {
      const target = event.target;
      target.style.height = 'auto';
      target.style.height = `${target.scrollHeight / 10}rem`;
    }
    );
    /* Initial resize */
    textarea.style.height = `${textarea.scrollHeight / 10}rem`;
  });
}());

// (function checkNote() {

//   if (document.getElementById('b1-note')) {
//     document.getElementById('b1-note').style.animationPlayState = 'running';
//   }
// }
// )();