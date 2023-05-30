const btns = document.querySelectorAll('.btns__btn');
const [btnStart, btnReset] = btns;

const cards = [
  'images/dama-karo.png',
  'images/dama-pik.png',
  'images/dama-kier.png'
]
const card_back = 'images/back.png';

const [damaKaro, damaPik, damaKier] = cards

const images = document.querySelectorAll('.wrapper__card');
const [referenceDamaKaro, referenceDamaPik, referenceDamaKier] = images

let [i, j, k, index, numberOfHits, clickCounter, numberOfAttempts] = [0, 1, 2, 0, 0, 0, 0]


btnStart.addEventListener('click', function () {
  clickCounter = 0
  console.log(
    `Ilość prób: ${++numberOfAttempts} 
Ilość trafień: ${numberOfHits} 
To jest: ${(numberOfHits / numberOfAttempts * 100).toFixed(0)}%`
  );
  btnStart.disabled = true;
  images.forEach(image => {
    image.classList.toggle('rotate');
    image.classList.toggle('rotate-one');
    image.setAttribute('src', card_back);
  })

  i = Math.floor(Math.random() * 3);
  const numbers = [0, 1, 2];
  index = numbers.find(number => number == i)
  numbers.splice(index)

  switch (numbers.length) {
    case 0: j = 1, k = 2;
      break;
    case 1: j = 0, k = 2;
      break;
    case 2: j = 0, k = 1;
  }
})

btnReset.addEventListener('click', () => {
  btnStart.disabled = false;
  btnReset.disabled = true;
  images.forEach((image, i) => {
    image.setAttribute('src', cards[i])
    image.classList.toggle('rotate')
    image.classList.toggle('rotate-one')
  })
});

referenceDamaKaro.addEventListener('click', () => {
  clickCounter++;
  btnStart.disabled = false;
  if (cards[i] == damaPik && clickCounter == 1) {
    numberOfHits++
    console.log(`\nHurra, trafiłeś`);
  }
  referenceDamaKaro.setAttribute('src', cards[i]);
  referenceDamaKaro.classList.toggle('rotate');
  referenceDamaKaro.classList.toggle('rotate-one');

})

referenceDamaPik.addEventListener('click', () => {
  clickCounter++;
  btnStart.disabled = false;
  if (cards[j] == damaPik && clickCounter == 1) {
    numberOfHits++
    console.log(`\nHurra, trafiłeś`);
  }
  referenceDamaPik.setAttribute('src', cards[j])
  referenceDamaPik.classList.toggle('rotate');
  referenceDamaPik.classList.toggle('rotate-one');
})

referenceDamaKier.addEventListener('click', () => {
  clickCounter++;
  btnStart.disabled = false;
  if (cards[k] == damaPik && clickCounter == 1) {
    numberOfHits++;
    console.log(`\nHurra, trafiłeś`);
  }
  referenceDamaKier.setAttribute('src', cards[k])
  referenceDamaKier.classList.toggle('rotate');
  referenceDamaKier.classList.toggle('rotate-one');
})
