# Forecast evaluation
This  folder contains the python scripts for doing forecast evaluation. When it is your week to be the evaluator you should follow the instructions below to score the forecasts.  Additionally you should modify the scripts here to provide some added functionality and if needed update the instructions for future forecast evaluators.

## Step by step Instructions
1. Create a branch for your forecast evaluation work

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
