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

// Dialog #dialog-instructions handling
// If user closes the dialog, the section #instructions will be added to the DOM:
const dialog = document.getElementById('dialog-instructions');
if (dialog) {
  dialog.addEventListener('close', () => {
    const instructions = document.getElementById('instructions');
    instructions.style.display = 'block';
    // Also an animation will be added to the section #instructions that takes 3 seconds:
    instructions.style.animation = 'drop_into_view 3s';
  });
}
