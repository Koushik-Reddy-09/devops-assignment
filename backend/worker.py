from celery import Celery
import time

# Configure Celery to use Redis as the message broker
celery = Celery(
    "worker", 
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/1",  
)


@celery.task
def write_log_celery(message: str):
    time.sleep(10)
    with open("log_celery.txt", "a") as f:
        f.write(f"{message}\n")
    return f"Task completed: {message}"

