# Definire una route /about che ritorni un breve testo HTML con descrizione dell’app o dell’autore.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return "<h1> Home <h1>"

@app.route('/about')
def show_about() -> str:
    return f"""
    
    <h3> GlowTrack helps you build healthy habits effortlessly. <br>
    Set goals, track progress, and celebrate small wins with a simple, colorful interface that keeps you motivated every day. <h3>

    """

app.run(debug=True)