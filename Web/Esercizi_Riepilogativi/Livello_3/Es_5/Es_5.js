// 25. Promise Simulata Richiesto: simulare recupero dati dopo un ritardo. Usare: Promise, timeout. 
// Risultato: testo che compare dopo alcuni secondi.

function RecuperoDati (dati) {

    return new Promise(function(resolve) {
        
        setTimeout(function() {
            
            resolve(dati);
        }, 5000);
    });
}

RecuperoDati("Ecco i tuoi dati")

    .then(function(messaggio) {
        document.getElementById("promise_result").innerHTML = messaggio;
    })

    .catch(function(errore) {
        document.getElementById("promise_result").innerHTML = errore;
    })