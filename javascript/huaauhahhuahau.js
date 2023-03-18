// Importando o módulo
const fs = require('fs');

// Lendo o conteúdo da linha de comando
let leitura = fs.readFileSync(0, 'utf8');

let risadas = leitura.split('\n');
risadas.pop();

let risada = risadas.pop();

let vogal = [];

for (let i = 0; i < risada.length; i++) {
  if (
    risada[i] === 'a' ||
    risada[i] === 'e' ||
    risada[i] === 'i' ||
    risada[i] === 'o' ||
    risada[i] === 'u'
  ) {
    vogal.push(risada[i]);
  }
}

let vogal_inverso = [];

for (let i = vogal.length - 1; i >= 0; i--) {
  vogal_inverso.push(vogal[i]);
}

vogal = vogal.join('');
vogal_inverso = vogal_inverso.join('');

// console.log(vogal);
// console.log(vogal_inverso);

if (vogal === vogal_inverso) {
  console.log('S');
} else {
  console.log('N');
}
