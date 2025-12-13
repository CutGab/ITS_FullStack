let div = document.createElement("div");

function Aggiungi() {
    // 1. Grab the input value
    let inputValue = document.getElementById("textinput").value;

    // 2. Create a new <p> element
    let p = document.createElement("p");

    // 3. Set the text of <p> to the input value
    p.textContent = inputValue;

    // 4. Append the new <p> to the visible container
    document.getElementById("show").appendChild(p);
}

document.getElementById("lista").addEventListener("click", Aggiungi);

function ShowLista () {
    
    return `Lista: ${div.textContent}`;
}

document.getElementById("show").innerHTML = ShowLista();