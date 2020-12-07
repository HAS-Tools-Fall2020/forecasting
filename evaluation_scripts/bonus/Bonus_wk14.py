# %%
# Week 14 Bonus Script
# Evaluator: Xenia
# Date: December 01, 2020

# Since we are celebrating 4th of July (yes, we are), the bonus will be given \
# randomly to those which name starts with letters "U", "S", or "A" (USA).

# %%
import pandas as pd
import sys
sys.path.append('../')
import eval_functions as ef
import random

# %%
# ENTER INFO HERE
weekly_winners = ["Diana", "Alexa", "Ben", "Jake"]
evaluators = ["Xenia"]

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
nstudent = len(firstnames)
nstudent

# %%
# Checking for the names that starts with "U", "S", or "A" letters.

checkU = 'U'
checkS = 'S'
checkA = 'A'

U_names = [idx for idx in firstnames if idx[0].lower() == checkU.lower()] 
S_names = [idx for idx in firstnames if idx[0].lower() == checkS.lower()] 
A_names = [idx for idx in firstnames if idx[0].lower() == checkA.lower()] 
  
# print result
USA_names = U_names + S_names + A_names
print("The list of matching first letter with USA is: " + str(USA_names))

# %%
bonus_list = random.sample(USA_names, 3)
print(bonus_list)

# %%
# Calling function: write_bonus(bonus_names, weeknum)
ef.write_bonus(bonus_list, 14)

# %%
