# This script contains the functions used for plotting different plots in
# other scripts used for evaluation.

# Author: Shweta Narkhede and Camilo Salcedo
# Created on: Oct 24th, 2020
# %%
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import eval_functions as ef
import seaborn as sns

# %% Functions


def get_histogram(forecasts, obs_week, week):
    """Get Histograms:
    -----------------------------------
    This function plots histograms of predicted weekly flow data and
    the count of the flow value prediction. It also plots observed weekly
    data for last week for comaparision.
    -----------------------------------
    Parameters:
    forecasts  = array
                every student's forecast for either week 1 or 2
    obs_week    = float
                provides week's observed flow
    week        = Week number for the forecast (1 or 2)
    -----------------------------------
    Outputs:
    figure of Histogram plot
    """
    plt.figure(figsize=(8, 6))
    plt.hist(forecasts, bins=120, color='blue', alpha=0.75,
             label='Student Guesses')
    histogram = plt.plot([obs_week]*3, np.arange(0, 3, 1), color='red',
                         linestyle='-', label='Actual mean')
    title_string = 'Student guesses for Week '+str(week)
    plt.title(title_string)
    plt.xlabel('Flow Forecast (cfs)')
    plt.ylabel('Count')
    plt.legend(loc='upper left')
    return histogram


def get_simpleplot(forecasts, obs_week, week):
    """Get Simple plot:
    ------------------------------------
    This function plots a simple line plot of student's weekly averaged
    forecast for a week
    ------------------------------------
    Parameters:
    forecasts = array
                provides weekly forecasted flow of each student
    obs_week  = float
                week's observed flow
    week = string
                Week number for the forecast (1 or 2)
    ------------------------------------
    Outputs: figure of simple line plot

    """
    fig, ax = plt.subplots()
    clean_forecasts = [x for x in forecasts if not np.isnan(x)]
    class_avg = np.mean(clean_forecasts)
    simple_plot = ax.plot(forecasts, '-g', label='Forecast', alpha=.8)
    plt.axhline(y=class_avg, linestyle='dashed',
                label='Class Avg', alpha=.8, color='red')
    plt.axhline(y=obs_week, linestyle='dotted', label='Observed',
                alpha=.8, color='blue')
    plt.xticks(np.arange(0, 19, 1))
    title_string = 'Week '+str(week)+' Forecasts'
    ax.set(title=title_string, xlabel="Students",
           ylabel="Weekly Avg Flow [cfs]")
    ax.legend(fancybox=True, framealpha=1, shadow=True,
              borderpad=1)

    fig.set_size_inches(10, 4)
    return simple_plot


def plot_class_forecasts(df, week_flows, leadtime, type_plot):
    """ plot_class_forecasts()
    ---------------------------------------------------------------------
    This function plots the forecasts submitted by each student for both
    Week 1 & 2 Forecasts. In addition, is capable of plotting the absolute
    error in regards the observed value.
    ---------------------------------------------------------------------
    Parameters:
    df = Dataframe
        Includes the weekly forecast values for Week 1 and 2 for each student.
    week_flows = Dataframe
                 Observed flows per week obtained from USGS.
    leadtime: int
          leadtime for the forecast. It can only be 1 or 2
    type_plot: string
               Enter 'forecasts' to plot all submitted values, or 'abs_error'
               to plot the deviation from the observed value.
    ---------------------------------------------------------------------
    Outputs: Plot of the forecasted values or the absolute error depending the
             user input
    """

    # Request the parameters for the plots
    y_low = (input('Please introduce the lower limit for y-Axis (Hit enter for \
             default value 0):'))
    y_max = (input('Please introduce the upper limit for y-Axis (Hit enter for \
            default values):'))

    plot_weeks_inp = input('Please introduce the list of weeks to consider as \
        ["Week #", "Week #", ...]. Otherwise, if you want to include all weeks\
        hit enter:')

    if plot_weeks_inp == '':
        column_weeks = [i for i in df.columns]
    else:
        column_weeks = [i for i in df.columns if i in plot_weeks_inp]

    # Markers for the plot
    markers = ['o', 'v', '^', 'D', '>', 's', 'P', 'X', '<', '>',
               'X', 'o', 'v', 's', '^', 'P', '<', 'D', 's']

    # Get the array of firstnames for the plot
    firstnames = ef.getFirstNames()

    # Trim and set index the same weekly flow (start 8/23)
    weekly_flows = week_flows.iloc[1:len(column_weeks) + 1, 3:4]
    weekly_flows.set_index(df.columns, append=False, inplace=True)

    # Assign values depending the plot type selected
    if type_plot == 'abs_error':
        df = df.T.subtract(weekly_flows['observed'], axis=0).T
        plot_ylabel = "Deviation from Weekly Avg Flow [cfs]"
        plot_title = 'Absolute Error in '+str(leadtime) + ' Week Forecast for \n\
        HAS-Tools Class'
    elif type_plot == 'forecast':
        plot_ylabel = "Weekly Avg Flow [cfs]"
        plot_title = str(leadtime)+' Week Forecast for HAS-Tools Class \n '

    # Plotting process
    fig, ax = plt.subplots()
    ax.plot(df.T)
    for i, line in enumerate(ax.get_lines()):
        line.set_marker(markers[i])

    # Plot observed flow if the selected plot is the forecast
    if type_plot == 'forecast':
        ax.plot(column_weeks, weekly_flows['observed'], color='black',
                marker='o', linestyle='--', linewidth=3)
        plot_labels = firstnames + ['Observed Flow']
    elif type_plot == 'abs_error':
        plot_labels = firstnames

    # Format for labels and plot title
    ax.set_xlabel('Weeks \n', fontsize=13, fontweight='bold')
    ax.set_ylabel(plot_ylabel, fontsize=13, fontweight='bold')
    ax.set_title(plot_title, fontsize=15, fontweight='bold')

    # Assigns the limits for y-axis based on user's input
    if y_low == '' and y_max != '':
        ax.set_ylim(df[column_weeks].min().min(), float(y_max))
    elif y_max == '' and y_low != '':
        ax.set_ylim(float(y_low), df[column_weeks].max().max())
    elif y_max == '' and y_low == '':
        ax.set_ylim(df[column_weeks].min().min(), df[column_weeks].max().max())
    else:
        ax.set_ylim(float(y_low), float(y_max))

    ax.legend(plot_labels, loc='lower center',
              bbox_to_anchor=(.5, -0.4), ncol=6)
    fig.set_size_inches(9, 5)
    plt.show()


def plot_class_summary(df, week_flows, week, type_plot):
    """ plot_class_summary()
    ---------------------------------------------------------------------
    This function plots the summary for the forecasts submitted by the students
    for Week 1 & 2 Forecasts. It includes values such as the mean, median, min
    and max values, among others. It can be plotted as a box-whiskers plot or a
    regular plot.
    ---------------------------------------------------------------------
    Parameters:
    df = Dataframe
        Includes the weekly forecast values for Week 1 and 2 for each student.
    week_flows = Dataframe
                 Observed flows per week obtained from USGS.
    week: int
          The week for the forecast. It can only be 1 or 2
    type_plot: string
               Enter 'box' to plot the summary using a Box-Whiskers plot or
               'plot' to plot it as a regular plot.
    ---------------------------------------------------------------------
    Outputs: Plot showing the main properties of the forecast entries for HAS
             Tools class as a either a Box-Whiskers plot or a regular plot
             depending the user input
    """

    # Request the plotting parameters
    y_low = (input('Please introduce the lower limit for y-Axis (Hit enter for \
           default value 0):'))
    y_max = (input('Please introduce the upper limit for y-Axis (Hit enter for \
           default values):'))

    plot_weeks_inp = input('Please introduce the list of weeks to consider as \
        ["Week #", "Week #", ...]. Otherwise, if you want to include all weeks\
        hit enter:')

    if plot_weeks_inp == '':
        column_weeks = [i for i in df.columns]
    else:
        column_weeks = [i for i in df.columns if i in plot_weeks_inp]

    # Plotting process depending on the type of plot selected
    if type_plot == 'box':

        fig, ax = plt.subplots()
        # Setup of the features of the boxplot
        boxprops = dict(linestyle='-', linewidth=0.8, color='#00145A',
                        facecolor='white')
        capprops = dict(color='#00145A')
        whiskerprops = dict(color='#00145A', linestyle='--')
        medianprops = dict(linewidth=1.2, color='#E80B5F')

        # Plot boxplot and stripplot and set labels and title
        total_data = pd.melt(df[column_weeks])
        ax = sns.boxplot(x='variable', y='value', data=total_data,
                         linewidth=0.8, width=0.4, showfliers=False,
                         whiskerprops=whiskerprops, color='w', boxprops=boxprops,
                         medianprops=medianprops, capprops=capprops)
        ax = sns.stripplot(x='variable', y='value', data=total_data,
                           jitter=True, alpha=0.5)
        ax.set_ylabel('Flow (cfs)', fontsize=13, fontweight='bold')
        ax.set_xlabel('\n Weeks', fontsize=13, fontweight='bold')
        ax.set_title('Weekly Discharge Prediction for Week'+str(week)+'\n',
                     fontsize=15, fontweight='bold')

        # Assigns the limits for y-axis based on user's input
        if y_low == '' and y_max != '':
            ax.set_ylim(0, float(y_max))
        elif y_max == '' and y_low != '':
            ax.set_ylim(float(y_low), df[column_weeks].max().max())
        elif y_max == '' and y_low == '':
            ax.set_ylim(0, df[column_weeks].max().max())
        else:
            ax.set_ylim(float(y_low), float(y_max))

        # Plot mean and observed values
        ax.plot(np.mean(df[column_weeks]), linestyle='dashed', linewidth=1.5,
                marker='o', markersize=4, color='#0E6FDC',
                label='Class Average')
        ax.plot(column_weeks, week_flows['observed'][1:len(column_weeks)+1],
                color='black', marker='o', linestyle='--', markersize=4,
                label='Observed')

        # Legend
        ax.legend(loc='lower center',
                  bbox_to_anchor=(.5, -0.4), ncol=5)

    elif type_plot == 'plot':

        plt.style.use('seaborn-whitegrid')

        # Plot boxplot and stripplot and set labels and title
        ay = plt.plot(column_weeks, df[column_weeks].mean(), marker='o',
                      label='Class Average')
        ay = plt.plot(column_weeks, df[column_weeks].quantile(0.25), marker='o',
                      label='Lower Quantile')
        ay = plt.plot(column_weeks, df[column_weeks].quantile(0.75), marker='o',
                      label='Upper Quantile')
        ay = plt.plot(column_weeks, df[column_weeks].min(), marker='o',
                      label='Min')
        ay = plt.plot(column_weeks, df[column_weeks].max(), marker='o',
                      label='Max')
        ay = plt.plot(column_weeks, week_flows['observed'][1:len(column_weeks)+1], color='black', marker='o', linestyle='--',
                      label='Observed')
        plt.ylabel('Flow (cfs)', fontsize=13, fontweight='bold')
        plt.xlabel('\n Weeks', fontsize=13, fontweight='bold')
        plt.title('Weekly Discharge Prediction for Week # '+str(week)+'\n',
                  fontsize=15, fontweight='bold')

        # Assigns the limits for y-axis based on user's input
        if y_low == '' and y_max != '':
            plt.ylim(0, float(y_max))
        elif y_max == '' and y_low != '':
            plt.ylim(float(y_low), df[column_weeks].max().max())
        elif y_max == '' and y_low == '':
            plt.ylim(0, df[column_weeks].max().max())
        else:
            plt.ylim(float(y_low), float(y_max))

        # Legend
        plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.4), ncol=3)


# %%
