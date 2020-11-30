#!/usr/bin/env python
# coding: utf-8

# # Rolling Windows
#
# ## Pandas.DataFrame.rolling
#
#
# You've just learned about rolling windows.  Let's see how we can use rolling function in pandas to create the rolling windows
#
# First, let's create a simple dataframe!
#

# In[ ]:


import numpy as np
import pandas as pd
from datetime import datetime

dates = pd.date_range(datetime.strptime("10/10/2018", "%m/%d/%Y"), periods=11, freq="D")
close_prices = np.arange(len(dates))

close = pd.Series(close_prices, dates)
close


# Here, we will introduce rolling function from pandas.  The rolling function helps to provide rolling windows that can be customized through different parameters.
#
# You can learn more about [rolling function here](https://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.DataFrame.rolling.html)
#
# Let's take a look at a quick sample.

# In[ ]:


close.rolling(window=3)


# This returns a Rolling object. Just like what you've seen before, it's an intermediate object similar to the GroupBy object which breaks the original data into groups. That means, we'll have to apply an operation to these groups. Let's try with sum function.

# In[ ]:


close.rolling(window=3).sum()


# The window parameter defines the size of the moving window. This is the number of observations used for calculating the statistics which is the "sum" in our case.
#
# For example, the output for 2018-10-12 is 3, which equals to the sum of the previous 3 data points, 0 + 1 + 2.
# Another example is 2018-10-20 is 27, which equals to 8+ 9 + 10
#
# Not just for summation, we can also apply other functions that we've learned in the previous lessons, such as max, min or even more.
#
# Let's have a look at another quick example

# In[ ]:


close.rolling(window=3).min()


# Now, the output returns the minimum of the past three data points.
#
# By the way, have you noticed that we are getting NaN for close.rolling(window = 3).sum().  Since we are asking to calculate the mininum of the past 3 data points.  For 2018-10-10 and 2018-10-11, there are no enough data points in the past for our calculation, that's why we get NaN as outputs.
#
# There are many other parameters you can play with for this rolling function, such as min_period or so.  Please refer to [the python documentation](https://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.DataFrame.rolling.html) for more details
#

# ## Quiz: Calculate Simple Moving Average
#
# Through out the program, you will learn to generate alpha factors.  However, signals are always noisy.  A common practise from the industry is to smooth the factors by using simple moving average.  In this quiz, we can create a simple function that you can specify the rolling window and calculate the simple moving average of a time series.

# In[ ]:


import quiz_tests


def calculate_simple_moving_average(rolling_window, close):
    """
    Compute the simple moving average.

    Parameters
    ----------
    rolling_window: int
        Rolling window length
    close : DataFrame
        Close prices for each ticker and date

    Returns
    -------
    simple_moving_average : DataFrame
        Simple moving average for each ticker and date
    """
    # TODO: Implement Function

    return close.rolling(window=rolling_window).mean()


quiz_tests.test_calculate_simple_moving_average(calculate_simple_moving_average)


# ## Quiz Solution
# If you're having trouble, you can check out the quiz solution [here](rolling_windows_solution.ipynb).
