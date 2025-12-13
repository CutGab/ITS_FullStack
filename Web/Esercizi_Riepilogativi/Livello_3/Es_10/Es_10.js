// 30. Dashboard con Conteggi
// Richiesto: contare elementi completati e non completati.
// Usare: filter per due insiemi distinti.
// Risultato: dashboard con due valori numerici separati.

const tasks = [

    {done: false, name: "Get food"},
    {done: true, name: "Socialize"},
    {done: true, name: "Wake up"},
    {done: false, name: "Get food"},
    {done: false, name: "Sleep at a reasonable time"},
    {done: true, name: "Game"},
    {done: true, name: "Shower"}

]

var done_tasks = tasks.filter(function(task){
    return task.done;
}).length;

var todo_tasks = tasks.filter(function(task){
    return !task.done;
}).length;

document.getElementById("complete").innerHTML = "Completati: " + done_tasks;
document.getElementById("to_do").innerHTML = "Da Completare: " + todo_tasks;