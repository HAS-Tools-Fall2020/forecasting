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
import matplotlib.pyplot as plt
import dataretrieval.nwis as nwis
import os


# %%
# User variables
# forecast_week is the week number that you are going to be judging. 
# You can find this in the seasonal_forecst_Dates.pdf 
# You should look up the forecast number for the week that just ended
forecast_week = 7   #week 7 (Jake 10/8/20)  wk 5 (Schulze 9/28), wk 6 (marcelain 10/5)

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

#%%
# changes Jake made next two cells
weeks = []
for i in range (16):
    # this is done because python counts 1 behind 
    i=i+1
    weeks.append('week_' '%s'%i)

#%%
forecasts_1=np.zeros([nstudent,len(weeks)])
forecasts_2=np.zeros([nstudent,len(weeks)]) # The 2week forecasts for this week

for i in range(nstudent):
    filename = names[i] + '.csv'
    filepath = os.path.join('..', 'forecast_entries', filename)
    print(filepath)
    temp = pd.read_csv(filepath, index_col='Forecast #')
    for n in range(1, forecast_week+1):
        forecasts_1[i,n-1] = temp.loc[(n), '1week']
        forecasts_2[i,n-1] = temp.loc[(n), '2week']

# %%
# Read in the streamflow data and get the weekly average
obs_day = nwis.get_record(sites=station_id, service='dv',
                      start=start_date, end=stop_date, parameterCd='00060')
obs_week = np.mean(obs_day['00060_Mean'])

dif1 = abs(forecasts_1[:, forecast_week-2]-obs_week)
dif2 = abs(forecasts_2[:, forecast_week-3]-obs_week)

print('Average streamflow for this week:', np.round(obs_week,3))

#%%
#These are data frames you can use for graphing
weekly_forecast1w = pd.DataFrame({}, index=firstnames)
weekly_forecast2w = pd.DataFrame({}, index=firstnames)

for i in range(16):
    weekly_forecast1w.insert(i,'week_%s'%(i+1), forecasts_1[:,i], True)
    weekly_forecast2w.insert(i,'week_%s'%(i+1), forecasts_2[:,i], True)

# %%
#Make a data frame for the results
summary = pd.DataFrame({'start': start_date, 'end': stop_date, 'observation': obs_week,
                        '1week_forecast': forecasts_1[:, forecast_week-2], '1week_difference': dif1, 
                        '2week_forecast': forecasts_2[:, forecast_week-3], '2week_difference': dif2}, index=firstnames)

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

# Add Histogram of results, plots each student's guess, and the actual mean value for
# week one.
plt.hist(forecasts_1[:, forecast_week-2],bins=120,color = 'blue', alpha=0.75, label = 'Student Guesses')
plt.plot([obs_week]*3, np.arange(0,3,1),color='orange',linestyle= '-',label = 'Actual mean')
plt.title('Student Guesses and actual mean, week 1')
plt.xlabel('Flow Forecast')
plt.ylabel('Count')
plt.legend(loc = 'upper right')
# %%
# %%

# Add Histogram of results, plots each student's guess, and the actual mean value for
# 2week updated to match 1 week by Jake
plt.hist(forecasts_2[:, forecast_week-3],bins=120,color = 'blue', alpha=0.75, label = 'Student Guesses')
plt.plot([obs_week]*3, np.arange(0,3,1),color='orange',linestyle= '-',label = 'Actual mean')
plt.title('Student Guesses and actual mean, week 1')
plt.xlabel('Flow Forecast')
plt.ylabel('Count')
plt.legend(loc = 'upper right')
# %%
# Week 6 addition:  Line plots
# Week 1 - Obs vs Forecasts
class_avg1 = np.mean(forecasts_1[:, forecast_week-2])

fig, ax = plt.subplots()
ax.plot(forecasts_1[:, forecast_week-2], '-g', label='Forecast', alpha=.8)
plt.axhline(y=class_avg1, linestyle='dashed', label='Class Avg', alpha=.8, color = 'red')
plt.axhline(y=obs_week, linestyle='dotted', label='Observed', alpha=.8, color = 'blue')
plt.xticks(np.arange(0, 19, 1))
ax.set(title="Week 1 Forecasts", xlabel="Students", 
        ylabel="Weekly Avg Flow [cfs]")
ax.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1)

fig.set_size_inches(10,4)
#plt.savefig('Lplot_1.png')
plt.show()

# Week 2 - Obs vs Forecasts
class_avg2 = np.mean(forecasts_2[:, forecast_week-3])

fig, ax = plt.subplots()
ax.plot(forecasts_2[:, forecast_week-3], '-g', label='Forecast', alpha=.8)
plt.axhline(y=class_avg2, linestyle='dashed', label='Class Avg', alpha=.8, color = 'red')
plt.axhline(y=obs_week, linestyle='dotted', label='Observed', alpha=.8, color = 'blue')
plt.xticks(np.arange(0, 19, 1))
ax.set(title="Week 2 Forecasts", xlabel="Students", 
        ylabel="Weekly Avg Flow [cfs]",)
ax.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1)

fig.set_size_inches(10,4)
#plt.savefig('Lplot_2.png')

plt.show()
# %%
# Week 7 addition, create dataframe containing weekly flows
# NOTE: Must first run Get_Observations.py script
weekly_flows = pd.read_csv("../weekly_results/weekly_observations.csv")

# %% Week 7 addition, format new dataframes for weekly plotting, and assign same index
#trim and tanspose to make plotting easier
weekly_forecast1w_graph = weekly_forecast1w.iloc[:,0:forecast_week].T 
weekly_forecast2w_graph = weekly_forecast2w.iloc[:,0:forecast_week].T 
#trim and set index the same
weekly_flows_graph = weekly_flows.iloc[:forecast_week,3:4]
weekly_flows_graph.set_index(weekly_forecast1w_graph.index, append=False, inplace=True) 


# %% 
# Week 7 addition, plot timeseries of 1 week forecasts and observed weekly avgerage flow
markers = ['o', 'v', '^', 'D', '>', 's', 'P', 'X', '<', '>', 'X', 'o', 'v', 's', '^','P','<', 'D', 's']
fig, ax = plt.subplots()
ax.plot(weekly_forecast1w_graph)
for i, line in enumerate(ax.get_lines()):
    line.set_marker(markers[i])
ax.plot(weekly_flows['observed'], color = 'black', marker='o', linestyle='--', linewidth = 3 )
ax.set(title="1 Week Forecast", xlabel="Week", ylabel="Weekly Avg Flow [cfs]")
plot_labels = firstnames + ['Observed Flow']
ax.legend(plot_labels, loc='lower center', bbox_to_anchor=(.5, -0.4), ncol=5)
fig.set_size_inches(9,5)
plt.show()
#fig.savefig("1Wk_Forecasts")


# %% 
# Week 7 addition, plot timeseries of 1 week forecast error
Errow_1wk = weekly_forecast1w_graph.subtract(weekly_flows_graph['observed'],axis=0)

fig, ax = plt.subplots()
ax.plot(Errow_1wk)
for i, line in enumerate(ax.get_lines()):
    line.set_marker(markers[i])
plt.axhline(y=0, color = 'black', linestyle='--', linewidth = 3 )
ax.set(title="1 Week Forecast Error", xlabel="Week", ylabel="Deviation from Weekly Avg Flow [cfs]", ylim=[-60,60])
plot_labels = firstnames
ax.legend(plot_labels, loc='lower center', bbox_to_anchor=(.5, -0.4), ncol=5)
fig.set_size_inches(9,5)
plt.show()
#fig.savefig("1Wk_Error")


# %% 
# Week 7 addition, plot timeseries of 2 week forecasts and observed weekly avgerage flow
fig, ax = plt.subplots()
ax.plot(weekly_forecast2w_graph)
for i, line in enumerate(ax.get_lines()):
    line.set_marker(markers[i])
ax.plot(weekly_flows['observed'], color = 'black', marker='o', linestyle='--', linewidth = 3 )
ax.set(title="2 Week Forecast", xlabel="Week", ylabel="Weekly Avg Flow [cfs]")
plot_labels = firstnames + ['Observed Flow']
ax.legend(plot_labels, loc='lower center', bbox_to_anchor=(.5, -0.4), ncol=5)
fig.set_size_inches(9,5)
plt.show()
#fig.savefig("2Wk_Forecasts")


# %% 
# Week 7 addition, plot timeseries of 2 week forecast error
Errow_2wk = weekly_forecast2w_graph.subtract(weekly_flows_graph['observed'],axis=0)

fig, ax = plt.subplots()
ax.plot(Errow_2wk)
for i, line in enumerate(ax.get_lines()):
    line.set_marker(markers[i])
plt.axhline(y=0, color = 'black', linestyle='--', linewidth = 3 )
ax.set(title="2 Week Forecast Error", xlabel="Week", ylabel="Deviation from Weekly Avg Flow [cfs]", ylim=[-60,60])
plot_labels = firstnames
ax.legend(plot_labels, loc='lower center', bbox_to_anchor=(.5, -0.4), ncol=5)
fig.set_size_inches(9,5)
plt.show()
#fig.savefig("2Wk_Error")

# %%
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

plt.plot(weeks, weekly_forecast1w.mean(), marker='o', label='class average')
plt.plot(weeks, weekly_forecast1w.quantile(0.25), marker='o', label='lower quantile')
plt.plot(weeks, weekly_forecast1w.quantile(0.75), marker='o', label='upper quantile')
plt.plot(weeks, weekly_forecast1w.min(), marker='o', label='min')
plt.plot(weeks, weekly_forecast1w.max(), marker='o', label='max')
plt.plot(weeks, weekly_flows['observed'], color = 'black', marker='o', linestyle='--', label='observed')
plt.ylabel('Flow (cfs)');
plt.ylim([0, 1000])
plt.xlim([0, forecast_week-1])
plt.title('Weekly Discharge Prediction');
plt.xticks(rotation=45,fontsize=10)
plt.legend()

# %%
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

plt.plot(weeks, weekly_forecast1w.mean(), marker='o', label='class average')
plt.plot(weeks, weekly_forecast1w.quantile(0.25), marker='o', label='lower quantile')
plt.plot(weeks, weekly_forecast1w.quantile(0.75), marker='o', label='upper quantile')
plt.plot(weeks, weekly_forecast1w.min(), marker='o', label='min')
plt.plot(weeks, weekly_forecast1w.max(), marker='o', label='max')
plt.plot(weeks, weekly_flows['observed'], color = 'black', marker='o', linestyle='--', label='observed')
plt.ylabel('Flow (cfs)')
plt.ylim([0, 150])
plt.xlim([0, forecast_week-1])
plt.title('Weekly Discharge Prediction')
plt.xticks(rotation=45,fontsize=10)
plt.legend()
