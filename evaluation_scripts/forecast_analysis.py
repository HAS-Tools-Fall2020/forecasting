
# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import dataretrieval.nwis as nwis
import os
import eval_functions as ef
import plot_functions as pf
import dataframe_image as dfi


# %%
forecast_week = int(input('What forecast week is it? (1-16): '))   # week 12 (Quinn and Ben 11/13/20)

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
    weeks.append('Week ' '%s' % (i+1))

# %%
# making two empty arrays to  hold the forecasts
forecasts_1 = np.zeros([nstudent, len(weeks)])  # 1wk forecast for this week
forecasts_2 = np.zeros([nstudent, len(weeks)])  # 2wk forecasts for this week

# Reading the individual student forecast csvs
# to populate the dataframe
# Week 10 modification: using student_csv function
for i in range(nstudent):
    temp = ef.student_csv(names[i])
    for n in range(1, forecast_week+1):
        forecasts_1[i, n-1] = temp.loc[(n), '1week']
        forecasts_2[i, n-1] = temp.loc[(n), '2week']

# %%
# compiled into data frames you can use for graphing
weekly_forecast1w = pd.DataFrame({}, index=firstnames)
weekly_forecast2w = pd.DataFrame({}, index=firstnames)

for i in range(16):
    weekly_forecast1w.insert(i, 'Week %s' % (i+1), forecasts_1[:, i], True)
    weekly_forecast2w.insert(i, 'Week %s' % (i+1), forecasts_2[:, i], True)

# everything above this can be copied
# and pasted into your analysis

# %%
# Week 7 addition, create dataframe containing weekly flows
# NOTE: Must first run Get_Observations.py script
weekly_flows = pd.read_csv("../weekly_results/weekly_observations.csv")

# %%
# Week 10 addition:
# Weekly Root Mean Square Error (RMSE) along the week1 and week2 forecasts
# from the first competition to the most recent.

observation = pd.DataFrame(weekly_flows['observed']).iloc[:, 0]
prediction = [weekly_forecast1w, weekly_forecast2w]

weekly_rmse = pd.DataFrame({}, index=firstnames)

for w in range(len(prediction)):
    rmse_list = []
    for i in range(nstudent):
        pred = pd.DataFrame(prediction[w].iloc[i])
        pred.reset_index(inplace=True)
        rmse_list.append(ef.simpleRMSE(pred.iloc[:, 1], observation, 3))
    weekly_rmse.insert(w, 'RMSE_W%s' % (w+1), rmse_list, True)

# Seasonal RMSE from the first competition to the most recent.
seasonal_rmse = pd.DataFrame({}, index=weeks[:forecast_week])

for i in range(nstudent):
    temp = ef.student_csv(names[i])
    rmse_list = []
    for n in range(forecast_week):
        pred = pd.DataFrame(temp.iloc[n][3:])
        pred.reset_index(inplace=True)
        if pred.iloc[:, 1].sum() == 0:
            rmse_list.append(np.NaN)
        else:
            rmse_list.append(ef.simpleRMSE(pred.iloc[:, 1], observation, 3))

    seasonal_rmse[firstnames[i]] = rmse_list


# Week 13 additions start (Adam, Jill)
# %%
# gives the maximum value RMSE per week
max_wk = seasonal_rmse.max(axis=1)
max_wk

# %%
# gives the mininum value RMSE per week
min_wk = seasonal_rmse.min(axis=1)
min_wk

# %%
# finds person with minimum weekly RMSE
# looks at seasonal_rmse df and pulls out MINIMUM weekly RMSE value\
# and lists column name (person)
min_weekly_RMSE = seasonal_rmse.idxmin(axis=1)
min_weekly_RMSE

# %%
# # finds person with maximum weekly RMSE
# looks at seasonal_rmse df and pulls out MAXIMUM weekly RMSE value\
# and lists column name (person) 
max_weekly_RMSE = seasonal_rmse.idxmax(axis=1)
max_weekly_RMSE

# %%
# Converts min_weekly_RMSE series to df
min_weekly_RMSE_df = min_weekly_RMSE.to_frame(name="RMSE-weekly_min")

# %%
# Converts max_weekly_RMSE series to df
max_weekly_RMSE_df = max_weekly_RMSE.to_frame(name="RMSE-weekly_max")

# %%
# Join two dataframes
Min_Max_RMSE = min_weekly_RMSE_df.join(max_weekly_RMSE_df)
Min_Max_RMSE
print(Min_Max_RMSE)
dfi.export(Min_Max_RMSE, "all_charts/Min-Max-Weekly_RMSE.png")

# %%
# Calculates the mean seasonal RMSE per person (for each column)/
# over all weeks (seasonal forecast entries)
mean_RMSE = seasonal_rmse.mean(axis=0)

# %%
# Converts mean_weekly_RMSE series to df
mean_RMSE_df = mean_RMSE.to_frame(name = "Overall_Seasonal_Average-RMSE")

# %%
# Sort dataframe by values acsending to get top 3 "winners"
# print dataframe to a PNG
Overall_Seas_Min = mean_RMSE_df.sort_values(by=["Overall_Seasonal_Average-RMSE"], ascending=True)
dfi.export(Overall_Seas_Min, "all_charts/Overall_Seasonal_Average-RMSE.png")
Overall_Seas_Min

# Week 13 additions end (Adam, Jill)

# %%
# Probably will be use as bonus input? Still to be worked on later in the week.
weekly_rmse_mean = pd.DataFrame(weekly_rmse.mean(axis=1)).sort_values(0)
seasonal_rmse_mean = pd.DataFrame(seasonal_rmse.mean(axis=0)).sort_values(0)

# %% Week 7 addition, format new dataframes for
# weekly plotting, and assign same index
# trim and tanspose to make plotting easier
weekly_forecast1w_graph = weekly_forecast1w.iloc[:, 0:forecast_week-1].T
weekly_forecast2w_graph = weekly_forecast2w.iloc[:, 0:forecast_week-1].T


# %% Week 9 Addition: Plot results using the functions from plot_functions

# Plot 1 and 2 Week forecasts values for each student

pf.plot_class_forecasts(weekly_forecast1w_graph.T, weekly_flows, 1,
                        'forecast')
pf.plot_class_forecasts(weekly_forecast2w_graph.T, weekly_flows, 2,
                        'forecast')


# %%
# Plot errors (deviation) in 1 and 2 Week forecasts values for each student

pf.plot_class_forecasts(weekly_forecast1w_graph.T, weekly_flows, 1, # removed '-1' from weekly_flows to make the imput 1 equal to Week_1!
                        'abs_error')
pf.plot_class_forecasts(weekly_forecast2w_graph.T, weekly_flows, 2, # removed '-1' from weekly_flows to make the imput 1 equal to Week_1!
                        'abs_error')


# %%
# Plot the evolution of the forecasts for the HAS-Tools Class
# Use 'box' as the last parameter to plot a box-whiskers plot.
# Use 'plot' as the last parameter to plot the summary as series

# 1 Week Forecast
pf.plot_class_summary(weekly_forecast1w_graph.T, weekly_flows, 1, 'box')

# 2 Week Forecast
pf.plot_class_summary(weekly_forecast1w_graph.T, weekly_flows, 2, 'box')


# %%
# Week 10 plots of root mean square errors

# Line plot of the seasonal root mean square error
rmse_sea_path = "all_charts/Seasonal_Root_Mean_Square_Error1.png"
pf.plot_seasonal_rmse(rmse_sea_path, seasonal_rmse)

# Histogram of the weekly root mean square error
rmse_his_path = "all_charts/Root_Mean_Square_Error_Histogram1.png"
pf.rmse_histogram(rmse_his_path, weekly_rmse)

# %%
