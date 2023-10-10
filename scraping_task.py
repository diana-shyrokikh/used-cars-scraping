import pytz
from celery import Celery

from celery.schedules import crontab

from cars_scraping import get_all_cars
from utils import write_used_cars_data_json

kyiv_timezone = pytz.timezone("Europe/Kiev")

app = Celery(
    "scraping_task",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
)
app.conf.timezone = kyiv_timezone


@app.task
def start_cars_scraping():
    print("Scraping was started")

    get_all_cars()

    return "Task completed successfully"


@app.task
def start_dumping_db():
    print("Dumping db was started")

    write_used_cars_data_json()

    return "Task completed successfully"


app.conf.beat_schedule = {
    "start_cars_scraping": {
        "task": "scraping_task.start_cars_scraping",
        "schedule": crontab(hour=12, minute=0),
    },
    "start_dumping_db": {
        "task": "scraping_task.start_dumping_db",
        "schedule": crontab(hour=0, minute=0),
    },
}


if __name__ == "__main__":
    app.start()
