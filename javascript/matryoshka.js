// Importando o módulo
const fs = require('fs');

// Lendo o conteúdo da linha de comando
let leitura = fs.readFileSync(0, 'utf8');

let numeros = leitura.split('\n');

let numbers = numeros[1].split(' ');

//transformando a string em inteiro
let inteiros = numbers.map(num => {
  return parseInt(num);
});

let qtd = 0;
let mudanca = [];
let copia = inteiros.slice();
copia.sort((a, b) => a - b);

for (let i = 0; i < inteiros.length; i++) {
  if (inteiros[i] !== copia[i]) {
    qtd++;
    mudanca.push(inteiros[i]);
  }
}

mudanca.sort((a, b) => a - b);

console.log(qtd);
if (mudanca.length > 0) {
  console.log(mudanca.join(' '));
}
