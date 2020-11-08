# Abigail and Danielle's Bonus script

# %% This week's bonus points will go to those with the lowest ranking

import pandas as pd
import numpy as np
import os

# %%
filepath = os.path.join('..','weekly_results', 'score_details.csv')
points = pd.read_csv(filepath)
print(points)

# %%
points['Total_bonus'] = points[['fcst2_bonus', 'fcst3_bonus', 'fcst4_bonus', 'fcst5_bonus',\
                                'fcst6_bonus', 'fcst7_bonus', 'fcst8_bonus', 'fcst9_bonus',\
                                'fcst10_bonus']].sum(axis=1)
bonus = points[['name','Total_bonus']]
print(bonus)

# %%
# %% This is from Diana and Alcely's script with conditionals to not include winners 

# This script below use a while loop that will determine the bonus point
# winners with the lowest ranking, as long as they are not already
# weekly forecast winners and are not the script writers

i = 0
j = 0
while j < 3:
    if ranks['rank'].iloc[i] != list(summary.loc[summary['1week_ranking'] == 1].index)[0] and \
       ranks['rank'].iloc[i] != list(summary.loc[summary['1week_ranking'] == 2].index)[0] and \
       ranks['rank'].iloc[i] != list(summary.loc[summary['1week_ranking'] == 3].index)[0] and \
       ranks['rank'].iloc[i] != list(summary.loc[summary['2week_ranking'] == 1].index)[0] and \
       ranks['rank'].iloc[i] != list(summary.loc[summary['2week_ranking'] == 2].index)[0] and \
       ranks['rank'].iloc[i] != list(summary.loc[summary['2week_ranking'] == 3].index)[0] and \
       ranks['rank'].iloc[i] != 'Danielle' and weekly_rmse_mean['rank'].iloc[i] != 'Abigail':
       j=j+1
       print(ranks['rank'].tail(3))
    i=i+1

# %%
