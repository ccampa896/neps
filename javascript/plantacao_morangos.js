// Importando o módulo
const fs = require('fs');

// Lendo o conteúdo da linha de comando
let leitura = fs.readFileSync(0, 'utf8');

// Dividindo a leitura nas quebras de linha, ou seja, "\n"
let linhas = leitura.split('\n');

//transformando a string em inteiro
let inteiro = linhas.map(num => {
  return parseInt(num);
});

// Realizando o cálculo da área
let area1 = inteiro[0] * inteiro[1];

let area2 = inteiro[2] * inteiro[3];

if (area1 > area2) {
  console.log(area1);
} else {
  console.log(area2);
}
