function openOverlay() {

    document.getElementById("overlay").style.display = "block";
}

function closeOverlay() {
    document.getElementById("overlay").style.display = "none";
}

document.getElementById("b").addEventListener("click", openOverlay);

document.getElementById("bc").addEventListener("click", closeOverlay);