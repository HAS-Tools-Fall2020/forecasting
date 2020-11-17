# --------------------------------------
# 11162020 - Quinn and Ben Bonus Script!
# Award Bonus points to those who have
# been adjusting their seasonal forecasts
# 1) this script counts the number of unique
#   non-NaN seasonal forecast entries
# 2) it removes from the pool of possible winners
#   the top three point getters through prior week
# 3) it then awards bonus points to those with most
#   novel guesses
# --------------------------------------

# %%

import pandas as pd
import numpy as np
import os
import glob as glob
import sys
sys.path.append('../')
import eval_functions as ef
import matplotlib.pyplot as plt

# %%

# input week
# week 12 (Quinn and Ben, 11/14)
forecast_week = int(input('What forecast week is it? (1-16): '))
# get last names
lastnames = ef.getLastNames()
firstnames = ef.getFirstNames()

out_df = pd.DataFrame(columns=['lastname', 'name', 'mn_std', 'sum_ct'])

# %%
# Loop through csvs
for i in range(len(lastnames)):
    fnm = firstnames[i]
    lnm = lastnames[i]
    # read in csv
    filepath = os.path.join('../../forecast_entries', lnm+'.csv')
    print(filepath)
    temp = pd.read_csv(filepath, index_col='Forecast #')
    # calculate standard deviation within each week over semester
    std = temp.iloc[:forecast_week, 3:].std()
    # calculate the count of novel values witheach week over the semester
    ct = temp.iloc[:forecast_week, 3:].nunique(axis=0)
    # mean of standard deviation for each week along 16 week semester
    mn_std = round(std.mean(), 2)
    # sum of counts for each week along 16 week semester
    sum_ct = round(ct.sum(), 2)
    # Append to out df w/ index of lastname and mean_std as value
    in_df = pd.DataFrame({'lastname': [lnm], 'name': [fnm],
                          'mn_std': [mn_std], 'sum_ct': [sum_ct]})
    out_df = out_df.append(in_df)
    del(fnm, lnm, filepath, temp, std, ct, mn_std, sum_ct, in_df)

out_df.set_index('name', inplace=True)
# %%
# read in scoreboard
filename = 'scoreboard.csv'
filepath = os.path.join('../../weekly_results', filename)
scoreboard = pd.read_csv(filepath)
scoreboard.set_index('name', inplace=True)
# join to out_df
out_df = out_df.join(scoreboard)

# %%
# visualize
fig, ax = plt.subplots()
# data
ax.scatter(out_df['total'], out_df['sum_ct'],label='students')
# fake best fit line, lolol
ax.plot([0, 12], [160, 60], color='black', label='*best fit')
ax.set_ylim(50, 170)
ax.set_ylabel('total count of novel guesses')
ax.set_xlim(0, 12)
ax.set_xlabel('total number of points')
fig.legend()
fig.show()

# %%
# sort
out_df = out_df.sort_values('sum_ct', ascending=False)
# remove overall leaders from week 11
out_df = out_df[out_df['rank'] > 3]
# remove evaluators
out_df.drop(['Quinn'], inplace=True)
# select top three
final_people = out_df.head(3).index.values.tolist()

# %%
# write bonus
ef.write_bonus(final_people, 12)


# %%
