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

1. Create a branch for your forecast evaluation work. You can refer to the
 - first pull the forecast repo to make sure you are up to date and have the latest
 - Create a branch for your work by right clicking on the current master and selecting 'create branch here'. You will be prompted to name your branch -- name it whatever you want. I named mine "eval_dev"
 ![](assets/Readme-eef849b6.png)
 - When this is successfully done you will see that you are now working on your new branch and not the master. (Note you can always swap back to the master branch by selecting it from your local branches and 'checking it out')
 ![](assets/Readme-36b541e3.png)


2. Make some updates to files and **commit** your changes using your standard GitHub workflow.  

3. Click **Push** to push your branch to GitHub. When you do you will see a dialog that looks like this. Keep this set to 'origin' as shown here and select *submit*.
![](assets/Readme-1278d7ba.png)

4. From here you can continue committing changes and pushing them as you normally would. Note that you will be pushing to your branch on GithHub though not the master branch. You can see that in the image below both my local and remote versions are up to date with the 'Eval_Dev' branch and the master branch is behind my changes.
![](assets/Readme-6bbd36b3.png)

5. Finally when you are done you should submit a pull request to merge your changes into the master repo. Before you do this make sure all of your changes are committed and pushed.
  - Right click on your branch and select 'start a pull request'
  ![](assets/Readme-75f975d9.png)
  - Fill out the information for your pull request.  Select me as your reviewer. Then say 'create pull request'
  ![](assets/Readme-05707ea7.png)


___
<a name="evaluation"></a>
## Evaluation Instructions

1. **Install necessary Packages** To run these scripts you will need to first add the following to your hastools conda environment by doing the following from your shell:

 ```
 conda activate hastools
 conda install pip
 pip install dataretrieval
 ```
2.  ** Work on your added functionality** Look through the scripts in this folder and add the functionality you would like. When you are done adding functionality you can do a pull request to merge your branch back in with the mater.

3. **Score the Forecasts After noon on Monday** pull the latest updates from everyone and run the weekly forecast evaluation. Using the `score_weekly.py` script. You will need to update the following the forecast week to run this script. You can look that up in the `Seasonal_Forecast_Dates.pdf` file. This will create the `forecast_week4_results.csv` file. Look at these results and the results that get printed from the script to see how everyone did.

4. **Assign Bonus points** After you do the scoring decide how you will assign bonus points. You should write your  own analysis script to determine how to assign bonus points you can save this  as  `Bonus_wk#.py`. Once the bonus points are decided, change the  `names` and `forecast_week` in the the bonus points cell on `Bonus_Points.py` and run this section to write out your Bonus points file for this week.

5. **Calculate total scores** Run `Scoreboard.py` script to see the overall rankings and total scores.

6. **Review the forecasts to date** Using the `Get_Observations.py` script, update the forecast week number and run the script to update the csv file containing the weekly average flows. Then update the week number in `forecast_analysis.py` and run the script to review the class performance of weekly forecasts to date. The `forecast_analysis.py` script will produce timeseries graphs of everyone's 1 week and 2 week forecasts, so we can review everyone's performance to date.

7. **Update the markdown file with your scores** update the README.md file in the main directory of this folder with the points you applied this week and the updated overall scores.
