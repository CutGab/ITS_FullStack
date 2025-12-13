let nomi = [
    "Luca",
    "Andrea",
    "Lorenzo",
    "Davide",
    "Erald",
    "Marco"
];

const input = document.getElementById("contentInput");
const content = document.getElementById("content");

function updateList() {

    const value = input.value.toLowerCase();

    const filtered = nomi.filter(name => name.toLowerCase().startsWith(value));

    const oldResults = content.querySelectorAll(".name");
    oldResults.forEach(el => el.remove());

    filtered.forEach(name => {
        content.insertAdjacentHTML("beforeend",`<p class="name">${name}</p>`);
    });
};

document.getElementById("contentInput").addEventListener("input", updateList);