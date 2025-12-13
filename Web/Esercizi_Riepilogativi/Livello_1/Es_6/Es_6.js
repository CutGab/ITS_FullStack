let n =  0;

document.getElementById("Numero").textContent = n;

document.getElementById("BOTTONE").addEventListener("click", increment);

function increment () {

    n = n + 1
    
    document.getElementById("Numero").textContent = n;

}