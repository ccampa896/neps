// Importando o módulo
const fs = require('fs');

// Lendo o conteúdo da linha de comando
let leitura = fs.readFileSync(0, 'utf8');

let palavra = leitura.split('\n');
let qtd = 0;

for (let i = 0; i < palavra[0].length; i++) {
  if (palavra[0][i] === palavra[1]) {
    qtd++;
  }
}

console.log(qtd);
