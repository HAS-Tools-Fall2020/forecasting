#%%
import pandas as pd
import numpy as np
#%%
weeknum = 7
filename = 'forecast_week' + str(weeknum) + '_results.csv'
filepath = os.path.join('../weekly_results', filename)
data = pd.read_csv(filepath)
# %%
data['sum'] = data['1week_difference'] + data['2week_difference']
data.sort_values('sum')