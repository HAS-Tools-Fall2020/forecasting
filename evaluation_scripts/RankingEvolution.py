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
file_list = glob(os.path.join('../weekly_results', 'forecast_week*.csv'))
file_listB = glob(os.path.join('../weekly_results', 'bonus*.csv'))

# Get the week numbers from the file list by splitting the strings
forecast_names = [file_list[i].split('_')[2] for i in range(len(file_list))]
bonus_names = [file_listB[i].split('_')[2][0:-4] for i in range(len(file_list))]

# Then get out just the week numbers and 
forecast_nums = [int(i[4::]) for i in forecast_names]
forecast_nums = np.sort(forecast_nums)

bonus_nums = [int(i[4::]) for i in bonus_names]
bonus_nums = np.sort(bonus_nums)

# %%
# setup a dataframe with all zeros for the scoreboard
# use the first summary file to make the name index
temp = pd.read_csv(file_list[0], index_col='name')
scoreboard = pd.DataFrame(data = np.zeros((len(temp),2)), 
                          index = temp.index, 
                          columns=['regular', 'bonus'])

# Setup a weekly scoreboard similar to above
score_weekly = pd.DataFrame(data=np.zeros(len(temp)),
                            index=temp.index,
                            columns=['Total'])

# %%
#calculate the scores
#loop through reading summaries and add in the regular points
#for file in file_list:
for f in range(np.min(forecast_nums), np.max(forecast_nums)+1):
    fname = 'forecast_week' + str(f) +  '_results.csv'
    filetemp = os.path.join('../weekly_results', fname)
    print(filetemp)
    temp=pd.read_csv(filetemp, index_col='name')
    scoreboard['regular'] += temp['1week_points']+ temp['2week_points']

    # add the values to the week table: 
    score_weekly = score_weekly.join(temp['1week_points'])
    score_weekly = score_weekly.rename(
        columns={'1week_points': ('fcst' + str(f) + '_1wk')})
    score_weekly = score_weekly.join(temp['2week_points'])
    score_weekly = score_weekly.rename(
        columns={'2week_points': ('fcst' + str(f) + '_2wk')})


# Add in the bonus points

#for file in file_listB:
for f in range(np.min(bonus_nums), np.max(bonus_nums)+1):
    fname = 'bonus_week' + str(f) + '.csv'
    filetemp = os.path.join('../weekly_results', fname)
    print(filetemp)

    tempB=pd.read_csv(filetemp, index_col='name')
    scoreboard['bonus'] += tempB['points']

    # add the values to the week table:
    score_weekly = score_weekly.join(tempB['points'])
    score_weekly = score_weekly.rename(
        columns={'points': ('fcst' + str(f) + '_bonus')})



scoreboard['total'] = scoreboard['bonus'] + scoreboard['regular']


scoreboard['rank'] = scoreboard.total.rank(method='dense', ascending=False)
scoreboard = scoreboard.sort_values(by='total', ascending=False)
print(scoreboard)

# %%
# Write out the scoreboard
fname='scoreboard.csv'
filetemp = os.path.join('../weekly_results', fname)
scoreboard.to_csv(filetemp, index_label='name')

# Write out the scoreboard
fname = 'score_details.csv'
filetemp = os.path.join('../weekly_results', fname)
score_weekly.to_csv(filetemp, index_label='name')

# %%

for i in range(2, 17):
    ranking_weekly_evol = pd.DataFrame(data=np.zeros((len(temp))),
                            index=temp.index,
                            columns=[('rank' + str(i))])
    ranking_weekly_csv = pd.DataFrame(data=np.zeros((len(temp))),
                            index=temp.index,
                            columns=[('rank' + str(i))])
    ranking_weekly_evol[('rank' + str(i))] = temp['1week_points']+ temp['2week_points'] + tempB['points']
    print(ranking_weekly_evol)

=======
i = 0
f = 4
for i in range(np.min(forecast_nums), np.max(forecast_nums)+1):
    fname = 'forecast_week' + str(i) +  '_results.csv'
    filetemp = os.path.join('../weekly_results', fname)
    print(filetemp)
    temp=pd.read_csv(filetemp, index_col='name')
    fnameB = 'bonus_week' + str(i) + '.csv'
    filetempB = os.path.join('../weekly_results', fnameB)
    print(filetempB)
    tempB=pd.read_csv(filetempB, index_col='name')

    ranking_weekly_evol = pd.DataFrame(data=np.zeros((len(temp))),
                            index=temp.index,
                            columns=[('rank' + str(i))])
    ranking_weekly_evol[('TotalPoints_Week' + str(i+ 1))] = temp['1week_points'] + temp['2week_points'] + tempB['points'] + ranking_weekly_evol[('TotalPoints_Week' + str(i))]
    ranking_weekly_evol[('rank' + str(i))] = ranking_weekly_evol[('TotalPoints_Week' + str(i))].rank(ascending=False, method='dense')
    ranking_weekly_evol = ranking_weekly_evol.sort_values(by=('TotalPoints_Week' + str(i)), ascending=False)
    
    # add the values to the week table:
    ranking_weekly_evol.append(ranking_weekly_evol[('rank' + str(i))])

    print(ranking_weekly_evol)



# Write out the ranking_weekly
fname = 'ranking_weekly2.csv'
filetemp = os.path.join('../weekly_results', fname)
ranking_weekly_evol.to_csv(filetemp, index_label='name')

# %%
# NEW TRY
fname = 'score_details.csv'
filetemp = os.path.join('../weekly_results', fname)
print(filetemp)
score_details = pd.read_csv(filetemp, index_col='name')

# %%
week1_list = ['fcst2_1wk', 'fcst3_1wk', 'fcst4_1wk', 'fcst5_1wk',
            'fcst6_1wk', 'fcst7_1wk', 'fcst8_1wk', 'fcst9_1wk',
            'fcst10_1wk', 'fcst11_1wk', 'fcst12_1wk',
            'fcst13_1wk']
week2_list = ['fcst2_2wk', 'fcst3_2wk', 'fcst4_2wk', 'fcst5_2wk',
            'fcst6_2wk', 'fcst7_2wk', 'fcst8_2wk', 'fcst9_2wk',
            'fcst10_2wk', 'fcst11_2wk', 'fcst12_2wk',
            'fcst13_2wk']
bonus_list = ['fcst2_bonus', 'fcst3_bonus', 'fcst4_bonus',
            'fcst5_bonus', 'fcst6_bonus', 'fcst7_bonus',
            'fcst8_bonus', 'fcst9_bonus', 'fcst10_bonus',
            'fcst11_bonus', 'fcst12_bonus', 'fcst13_bonus',]


oneweeks = score_weekly[week1_list]
twoweeks = score_weekly[week2_list]
bonus = score_weekly[bonus_list]

weekly_totals = pd.DataFrame(data=np.zeros((np.max(forecast_nums)+1))),
                index=oneweeks.index,
                columns=['RankTotal'])

weekly_totals['total'] = oneweeks + twoweeks + bonus

weekly_totals.cumsum(axis=1)

# %%
weekly_totals_one_two = oneweeks.add(twoweeks, fill_value=1)
weekly_totals = weekly_totals_one_two.add(bonus, fill_value=1)

weekly_totals = weekly_totals.sort_values(ascending=True, by='name')
weekly_totals[sorted(weekly_totals.columns)]

# %%
#2.  Take weekly points Dataframe and convert to cumulative weekly points
semester_total = weekly_totals.copy()

for i in range(1, (np.max(forecast_nums)+1)):
    semester_total[:i] = semester_total[:(i)] + weekly_totals[:i]

# 3. Convert  Cumulative weekly points to ranks
ranking = semester_total.rank(axis=1, ascending=False)

