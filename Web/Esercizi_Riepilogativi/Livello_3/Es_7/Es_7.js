async function fetch_result(API_call) {

    try {
        const response = await fetch(API_call);
        const data = await response.json();
        document.getElementById("async_result_title").innerHTML = data.title;
        document.getElementById("async_result_body").innerHTML = data.body;

        
    } catch (error) {

        document.getElementById("async_result").innerHTML = "Errore nel recupero dei dati"
        
    }
    
}

fetch_result("https://jsonplaceholder.typicode.com/posts/1")