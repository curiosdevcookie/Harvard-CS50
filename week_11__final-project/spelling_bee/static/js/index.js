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


  // Share button:
  function shareText() {
    const definitionArea = document.getElementById('definition-area');
    const textToShare = definitionArea.innerText;

    const wordlist = document.getElementById('word-list-ul');
    const word = wordlist.lastElementChild;
    const wordToShare = word.innerText;

    const scoreArea = document.getElementById('score-area');
    const scoreToShare = scoreArea.innerText;

    const svg = document.getElementById('comb');
    const svgToShare = svg.outerHTML;

    const urlToShare = 'https://urban-spelling-bee.fly.dev/';

    if (navigator.share) {
      const svgBlob = new Blob([svgToShare], { type: 'image/svg+xml' });

      const reader = new FileReader();
      reader.onload = function () {
        const svgDataUrl = reader.result;

        const canvas = document.createElement('canvas');
        const context = canvas.getContext('2d');

        const img = new Image();
        img.onload = function () {
          canvas.width = img.width;
          canvas.height = img.height;
          context.drawImage(img, 0, 0);

          canvas.toBlob(function (blob) {
            const imageToShare = [new File([blob], 'comb.png', { type: 'image/png' })];

            navigator.share({
              text: `I found "${wordToShare}" which has the definition "${textToShare}". I played on ${urlToShare} and my score is ${scoreToShare} points with these letters:`,
              files: imageToShare
            })
              .then(() => console.log('Text shared successfully.'))
              .catch((error) => console.log('Error sharing text:', error));
          });
        };

        img.src = svgDataUrl;
      };

      reader.readAsDataURL(svgBlob);
    } else {
      console.log('Web Share API not supported.');
      // Fallback to copying text to clipboard
      copyToClipboard();
    }
  }

  // Check if Web Share API is supported
  if (navigator.share) {
    const copyButton = document.getElementById('copyToClipboard');
    copyButton.style.display = 'none';

    const shareButton = document.getElementById('shareButton');
    shareButton.style.display = 'block';
    shareButton.onclick = shareText;
  } else {
    const copyButton = document.getElementById('copyToClipboard');
    copyButton.style.display = 'block';
    copyButton.onclick = copyToClipboard;
  }
}