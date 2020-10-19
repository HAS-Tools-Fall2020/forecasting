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

# %%
