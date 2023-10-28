import time
import atexit

from apscheduler.schedulers.background import BackgroundScheduler
from Models.Station import Station

scheuler = BackgroundScheduler


def start_station_update(station: Station, freq: int):
    global scheduler
    scheuler.add_job(station.update(), trigger='interval', seconds=freq)
    scheuler.start()
