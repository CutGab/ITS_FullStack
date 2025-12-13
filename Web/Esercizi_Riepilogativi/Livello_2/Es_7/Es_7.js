const array = [
    1,
    2,
    3,
    4
];

let [a, b] = array;

[a,b] = [b,a]

document.getElementById("content").innerHTML =  `<h1> Primo valore: ${a} </h1> <br> <h1> Secondo valore: ${b} </h1>`