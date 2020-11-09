# This script is to make sure all individual team members have the same forecast
# Created by Danielle and Abigail (11/10/2020)

# %%
import pandas as pd
import numpy as np
import os
import eval_functions as ef
import dataretrieval.nwis as nwis
import matplotlib.pyplot as plt
import plot_functions as pf

# %%
def checkteam(member_list, team_name):
    ''' Check Team Forecasts:
    ----------------------------------------------
    This function checks whether or not team members have the same forecast.
    It calculates the standard deviation of team members forecasts,
    and if the standard devation is different than 0, then it will return a message
    and plot to see which team member deviated.
    ----------------------------------------------
    Parameters:
     - member_list: A previously defined list of team member names
     - team_name: The team name

    '''
    teamdf = pd.DataFrame()
    for i in member_list:
        f = teamsdf.loc[i]
        teamdf = teamdf.append(f)
    if teamdf.std == 0:
        print(team_name, "has has all the same forecasts")
    else:
        print("A team member in ", team_name, " does not have the same forecast")
        df = teamdf.T
        fig, ax = plt.subplots()
        ax.plot(df)
        ax.set(title=team_name, xlabel="Forecast", ylabel="Flow Prediction (cfs)")
        ax.legend()
        plt.show()




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
    temp = pd.read_csv(filepath, index_col='Forecast #')
    forecasts[i,:] = temp.loc[forecast_num][3:]

# %%
# From score_seaonal because the weekly one was being weird when I tried
# to combine it with seasonal
# User settings
forecast_num = 11
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
team3 = ['Camilo', 'Diana', 'Xenia', 'Danielle']
team4 = ['Alexa', 'Quinn', 'Abigail']
team5 = ['Jill', 'Mekha', 'Jake']

# %% Making a dataframe but with an added column for teams
teamsdf = forecastsDF

# this isn't working

# %% trying to create dataframes for each team
# team1 = [Adam, Lourdes, Patrick, Ben]
team1df = pd.DataFrame()
team2df = pd.DataFrame()
team3df = pd.DataFrame()
team4df = pd.DataFrame()
team5df = pd.DataFrame()

for i in team1:
    f = teamsdf.loc[i]
    team1df = team1df.append(f)

for i in team2:
    f = teamsdf.loc[i]
    team2df = team2df.append(f)

for i in team3:
    f = teamsdf.loc[i]
    team3df = team3df.append(f)

for i in team4:
    f = teamsdf.loc[i]
    team4df = team4df.append(f)

for i in team5:
    f = teamsdf.loc[i]
    team5df = team5df.append(f)

# %%
print(team5df)
# %%
team1df['stdev'] = team1df.std(axis=1)
team1df.describe()
print(team1df)

# %%
print(team1df.std())

# %%
if team1df.std == 0:
    print('All team members have the same forecast')
else:
    print('A team member does not have the same forecast as another')
    df = team1df.T
    fig, ax = plt.subplots()
    ax.plot(df)
    ax.set(title="Team 1", xlabel="Forecast", ylabel="Flow Prediction (cfs)")
    plt.show()

# %%
teamx = pd.DataFrame()
# %%
checkteam(team1, "Team 1")
# %%
