from flask import Flask, jsonify, url_for
from Main import fm

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "descrizione": "Welcome to Rent Service API",
        "Links": {
            "Lista veicoli": url_for('get_veicoli'),
            "Ford Transit": url_for('get_veicolo', plate_id = "XY789ZT"),
            "BMW Z4": url_for('get_veicolo', plate_id = "EF456GH"),
            "Tempo Preparazione Ford Transit": url_for('get_preptime', plate_id = "XY789ZT" ),
            "Tempo Preparazione BMW Z4": url_for('get_preptime', plate_id = "EF456GH" )
        }
    })

@app.route('/vehicles')
def get_veicoli():    

    return jsonify(fm.list_all())

@app.route('/vehicles/<string:plate_id>')
def get_veicolo(plate_id: str):

    veicolo = fm.get(plate_id)
    return jsonify(veicolo.__dict__)

@app.route('/vehicles/<string:plate_id>/prep-time', defaults={"factor": 1.0})
@app.route('/vehicles/<string:plate_id>/prep-time/<float:factor>')
def get_preptime(plate_id: str, factor: float):

    veicolo = fm.get(plate_id)
    return jsonify(veicolo.estimated_prep_time(factor))

@app.route('/vehicles/<string:plate_id>', methods = ['POST'])
def create_vehicle(plate_id: str):

    veicolo = request.get_json()


if __name__ == "__main__":
    app.run(debug=True)
