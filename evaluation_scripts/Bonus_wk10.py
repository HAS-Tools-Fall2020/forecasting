# %%
# Alcely and Diana's Bonus Script

import pandas as pd
import numpy as np
import os

# %%    
# Note: Run Forecast_analysis.py and Score_Weekly.py  first

weekly_rmse_mean = pd.DataFrame(weekly_rmse.mean(axis=1)).sort_values(0)

# can choose to use seasonal mean if desired
# seasonal_rmse_mean = pd.DataFrame(seasonal_rmse.mean(axis=0)).sort_values(0)

# This adds back in a 0-1 index
weekly_rmse_mean.reset_index(inplace=True)

# This script below is a while loop that will determine the bonus point
# winners from our rmse function, as long as they are not already
# weekly forecast winners and are not the script writers (i.e., Diana
# and Alcely)

i = 0
j = 0
while j < 3:
    if weekly_rmse_mean['index'].iloc[i] != list(summary.loc[summary['1week_ranking'] == 1].index)[0] and \
       weekly_rmse_mean['index'].iloc[i] != list(summary.loc[summary['1week_ranking'] == 2].index)[0] and \
       weekly_rmse_mean['index'].iloc[i] != list(summary.loc[summary['1week_ranking'] == 3].index)[0] and \
       weekly_rmse_mean['index'].iloc[i] != list(summary.loc[summary['2week_ranking'] == 1].index)[0] and \
       weekly_rmse_mean['index'].iloc[i] != list(summary.loc[summary['2week_ranking'] == 2].index)[0] and \
       weekly_rmse_mean['index'].iloc[i] != list(summary.loc[summary['2week_ranking'] == 3].index)[0] and \
       weekly_rmse_mean['index'].iloc[i] != 'Diana' and weekly_rmse_mean['index'].iloc[i] != 'Alcely':
       j=j+1
       print(weekly_rmse_mean['index'].iloc[i])
    i=i+1

# %%
