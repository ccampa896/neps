// Importando o módulo
const fs = require("fs");

// Lendo o conteúdo da linha de comando
let leitura = fs.readFileSync(0, "utf8");

// Dividindo a leitura nas quebras de linha, ou seja, "\n"
let linhas = leitura.split("\n");


//transformando a string em inteiro
let inteiro = linhas.map((num) => {
    return  parseInt(num);
})

// Realizando a subtração
let sub = inteiro[0] + inteiro[1];

// Imprimindo a subtração
console.log(sub);
