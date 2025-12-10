const array_food = [

    {nome: "Spaghetti", categoria: "Pasta", prezzo: 21.99},
    {nome: "Pennette", categoria: "Pasta", prezzo: 12.99},
    {nome: "Fagioli in scatola", categoria: "Legumi", prezzo: 10.50},
    {nome: "Lenticchie", categoria: "Legumi", prezzo: 10.99},

];

const elementi_filtrati = array_food.filter(function(elemento) {

    return elemento.categoria == "Pasta" && elemento.prezzo < 22.00

});

document.getElementById("array_filter").innerHTML = JSON.stringify(elementi_filtrati);