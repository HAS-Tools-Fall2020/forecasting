# %%
import pandas as pd
import numpy as np
from glob import glob
import os

# %%
#CHANGE these Lines to assign BONUS points
bonus_names = ['Adam', 'Patrick', 'Ty'] #names  to aply  bonus  to
weeknum = 5 #forecast week -- this should be the forecast_week you are judging
            # The same as the forecast week number you used in the score_weekly
random_flag  = False #Set this to true if you wan to override the names
               # listed  here and asign points randomly 
             
#%%
# Add bonus points if you would like
file_listB = glob(os.path.join('../weekly_results', 'bonus*.csv'))
temp = pd.read_csv(file_listB[0], index_col='name')
bonus = pd.DataFrame(data=np.zeros(len(temp)), 
                    index=temp.index,
                    columns=['points'])
del(temp)

bonus.loc[bonus_names, 'points'] = 1

filename='bonus_week' + str(weeknum) + '.csv'
bonus_file = os.path.join('../weekly_results', filename )

bonus.to_csv(bonus_file)


