// 28. Lista Utenti da API
// Richiesto: ottenere elenco utenti remoto e mostrarlo come lista.
// Usare: fetch, cicli, creazione nodi DOM.
// Risultato: lista di nomi completa ordinata.

function fetch_dati (API_CALL) {

    fetch(API_CALL)
    .then(function(response){
        return response.json()
    
    })

    .then(function(data) {

        const array_nomi = data.map(function(elemento){

            return (
                `${elemento.name}`
            )
        })
        
        const sorted_array = array_nomi.sort()

        let lista = ""

        sorted_array.forEach(nome => {

            lista += `<li> ${nome} </li>`
            
        });

        document.getElementById("list_fetch").innerHTML = lista;
                
    })

}

fetch_dati("https://jsonplaceholder.typicode.com/users")
