const movimenti = [ 15, -4, -2, 20];

const saldo = movimenti.reduce(function(sommatoria, numero) {

    return sommatoria + numero;

}, 0);

document.getElementById("saldo_array").innerHTML = saldo;