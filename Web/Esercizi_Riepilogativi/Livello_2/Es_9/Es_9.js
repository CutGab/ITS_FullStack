const piatto = {ingrediente1: "pasta", ingrediente2: "sugo", ingrediente3: "olio"};

let new_piatto = {...piatto,ingrediente2: "pomodoro"};

document.getElementById("content").innerHTML = `<h1> 
                                                    Ingrediente 1: ${new_piatto.ingrediente1} <br> 
                                                    Ingrediente 2: ${new_piatto.ingrediente2} <br> 
                                                    Ingrediente 3: ${new_piatto.ingrediente3} <br>
                                                </h1>`;
