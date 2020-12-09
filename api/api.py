'''
This module is the Flask endpoint for matchpoint's API backend. 

Use the 'api' namespace for all routes within this app.
'''
import time
from flask import Flask

app = Flask(__name__)

@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}
