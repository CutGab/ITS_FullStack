const selectMarca = document.getElementById('marca');
const selectModello = document.getElementById('modello');

selectMarca.addEventListener("change", (e) => {
    const selectedMarca = selectMarca.value
    selectModello.disabled = selectedMarca === ""
    selectModello.innerHTML = ""
    modelliPerMarca[selectedMarca].forEach(element => {

        const option = document.createElement("option")
        
            option.value = element
            option.textContent = element

        selectModello.appendChild(option)
    });
})