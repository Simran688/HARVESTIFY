# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 09:12:36 2024

@author: hp
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 22:12:45 2024
@author: hp
"""

import flask
import logging
import pickle
import pandas as pd
from datetime import datetime
import random
import json
import requests
from flask import redirect

app = flask.Flask(__name__)

def initialize_logging():
    # Initialize logging
    logging.basicConfig(filename='FlaskApp.log', level=logging.INFO)
    
@app.route('/crop', methods=['GET'])
def predict_crop():
    try:
        # Simulated data retrieval from external sources
        random.seed(datetime.now())
        url = "https://api.thingspeak.com/channels/1026655/feeds.json?api_key=AA58RVXIO5E9T336&results=2"
        humidity_url = "http://blynk-cloud.com/TtGVPcqUUMtN8vr1xqU680Fv0TXxHEUm/get/V7"
        temperature_url = "http://blynk-cloud.com/TtGVPcqUUMtN8vr1xqU680Fv0TXxHEUm/get/V8"
        
        # Mock response for demonstration purposes
        response = {
            'crop': 'Rice',
            'soil_moisture': 'Medium'
        }
        
        return json.dumps(response)  # Return predicted crop and soil moisture
    except Exception as e:
        logging.error("Error in predict_crop: " + str(e))
        return "Caught error: " + str(e)

@app.route('/fertilizer', methods=['GET'])
def fert_recommend():
    try:
        # Simulated fertilizer recommendation based on crop and soil parameters
        response = {
            'fertilizer': 'NPK 10-10-10'
        }
        
        return json.dumps(response)  # Return recommended fertilizer
    except Exception as e:
        logging.error("Error in fert_recommend: " + str(e))
        return "Caught error: " + str(e)

@app.route('/index', methods=['GET'])
def redirect_to_index():
    return "Super Awesome code is running in the background!!"

if __name__ == "__main__":
    initialize_logging()
    app.run(debug=True, port=5000)
