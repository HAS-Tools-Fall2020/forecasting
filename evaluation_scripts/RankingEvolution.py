# This script calculates the evolution of the ranking for everyone and getting\
# a CSV and a plot of the ranking evolution

# %%
import pandas as pd
import numpy as np
from glob import glob
import os
import matplotlib.pyplot as plt
from pandas.plotting import table

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
# NOTE: Update the number of the week
# Xenias Week 14 addition
# I need a BIG help with for loops D:

Points2 = score_weekly['fcst2_1wk'] + score_weekly['fcst2_2wk'] + score_weekly['fcst2_bonus']
Points3 = score_weekly['fcst3_1wk'] + score_weekly['fcst3_2wk'] + score_weekly['fcst3_bonus']
Points4 = score_weekly['fcst4_1wk'] + score_weekly['fcst4_2wk'] + score_weekly['fcst4_bonus']
Points5 = score_weekly['fcst5_1wk'] + score_weekly['fcst5_2wk'] + score_weekly['fcst5_bonus']
Points6 = score_weekly['fcst6_1wk'] + score_weekly['fcst6_2wk'] + score_weekly['fcst6_bonus']
Points7 = score_weekly['fcst7_1wk'] + score_weekly['fcst7_2wk'] + score_weekly['fcst7_bonus']
Points8 = score_weekly['fcst8_1wk'] + score_weekly['fcst8_2wk'] + score_weekly['fcst8_bonus']
Points9 = score_weekly['fcst9_1wk'] + score_weekly['fcst9_2wk'] + score_weekly['fcst9_bonus']
Points10 = score_weekly['fcst10_1wk'] + score_weekly['fcst10_2wk'] + score_weekly['fcst10_bonus']
Points11 = score_weekly['fcst11_1wk'] + score_weekly['fcst11_2wk'] + score_weekly['fcst11_bonus']
Points12 = score_weekly['fcst12_1wk'] + score_weekly['fcst12_2wk'] + score_weekly['fcst12_bonus']
Points13 = score_weekly['fcst13_1wk'] + score_weekly['fcst13_2wk'] + score_weekly['fcst13_bonus']
Points14 = score_weekly['fcst14_1wk'] + score_weekly['fcst14_2wk'] + score_weekly['fcst14_bonus']

Acum2 = Points2
Acum3 = Acum2 + Points3
Acum4 = Acum3 + Points4
Acum5 = Acum4 + Points5
Acum6 = Acum5 + Points6
Acum7 = Acum6 + Points7
Acum8 = Acum7 + Points8
Acum9 = Acum8 + Points9
Acum10 = Acum9 + Points10
Acum11 = Acum10 + Points11
Acum12 = Acum11 + Points12
Acum13 = Acum12 + Points13
Acum14 = Acum13 + Points14

df2 = pd.DataFrame(Acum2)
df2.columns = ['acum2']
df2['rank2'] = df2.rank(ascending=False, method='dense')
df2

df3 = pd.DataFrame(Acum3)
df3.columns = ['acum3']
df3['rank3'] = df3.rank(ascending=False, method='dense')
df3

df4 = pd.DataFrame(Acum4)
df4.columns = ['acum4']
df4['rank4'] = df4.rank(ascending=False, method='dense')
df4

df5 = pd.DataFrame(Acum5)
df5.columns = ['acum5']
df5['rank5'] = df5.rank(ascending=False, method='dense')
df5

df6 = pd.DataFrame(Acum6)
df6.columns = ['acum6']
df6['rank6'] = df6.rank(ascending=False, method='dense')
df6

df7 = pd.DataFrame(Acum7)
df7.columns = ['acum7']
df7['rank7'] = df7.rank(ascending=False, method='dense')
df7

df8 = pd.DataFrame(Acum8)
df8.columns = ['acum8']
df8['rank8'] = df8.rank(ascending=False, method='dense')
df8

df9 = pd.DataFrame(Acum9)
df9.columns = ['acum9']
df9['rank9'] = df9.rank(ascending=False, method='dense')
df9

df10 = pd.DataFrame(Acum10)
df10.columns = ['acum10']
df10['rank10'] = df10.rank(ascending=False, method='dense')
df10

df11 = pd.DataFrame(Acum11)
df11.columns = ['acum11']
df11['rank11'] = df11.rank(ascending=False, method='dense')
df11

df12 = pd.DataFrame(Acum12)
df12.columns = ['acum12']
df12['rank12'] = df12.rank(ascending=False, method='dense')
df12

df13 = pd.DataFrame(Acum13)
df13.columns = ['acum13']
df13['rank13'] = df13.rank(ascending=False, method='dense')
df13

df14 = pd.DataFrame(Acum14)
df14.columns = ['acum14']
df14['rank14'] = df14.rank(ascending=False, method='dense')
df14

# %%
# Merge Acumulative points
# NOTE: Update the number of the week

rank_evol2 = df2
rank_evol3  = pd.merge(rank_evol2, df3, right_index=True, left_index=True)
rank_evol4  = pd.merge(rank_evol3, df4, right_index=True, left_index=True)
rank_evol5  = pd.merge(rank_evol4, df5, right_index=True, left_index=True)
rank_evol6  = pd.merge(rank_evol5, df6, right_index=True, left_index=True)
rank_evol7  = pd.merge(rank_evol6, df7, right_index=True, left_index=True)
rank_evol8  = pd.merge(rank_evol7, df8, right_index=True, left_index=True)
rank_evol9  = pd.merge(rank_evol8, df9, right_index=True, left_index=True)
rank_evol10  = pd.merge(rank_evol9, df10, right_index=True, left_index=True)
rank_evol11  = pd.merge(rank_evol10, df11, right_index=True, left_index=True)
rank_evol12  = pd.merge(rank_evol11, df12, right_index=True, left_index=True)
rank_evol13  = pd.merge(rank_evol12, df13, right_index=True, left_index=True)
rank_evol14  = pd.merge(rank_evol13, df14, right_index=True, left_index=True)

# %%
# Write out the ranking evolution CSV
# NOTE: Update the number of the week
fname = 'ranking_weekly.csv'
filetemp = os.path.join('../weekly_results', fname)
rank_evol14.to_csv(filetemp, index_label='name')

# %%
# Ploting the rank evolution, but it does not seems ok.
rank_evol14.plot()

# %%
# Creating the transpose of the ranking evolution dataframe to plot it better
rank_evol14T = rank_evol14.T

# Selecting the 'y' values between the name of students

y = ['Ty','Lourdes','Diana','Quinn','Abigail','Alcely','Richard','Alexa',
    'Xenia','Ben','Shweta','Patrick','Jill','Mekha','Jake','Camilo','Scott',
    'Adam']

rank_evol14T.iloc[0::2].plot(y=y, title='Ranking Evolution', xlabel='Week',\
                             ylabel='Score')
plt.show()

# %%
