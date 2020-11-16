# 11122020 - Quinn Hull - archived/antiquated script (will not run)

import random               # Added for the assign random points by Schulze 9/25/20
# %%
# Random distribution of bonus points
# New block added by Schulze 9/25/20, for assigning the names to a 3-d array
# with first and last names, sorted alphabetically. The 3 students to get a point are
# randomly chosen and their names returned.

if random_flag:
    firstnames = np.array(['Ty', 'Lourdes', 'Diana', 'Quinn', 'Abigail', 'Alcely', 'Richard',
                           'Alexa', 'Xenia', 'Ben', 'Shweta',
                           'Patrick', 'Jill', 'Mekha', 'Jake', 'Camilo',
                           'Scott', 'Adam', 'Danielle'])
    # Selects 3 indicies from an array the lenght of our classlist
    selection = random.sample(range(0, 18), 3)
    # Takes the place of the bonus_names call in the block below
    bonus_names = firstnames[selection]
    #print(selection)                               # Used to verify the selection did not duplicate
    # Visually verifies the selection being made from the array above

print(bonus_names)
