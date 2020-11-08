# This script is to make sure all individual team members have the same forecast
# Created by Danielle and Abigail (11/10/2020)

# %%
import pandas as pd
import numpy as np
import os
import eval_functions as ef
import dataretrieval.nwis as nwis
import plot_functions as pf

# %% User variables:
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
# From score_seaonal because the weekly one was being weird when I tried
# to combine it with seasonal
# User settings
forecast_num = 2
names = ef.getLastNames()
firstnames = ef.getFirstNames()
nstudent = len(names)

# %% 
# Pull in everyones forecasts for a given week and write it out
forecasts = np.zeros((nstudent, 18))
for i in range(nstudent):
    #i = 0
    filename = names[i] + '.csv'
    filepath = os.path.join('..', 'forecast_entries', filename)
    print(filepath)
    temp = pd.read_csv(filepath, index_col='Forecast #')
    forecasts[i,:] = temp.loc[forecast_num][1:]

# %%
# put it into a data frame for labeling rows and columns
col_names = [str(x) for x in range(1, 19)]
forecastsDF = pd.DataFrame(data=forecasts, index=firstnames, columns=col_names)
# %%
# Now to make lists of teams
team1 = ['Adam', 'Lourdes', 'Patrick', 'Ben']
team2 = ['Alcely', 'Shweta', 'Richard', 'Scott']
team3 = ['Camillo', 'Diana', 'Xenia', 'Danielle']
team4 = ['Alexa', 'Quinn', 'Abagail']
team5 = ['Gillian', 'Mekha', 'Jacob']

# %% Making a dataframe but with an added column for teams
teamsdf = forecastsDF

# %%
# I think we need some for loops up in there but I can't for loop right now
# because I already forgot how for loops work, despite learning them like 5x
# ~Danielle
for i in teamsdf:
    if teamsdf['index' == i]:
        teamsdf['team_number' == 1]

# %% for later    
elif teamsdf['index' == team2]:
    teamsdf['team_number' == 2]


# %%
