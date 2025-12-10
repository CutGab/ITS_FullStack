const voti_studenti = [ 
    {nome: "Alice", voti: [18, 20, 15, 17]},
    {nome: "Luca", voti: [12, 14, 16, 18]},
    {nome: "Giulia", voti: [20, 19, 18, 20]},
    {nome: "Marco", voti: [10, 15, 13, 14]},
];

const medie = voti_studenti.map(function(elemento) {
    return elemento.voti.reduce(function(sommatoria, voto){
        return sommatoria + voto;
    }, 0) /elemento.voti.length;
});

const final_media = medie.reduce(function(media_finale, voto) {

    return media_finale + voto

}, 0) / voti_studenti.length;

const display_medie_studenti = voti_studenti.map(function(studente, index){

    return `Nome: ${studente.nome} Media: ${medie[index]}`

})

document.getElementById("media_array").innerHTML = display_medie_studenti.join("<br>");
document.getElementById("media_finale_array").innerHTML = `La media di tutti gli studenti equivale a ${final_media}`;
