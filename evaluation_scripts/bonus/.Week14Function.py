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

# %%
