# Abigail and Danielle's Bonus script
# %% This week's bonus points will go to those with the lowest ranking

import pandas as pd
import numpy as np
import os

# %%
filepath = os.path.join('..','weekly_results', 'score_details.csv')
points = pd.read_csv(filepath)

# %%
# Creating a dataframe showing total bonus points for each student
points['Total_bonus'] = points[['fcst2_bonus', 'fcst3_bonus', 'fcst4_bonus', 'fcst5_bonus',\
                                'fcst6_bonus', 'fcst7_bonus', 'fcst8_bonus', 'fcst9_bonus',\
                                'fcst10_bonus']].sum(axis=1)
bonus = points[['name','Total_bonus']]
print(bonus)

# %%
# Reading week 11 results into dataframe to exclude current scorers from 
# consideration

# CHANGE FILEPATH TO 'FORECAST_WEEK11_RESULTS' FOR EVALUATION
filepath = os.path.join('..','weekly_results', 'forecast_week10_results.csv')
new_points = pd.read_csv(filepath)

new_points = new_points[(new_points['1week_points'] ==0)]
new_points = new_points[(new_points['2week_points'] == 0)]
new_points = new_points[(new_points.name != 'Abigail') &
             (new_points.name != 'Danielle')]

# %%
# Cross referencing original 'bonus' dataframe with
# the conditions set in 'new_points' dataframe
final_people = bonus[bonus.name.isin(new_points.name)]
final_people = final_people.nsmallest(3, columns = 'Total_bonus', keep = 'first')
print('Week 11 bonus point recipients',final_people)
# %%
# This should put the bonus point recipients into csv
# BUT we want to change their values to 1 and still include the other students
filename_out = 'bonus_week' + str(forecast_week) + '.csv'
filepath_out = os.path.join('..', 'weekly_results', filename_out)
summary.to_csv(filepath_out, index_label='name')
# %%
