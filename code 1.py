
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.cm as cm
import seaborn as sns
from pandas import DataFrame, read_csv

file_name = "worldbankapi.csv"

def data():
        '''
        Retrieve data from the CSV and extract the required 
        columns and rows
        '''
        df = pd.read_csv("/content/drive/My Drive/Colab Notebooks/"+file_name)
        df_t = df.transpose()
        # years in columns
        df_1_ = df.iloc[0:0, 4:]  

        # Last 6 years in columns for consideration
        df1 = df.iloc[0:0, 35::5] 
        df2 = df1.dropna()

        # Unique contries in the column
        df3 = df.iloc[2:, 0]
        df4 = df3.unique()

parameters_bar = ['Total greenhouse gas emissions (kt of CO2 equivalent)',
              'CO2 emissions (kg per PPP $ of GDP)']

sel_countries = ['Bangladesh', 'Brazil', 'Canada','China',
                 'France','India','United Kingdom']

df = pd.read_csv("/content/drive/My Drive/Colab Notebooks/"+file_name)
df2 = df.iloc[0:0, 35::5].dropna()
df4 = df.iloc[2:, 0].unique()
