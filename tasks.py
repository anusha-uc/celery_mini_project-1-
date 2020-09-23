from celery import Celery
import virtualenv
from time import sleep
import eventlet
app=Celery('tasks',broker='amqp://localhost',
            backend='rpc://')

@app.task

def longtime_add(time_input):
    print ('long time task begins')
    # sleep 5 seconds
    sleep(5)
    print ('long time task finished')
    if time_input < 12:
        return "Input given is less than 12"
    elif time_input == 12:
        return "Input given is 12"
    else:
        return "Input given is greater than 12"
