# This script can be used to score the 1 week and 2 week forecast forecasts

# You should run this script twice first to judge the one week forecasts from last week
# And then to judge the two week forecasts from two weeks ago

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
# forecast_week is the week number that you are going to be judging. 
# You can find this in the seasonal_forecst_Dates.pdf 
# You should look up the forecast number for the week that just ended
forecast_week = 4                       # Changed to week 5 by Schulze. 9/22/20

# %%
station_id = "09506000"

# list of students in the class
names=['ferre', 'fierro', 'hsieh', 'hull', 'kahler', 'lau', 'marcelain',
        'marcovecchio', 'medina', 'mitchell', 'narkhede',
        'neri', 'noonan', 'pereira', 'ridlinghaver', 'salcedo',
        'schulze', 'stratman', 'tadych']
firstnames=['Ty', 'Lourdes', 'Diana', 'Quinn', 'Abigail', 'Alcely', 'Richard',
        'Alexa', 'Xenia', 'Ben', 'Shweta',
        'Patrick', 'Jill', 'Mekha', 'Jake', 'Camilo',
        'Scott', 'Adam', 'Danielle']
nstudent=len(names)


datefile = os.path.join('..', 'Seasonal_Foercast_Dates.csv')
forecast_dates=pd.read_csv(datefile, index_col='forecast_week')

start_date = forecast_dates.loc[forecast_week, 'start_date']
stop_date = forecast_dates.loc[forecast_week, 'end_date']

print("Evaluating forecasts for", start_date, 'To', stop_date)


# %%
# Read in everyone's forecast entries
forecasts1=np.zeros(nstudent) # The 1week forecasts for this week
forecasts2=np.zeros(nstudent) # The 2week forecasts for this week

for i in range(nstudent):
    #i = 0
    filename = names[i] + '.csv'
    filepath = os.path.join('..', 'forecast_entries', filename)
    print(filepath)
    temp = pd.read_csv(filepath, index_col='Forecast #')
    #print(temp.loc[(forecast_week - 1), '1week'])
    forecasts1[i] = temp.loc[(forecast_week - 1), '1week']
    forecasts2[i] = temp.loc[(forecast_week - 2), '2week']

# %%
# Read in the streamflow data and get the weekly average
obs_day = nwis.get_record(sites=station_id, service='dv',
                      start=start_date, end=stop_date, parameterCd='00060')
obs_week = np.mean(obs_day['00060_Mean'])
dif1 = abs(forecasts1-obs_week)
#dif2 = np.zeros(nstudent)
dif2 = abs(forecasts2-obs_week)

print('Average streamflow for this week:', np.round(obs_week,3))

# %%

# New block added by Schulze 9/22/20, for assigning the names to a 3-d array 
# with first and last names, sorted alphabetically. The 3 students to get a point are 
# randomly chosen and their names returned.

np.array(firstnames).sort()






# %%
#Make a data frame for the results
summary = pd.DataFrame({'start': start_date, 'end': stop_date, 'observation': obs_week,
                        '1week_forecast': forecasts1, '1week_difference': dif1, 
                        '2week_forecast': forecasts2, '2week_difference': dif2}, index=firstnames)

#Rank the forecasts
summary['1week_ranking'] = summary['1week_difference'].rank(ascending=True, method='dense', na_option='bottom')
summary['2week_ranking'] = summary['2week_difference'].rank(ascending=True, method='dense', na_option='bottom')


#Add points for the 1 week forecasts
summary['1week_points'] = np.zeros(nstudent)
summary.loc[summary['1week_ranking'] == 1, '1week_points'] = 2
summary.loc[summary['1week_ranking'] == 2, '1week_points'] = 1
summary.loc[summary['1week_ranking'] == 3, '1week_points'] = 1

#Add points for the 2 week forecasts
summary['2week_points'] = np.zeros(nstudent)
summary.loc[summary['2week_ranking'] == 1, '2week_points'] = 2
summary.loc[summary['2week_ranking'] == 2, '2week_points'] = 1
summary.loc[summary['2week_ranking'] == 3, '2week_points'] = 1

#summary['2week_ranking'] = 0
#summary['2week_points'] = 0

# %%
# Write out the reults
filename_out = 'forecast_week' + str(forecast_week) + '_results.csv'
filepath_out = os.path.join('..', 'weekly_results', filename_out)
summary.to_csv(filepath_out, index_label='name')


# %%
# print a summary
print('1 Week Forecast (', start_date, '-', stop_date, ')')
print('Observed Flow =', round(obs_week,3))
print('Frist Place = ', list(summary.loc[summary['1week_ranking']==1].index), 
        'flow forecast = ', summary.loc[summary['1week_ranking']==1, '1week_forecast'].head(1).values)
print('Second Place = ', list(summary.loc[summary['1week_ranking']==2].index), 
        'flow forecast = ', summary.loc[summary['1week_ranking']==2, '1week_forecast'].head(1).values)
print('Third Place = ', list(summary.loc[summary['1week_ranking']==3].index), 
        'flow forecast = ', summary.loc[summary['1week_ranking']==3, '1week_forecast'].head(1).values)

print('2 Week Forecast (', start_date, '-', stop_date, ')')
print('Observed Flow =', round(obs_week,3))
print('Frist Place = ', list(summary.loc[summary['2week_ranking']==1].index), 
        'flow forecast = ', summary.loc[summary['2week_ranking']==1, '2week_forecast'].head(1).values)
print('Second Place = ', list(summary.loc[summary['2week_ranking']==2].index), 
        'flow forecast = ', summary.loc[summary['2week_ranking']==2, '2week_forecast'].head(1).values)
print('Third Place = ', list(summary.loc[summary['2week_ranking']==3].index), 
        'flow forecast = ', summary.loc[summary['2week_ranking']==3, '2week_forecast'].head(1).values)


# %%

# Add Histogram of results, plots each student's guess, and 