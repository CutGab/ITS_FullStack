document.getElementById("numericInput").addEventListener("change", Controlla);

function Controlla () {

    let t = document.getElementById("inputValue").value;
    let n = document.getElementById("numericInput").value;
    let e = document.getElementById("errorMessage");
    
    mess = (t.length >= n ? e.textContent = "Sei apposto" : e.textContent = "SEI SOTTO LA SOGLIA");   
}

