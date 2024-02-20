# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 22:28:31 2024

@author: hp
"""

# initialization.py

def run_flask_app_internal():
    from app_config import app
    app.run(port=5555, host="0.0.0.0")
