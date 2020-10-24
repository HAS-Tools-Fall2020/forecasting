
# Script for assigning bonus points for week 9

# Author: Shweta Narkhede and Camilo Salcedo
# Created on: Oct 24th, 2020
# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import dataretrieval.nwis as nwis
import os
import eval_functions as ef

# %%
forecast_week = 8   # week 8 (Lourdes/Alexa 10/19/20)

# %%
station_id = "09506000"

# list of students in the class
# get lists using functions in eval_functions.py
names = ef.getLastNames()
firstnames = ef.getFirstNames()
nstudent = len(names)

# get start and stop dates using functions in eval_functions.py
dates = ef.weekDates(forecast_week)
start_date = dates[0]
stop_date = dates[1]

print("Evaluating forecasts up to", start_date, 'To', stop_date)

# %%
# Setting up a list of week numbers to be used in plotting
weeks = []
for i in range(16):
    # this is done because python counts 1 behind
    weeks.append('week_' '%s' % (i+1))

# %%
# mamking two empty arrays to  hold the forecasts
forecasts_1 = np.zeros([nstudent, len(weeks)])  # 1wk forecast for this week
forecasts_2 = np.zeros([nstudent, len(weeks)])  # 2wk forecasts for this week

# Reading the individual student forecast csvs
# to populate the dataframe
for i in range(nstudent):
    filename = names[i] + '.csv'
    filepath = os.path.join('..', 'forecast_entries', filename)
    print(filepath)
    temp = pd.read_csv(filepath, index_col='Forecast #')
    for n in range(1, forecast_week+1):
        forecasts_1[i, n-1] = temp.loc[(n), '1week']
        forecasts_2[i, n-1] = temp.loc[(n), '2week']

# %%
# compiled into data frames you can use for graphing
weekly_forecast1w = pd.DataFrame({}, index=firstnames)
weekly_forecast2w = pd.DataFrame({}, index=firstnames)

for i in range(16):
    weekly_forecast1w.insert(i, 'week_%s' % (i+1), forecasts_1[:, i], True)
    weekly_forecast2w.insert(i, 'week_%s' % (i+1), forecasts_2[:, i], True)

# everything above this can be copied
# and pasted into your analysis

# %%
# Week 7 addition, create dataframe containing weekly flows
# NOTE: Must first run Get_Observations.py script
weekly_flows = pd.read_csv("../weekly_results/weekly_observations.csv")

# %% Week 7 addition, format new dataframes for
# weekly plotting, and assign same index
# trim and tanspose to make plotting easier
weekly_forecast1w_graph = weekly_forecast1w.iloc[:, 0:forecast_week-1].T
weekly_forecast2w_graph = weekly_forecast2w.iloc[:, 0:forecast_week-1].T
# trim and set index the same, weekly flow start 8/23
# while student forecasts start 8/30 so need to trim dataset
weekly_flows_graph = weekly_flows.iloc[1:forecast_week, 3:4]
weekly_flows_graph.set_index(weekly_forecast1w_graph.index,
                             append=False, inplace=True)


# %%
# WE CAN DELETE ABOVE PART IF WE RUN CODE AFTER RUNNING FORECAST ANALYSIS
# %%
# This week's bonus points goes to those who has highest error in prediction
# between consecutive weekly flow

# Getting differences between consecutive weekly average flows
obs_var = np.diff(weekly_flows['observed'], axis=0)
pred_var = np.subtract(forecasts_2, forecasts_1)

# For loop for getting errors in weekly prediction for each student
err = np.zeros([nstudent, 6])
max_err = np.zeros([nstudent, 1])
for i in range(nstudent):
    err[i] = (obs_var[0:6] - pred_var[i][0:6])
    # max error in consecutive week pred difference
    max_err[i] = np.max(np.absolute(err[i]))

max_error_df = pd.DataFrame(names, columns=['Names'])
max_error_df['Max error in prediction'] = max_err
max_error_df = max_error_df.sort_values(
    by='Max error in prediction', ascending=False)
# Bonus points this week goes to:
Bonus_winners = max_error_df.head(3)

# get winners list from other code
Weekly_winners = pd.DataFrame(winners, columns='names')

if Bonus_winners.Names.isin([weekly_winners]):
    Bonus_winners == []  # delete row for which above cond is true
Bonus_winners = max_error_df.head(3)
print(Bonus_winners.Names)
# Check if Bonus_winners are the forecast winners of this week or evaluators, if yes,
# drop that and select next in sorted list


def get_markerplot():
    """
    ------------------------------------

    ------------------------------------
    Parameters:


    ------------------------------------
    Outputs:

    """

    return marker_plot


def get_boxwhiskplot():
    """
    ------------------------------------

    ------------------------------------
    Parameters:


    ------------------------------------
    Outputs:

    """

    return boxwhiskplot


# %%
class_avg1 = np.mean(forecasts1)

fig, ax = plt.subplots()
ax.plot(forecasts1, '-g', label='Forecast', alpha=.8)
plt.axhline(y=class_avg1, linestyle='dashed',
            label='Class Avg', alpha=.8, color='red')
plt.axhline(y=obs_week, linestyle='dotted', label='Observed',
            alpha=.8, color='blue')
plt.xticks(np.arange(0, 19, 1))
ax.set(title="Week 1 Forecasts", xlabel="Students",
       ylabel="Weekly Avg Flow [cfs]")
ax.legend(fancybox=True, framealpha=1, shadow=True,
          borderpad=1)

fig.set_size_inches(10, 4)
# plt.savefig('Lplot_1.png')
plt.show()

# Week 2 - Obs vs Forecasts
class_avg2 = np.mean(forecasts2)

fig, ax = plt.subplots()
ax.plot(forecasts2, '-g', label='Forecast', alpha=.8)
plt.axhline(y=class_avg2, linestyle='dashed',
            label='Class Avg', alpha=.8, color='red')
plt.axhline(y=obs_week, linestyle='dotted', label='Observed',
            alpha=.8, color='blue')
plt.xticks(np.arange(0, 19, 1))
ax.set(title="Week 2 Forecasts", xlabel="Students",
       ylabel="Weekly Avg Flow [cfs]",)
ax.legend(fancybox=True, framealpha=1, shadow=True,
          borderpad=1)

fig.set_size_inches(10, 4)
# plt.savefig('Lplot_2.png')

plt.show()


title_string1 = 'Student guesses for Week 1'
histogram1 = pf.get_histogram(forecasts1, obs_week, title_string1)

title_string2 = 'Student guesses for Week 2'
histogram2 = pf.get_histogram(forecasts2, obs_week, title_string2)

class_avg1 = np.mean(forecasts1)
title_string = 'Week 2 Forecasts'
simpleplot1 = pf.get_simpleplot(
    forecasts1, class_avg1, obs_week, title_string1)

class_avg2 = np.mean(forecasts1)
title_string2 = 'Week 2 Forecasts'
simpleplot2 = pf.get_simpleplot(
    forecasts2, class_avg2, obs_week, title_string2)
