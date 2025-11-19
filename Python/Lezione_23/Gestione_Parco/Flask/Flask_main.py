import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, jsonify, url_for
from Main import my_park

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "descrizione": "Welcome to Park API",
        "altri link": {
            "Tutte le giostre": url_for('list_rides'),
            "Giostra_1": url_for('get', id = "1"),
            "Giostra_2": url_for('get', id = "2"),
            "Tempo Attesa Giostra 1": url_for("get_wait", id = 1),
            "Tempo Attesa Giostra 2": url_for("get_wait", id = 2)

        }
    })

@app.route('/rides')
def list_rides():
    rides_info = []
    
    for ride in my_park.list_all():

        rides_info.append(ride.info())

    return jsonify(rides_info)

@app.route('/rides/<string:id>')
def get(id:str):
    return jsonify(my_park.get(id).info())

@app.route('/rides/<string:id>/wait', defaults = {"crowd":1.0})
@app.route('/rides/<string:id>/wait/<float:crowd>')
def get_wait(id: str, crowd: float):
    
    ride = my_park.get(id)
    wait = ride.wait_time(crowd_factor = crowd)
    return jsonify({"Tempo attesa": wait})


if __name__ == "__main__":
    app.run(debug=True)
