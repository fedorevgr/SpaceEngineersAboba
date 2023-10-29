from apscheduler.schedulers.background import BackgroundScheduler
from Models.Station import Station


def start_station_update(scheduler: BackgroundScheduler, station: Station, freq: int) -> None:
    scheduler.add_job(lambda x: station.update(), trigger='interval', seconds=freq)
    scheduler.start()
