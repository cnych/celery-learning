# -*- coding: utf-8 -*-
import time
from celery import Celery


broker = 'redis://localhost:6379/1'
backend = 'redis://localhost:6379/2'
app = Celery('my_task', broker=broker, backend=backend)


@app.task
def add(x, y):
    print 'enter call func....'
    time.sleep(4)
    return x + y
