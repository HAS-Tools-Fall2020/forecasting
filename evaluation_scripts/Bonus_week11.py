# Abigail and Danielle's Week 11 Bonus script 
# %% 
# This week's bonus points will go to those with lowest cumulative
# bonus points

import pandas as pd
import numpy as np
import os
import glob as glob
import eval_functions as ef
# %%
filepath = os.path.join('..','weekly_results', 'score_details.csv')
points = pd.read_csv(filepath)

# %%
# Creating a dataframe showing cumulative bonus points for each student
points['Total_bonus'] = points[['fcst2_bonus', 'fcst3_bonus', 'fcst4_bonus', 'fcst5_bonus',\
                                'fcst6_bonus', 'fcst7_bonus', 'fcst8_bonus', 'fcst9_bonus',\
                                'fcst10_bonus']].sum(axis=1)
bonus = points[['name','Total_bonus']]
print(bonus)

# %%
# Reading week 11 results into dataframe
# Change file name to match current week
filepath = os.path.join('..','weekly_results', 'forecast_week11_results.csv')
bonus_eligible = pd.read_csv(filepath)

# Excluding evaluators and people who received points this week
evaluators = ['Abigail', 'Danielle']
bonus_eligible = bonus_eligible[(bonus_eligible['1week_points'] ==0) &
            (bonus_eligible['2week_points'] ==0)]
bonus_eligible = bonus_eligible[(bonus_eligible.name != evaluators[0]) &
            (bonus_eligible.name != evaluators[1])]
bonus_eligible
# %%
# Grabbing original 'bonus' dataframe with the conditions set in 'new_points' df
# to identify who is eligible for bonus points
final_people = bonus[bonus.name.isin(bonus_eligible.name)]
final_people = final_people.nsmallest(6, columns = 'Total_bonus', keep = 'first')
print('Week 11 bonus point eligible')
final_people

# %%
# Recipients are randomly selected from those having the lowest accumulated
# bonus points, are not the evaluator(s), and did not score for current week 
final_people = final_people.sample(n=3)
final_people
# %%
# Creat list of names and feed into function to create bonus_week11.csv
final_people = ["Mekha", "Quinn", "Ty"]

# final_people = final_people.loc[final_people.name]
ef.write_bonus(final_people, 11)
# %%
