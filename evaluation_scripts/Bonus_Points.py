# This script calcualtes the total scores for everyone using
# the summary outputs from the score_weekly.py

# %%
import pandas as pd
import numpy as np
from glob import glob
import os
import random               # Added for the assign random points by Schulze 9/25/20

# %%
#CHANGE these Lines to assign BONUS points
bonus_names = ['Adam', 'Patrick', 'Ty'] #names  to aply  bonus  to
weeknum = 5 #forecast week -- this should be the forecast_week you are judging
            # The same as the forecast week number you used in the score_weekly
random_flag  = False #Set this to true if you wan to override the names
               # listed  here and asign points randomly 

# %%
# Random distribution of bonus points
# New block added by Schulze 9/25/20, for assigning the names to a 3-d array 
# with first and last names, sorted alphabetically. The 3 students to get a point are 
# randomly chosen and their names returned.

if random_flag: 
    firstnames=np.array(['Ty', 'Lourdes', 'Diana', 'Quinn', 'Abigail', 'Alcely', 'Richard',
            'Alexa', 'Xenia', 'Ben', 'Shweta',
            'Patrick', 'Jill', 'Mekha', 'Jake', 'Camilo',
            'Scott', 'Adam', 'Danielle'])
    selection = random.sample(range(0,18), 3)       # Selects 3 indicies from an array the lenght of our classlist
    bonus_names = firstnames[selection]             # Takes the place of the bonus_names call in the block below
    #print(selection)                               # Used to verify the selection did not duplicate
                                # Visually verifies the selection being made from the array above

print(bonus_names) 
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


