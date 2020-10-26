
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
# NOTE: Run 'Score_Weekly.py' and 'forecast_analysis.py' BEFORE running the Bonus_wk9.py code

# %%
# This week's bonus points goes to those who has highest error in prediction
# between consecutive weekly flow
column_weeks = [i for i in weekly_forecast1w_graph.T.columns[0:7]]
week_flows = weekly_flows.iloc[1:len(column_weeks) + 1, 3:4]
week_flows.set_index(weekly_forecast1w_graph.T.columns[0:7], append=False, inplace=True)

# Getting differences between consecutive weekly average flows
obs_var = np.diff(week_flows['observed'], axis=0)
pred_var = np.subtract(forecasts_2, forecasts_1)

# For loop for getting errors in weekly prediction for each student
err = np.zeros([nstudent, len(column_weeks)-1])
max_err = np.zeros([nstudent, 1])
for i in range(nstudent):
    err[i] = (obs_var[0:len(column_weeks)+1] - pred_var[i][0:len(column_weeks)-1])
    # max error in consecutive week pred difference
    max_err[i] = np.max(np.absolute(err[i]))

max_error_df = pd.DataFrame(firstnames, columns=['Names'])
max_error_df['Max error in prediction'] = max_err
max_error_df = max_error_df.sort_values(
    by='Max error in prediction', ascending=False)
# Bonus points this week goes to:
Bonus_winners = max_error_df.head(3)
print(Bonus_winners)

#%%

# get winners list from other code
weekly_winners = pd.DataFrame(columns=['Week', 'Names'])
for i in range(1, 4):

    weekly_winners = weekly_winners.append({'Week':1, 'Names': summary.loc[summary['1week_ranking'] == i].index[0]},ignore_index=True)
    weekly_winners = weekly_winners.append({'Week':2, 'Names': summary.loc[summary['2week_ranking'] == i].index[0]},ignore_index=True)

print('The weekly winners are:',weekly_winners)

# The counter will start in 3 because the first three places were taken as winners before
i=3

# Check if Bonus_winners are the forecast winners of this week or evaluators, if yes,
# drop that and select next in sorted list

while Bonus_winners[Bonus_winners.Names.isin(weekly_winners['Names'])].any()['Names']==True:

    # Delete row for which above condition is true
    Bonus_winners.drop(Bonus_winners[Bonus_winners.Names.isin(weekly_winners['Names']) == True].index, inplace=True)

    # Add the next person in the list
    Bonus_winners = Bonus_winners.append(max_error_df.head().iloc[i:i+(3-Bonus_winners.shape[0])])
    i=i+1

print('The Bonus winners for this week are:\n', Bonus_winners.Names)


