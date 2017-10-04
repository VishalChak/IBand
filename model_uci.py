# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 18:31:28 2017

@author: 10639497
"""

path = "D:\\Vishal\\IBand\\DataSet\\statlogHeart\\train.csv"

import pandas as pd

df = pd.read_csv(path)

print(df.head())