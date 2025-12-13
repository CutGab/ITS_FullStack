const car = {modello: "Fiat Panda", anno: 1990}

document.getElementById("car").innerHTML = ShowModello();

function ShowModello () {
    return `Modello: ${car.modello} ${car.anno}`;
}