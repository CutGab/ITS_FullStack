# Navigazione dinamica

# Creare una pagina con elenco utenti fittizi e i relativi link ai loro profili generati con url_for.

from flask import Flask, url_for

app = Flask (__name__)

@app.route('/')
def show_home() -> str:
    return f"""
    
    <h1> Benvenuto! </h1> <br>

    <h3> <a href="{url_for("show_utenti")}"> Staff del nostro sito </a> </h3>

    """

@app.route('/utenti')
def show_utenti() -> str:
    return f"""
    
    <a href="{url_for("show_user_profile", username = "Gabriele", age = 21)}"> Gabriele </a> <br>
    <a href="{url_for("show_user_profile", username = "Anna", age = 19)}"> Anna </a> <br>
    <a href="{url_for("show_user_profile", username = "Luca", age = 22)}"> Luca </a> <br>



    """

@app.route('/user/<string:username>/age/<int:age>')
def show_user_profile(username: str, age: int) -> str:
    return f"<h1> Nome: {username} <br> Età: {age}<h1>"

app.run(debug=True)