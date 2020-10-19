#%% Libraries that you'll need
import pandas as pd
import numpy as np
from glob import glob
import os
import random      
import eval_functions as ev_fn         
#%%
bonus_names = ['Adam', 'Patrick', 'Ty'] #names  to aply  bonus  to
weeknum = 5 #forecast week -- this should be the forecast_week you are judging
            # The same as the forecast week number you used in the score_weekly
random_flag  = False #Set this to true if you wan to override the names
               # listed  here and asign points randomly 
             
           
ev_fn.write_bonus(bonus_names,weeknum)

# %% This week method

weeknum = 7  #forecast week -- this should be the forecast_week you are judging
             # The same as the forecast week number you used in the score_weekly
filename = 'forecast_week' + str(weeknum) + '_results.csv'
filepath = os.path.join('../weekly_results', filename)
data = pd.read_csv(filepath)

#%% test 
weeknum = 7
def data_week(week_no):
    filename_2 = 'forecast_week' + str(week_no) + '_results.csv'
    filepath_2 = os.path.join('../weekly_results', filename_2)
    data_2 = pd.read_csv(filepath_2)
    data_2['sum'] = data['1week_difference'] + data['2week_difference']
    data_new = data_2.loc[(data_2['1week_points'] <1) & (data_2['2week_points']<1)] 
    names_no = data_new["name"]
    data_new_yes = data_2.loc[(data_2['1week_points'] >=1) | (data_2['2week_points']>=1)]
    names_yes = data_new_yes["name"]
    return(names_no,names_yes)

# Looking at students that didn;e get a point 
# in the previous 3 weeks
testno,testyes = data_week(weeknum)
print(testno)
print(testyes)
test_1n0,test_1yes = data_week(weeknum-1)
print(test_1n0)
print(test_1yes)
test_2no,test_2yes = data_week(weeknum-2)
print(test_1n0)
print(test_2yes)

#%% Addign those names to a list
frames_no = [testno, test_1n0, test_2no]
frames_yes = [testyes, test_1yes, test_2yes]
all_names_no = pd.concat(frames_no)
all_names_yes = pd.concat(frames_yes)

print("Students that didn't get a point last 3 weeks",all_names_no)
print("Students that got a point last in the previous last 3 weeks",all_names_yes)

# Here I delete names that pople that has gotten a point
# Here I randmly select the 3 names that willl get the point htis week

# %% Summs up error from week 1 and week 2
#data['sum'] = data['1week_difference'] + data['2week_difference']
#data.sort_values('sum')
#print(data)
#data.nlargest(3, 'sum', keep='all')["name"]
