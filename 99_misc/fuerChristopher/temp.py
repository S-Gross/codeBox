# import of numpy, pandas and matplotlib
import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt



# read the csv data from Desktop
data_household_power_consumption = pd.read_csv('Test.csv', sep=';', parse_dates=['Date'])

# mark the first line as header
data_household_power_consumption.head()




# print the dtypes -> all variables are objects
#print(data_household_power_consumption.dtypes)

#print some statistics
#print(data_household_power_consumption.describe())

# downsize the DataFrame to 'Global_active_power' and 'Voltage'
data_plot = data_household_power_consumption[['Global_active_power', 'Voltage']]
data_plot.head()


for idx, ele in enumerate( data_plot["Voltage"]):
    print(str(idx))
    print(float(ele))

#print(data_plot)



#Hier fängt der Fehler an. Ziel ist es Voltage über Global_active_power zu plotten.
#Dazu würde ich gerne die Objekte zu einem float umschreiben lassen. Dabei bekomme ich aber einen Fehler


#data_plot = data_plot.astype(float)

#plt.plot(data_household_power_consumption['Global_active_power'], data_household_power_consumption['Voltage'])
plt.plot(data_household_power_consumption['Global_active_power'])


plt.show()
"""