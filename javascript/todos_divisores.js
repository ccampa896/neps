// Importando o módulo
const fs = require('fs');

// Lendo o conteúdo da linha de comando
let leitura = fs.readFileSync(0, 'utf8');

let numero = parseInt(leitura.split('\n'));

divisores = [];
for (let i = 1; i <= numero; i++) {
  if (numero % i === 0) {
    divisores.push(i);
  }
}

console.log(divisores.join(' '));
