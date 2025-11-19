# Generazione link interni

# Usare url_for per creare automaticamente i link alle route definite, ed esporli in una pagina principale (homepage con link a /about, /user/..., ecc.).

from flask import Flask, url_for

app = Flask (__name__)

@app.route('/')
def show_home() -> str:
    return f"""
    
    <a href="{url_for("show_about")}">About</a>
    <a href="{url_for("show_user_profile", username = "Gabriele", age = 21)}"> You </a>

    """


@app.route('/about')
def show_about() -> str:
    return f"""
    
    <h3> GlowTrack helps you build healthy habits effortlessly. <br>
    Set goals, track progress, and celebrate small wins with a simple, colorful interface that keeps you motivated every day. <h3>

    """

@app.route('/user/<string:username>/age/<int:age>')
def show_user_profile(username: str, age: int) -> str:
    return f"<h1> Ciao, {username}!\n{age} anni.<h1>"

app.run(debug=True)