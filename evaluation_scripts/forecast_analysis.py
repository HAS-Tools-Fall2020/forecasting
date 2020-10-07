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
forecast_week = 6       # wk 5 (Schulze 9/28), wk 6 (marcelain 10/5)

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
#could be used for graphing 
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
        forecasts_1[i,n-1] = temp.loc[(n), '1week'] #, temp.loc[((2), '1week')] #((forecast_week - 2), '1week'), ((forecast_week - 3), '1week'),((forecast_week - 4), '1week'),((forecast_week - 5), '1week'),((forecast_week - 6), '1week'),((forecast_week - 7), '1week'),((forecast_week - 8), '1week'),((forecast_week - 9), '1week'),((forecast_week - 10), '1week'),((forecast_week - 11), '1week'),((forecast_week - 12), '1week'),((forecast_week - 13), '1week'),((forecast_week - 14), '1week'),((forecast_week - 15), '1week'),((forecast_week - 16), '1week')]
        forecasts_2[i,n-1] = temp.loc[(n), '2week']#, temp.loc[((forecast_week - 2), '2week')] #((forecast_week - 2), '2week'), ((forecast_week - 3), '2week'),((forecast_week - 4), '2week'),((forecast_week - 5), '2week'),((forecast_week - 6), '2week'),((forecast_week - 7), '2week'),((forecast_week - 8), '2week'),((forecast_week - 9), '2week'),((forecast_week - 10), '2week'),((forecast_week - 11), '2week'),((forecast_week - 12), '2week'),((forecast_week - 13), '2week'),((forecast_week - 14), '2week'),((forecast_week - 15), '2week'),((forecast_week - 16), '2week')]


# %%
# Read in the streamflow data and get the weekly average
obs_day = nwis.get_record(sites=station_id, service='dv',
                      start=start_date, end=stop_date, parameterCd='00060')
obs_week = np.mean(obs_day['00060_Mean'])

dif1 = abs(forecasts_1[:, forecast_week-2]-obs_week)
dif2 = abs(forecasts_2[:, forecast_week-3]-obs_week)

print('Average streamflow for this week:', np.round(obs_week,3))

#%%
#mehka these are the data frames I made that we talked about in class
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

# Add Histogram of results, plots each student's guess.
plt.figure(figsize=(8,6))
plt.hist(forecasts_2[:, forecast_week-3],bins=120,color = 'blue', alpha=0.75, label = 'Student Guesses')
plt.plot([obs_week]*3, np.arange(0,3,1),color='orange',linestyle= '-',label = 'Actual mean')
plt.title('Student Guesses, week 2')
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

# Week 2 - Obs vs Forecasts
#%%
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

#%%
# if you'd rather use one time lag for you pred iction uncomment these two cells
# creating a model for the single time lag scenario
from sklearn.linear_model import LinearRegression
#%%

model = LinearRegression()
x=summary['2week_forecast'].values.reshape(-1,1) 
y=summary['1week_forecast'].values
model.fit(x,y)

r_sq = model.score(x, y)

#printing everything
print('coefficient of determination:', np.round(r_sq,2)) 
print('intercept:', np.round(model.intercept_, 2))
print('slope:', np.round(model.coef_, 2))

# generate preditions for training phase and testing phase (training phase is used to generate coefecients and intercepts then applied to each period)
q_pred = model.predict(summary['2week_forecast'].values.reshape(-1,1))



#%%
#%%
# 5. Scatter plot of t vs t-1 flow with normal axes
fig, ax = plt.subplots()
ax.scatter(summary['2week_forecast'], summary['1week_forecast'], marker='o',
              color='blueviolet', label='student guesses')
ax.scatter(obs_week, obs_week, s= 90, marker='*',
              color='red', label='observed flow')
ax.scatter(summary['2week_forecast'].mean(), summary['1week_forecast'].mean(),s= 90, marker='x',
              color='blue', label='student mean')
ax.set(xlabel='2 week forecasts', ylabel='1 week forecasts')
ax.plot(np.sort(summary['2week_forecast']), np.sort(q_pred), label='Trend line')
ax.legend()


# %%
