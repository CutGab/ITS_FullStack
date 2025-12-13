const persona = {
    id: 1,
    contatto: {
        nome: "vattela",
        email: "vattelapesca@gmail.com"
    }
};

const {contatto: {nome, email}} = persona;

document.getElementById("content").innerHTML = `<h1>${nome}</h1><p>${email}</p>`;