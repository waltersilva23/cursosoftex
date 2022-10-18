function boasvindas(){
    console.log("\nSeja bem-vindo(a) a calculadora teste") //função 1
}

function bloco1(num1, num2) {  //função 2
    if(operador == 1){
        resultado = parseFloat(num1) + parseFloat(num2);
    }
    if(operador == 2){
        resultado = parseFloat(num1) - parseFloat(num2);
    }
    if(operador == 3) {
        resultado = parseFloat(num1) * parseFloat(num2);
    }
    return resultado;
}

const bloco2 = (num1, num2) => resultado = parseFloat(num1) / parseFloat(num2); //função 3

boasvindas()

var readlineSync = require("readline-sync")
var num1 = readlineSync.question('\nDigite o primeiro valor: ');
var num2 = readlineSync.question('\nDigite o segundo valor: ');
console.log("\nInforme a operação que deseja utilizar: \n1- adição \n2- subtração \n3- multiplicação \n4- divisão");
var operador = readlineSync.question("\n");

if (operador == 1 || operador == 2 || operador == 3){
    var resultado = bloco1(num1, num2);
}
if (operador == 4){
    var resultado = bloco2(num1, num2);
}
else{
    console.log("\nVocê digitou uma operação inválida.")
}

console.log("\n" + resultado)
