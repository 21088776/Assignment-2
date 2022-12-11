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

'''Plotting of Bar Chart begins here'''

# For loop for bar graph plot
for para in parameters_bar:

  df5_0 = df.loc[df['Country Name'] == sel_countries[0]]
  df5_1 = df5_0.loc[df5_0['Indicator Name'] == para]
  df5 = df5_1.iloc[0, 35::5]

  df6_0 = df.loc[df['Country Name'] == sel_countries[1]]
  df6_1 = df6_0.loc[df6_0['Indicator Name'] == para]
  df6 = df6_1.iloc[0, 35::5]

  df7_0 = df.loc[df['Country Name'] == sel_countries[2]]
  df7_1 = df7_0.loc[df7_0['Indicator Name'] == para]
  df7 = df7_1.iloc[0, 35::5]

  df8_0 = df.loc[df['Country Name'] == sel_countries[3]]
  df8_1 = df8_0.loc[df8_0['Indicator Name'] == para]
  df8 = df8_1.iloc[0, 35::5]

  df9_0 = df.loc[df['Country Name'] == sel_countries[4]]
  df9_1 = df9_0.loc[df9_0['Indicator Name'] == para]
  df9 = df9_1.iloc[0, 35::5]

  df10_0 = df.loc[df['Country Name'] == sel_countries[5]]
  df10_1 = df10_0.loc[df10_0['Indicator Name'] == para]
  df10 = df10_1.iloc[0, 35::5]

  df11_0 = df.loc[df['Country Name'] == sel_countries[6]]
  df11_1 = df11_0.loc[df11_0['Indicator Name'] == para]
  df11 = df11_1.iloc[0, 35::5]

  # Set width of bar
  barWidth = 0.05
  fig = plt.subplots(figsize = (10, 7))
  
  # Set height of bar
  year_0 = [df5[0], df6[0], df7[0], df8[0], df9[0], df10[0], df11[0]]
  year_1 = [df5[1], df6[1], df7[1], df8[1], df9[1], df10[1], df11[1]]
  year_2 = [df5[2], df6[2], df7[2], df8[2], df9[2], df10[2], df11[2]]
  year_3 = [df5[3], df6[3], df7[3], df8[3], df9[3], df10[3], df11[3]]
  year_4 = [df5[4], df6[4], df7[4], df8[4], df9[4], df10[4], df11[4]]
  year_5 = [df5[5], df6[5], df7[5], df8[5], df9[5], df10[5], df11[5]]
  
  # Set position of bar on X axis
  br1 = np.arange(7)
  br2 = [x + barWidth for x in br1]
  br3 = [x + barWidth for x in br2]
  br4 = [x + barWidth for x in br3]
  br5 = [x + barWidth for x in br4]
  br6 = [x + barWidth for x in br5]
  
  # Make the plot
  plt.bar(br1, year_0, color = 'r', width = barWidth,
          edgecolor = 'grey', label = df2.columns[1])
  plt.bar(br2, year_1, color ='g', width = barWidth,
          edgecolor = 'grey', label = df2.columns[2])
  plt.bar(br3, year_2, color ='b', width = barWidth,
          edgecolor = 'grey', label = df2.columns[3])
  plt.bar(br4, year_3, color ='y', width = barWidth,
          edgecolor = 'grey', label = df2.columns[4])
  plt.bar(br5, year_4, color ='c', width = barWidth,
          edgecolor = 'grey', label = df2.columns[5])
  plt.bar(br6, year_5, color ='k', width = barWidth,
          edgecolor = 'grey', label = df2.columns[6])

  # Adding Xticks
  plt.xlabel('Country Name', fontsize = 10)
  plt.ylabel('Value', fontsize = 10)
  plt.xticks([r + barWidth*2.5 for r in range(7)], 
        [sel_countries[0], sel_countries[1], sel_countries[2],
        sel_countries[3], sel_countries[4], sel_countries[5],
        sel_countries[6]])

  # Set Y axis to represent scientific values
  plt.ticklabel_format(axis = "y", style = "sci", scilimits = (0,0))

  # Plot the graph
  plt.legend()
  plt.show()

#-----End of for loop---------

'''Plotting of Line Chart begins here'''

parameters_line = ['Arable land (% of land area)', 
        'Forest area (% of land area)']

# For loop for line graph plot
for para1 in parameters_line:

  df5_0 = df.loc[df['Country Name'] == sel_countries[0]]
  df5_1 = df5_0.loc[df5_0['Indicator Name'] == para1]
  df5 = df5_1.iloc[0, 35::5]

  df6_0 = df.loc[df['Country Name'] == sel_countries[1]]
  df6_1 = df6_0.loc[df6_0['Indicator Name'] == para1]
  df6 = df6_1.iloc[0, 35::5]

  df7_0 = df.loc[df['Country Name'] == sel_countries[2]]
  df7_1 = df7_0.loc[df7_0['Indicator Name'] == para1]
  df7 = df7_1.iloc[0, 35::5]

  df8_0 = df.loc[df['Country Name'] == sel_countries[3]]
  df8_1 = df8_0.loc[df8_0['Indicator Name'] == para1]
  df8 = df8_1.iloc[0, 35::5]

  df9_0 = df.loc[df['Country Name'] == sel_countries[4]]
  df9_1 = df9_0.loc[df9_0['Indicator Name'] == para1]
  df9 = df9_1.iloc[0, 35::5]

  df10_0 = df.loc[df['Country Name'] == sel_countries[5]]
  df10_1 = df10_0.loc[df10_0['Indicator Name'] == para1]
  df10 = df10_1.iloc[0, 35::5]

  df11_0 = df.loc[df['Country Name'] == sel_countries[6]]
  df11_1 = df11_0.loc[df11_0['Indicator Name'] == para1]
  df11 = df11_1.iloc[0, 35::5]

  # First plot with X and Y data
  x = [df2.columns[0], df2.columns[1], df2.columns[2], df2.columns[3], 
       df2.columns[4], df2.columns[5]]
  y0 = [df5[0], df5[1], df5[2], df5[3], df5[4], df5[5]]
  y1 = [df6[0], df6[1], df6[2], df6[3], df6[4], df6[5]]
  y2 = [df7[0], df7[1], df7[2], df7[3], df7[4], df7[5]]
  y3 = [df8[0], df8[1], df8[2], df8[3], df8[4], df8[5]]
  y4 = [df9[0], df9[1], df9[2], df9[3], df9[4], df9[5]]
  y5 = [df10[0], df10[1], df10[2], df10[3], df10[4], df10[5]]
  y6 = [df11[0], df11[1], df11[2], df11[3], df11[4], df11[5]]

  plt.plot(x, y0, '-.', color = 'm', label = sel_countries[0])
  plt.plot(x, y1, '-.', color = 'k', label = sel_countries[1])
  plt.plot(x, y2, '-.', color = 'r', label = sel_countries[2])
  plt.plot(x, y3, '-.', color = 'g', label = sel_countries[3])
  plt.plot(x, y4, '-.', color = 'b', label = sel_countries[4])
  plt.plot(x, y5, '-.', color = 'c', label = sel_countries[5])
  plt.plot(x, y6, '-.', color = 'y', label = sel_countries[6])
  
  plt.xlabel("Year")
  plt.ylabel("Value")
  plt.title(para1)
  plt.legend(loc = 1, prop = {'size': 7})
  plt.show()

#-----End of for loop---------



