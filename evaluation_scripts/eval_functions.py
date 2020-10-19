# %%
import pandas as pd
import os

# %%
# Alexa's Forecast Functions Week 8


def getLastNames():
    """Get classlist of last names.
    ---------------------------------
    This function takes no input and returns the list of
    students' last names in the class.  This makes it easy to
    access the class list from any script.
    ---------------------------------
    Parameters:
    none
    ----------------------------------
    Outputs:
    lastNames = list of strings
                contains students's last names
    """
    lastNames = ['ferre', 'fierro', 'hsieh', 'hull', 'kahler',
                 'lau', 'marcelain', 'marcovecchio', 'medina',
                 'mitchell', 'narkhede', 'neri', 'noonan',
                 'pereira', 'ridlinghaver', 'salcedo',
                 'schulze', 'stratman', 'tadych']
    return lastNames


def getFirstNames():
    """Get classlist of first names.
    ---------------------------------
    This function takes no input and returns the list of
    students' first names in the class.  This makes it easy to
    access the class list from any script.
    ---------------------------------
    Parameters:
    none
    ----------------------------------
    Outputs:
    firstNames = list of strings
                 contains student's first names
    """
    firstNames = ['Ty', 'Lourdes', 'Diana', 'Quinn',
                  'Abigail', 'Alcely', 'Richard',
                  'Alexa', 'Xenia', 'Ben', 'Shweta', 'Patrick',
                  'Jill', 'Mekha', 'Jake', 'Camilo',
                  'Scott', 'Adam', 'Danielle']
    return firstNames


def weekDates(weekNumber):
    """Compute the one and two week forecasts using model.
    ---------------------------------
    This function takes no input and returns the list of
    students' first names in the class.  This makes it easy to
    access the class list from any script.
    ---------------------------------
    Parameters:
    weekNumber = integer
                 number indicating the week of the semester
    ----------------------------------
    Outputs:
    startDate = string
                contains start date of forecast week
    stopDate = string
               contains end date of forecast week
    """

    datefile = os.path.join('..', 'Seasonal_Foercast_Dates.csv')
    forecast_dates = pd.read_csv(datefile,
                                 index_col='forecast_week')

    startDate = forecast_dates.loc[weekNumber, 'start_date']
    stopDate = forecast_dates.loc[weekNumber, 'end_date']
    return startDate, stopDate
