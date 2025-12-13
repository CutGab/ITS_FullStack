// 29. Promise.all per Chiamate Multiple
// Richiesto: ottenere post e commenti contemporaneamente.
// Usare: Promise.all.
// Risultato: dati aggregati visibili insieme.

function fetch_multiple(API_CALL, API_CALL_2) {

    const post = fetch(API_CALL);
    const commenti = fetch(API_CALL_2);

    return Promise.all([post, commenti])
        .then(function(array_response) {
            return Promise.all([array_response[0].json(), array_response[1].json()]);
        })
        
        .then(([post, commenti]) => {
            document.getElementById("post").innerHTML = JSON.stringify(post.title);
            document.getElementById("comment").innerHTML = commenti.map(c => c.body).join("<br><br>");
        });

}

fetch_multiple(
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/comments?postId=1"
);