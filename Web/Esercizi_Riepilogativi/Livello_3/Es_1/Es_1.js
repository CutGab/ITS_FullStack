const persone = [
    
    {nome: "Mario", cognome: "Rossi"},
    {nome: "Luigi", cognome: "Verdi"},
    {nome: "Wario", cognome: "Gialli"}
];
        

const persone_stringhe = persone.map(function(persona) {
    return `${persona.nome} ${persona.cognome}`;
});

document.getElementById("array_string").innerHTML = persone_stringhe;