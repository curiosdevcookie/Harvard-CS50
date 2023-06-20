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

window.addEventListener('DOMContentLoaded', function () {

  showInstructionsDialog();

  setupButton('buttonCopyOrShareResult', eitherCopyOrShareResult);

  showPangramPoints();

  animateBeeOncePerScreensize();

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



  const scoreArea = document.getElementById('score-area');
  const score = scoreArea.innerText;
  const sectionResults = document.getElementById('results');

  if (score > 0) {
    sectionResults.style.display = 'block';
  } else {
    sectionResults.style.display = 'none';
  }



  // Setup buttons according to availability status of the Web Share API:
  function setupButton(buttonId, clickHandler) {
    const button = document.getElementById(buttonId);
    const action = navigator.share ? 'Share Results! ' : 'Copy Results!';

    button.innerHTML = action;
    button.addEventListener('click', clickHandler);
  }

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
          console.log("Shared");
        } else {
          navigator.clipboard.writeText(`${textToShare} ${randomSevenToShare}`);
          console.log("Copied");
        }
      });
    };

    img.src = URL.createObjectURL(svgBlob);

  }

  // Show the pangram bonus points:
  function showPangramPoints() {
    const pElement = document.querySelector('dialog p');
    if (pElement && pElement.textContent.includes('🐝')) {
      const pangram = document.getElementById('pangram-found');
      pangram.style.display = 'block';
    }
  }


  // Show the bee animation only once per session:
  function animateBeeOncePerScreensize() {
    const bee = document.getElementById('beeOne');
    const beeInnerWrapper = document.getElementById('beeOneInnerWrapper');
    if (!sessionStorage.getItem('beeShown')) {
      if (window.innerWidth <= 768) {
        // Add class for smaller screens and set animation duration
        bee.style.animation = 'fly-small-screens 13s, jiggle 1s infinite';
        bee.style.top = '10%';
        bee.style.left = '72%';
        beeInnerWrapper.setAttribute('transform', 'rotate(90 50 50)');

      } else {
        // Add class for larger screens and set animation duration
        bee.style.animation = 'fly-large-screens 13s, jiggle 1s infinite';
        bee.style.top = '10%';
        bee.style.right = '68%';
      }
      sessionStorage.setItem('beeShown', 'true');
    }
  }
});
