# This script contains the functions used for plotting different plots in other scripts used for evaluation

# Author: Shweta Narkhede and Camilo Salcedo
# Created on: Oct 24th, 2020
# %%
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

# %%


def get_histogram(forecasts1, obs_week, title_string):
    """Get Histograms:
    -----------------------------------
    This function plots histograms of predicted weekly flow data and
    the count of the flow value prediction. It also plots observed weekly
    data for last week for comaparision.
    -----------------------------------
    Parameters:
    forecasts1  = array
                every student's forecast for week 1
    obs_week    = float
                provides week's observed flow
    title_string = string
                   provides the title of the histogram
    -----------------------------------
    Outputs:
    figure of Histogram plot
    """
    plt.figure(figsize=(8, 6))
    plt.hist(forecasts1, bins=120, color='blue', alpha=0.75,
             label='Student Guesses')
    histogram = plt.plot([obs_week]*3, np.arange(0, 3, 1), color='red',
                         linestyle='-', label='Actual mean')
    plt.title(title_string)
    plt.xlabel('Flow Forecast (cfs)')
    plt.ylabel('Count')
    plt.legend(loc='upper left')
    return histogram


def get_simpleplot(forecasts, class_avg, obs_week, title_string):
    """Get Simple plot:
    ------------------------------------
    This function plots a simple line plot of student's weekly averaged
    forecast for a week
    ------------------------------------
    Parameters:
    forecasts = array
                provides weekly forecasted flow of each student
    class_avg = float
                provide average value of flow forecatsed by all students
    obs_week  = float
                week's observed flow
    title_string = string
                   provides the title of the plot
    ------------------------------------
    Outputs: figure of simple line plot

    """
    fig, ax = plt.subplots()
    simple_plot = ax.plot(forecasts, '-g', label='Forecast', alpha=.8)
    plt.axhline(y=class_avg, linestyle='dashed',
                label='Class Avg', alpha=.8, color='red')
    plt.axhline(y=obs_week, linestyle='dotted', label='Observed',
                alpha=.8, color='blue')
    plt.xticks(np.arange(0, 19, 1))
    ax.set(title=title_string, xlabel="Students",
           ylabel="Weekly Avg Flow [cfs]")
    ax.legend(fancybox=True, framealpha=1, shadow=True,
              borderpad=1)

    fig.set_size_inches(10, 4)
    return simple_plot
