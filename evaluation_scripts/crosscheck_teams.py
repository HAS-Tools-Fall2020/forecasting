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
        # this code is not showing the legend properly
       # fig, ax = plt.subplots()
        #ax.plot(df)
        #ax.set(title=team_name, xlabel="Forecast", ylabel="Flow Prediction (cfs)")
       #ax.legend()
        # this code I found online has a legend of the names but
        # does not have all the other great things, like title
        df.plot(legend=True)
        plt.show()




# %% User variables:
# forecast_week: the week number that you are judging.
#                Use number for week that just ended,
#                found in seasonal_forecst_Dates.pdf

forecast_num = 10  # week 11 (Danielle and Abigail, 11/10)

# Getting names
names = ef.getLastNames()
firstnames = ef.getFirstNames()
nstudent = len(names)

# Pull in everyones forecasts for a given week and write it out
forecasts = np.zeros((nstudent, 18))
for i in range(nstudent):
    #i = 0
    filename = names[i] + '.csv'
    filepath = os.path.join('..', 'forecast_entries', filename)
    print(filepath)
    temp = pd.read_csv(filepath, index_col='Forecast #')
    forecasts[i,:] = temp.loc[forecast_num][1:]

# put it into a data frame for labeling rows and columns
col_names = [str(x) for x in range(1, 19)]
forecastsDF = pd.DataFrame(data=forecasts, index=firstnames, columns=col_names)
teamsdf = forecastsDF

# Now to make lists of teams
team1 = ['Adam', 'Lourdes', 'Patrick', 'Ben']
team2 = ['Alcely', 'Shweta', 'Richard', 'Scott']
team3 = ['Camilo', 'Diana', 'Xenia', 'Danielle']
team4 = ['Alexa', 'Quinn', 'Abigail']
team5 = ['Jill', 'Mekha', 'Jake']

# Using the function on the teams

checkteam(team1, "Team 1")
checkteam(team2, "Team 2")
checkteam(team3, "Team 3")
checkteam(team4, "Team 4")
checkteam(team5, "Team 5")

# %%
