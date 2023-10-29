import atexit

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, jsonify
from Models.Station import Station
from app.config import *

station = Station()
app = Flask(__name__)


@app.route('/')
def index():
    return str(station.get_position())


@app.route('/api/get-position', methods=['GET'])
def get_position():
    """Get realtime station position"""

    x, y = station.get_position()
    response = jsonify({
        'x': x,
        'y': y
    })

    return response


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(lambda: station.update(), trigger='interval', seconds=UPDATE_FREQUENCY_SECONDS)
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())

    app.run(debug=DEBUG)
