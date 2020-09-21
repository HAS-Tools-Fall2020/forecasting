# This script calcualtes the total scores for everyone using
# the summary outputs from the score_weekly.py

# %%
import pandas as pd
import numpy as np
from glob import glob
import os

# %%
# Make a list of all the files in the results folder with names
# starting with forecast and ending with week.csv
# For more information on glob refer to:
# https://www.earthdatascience.org/courses/intro-to-earth-data-science/
# Chapter 12 lesson 3
file_list = glob(os.path.join('../weekly_results', 'forecast*week.csv'))
file_listB = glob(os.path.join('../weekly_results', 'bonus*.csv'))
# %%
#CHANGE This
bonus_names = ['Ty', 'Lourdes'] #names  to aply  bonus  to
weeknum = 2 #forecast week -- this should be the forecast_week for the 
          # week 1 forecast you are judging
###

# Add bonus points if you would like
temp = pd.read_csv(file_list[0], index_col='name')
bonus = pd.DataFrame(data=np.zeros(len(temp)), 
                    index=temp.index,
                    columns=['points'])
del(temp)

bonus.loc[bonus_names, 'points'] = 1

filename='bonus' + str(weeknum) + '.csv'
bonus_file = os.path.join('../weekly_results', filename )

bonus.to_csv(bonus_file)

# %%
# setup a dataframe with all zeros for the scoreboard
# use the first summary file to make the name index
temp = pd.read_csv(file_list[0], index_col='name')
scoreboard = pd.DataFrame(data = np.zeros((len(temp),2)), 
                          index = temp.index, 
                          columns=['regular', 'bonus'])

# %%
#calculate the scores
#loop through reading summaries and add in the regular points
for file in file_list:
    print(file)
    temp=pd.read_csv(file, index_col='name')
    scoreboard['regular'] += temp['points']

# Add in thte bonus points
for file in file_listB:
    print(file)
    temp=pd.read_csv(file, index_col='name')
    scoreboard['bonus'] += temp['points']


scoreboard['total'] = scoreboard['bonus'] + scoreboard['regular']


scoreboard['rank'] = scoreboard.total.rank(method='dense', ascending=False)
scoreboard = scoreboard.sort_values(by='total', ascending=False)
print(scoreboard)

# %%
