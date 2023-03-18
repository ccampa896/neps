// Importando o módulo
const fs = require('fs');

// Lendo o conteúdo da linha de comando
let leitura = fs.readFileSync(0, 'utf8');

let numeros = leitura.split('\n').splice(0, 4);

total = numeros.shift();
numeros.sort((a, b) => a - b);

let qtd = 0;

for (let i = 0; i < numeros.length; i++) {
  if (total - numeros[i] >= 0) {
    total -= numeros[i];
    qtd++;
  }
}

console.log(qtd);
