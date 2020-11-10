# Forecast evaluation
This  folder contains the python scripts for doing forecast evaluation. When it is your week to be the evaluator you should follow the instructions below to score the forecasts.  Additionally you should modify the scripts here to provide some added functionality and if needed update the instructions for future forecast evaluators.
____
## Table of Contents:
1. [ GitHub Instructions](#github)
1. [ Evaluation Instructions](#eval)
___
<a name="github"></a>
## Github instructions
You will be using a  branching workflow for your feature development. To understand this workflow checkout [this link](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow). I will walk you through it step by step here using GitKraken.

#### 1. Create a branch for your forecast evaluation work.
Note: if there are two of you you should just create **one branch**  one person should create the branch and then the other should checkout this branch.

#### If you are the person creating the branch:
 - first pull the forecast repo to make sure you are up to date and have the latest
 - Create a branch for your work by right clicking on the current master and selecting 'create branch here'. You will be prompted to name your branch -- name it whatever you want. I named mine "eval_dev"
 ![](assets/Readme-eef849b6.png)
 - When this is successfully done you will see that you are now working on your new branch and not the master. (Note you can always swap back to the master branch by selecting it from your local branches and 'checking it out')
 ![](assets/Readme-36b541e3.png)
 - The last step is to push this branch to GitHub so others can see it
 Click **Push** to push your branch to GitHub. When you do you will see a dialog that looks like this. Keep this set to 'origin' as shown here and select *submit*.
 ![](assets/Readme-1278d7ba.png)

 #### If you are not the person creating the branch:
 - If you are the person who wants to use this branch you should see the new branch in your list of remote branches once the branch creator has followed the steps above. You just need to select the branch from the list of remote branches as shown below and click 'Checkout origin/NameofYourBranch'.
 ![](assets/Readme-b5f8abbf.png)

 - When this is successfully done you will see that you are now working on your new branch and not the master. (Note you can always swap back to the master branch by selecting it from your local branches and 'checking it out')
 ![](assets/Readme-36b541e3.png)

### 2. Make changes commit and push using you standard GitHub workflow.  
Follow your normal workflows exactly as you did before just this time you are pushing and pulling from the branch you created rather than master. Just make sure you coordinate with your partner so you don't create any conflicts if you are both trying to push changes to the same file.
 You can see that in the image below both my local and remote versions are up to date with the 'Eval_Dev' branch and the master branch is behind my changes.
![](assets/Readme-6bbd36b3.png)

### 3. When you are ready for me to review your code submit a pull request to merge your changes into the master repo. Before you do this make sure all of your changes are committed and pushed.
  - Right click on your branch and select 'start a pull request'
  ![](assets/Readme-75f975d9.png)
  - Fill out the information for your pull request.  Select me as your reviewer. Then say 'create pull request'
  ![](assets/Readme-05707ea7.png)
  - You can submit a pull request anytime you would like me to review your code. At the latest you should submit a request by Monday morning for your new functionality but I would encourage you to submit requests as early as possible along the way so I can give you feedback and you can make adjustments as needed.  

### 4. Finally when you are done with your development and your branch has been merged back into the master make sure you swap back to the master branch for your future work.  You do this just by checking out the master branch the same way you checked out your branch in the instructions above.


___
<a name="evaluation"></a>
## Evaluation Instructions

1. **Install necessary Packages** To run these scripts you will need to first add the following to your hastools conda environment by doing the following from your shell:

 ```
 conda activate hastools
 conda install pip
 pip install dataretrieval
 ```
2.  **Work on your added functionality** Look through the scripts in this folder and add the functionality you would like. When you are done adding functionality you can do a pull request to merge your branch back in with the mater.

3. **Score the Forecasts After noon on Monday***
pull the latest updates from everyone and run the weekly forecast evaluation. Using the `score_weekly.py` script. You will need to update the following the forecast week to run this script. You can look that up in the `Seasonal_Forecast_Dates.pdf` file. This will create the `forecast_week4_results.csv` file. Look at these results and the results that get printed from the script to see how everyone did.
****Note:*** If this is a team submission week, make sure to run `crosscheck_teams.py` to verify that all the forecasts are the same

4. **Assign Bonus points** After you do the scoring decide how you will assign bonus points. You should write your  own analysis script to determine how to assign bonus points you can save this  as  `Bonus_wk#.py`. Once the bonus points are decided you should use the function `write_bonus`  from the `eval_functions.py` script to write out your Bonus points file for this week. See the bottom of the `Bonus_wk8.py` script for an example of how to do this.

5. **Document your added functionality** If any of your changes alter the instructions provided in this file update the instructions here so that people will be able to use your added functionality correctly.

5. **Calculate total scores** Run `Scoreboard.py` script to see the overall rankings and total scores.

6. **Review the forecasts to date** Using the `Get_Observations.py` script, update the forecast week number and run the script to update the csv file containing the weekly average flows. Then update the week number in `forecast_analysis.py` and run the script to review the class performance of weekly forecasts to date. The `forecast_analysis.py` script will produce timeseries graphs of everyone's 1 week and 2 week forecasts, so we can review everyone's performance to date.

7. **Update the markdown file with your scores** update the README.md file in the main directory of this folder with the points you applied this week and the updated overall scores.
