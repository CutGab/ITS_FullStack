const url = "https://jsonplaceholder.typicode.com/posts/1";

let post = "";

// fetch che restituisce una promise

fetch(url).then(response => response.json()).then(ris =>
    {
        console.log("risultato fetch", ris)
        post = ris;
    }
).catch(err => console.log(err))

console.log("post", post);

// Non si può utilizzare il risultato di una chiamata asincrona nel codice sincrono