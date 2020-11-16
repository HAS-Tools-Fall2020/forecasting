# Forecast Eval Quinn and Ben

## Forecast Eval Tasks:

### 'git' organized
  0. Create branch of repo
    * follow readme - COMPLETE

  1. Archive old scripts
    * taking care to make sure there are no hidden dependencies
    * Take note of which need archival below in ('existing scripts in forecast eval repo')
    * annotate that these are 'archived' in header and in commit message (and readme?)
    * Thoughts:
      * ARCHIVE:
        * Summarzie_Scores.PY
        * 'Score_Seasonal.py' (I think)

  2. create bonus folder
    * old bonus scripts won't work, but it doesn't matter. Archive in 'bonus' folder - COMPLETE
    * annotate that these are 'archived' in header and in commit message - COMPLETE
    * edit the `'write_bonus'` function in `eval_functions.py` so that it looks up an additional directory
      * write_ bonus script updated from `file_listB = glob(os.path.join('../weekly_results', 'bonus*.csv'))` to `file_listB = glob(os.path.join('../../weekly_results', 'bonus*.csv'))`
      * COMPLETE
    * Created a bonus script (starter kit) of our own with appropropriate directory-responsive concerns... - COMPLETE

  3. create an 'figures' file to contain all pngs
    * ensure that the readme.md file know to look in asset file - COMPLETE all figures in the readme already read to the assets file
    * create a new figures file - COMPLETE
    * ensure that the new functions push these features to the 'figures' file - SEE BELOW
      * the scripts return figures, but do not save them.
    * ensure that outputs are given a unique name to reflect the week of evaluation - ONGOING (so as not to overwrite old figures)
      * @Ben We can add functionality in the script `eval_functions.py` to automatically save outputted figures with week-specific name to the new file `output_figures` in `weekly_results`

  4. Document the forecast_evaluation workflow (i.e. what the code is really doing)
    * Create an illustrator file showing the workflow/connectivity of functions / scripts - COMPLETE
      * add both file and png to assets file
    * Add this workflow chart to the readme with descriptive text - COMPLETE


  5. Update the readme - COMPLETE
    * Add step 4 (above) - COMPLETE
    * Ensure filenames and steps described are consistent - COMPLETE
    * Include an 'etiquette' notice so that the directory doesn't get trashed and confusing in the future - COMPLETE
      * use descriptive committing. We should be able to know what you did and why. - COMPLETE
      * include a place to write out (in text) your thinking and additions to the repo? - COMPLETE
      * remind to remove unnecessary files and try to be as concise as possible - COMPLETE
    * Rearrange the and annotate the order of things based on flow chart, separate into 'codes of conduct' and workflow - COMPLETE

    * Change log:
      * changed anchor tag to 'evaluation' header (see -> https://stackoverflow.com/questions/2822089/how-to-link-to-part-of-the-same-document-in-markdown/16426829#16426829)
      * changes forecast week4 results.csv to forecast week# results.csv
      * changes to description of bonus challenge to make it clearer that write_bonus needs to be used at the bottom of the script and says where the output csv will be saved
      * Added conda forge install of seaborn package to first step of workflow
      * rearranged the order of things to make it more self-describing and emphasize order and etiquette!

  6. check to make sure that the forecast point allocation reflects reality! - UNRESOLVED


  7. Get rid of:
    scoreboard.csv in main directory - UNRESOLVED
    scoreboard.png in main directory - UNRESOLVED

  8. Improve comments and documentation in the scripts - UNRESOLVED

  9. ADD 'input' to any script that needs to pull in the year - COMPLETE

### plot pretty
  0. Wait until 'git organized' is complete
  1. Keep in mind new dependencies establish in prior step
  2. Q thoughts:
    * @Ben We can add functionality in the script `eval_functions.py` to automatically save outputted figures with week-specific name to the new file `output_figures` in `weekly_results`


### bonus pt function
  * note the function 'write_bonus' needs to be called by the bonus function we write
  * note that the files and functions called by our bonus pt function need to respect the new location of the function
  * I created placeholder for our script `bonus_week12.py`
