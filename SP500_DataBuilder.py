# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 08:44:21 2023

@author: Hunt Gather Trade
"""
from datetime import datetime, timedelta

# import yfinance as yf
import pandas as pd
import numpy as np

import sqlalchemy
import mysql.connector

start_date = "2023-01-01"
end_date = (datetime.today() + timedelta(days = 1)).strftime("%Y-%m-%d")