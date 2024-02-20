# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 09:15:21 2024

@author: hp
"""

import tkinter as tk
from tkinter import messagebox
import logging
import pickle
import pandas as pd
from datetime import datetime
import random
import json
import requests

def initialize_logging():
    # Initialize logging
    logging.basicConfig(filename='FlaskApp.log', level=logging.INFO)

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
        
        messagebox.showinfo("Predicted Crop", f"Predicted Crop: {response['crop']}\nSoil Moisture: {response['soil_moisture']}")
    except Exception as e:
        logging.error("Error in predict_crop: " + str(e))
        messagebox.showerror("Error", "An error occurred while predicting the crop.")

def fert_recommend():
    try:
        # Simulated fertilizer recommendation based on crop and soil parameters
        response = {
            'fertilizer': 'NPK 10-10-10'
        }
        
        messagebox.showinfo("Recommended Fertilizer", f"Recommended Fertilizer: {response['fertilizer']}")
    except Exception as e:
        logging.error("Error in fert_recommend: " + str(e))
        messagebox.showerror("Error", "An error occurred while recommending fertilizer.")

def create_gui():
    root = tk.Tk()
    root.title("Crop Prediction and Fertilizer Recommendation")

    predict_button = tk.Button(root, text="Predict Crop", command=predict_crop)
    predict_button.pack(pady=10)

    fertilizer_button = tk.Button(root, text="Recommend Fertilizer", command=fert_recommend)
    fertilizer_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    initialize_logging()
    create_gui()
