#!/usr/bin/env python
# coding: utf-8

# # Rate of Returns Over Multiple Periods
#
# ## Numpy.cumsum and Numpy.cumprod
#
#
# You've just leared about active returns and passive returns.  Another important concept related to returns is "Cumulative returns" which is defined as the returns over a time period.  You can read more about rate of returns [here](https://en.wikipedia.org/wiki/Rate_of_return)!
#
# There are two ways to calcualte cumulative returns, depends on how the returns are calculated.  Let's take a look at an example.
#

# In[ ]:


import numpy as np
import pandas as pd
from datetime import datetime

dates = pd.date_range(datetime.strptime("1/1/2016", "%m/%d/%Y"), periods=12, freq="M")
start_price, stop_price = 0.24, 0.3
abc_close_prices = np.arange(
    start_price, stop_price, (stop_price - start_price) / len(dates)
)

abc_close = pd.Series(abc_close_prices, dates)
abc_close


# Here, we have the historical prices for stock ABC for 2016.  We would like to know the yearly cumulative returns for stock ABC in 2016 using time-weighted method, assuming returns are reinvested.  How do we do it?  Here is the formula:
#
# Assume the returns over n successive periods are:
#
# $ r_1, r_2, r_3, r_4, r_5, ..., r_n $
#
# The cumulative return of stock ABC over period n is the compounded return over period n:
#
# $ (1 + r_1)(1 + r_2)(1 + r_3)(1 + r_4)(1 + r_5)...(1 + r_n) - 1 $
#
# First, let's calculate the returns of stock ABC.

# In[ ]:


len(abc_close)


# In[ ]:


returns = abc_close / abc_close.shift(1) - 1
returns


# In[ ]:


len(returns)


# The cumulative return equals to the product of the daily returns for the n periods.
# That's a very long formula.  Is there a better way to calculate this.
#
#
# The answer is yes, we can use numpy.cumprod().
#
# For example, if we have the following time series: 1, 5, 7, 10 and we want the product of the four numbers.  How do we do it?  Let's take a look!

# In[ ]:


lst = [1, 5, 7, 10]
np.cumprod(lst)


# The last element in the list is 350, which is the product of 1, 5, 7, and 10.
#
# OK, let's use numpy.cumprod() to get the cumulative returns for stock ABC

# In[ ]:


(returns + 1).cumprod()[len(returns) - 1] - 1


# The cumulative return for stock ABC in 2016 is 22.91%.
#
# The other way to calculate returns is to use log returns.
#
# The formula of log return is the following:
#
# $ LogReturn = ln(\frac{P_t}{P_t - 1}) $
#
# The cumulative return of stock ABC over period n is the compounded return over period n:
#
# $ \sum_{i=1}^{n} r_i = r_1 + r_2 + r_3 + r_4 + ... + r_n $
#
# Let's see how we can calculate the cumulative return of stock ABC using log returns.
#
# First, let's calculate log returns.

# In[ ]:


log_returns = (np.log(abc_close).shift(-1) - np.log(abc_close)).dropna()
log_returns.head()


# The cumulative sum equals to the sum of the daily returns for the n periods which is a very long formula.
#
# To calculate cumulative sum, we can simply use numpy.cumsum().
#
# Let's take a look at our simple example of time series 1, 5, 7, 10.
#

# In[ ]:


lst = [1, 5, 7, 10]
np.cumsum(lst)


# The last element is 23 which equals to the sum of 1, 5, 7, 10
#
# OK, let's use numpy.cumsum() to get the cumulative returns for stock ABC

# In[ ]:


cum_log_return = log_returns.cumsum()[len(log_returns) - 1]
np.exp(cum_log_return) - 1


# The cumulative return for stock ABC in 2016 is 22.91% using log returns.

# ## Quiz: Arithmetic Rate of Return
#
# Now, let's use cumprod() and cumsum() to calculate average rate of return.
#
# For consistency, let's assume the rate of return is calculated as $ \frac{P_t}{P_t - 1} - 1 $
#
# ### Arithmetic Rate of Return:
#
# $ \frac{1}{n} \sum_{i=1}^{n} r_i = \frac{1}{n}(r_1 + r_2 + r_3 + r_4 + ... + r_n) $

# In[ ]:


import quiz_tests


def calculate_arithmetic_rate_of_return(close):
    """
    Compute returns for each ticker and date in close.

    Parameters
    ----------
    close : DataFrame
        Close prices for each ticker and date

    Returns
    -------
    arithmnetic_returns : Series
        arithmnetic_returns at the end of the period for each ticker

    """
    # TODO: Implement Function

    returns = close / close.shift(1) - 1
    arithmetic_returns = (
        returns.cumsum(axis=0).iloc[returns.shape[0] - 1] / returns.shape[0]
    )

    return arithmetic_returns


quiz_tests.test_calculate_arithmetic_rate_of_return(calculate_arithmetic_rate_of_return)


# ## Quiz Solution
# If you're having trouble, you can check out the quiz solution [here](cumsum_and_cumprod_solution.ipynb).
