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

window.onload = function () {

  showInstructionsDialog();
  function showInstructionsDialog() {
    const dialog = document.getElementById('dialog-instructions');
    const closeButton = document.getElementById('close-dialog');
    const instructions = document.getElementById('instructions');

    if (!sessionStorage.getItem('dialogShown')) {
      dialog.style.display = 'block';
      closeButton.addEventListener('click', function () {
        dialog.style.display = 'none';
        instructions.style.display = 'block';

        instructions.style.animation = 'drop_into_view 6s';
        sessionStorage.setItem('dialogShown', true);
      });

    } else {
      instructions.style.display = 'block';
      dialog.style.display = 'none';
    }
  }

  // Copy to clipboard:
  function copyToClipboard() {
    const definitionArea = document.getElementById('definition-area');
    const textToCopy = definitionArea.innerText;

    navigator.clipboard.writeText(textToCopy);
  }
  // Copy button onclick event
  const copyButton = document.getElementById('copyToClipboard');
  copyButton.onclick = copyToClipboard;


  // Share button:
  function shareText() {
    const definitionArea = document.getElementById('definition-area');
    const textToShare = definitionArea.innerText;
    const shareButton = document.getElementById('shareButton');

    if (navigator.share) {
      shareButton.style.display = 'block';
      navigator.share({
        text: textToShare
      })
        .then(() => console.log('Text shared successfully.'))
        .catch((error) => console.log('Error sharing text:', error));
    } else {
      console.log('Web Share API not supported.');
    }
  }

  // Share button onclick event
  const shareButton = document.getElementById('shareButton');
  shareButton.onclick = shareText;
}