
#%%
# Week 6 - Bonus Points assigned to lowest scores from previous week (see "Scoreboard.png")
bonus_names = ['Ben']       # Lowest score
bonus_potentials = ['Alcely', 'Shweta', 'Jake',
                    'Danielle', 'Ty']     # Second lowest scores (tied)
weeknum = 6  # Forecast week
random_flag = False  # Set this to true if you wan to override the names

# Create random loop to obtain a max of 3 bonus recipients
while len(bonus_names) < 3:
    # 1 random samples per iteration
    temp = random.sample(bonus_potentials, 1)
    if temp not in bonus_names:     # Ensure no repeats
        bonus_names = bonus_names + temp  # Add randomed name to 2nd list
print(bonus_names)
