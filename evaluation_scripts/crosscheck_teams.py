# This script is to make sure all individual team members have the same forecast
# Created by Danielle and Abigail (11/10/2020)

# %%
import pandas as pd
import numpy as np
import os
import eval_functions as ef
import dataretrieval.nwis as nwis
import plot_functions as pf

# User variables:
# forecast_week: the week number that you are judging.
#                Use number for week that just ended,
#                found in seasonal_forecst_Dates.pdf

forecast_num = 11  # week 11 (Danielle and Abigail, 11/10)

# get list of students in the class using functions
names = ef.getLastNames()
firstnames = ef.getFirstNames()
nstudent = len(names)

# get start and end date of forecast week for 1 wk forecast
forecasts = np.zeros((nstudent, 16))
for i in range(nstudent):
    #i = 0
    filename = names[i] + '.csv'
    filepath = os.path.join('..', 'forecast_entries', filename)
    print(filepath)
    temp = pd.read_csv(filepath, index_col='Forecast')
    forecasts[i,:] = temp.loc[forecast_num][3:]

# %%
