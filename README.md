# HAS Tools Forecast Competition
Welcome to the HAS streamflow forecasting competition! Over the course of the semester we will be honing our Python skills and testing them out using weekly streamflow forecasts of the Verde River.  The setup and scoring for the competition is as follows.

____
## Table of Contents:
1. [ Scoreboard](#scoreboard)
1. [ Instructions](#howto)
1. [ Scoring](#points)
1. [ Prizes!](#prizes)
1. [ Evaluator Instructions](#evaluator)
1. [ Evaluator Signup Dates](#evaluatorlist)

___
<a name="Scoreboard"></a>
## Scoreboard

|      | Name    | Points    |
|:-----|---------|---------  |
|  1   | Camilo    |    2    |
|  1   | Quinn     |    2    |
|  1   | Shweta    |    2    |
|  2   | Diana     |    1    |
|  2   | Scott     |    1    |
|  2   | Alcely    |    1    |
|  2   | Lourdus   |    1    |
|  2   | Abagail   |    1    |
|  2   | Richard   |    1    |
|  2  | Adam      |    1    |
|  3  |  Everyone Else       |     0      |


## Seasonal Forecast Leaders

|  Fcst #    | First   | Second    | Third    |
|:-----------|---------|---------  |--------- |
|  1         |         |           |          |
|  2         |         |           |          |
|  3         |         |           |          |
|  4         |         |           |          |
|  5         |         |           |          |
|  6         |         |           |          |
|  7         |         |           |          |
|  8         |         |           |          |
|  9         |         |           |          |
|  10        |         |           |          |
|  11        |         |           |          |
|  12        |         |           |          |

### Forecast 1 Points Awarded:
- **One Week forecast (8/30-9/5)**:
  - Observed flow = 60.22 cfs
  - First place: 60 cfs, Camilo, Quinn & Shweta
  - Second place: 59 cfs, Diana & Scott
  - Third place: 65 cfs, Lourdus & Alceley


- **Two week forecast (9/6 - 9/12)**:


- **Bonus points**:
  - Abagail, Richard & Adam
  - for being the first non ranking forecasts to be submitted on GitHub

-----
### Template forecast scoring text copy this above and fill out the info to add a new week.
### Forecast X Points Awarded:
- **One Week forecast (m/dd-m/dd)**:
  - Observed flow = XX cfs
  - First place: XX cfs, NAMES
  - Second place: XX cfs, NAMES
  - Third place: XX cfs, NAMES

- **Two week forecast (m/dd - m/dd)**:


- **Bonus points**:
  - NAMES
  - Reason

___
<a name="howto"></a>
## How to play:
It sounds complicated, but don't worry it's not that bad:
1. Every week you will generate three streamflow forecasts:
   - **Seasonal Forecast**: A weekly forecast for each of the 16 weeks of the semester using only the observed streamflow through the start of the semester.
   - **One week forecast**: A forecast for the streamflow next week using the data up to this week.
   - **Two week forecast**: A forecast for the streamflow two weeks from now using the data up to this week.

2. Streamflow forecasts are due by Monday at noon. Late forecasts  will not be accepted for the competition and will receive 0 points. The forecasting timelines are provided in the dates files contained in this folder.

3. Every week your forecast entries should be entered in your csv in the *forecast_entries* folder. All values should be entered as weekly average flow in **cubic feet per second [cfs]**


___
<a name="scoring"></a>
## How to get points:
First a disclaimer: Note that this scoring is only for the forecasting competition. For your class grade, submitting a forecast on time according to the instructions for the week will give you full credit regardless of how well your forecast rates with respect to others.

That said there will be prizes for the forecast competition (described below) and the scoring will be follows:

 - 2 points to the closest weekly forecast and 1 point to the second and third place forecasts awarded every week (ties are allowed and in that case all tied parties gets the same points)
 - 2 points to the closest 2 week forecast and 1 point to the second and third place forecasts awarded every week (ties are allowed and in that case all tied parties gets the same points)
 - 3 points to be awarded by the evaluator for the week to three *different* people based on whatever criteria the evaluator chooses (literally anything -- most wrong, best consistency between forecasts, most extreme forecast, greatest difference in one week vs two week performance). The only constraints are: (1) the evaluator cannot give points to themselves or the top three students on the current leaderboard and (2) they most show their work (e.g. a graph or a table)
 - The seasonal forecasts will be scored based on the RMSE across all 16 weeks for a given forecast at the end of the semester. With 2 points to the closest and 1 point to the second and third place scores for every forecast issued (i.e. there will be 15 sets of points awarded one for each week that seasonal forecasts were issued). We will keep a running tab on how everyone's seasonal forecasts are doing throughout the semester as observations come in but points will only be awarded at the end.

    *NOTE: I reserve the right to change the rules and award bonus points as I see fit throughout the semester to keep things interesting :)*

 ___
 <a name="prizes"></a>
 # Prizes
1. Every week the top scorer(s) for that week (i.e. just the points being awarded in the week not the overall score) will get a free pass on the written portion of the following week's assignment. Winners will still do the assignment and submit your forecast but can skip the written explanation part. The free pass is only good for the week following the winning.

2. At the end of sections one and two, the top three scorers overall will get an additional free pass on a writing assignment to be used any week they want in addition to three bonus points to be distributed to anyone other than themselves however they see fit.

3. At the end of semester the overall winner will be crowned and they will get a 5% bump on their overall course grade. Second and third place will receive a 3% bump.

 ___
 <a name="evaluators"></a>
 # Evaluator Job Description :

 Each week one person will be assigned the job of 'Evaluator'. Your job description is as follows. Note that for your development tasks you should create a branch and then do a pull request when you are ready to merge them in.

 1. **Run the forecast evaluation scripts to score the weekly forecasts** after the forecast submission deadline (noon on Monday). You will be evaluating two forecasts (1) the one week forecast from last week and (2) the two week forecast from  two weeks ago
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
    - To do this you only need to update the forecast_num(it shoudl be 1 - your previous forecast number) and the forecast_col to '2week'
    - Run the script again to generate the summary for that weekly forecast.


  - Look at the summary that is generated in the weekly_results folder and decide how you will assign your bonus points
    - Add the bonus points names to the top of the script and re-run so that these points get added to the csv.  
    
  - Next modify the forecast week number in 'Get_Observations.py' and run this script to download the most recent observations. If this has worked you should see the *./weekly_results/weekly_observations.csv* file has been updated with the most recent streamflow values.  

 1. Make an addition to improve the functionality of the forecast evaluation scripts. For example, you could make a graphical summary output, add something to autogenerate our leaderboard, move analysis into functions, add documentation, etc. Additional suggestions are also included at the top of each script but you can feel free to make whatever addition you would like. Note that your additions should be made directly to the evaluation scripts in the **evaluation_scripts** folder.
 3. Do some analysis on your own and assign your bonus points. Your analysis must be done in python, and can build on others if you want, but should be unique (i.e. don't use the same criteria as previous weeks). Your analysis should be submitted in a separate python script named: "lastname_weekx_analysis.py" in the *evaluation_scripts* folder. *Note:* this can use your added functionality but does not count as your added functionality).

 3. Update the **scoreboard**, **seasonal forecast leaders** and  **weekly points awarded** at the top of this readme.

 4. Make a short presentation for Tuesday class (1) summarizing the points awarded this week, (2) the current scores and how they changed, (3) how you awarded your bonus points and, (4) what functionality you added to our forecast calculation.

 *Note: You can start working on your analysis script and your functionality addition before the forecasts have actually been submitted and just run it after Monday at noon. For the analysis you can start on it anytime, as this will be occurring within your own script. For the functionality addition you can only start after class on Tuesday when the previous evaluator is finished.*

 ___
 <a name="evaluatorlist"></a>
 # Evaluator Assignments
 2. September 8: Laura
 3. September 15: Laura
 4. September 22:
 5. September 29:
 6. October 6:
 7. October 13:
 8. October 20:
 9. October 27:
 10. November 3:
 11. November 10:
 12. November 17:
 13. November 24:
 14. November 31:
 15. December 8:
