# This script downloads the observations from USGS aggreages to 
# weekly and saves as a csv
# Potential additions:
# Make this a function 
# Modify so it reads in the previous observation file and only adds in the new obs
# Read in all the data and once and aggreate to weekly in  one step using dates

# %%
import pandas as pd
import numpy as np
import dataretrieval.nwis as nwis
import os
#print(os.getcwd())

# %% 
# User settings
forecast_num = 4
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
    starti = date_table.loc[i, 'start_date']
    endi = date_table.loc[i, 'end_date']
    obs_day = nwis.get_record(sites=station_id, service='dv',
                          start=starti, end=endi, parameterCd='00060')
    #print(i)
    #print(np.mean(obs_day['00060_Mean']))
    date_table.loc[i, 'observed'] = np.mean(obs_day['00060_Mean'])

# %%
# Write the updated observations out
filepath_out = os.path.join('..','weekly_results', 'weekly_observations.csv')
date_table.to_csv(filepath_out, index_label='forecast_week')
