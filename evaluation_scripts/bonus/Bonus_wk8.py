# 11122020 - Quinn Hull - archived/antiquated script (will not run)

#%% Libraries that you'll need
import pandas as pd
import numpy as np
from glob import glob
import os
import random      
import eval_functions as ev_fn   
from itertools import chain
from collections import Counter

#%% Functions


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

def past_bonus(week_no):
    filename_3 = 'bonus_week' + str(week_no) + '.csv'
    filepath_3 = os.path.join('../weekly_results', filename_3)
    data_3 = pd.read_csv(filepath_3)
    bonus_ppl = data_3.loc[(data_3['points'] == 0)] 
    ppl_names = bonus_ppl["name"]
    return(ppl_names)


def long_selection(pp,val): 
    st = pd.DataFrame(pp) # Dataframe
    st_tr= st.transpose() # Good formatting
    st_tr.columns = ["Week2", "Week3", "Week4", "Week5", "Week6","Week7"] # Useful head
    tt = st_tr.apply(pd.Series.value_counts, axis=1) # To count how many times people has get bonus points
    tt_st = st_tr.count(axis='columns')
    t = pd.DataFrame(tt_st)
    t.columns = ["frequency"]
    ix = tt[t['frequency'] == val].index.tolist() 
    names = st_tr["Week2"].iloc[ix]
    return(names)


# %% This week method
weeknum = 8  #forecast week -- this should be the forecast_week you are judging
             # The same as the forecast week number you used in the score_weekly
#filename = 'forecast_week' + str(weeknum) + '_results.csv'
#filepath = os.path.join('../weekly_results', filename)
#data = pd.read_csv(filepath)


a = []
pp = []
# People that has not get any bonus point per week
for i in range(2,weeknum):
    a = past_bonus(i)
    pp.append(a)
valu=6
candidates_nb = long_selection(pp,valu)
cd_fn_nb = pd.DataFrame(candidates_nb)
# Bonus points assigned to
selection = random.sample(range(0, 10), 3)
bonus_names = cd_fn_nb["Week2"].iloc[selection]

ev_fn.write_bonus(bonus_names,weeknum)

# %%
