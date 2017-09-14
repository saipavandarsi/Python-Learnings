from celery import Celery
import json

app = Celery()


@app.task
def json_reader():
    json_data = open('cost_response.json').read()
    data = json.loads(json_data)
    print(data)
    return data