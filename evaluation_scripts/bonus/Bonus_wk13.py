# --------------------------------------
# 11242020 - Jill and Adam Bonus Script!
# Award Bonus points via a random emoji assignment
# Those who randomly receive the 1,2,3 medal emojis win.
# 1) this script generates a list of eligible people and
#    a list of emojis (containing 3 possible medal awards)
# 2) the emoji list is shuffled at random and then joined
#     to the eligible persons list
# 3) the dataframe is printed to a csv, which when pasted
#    into Atom, shows the resulting emoji codes in a Markdown.
# --------------------------------------

# %%
import pandas as pd
import sys
sys.path.append('../')
import eval_functions as ef
import random

# ENTER INFO HERE
weekly_winners = ["Ty", "Alexa", "Scott"]
evaluators = ["Adam", "Jill"]

# %%
# get list of students in the class using functions
# names = ef.getLastNames()
firstnames = ef.getFirstNames()
nstudent = len(firstnames)

# %%
# remove ineligible persons
not_eligible = weekly_winners + evaluators
for i in range(len(not_eligible)):
    firstnames.remove(not_eligible[i])

firstnames

# %%
# create list of emojis and shuffle randomly
# SHAPE (# of list items) MUST MATCH FIRSTNAMES LIST
emoji_list = ["&#x1F947;", "&#x1F948;", "&#x1F949;", "&#x1F62D;",
              "&#x1F62D;", "&#x1F62D;", "&#x1F622;",
              "&#x1F622;", "&#x1F622;", "&#x1F616;",
              "&#x1F616;", "&#x1F61E;", "&#x1F61E;",
              "&#x1F61E;"]
emoji_random = random.sample(emoji_list, 14)
print(emoji_random)

# %%
# convert lists to dictionaries within a dataframe
# write to csv
Full_list = pd.DataFrame(dict(emoji=emoji_random), index=firstnames)
Full_list.to_csv("random-emoji-generator-list.csv")
Full_list

# %%
award1 = "&#x1F947;"
award2 = "&#x1F948;"
award3 = "&#x1F949;"
Full_list["award1"] = Full_list["emoji"].str.find(award1)
Full_list["award2"] = Full_list["emoji"].str.find(award2)
Full_list["award3"] = Full_list["emoji"].str.find(award3)
Full_list

# %%
# Print list of bonus winners
bonus_list = Full_list[(Full_list['award1'] == 0)
                       | (Full_list['award2'] == 0)
                       | (Full_list['award3'] == 0)].index.tolist()
bonus_list

# %%
# write bonus using previous evaluator code
ef.write_bonus(bonus_list, 12)

# %%
