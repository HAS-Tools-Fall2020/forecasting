# Forecast evaluation
This  folder contains the python scripts for doing forecast evaluation. When it is your week to be the evaluator you should follow the instructions below to score the forecasts.  Additionally you should modify the scripts here to provide some added functionality and if needed update the instructions for future forecast evaluators.

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

 - To run these scripts you will need to first add the following to your hastools conda environment by doing the following from your shell:
 ```
 conda activate hastools
 conda install pip
 pip install climata
 ```

 - First evaluate the 1 week forecast for last week:
     - Open Score_weekly.py from the evaluation scripts and update the start and stop dates to match the start and stop dates for the previous week as listed in the Weekly_forecast_date.pdf
     - Set the forecast number to match the forecast number for which this set of dates is the week1 forecast
     - set the forecast_col to be '1week'
     - Run the script to evaluate the forecasts

 - Next evaluate the 2 week forecast made two weeks ago for last week:
   - To do this you only need to update the forecast_num(it should be 1 - your previous forecast number) and the forecast_col to '2week'
   - Run the script again to generate the summary for that weekly forecast.
