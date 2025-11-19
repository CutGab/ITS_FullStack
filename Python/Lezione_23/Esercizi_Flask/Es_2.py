# Route dinamica per profilo utente

# Creare un percorso /user/<nome> che restituisca “Benvenuto, <nome>!”.

# Testare con nomi diversi nell’URL.

# Route con parametri numerici

# Definire /square/<int:n> che ritorni il quadrato di n.

# Parametri multipli

# Creare /sum/<int:a>/<int:b> che restituisca la somma dei due numeri.

from flask import Flask

app = Flask (__name__)

@app.route('/')
def home():
    return "<h1> Home <h1>"

@app.route('/user/<string:nome>')
def show_user(nome: str) -> str:
    return f"<h1> Benvenuto, {nome}! <h1>"

@app.route('/square/<int:n>')
def show_square(n: int) -> str:
    return f"<h1> {n**2} <h1>"

@app.route('/sum/<int:j>/<int:k>')
def show_sum(j: int, k: int) -> str:
    return f"<h1> {j + k} <h1>"

app.run(debug=True)