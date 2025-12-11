fetch("https://jsonplaceholder.typicode.com/posts/1")
    .then(function(response){

        return response.json()
    })

    .then(function(data) {
        document.getElementById("fetch_title").innerHTML = data.title;
        document.getElementById("fetch_body").innerHTML = data.body;
    })

