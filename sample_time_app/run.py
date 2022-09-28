from flask import Flask
from datetime import datetime
import pendulum
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def get_current_time():
    time_ny = pendulum.timezone('America/New_York') 
    NY = datetime.now(time_ny)
    return NY.strftime("%H:%M:%S")

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
