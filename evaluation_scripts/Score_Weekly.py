# This script is used to score the 1 week and 2 week forecasts

# %%
import pandas as pd
import numpy as np
import os
import eval_functions as ef
import dataretrieval.nwis as nwis
import plot_functions as pf

# %%
# User variables:
# forecast_week: the week number that you are judging.
#                Use number for week that just ended,
#                found in seasonal_forecst_Dates.pdf

forecast_week = 9  # wk9 (Shweta & Camilo 10/27)

# %%
station_id = "09506000"

# get list of students in the class using functions
names = ef.getLastNames()
firstnames = ef.getFirstNames()
nstudent = len(names)

# get start and end date of forecast week for 1 wk forecast
week_date = ef.weekDates(forecast_week)
start_date = week_date[0]
stop_date = week_date[1]
print("Evaluating forecasts for", start_date, 'To', stop_date)

# get start and end date of forecast week for 2 wk forecast
week_date2 = ef.weekDates(forecast_week-1)
start_date_2wk = week_date2[0]
stop_date_2wk = week_date2[1]

# %%
# Read in everyone's forecast entries
forecasts1 = np.zeros(nstudent)  # 1 wk forecasts for this week
forecasts2 = np.zeros(nstudent)  # 2 wk forecasts for this week

for i in range(nstudent):
    # i = 0
    filename = names[i] + '.csv'
    filepath = os.path.join('..', 'forecast_entries', filename)
    print(filepath)
    temp = pd.read_csv(filepath, index_col='Forecast #')
    # print(temp.loc[(forecast_week - 1), '1week'])
    forecasts1[i] = temp.loc[(forecast_week - 1), '1week']
    forecasts2[i] = temp.loc[(forecast_week - 2), '2week']

# %%
# Read in the streamflow data and get the weekly average
obs_day = nwis.get_record(sites=station_id, service='dv',
                          start=start_date, end=stop_date,
                          parameterCd='00060')
obs_week = np.mean(obs_day['00060_Mean'])
dif1 = abs(forecasts1 - obs_week)
# dif2 = np.zeros(nstudent)

dif2 = abs(forecasts2 - obs_week)


print('Average streamflow for this week:', np.round(obs_week, 3))

# %%
# Make a data frame for the results
summary = pd.DataFrame({'start': start_date, 'end': stop_date,
                        'observation': obs_week,
                        '1week_forecast': forecasts1,
                        '1week_difference': dif1,
                        '2week_forecast': forecasts2,
                        '2week_difference': dif2},
                       index=firstnames)

# Rank the forecasts
summary['1week_ranking'] = summary['1week_difference'].rank(ascending=True,
                                                            method='dense',
                                                            na_option='bottom')
summary['2week_ranking'] = summary['2week_difference'].rank(ascending=True,
                                                            method='dense',
                                                            na_option='bottom')


# Add points for the 1 week forecasts
summary['1week_points'] = np.zeros(nstudent)
summary.loc[summary['1week_ranking'] == 1, '1week_points'] = 2
summary.loc[summary['1week_ranking'] == 2, '1week_points'] = 1
summary.loc[summary['1week_ranking'] == 3, '1week_points'] = 1

# Add points for the 2 week forecasts
summary['2week_points'] = np.zeros(nstudent)
summary.loc[summary['2week_ranking'] == 1, '2week_points'] = 2
summary.loc[summary['2week_ranking'] == 2, '2week_points'] = 1
summary.loc[summary['2week_ranking'] == 3, '2week_points'] = 1

# summary['2week_ranking'] = 0
# summary['2week_points'] = 0

# %%
# Write out the reults
filename_out = 'forecast_week' + str(forecast_week) + '_results.csv'
filepath_out = os.path.join('..', 'weekly_results', filename_out)
summary.to_csv(filepath_out, index_label='name')


# %%
# print a summary
print('1 Week Forecast (', start_date, '-', stop_date, ')')
print('Observed Flow =', round(obs_week, 3))
print('First Place = ', list(summary.loc[summary['1week_ranking'] == 1].index),
      'flow forecast = ', summary.loc[summary['1week_ranking'] == 1,
                                      '1week_forecast'].head(1).values)
print('Second Place = ', list(summary.loc[summary['1week_ranking'] == 2].index),
      'flow forecast = ', summary.loc[summary['1week_ranking'] == 2,
                                      '1week_forecast'].head(1).values)
print('Third Place = ', list(summary.loc[summary['1week_ranking'] == 3].index),
      'flow forecast = ', summary.loc[summary['1week_ranking'] == 3,
                                      '1week_forecast'].head(1).values)

print('2 Week Forecast (', start_date, '-', stop_date, ')')
print('Observed Flow =', round(obs_week, 3))
print('First Place = ', list(summary.loc[summary['2week_ranking'] == 1].index),
      'flow forecast = ', summary.loc[summary['2week_ranking'] == 1,
                                      '2week_forecast'].head(1).values)
print('Second Place = ', list(summary.loc[summary['2week_ranking'] == 2].index),
      'flow forecast = ', summary.loc[summary['2week_ranking'] == 2,
                                      '2week_forecast'].head(1).values)
print('Third Place = ', list(summary.loc[summary['2week_ranking'] == 3].index),
      'flow forecast = ', summary.loc[summary['2week_ranking'] == 3,
                                      '2week_forecast'].head(1).values)


# %%
# Week 9 addition:
# Replaced plotting script with functions

# Add Histogram of results, plots each student's guess,
# and the actual mean value for week 1 and week 2.
histogram1 = pf.get_histogram(forecasts1, obs_week, 1)

histogram2 = pf.get_histogram(forecasts2, obs_week, 2)

# Week 1 - Obs vs Forecasts
simpleplot1 = pf.get_simpleplot(forecasts1, obs_week, 1)

# Week 2 - Obs vs Forecasts
simpleplot2 = pf.get_simpleplot(forecasts2, obs_week, 2)

