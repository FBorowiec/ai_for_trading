#!/usr/bin/env python
# coding: utf-8

# # Covariance Matrix

# ## Install libraries

# In[ ]:


import sys

# get_ipython().system('{sys.executable} -m pip install -r requirements.txt')


# ## Imports

# In[ ]:


import numpy as np
import covariance_matrix_quiz_tests


# ## Hints
#
# ### covariance matrix
# If we have $m$ stock series, the covariance matrix is an $m \times m$ matrix containing the covariance between each pair of stocks.  We can use [numpy.cov](https://docs.scipy.org/doc/numpy/reference/generated/numpy.cov.html) to get the covariance.  We give it a 2D array in which each row is a stock series, and each column is an observation at the same period of time.
#
# The covariance matrix $\mathbf{P} =
# \begin{bmatrix}
# \sigma^2_{1,1} & ... & \sigma^2_{1,m} \\
# ... & ... & ...\\
# \sigma_{m,1} & ... & \sigma^2_{m,m}  \\
# \end{bmatrix}$

# ## Quiz

# In[ ]:


import numpy as np


def covariance_matrix(returns):
    """
    Create a function that takes the return series of a set of stocks
    and calculates the covariance matrix.

    Parameters
    ----------
    returns : numpy.ndarray
        2D array containing stock return series in each row.

    Returns
    -------
    x : np.ndarray
        A numpy ndarray containing the covariance matrix
    """

    # covariance matrix of returns
    cov = np.cov(returns)

    return cov


quiz_tests.test_covariance_matrix(covariance_matrix)


# In[ ]:


"""Test with a 3 simulated stock return series"""
days_per_year = 252
years = 3
total_days = days_per_year * years

return_market = np.random.normal(loc=0.05, scale=0.3, size=days_per_year)
return_1 = (
    np.random.uniform(low=-0.000001, high=0.000001, size=days_per_year) + return_market
)
return_2 = (
    np.random.uniform(low=-0.000001, high=0.000001, size=days_per_year) + return_market
)
return_3 = (
    np.random.uniform(low=-0.000001, high=0.000001, size=days_per_year) + return_market
)
returns = np.array([return_1, return_2, return_3])

"""try out your function"""
cov = covariance_matrix(returns)

print(f"The covariance matrix is \n{cov}")


# If you're stuck, you can also check out the solution [here](m3l4_covariance_solution.ipynb)

# In[ ]:
