// Importando o módulo
const fs = require('fs');

// Lendo o conteúdo da linha de comando
let leitura = fs.readFileSync(0, 'utf8');

let numeros = leitura.split('\n');

numeros.pop();

let numbers = numeros[1].split(' ');

//transformando a string em inteiro
let inteiros = numbers.map(num => {
  return parseInt(num);
});

let qtd = 0;

for (let i = 0; i < inteiros.length - 2; i++) {
  if (inteiros[i] === 1) {
    if (inteiros[i + 1] === 0) {
      if (inteiros[i + 2] === 0) {
        qtd++;
      }
    }
  }
}

console.log(qtd);
