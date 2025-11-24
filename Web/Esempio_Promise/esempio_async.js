const url = "https://jsonplaceholder.typicode.com/posts/1";

let post = "";

//Il risultato di una funziona sincrona sarà sempre una promise

async function getPost() {
    const response = await fetch(url)
    const ris = await response.json()
    console.log(ris)
    return ris;
}

post = getPost().then(ris => console.log(ris));
console.log("post", post)