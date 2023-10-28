from flask import Flask, jsonify
from Models.Station import Station
from background import start_station_update
from config import *

station = Station()
app = Flask(__name__)


@app.route('/api/get-position', methods=['GET'])
def get_position():
    '''Get realtime station position'''

    x, y = station.get_postion()
    response = jsonify({
        'x': x,
        'y': y
    })

    return response


if __name__ == '__main__':
    start_station_update(station=station, freq=UPDATE_FREQUENCY_SECONDS)
    app.run(debug=DEBUG)