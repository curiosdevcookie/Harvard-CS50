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

  // Setup buttons according to availability status of the Web Share API:
  function setupButton(buttonId, clickHandler) {
    const button = document.getElementById(buttonId);
    const action = navigator.share ? 'Share' : 'Copy';

    button.innerHTML = action;
    button.addEventListener('click', clickHandler);
  }

  // Copy or share a specific word and its definition:
  function eitherCopyOrShareWordDef() {

    const definitionArea = document.getElementById('definition-area');
    const definitionToShare = definitionArea.innerText;

    const wordlist = document.getElementById('word-list-ul');
    const word = wordlist.lastElementChild;
    const wordToShare = word ? word.innerText : 'a nothing';

    const textToShare = `I found "${wordToShare}" which has the definition "${definitionToShare}".`;

    if (navigator.share) {
      navigator.share({
        text: textToShare
      })
    } else {
      navigator.clipboard.writeText(textToShare);
    }
  }

  setupButton('buttonCopyOrShareWordDef', eitherCopyOrShareWordDef);

  // Copy or share the result, the comb/the played letters, the game url:
  function eitherCopyOrShareResult() {

    const scoreArea = document.getElementById('score-area');
    const scoreToShare = scoreArea.innerText;

    const randomSeven = document.getElementById('randomSeven');
    const randomSevenToShare = randomSeven.innerText;

    const svg = document.getElementById('comb');
    const svgToShare = svg.outerHTML;

    const urlToShare = 'https://urban-spelling-bee.fly.dev/';


    const svgBlob = new Blob([svgToShare], { type: 'image/svg+xml' });

    const reader = new FileReader();

    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');

    const img = new Image();
    img.onload = function () {
      canvas.width = img.width;
      canvas.height = img.height;
      context.drawImage(img, 0, 0);

      canvas.toBlob(function (blob) {
        const imageToShare = [new File([blob], 'comb.png', { type: 'image/png' })];
        const textToShare = `I played Urban Spelling Bee on ${urlToShare} and my score is ${scoreToShare} points with these letters:
        `;

        if (navigator.share) {
          navigator.share({
            text: textToShare,
            files: imageToShare
          })
        } else {
          navigator.clipboard.writeText(`${textToShare} ${randomSevenToShare}`);
        }
      });
    };

    img.src = URL.createObjectURL(svgBlob);

  }

  setupButton('buttonCopyOrShareResult', eitherCopyOrShareResult);
}

