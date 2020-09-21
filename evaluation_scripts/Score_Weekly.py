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
# forecast num refers to the forecast issue number. This is the same as the row number
# in the forecast entries csv. 
# refer to Weekly_Frorecast_Date.pdf for the 1 and 2 week forecast dates associated with each foreacst

#Set these  to the dates of the previous week, this is the week you will be evaluating
start_date = '2020-09-06'
stop_date =  '2020-09-12'

#select the forecast number and forecast week these dates correspond to
forecast_num = 2
forecast_col ='1week'

# %%
station_id = "09506000"

# list of students in the class
names=['ferre', 'fierro', 'hsieh', 'hull', 'kahler', 'lau', 'marcelain',
        'marcovecchio', 'medina', 'mitchell', 'narkhede',
        'neri', 'noonan', 'pereira', 'ridlinghaver', 'salcedo',
        'schulze', 'stratman', 'tadych']
firstnames=['Ty', 'Lourdes', 'Diana', 'Quinn', 'Abagail', 'Alcely', 'Richard',
        'Alexa', 'Xenia', 'Ben', 'Shweta',
        'Patrick', 'Jill', 'Mekha', 'Jake', 'Camilo',
        'Scott', 'Adam', 'Danielle']
nstudent=len(names)

# %%
# Read in everyone's forecast entries
forecasts=np.zeros(nstudent)

for i in range(nstudent):
    #i = 0
    filename = names[i] + '.csv'
    filepath = os.path.join('..', 'forecast_entries', filename)
    print(filepath)
    temp = pd.read_csv(filepath, index_col='Forecast #')
    print(temp.loc[forecast_num, forecast_col])
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
                        'forecast': forecasts, 'Difference': dif}, index=firstnames)

#Rank the forecasts
summary['ranking'] = summary['Difference'].rank(ascending=True, method='dense', na_option='bottom')

#Add points
summary['points'] = np.zeros(nstudent)
summary.loc[summary.ranking == 1, 'points'] = 2
summary.loc[summary.ranking == 2, 'points'] = 1
summary.loc[summary.ranking == 3, 'points'] = 1

# %%
# Write out the reults
filename_out = 'forecast' + str(forecast_num) + '_' + forecast_col + '.csv'
filepath_out = os.path.join('..', 'weekly_results', filename_out)
summary.to_csv(filepath_out, index_label='name')


# %%
# print a summary
print(forecast_col, 'Forecast (', start_date, '-', stop_date, ')')
print('Observed Flow =', obs_week)
print('Frist Place = ', list(summary.loc[summary['ranking']==1].index), 
        'flow forecast = ', summary.loc[summary['ranking']==1, 'forecast'].head(1).values)
print('Second Place = ', list(summary.loc[summary['ranking']==2].index), 
        'flow forecast = ', summary.loc[summary['ranking']==2, 'forecast'].head(1).values)
print('Third Place = ', list(summary.loc[summary['ranking']==3].index), 
        'flow forecast = ', summary.loc[summary['ranking']==3, 'forecast'].head(1).values)

# %%
