import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, jsonify, url_for
from main import rifugio

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "descrizione": "Welcome to my Shelter API",
        "altri link": {
            "Lista animali": url_for('get_animals'),
            "Check animale": url_for('get_animal', id = 'd1'),
            "Cibo per animale": url_for('get_animal_food', id = 'd1'),
            "Controlla adozione": url_for("check_adoption", id = 'd1')

        }
    })

@app.route('/animals')
def get_animals():    

    return jsonify(rifugio.list_all())

@app.route('/animal/<string:id>')
def get_animal(id: str):

    return jsonify(rifugio.get(id).info())

@app.route('/animal/<string:id>/food')
def get_animal_food(id: str):

    return jsonify(rifugio.get(id).daily_food_grams())

@app.route('/animal/<string:id>/adoption')
def check_adoption(id: str):

    return jsonify(rifugio.is_adopted(id))

if __name__ == "__main__":
    app.run(debug=True)
