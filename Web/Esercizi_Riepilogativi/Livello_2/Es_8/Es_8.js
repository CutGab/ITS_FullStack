const array = [

    [1,2,3,4,5],

    [6,7,8,9,10]

];

const [a, b] = array;


const arrayCombined = [...a,...b];

document.getElementById("content").innerHTML = `<h1> ${arrayCombined} </h1>`;