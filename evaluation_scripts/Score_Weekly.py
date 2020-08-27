# This script can be used to score the 1 week and 2 week forecast forecasts
# Potential additions - 
# Make this a functiona
# Addd graphical outputs
# Make a better interface for assigning bonus points
# Set the class roster from a file.
# Read in the forecast start and stop dates from a file automatically

# %%
import pandas as pd
import numpy as np
import dataretrieval.nwis as nwis
import os

# %%
# User variables
forecast_num = 1
start_date = '2020-08-03'
stop_date =  '2020-08-04'
station_id = "09506000"

forecast_col ='2week'

# NOTE: Bonus points shoudl always be added on the 1week forecast
bonus_names = []
#bonus_names = ['condon', 'aschoff'] #people to give bonus points to

# setup a class roster
names=['name1', 'name2', 'name3']
nstudent=len(names)

# %%
# Read in everyone's forecast entries
forecasts=np.zeros(nstudent)

for i in range(nstudent):
    #i = 0
    filename = names[i] + '.csv'
    filepath = os.path.join('..', 'forecast_entries', filename)
    print(filepath)
    temp = pd.read_csv(filepath, index_col='Forecast')
    forecasts[i] = temp.loc[forecast_num, forecast_col]

# %%
# Read in the streamflow data and get the weekly average
obs_day = nwis.get_record(sites=station_id, service='dv',
                      start=start_date, end=stop_date, parameterCd='00060')
obs_week = np.mean(obs_day['00060_Mean'])
dif = abs(forecasts-obs_week)

# %%

#Make a data frame for the results
summary = pd.DataFrame({'start': start_date, 'end': stop_date, 'observation': obs_week,
                        'forecast': forecasts, 'Difference': dif}, index=names)

#Rank the forecasts
summary['ranking'] = summary['Difference'].rank(ascending=True, method='dense', na_option='bottom')

#Add points
summary['points'] = np.zeros(nstudent)
summary.loc[summary.ranking == 1, 'points'] = 2
summary.loc[summary.ranking == 2, 'points'] = 1
summary.loc[summary.ranking == 3, 'points'] = 1

# Add some bonus points
summary['bonus_points'] =np.zeros(nstudent)
summary.loc[bonus_names, 'bonus_points'] += 1

#Get the total points
summary['total_points'] = summary.bonus_points + summary.points

# %%
# Write out the reults
filename_out = forecast_col + '_forecast' + str(forecast_num) + '.csv'
filepath_out = os.path.join('..', 'weekly_results', filename_out)
summary.to_csv(filepath_out, index_label='name')
