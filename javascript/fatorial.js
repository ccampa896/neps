// Importando o módulo
const fs = require('fs');

// Lendo o conteúdo da linha de comando
let leitura = fs.readFileSync(0, 'utf8');

let numero = parseInt(leitura.split('\n'));

function fat(num) {
  if (num === 0 || num === 1) {
    return 1;
  } else {
    return num * fat(num - 1);
  }
}

console.log(fat(numero));
