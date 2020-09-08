# This script downloads the observations from USGS aggreages to 
# weekly and saves as a csv

# we are using the climata package to download data
# if you don't have it installed you will need to 
# pip install cliamata before you start

# here is a climata example:
# https://www.earthdatascience.org/tutorials/acquire-and-visualize-usgs-hydrology-data/


# Potential additions:
# Make this a function 
# Modify so it reads in the previous observation file and only adds in the new obs
# Read in all the data and once and aggreate to weekly in  one step using dates

# %%
import pandas as pd
import numpy as np
import os
from climata.usgs import DailyValueIO
#print(os.getcwd())

# Climata tutorial 
# %% 
# User settings
# refer to Seasonal_Forecast_Dates.pdf for the 
# list of dates associated with each forecast week
# you should set forecast_week equal to the forecast
# week that just completed
forecast_week = 2
station_id = "09506000"

# %%
#read in the forecast data and setup a dataframe
filepath = os.path.join('..', 'Seasonal_Foercast_Dates.csv')
print(filepath)
date_table = pd.read_csv(filepath, index_col='forecast_week')

date_table['observed'] = np.empty(len(date_table))
date_table.observed = np.nan

# %%
# Read in the observations and get weekly averages
for i in range(1, forecast_num+1):
    print(i)
    starti = date_table.loc[i, 'start_date']
    endi = date_table.loc[i, 'end_date']

    #read in the data from USGS
    data = DailyValueIO(
        start_date=starti,
        end_date=endi,
        station=station_id,
        parameter='00060',
    )

    #format the flow and dates into lists
    for series in data:
        flow = [r[1] for r in series.data]
        dates = [r[0] for r in series.data]
    
    print(dates)
    date_table.loc[i, 'observed'] = np.mean(flow)


# %%
# Write the updated observations out
filepath_out = os.path.join('..','weekly_results', 'weekly_observations.csv')
date_table.to_csv(filepath_out, index_label='forecast_week')


# %%

