// Importando o módulo
const fs = require('fs');

// Lendo o conteúdo da linha de comando
let leitura = fs.readFileSync(0, 'utf8');

let numero = parseInt(leitura.split('\n'));

function fib(num) {
  if (num === 0 || num === 1) {
    return 1;
  } else {
    return fib(num - 1) + fib(num - 2);
  }
}

console.log(fib(numero));
