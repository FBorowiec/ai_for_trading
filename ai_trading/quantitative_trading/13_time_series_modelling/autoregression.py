#!/usr/bin/env python
# coding: utf-8

# # Autoregressive moving average

# ## Install packages

# In[ ]:


import sys

# get_ipython().system("{sys.executable} -m pip install -r requirements.txt")


# In[ ]:


import pandas as pd
import numpy as np
import os
from statsmodels.tsa.arima_model import ARMA
import matplotlib.pyplot as plt
import seaborn as sns
import quiz_tests


# In[ ]:


sns.set()
# note that for the figure size to show, this cell should be run
# separately from the import of pyplot
plt.style.use("ggplot")
plt.rcParams["figure.figsize"] = (14, 8)


# ## Simulate return series with autoregressive properties

# In[ ]:


from statsmodels.tsa.arima_process import ArmaProcess

np.random.seed(200)

ar_params = np.array([1, -0.5])
ma_params = np.array([1, -0.3])
ret = ArmaProcess(ar_params, ma_params).generate_sample(nsample=5 * 252)

ret = pd.Series(ret)
drift = 100
price = pd.Series(np.cumsum(ret)) + drift


# In[ ]:


ret.plot(
    figsize=(15, 6), color=sns.xkcd_rgb["pale purple"], title="simulated return series"
)
plt.show()


# In[ ]:


price.plot(
    figsize=(15, 6), color=sns.xkcd_rgb["baby blue"], title="simulated price series"
)
plt.show()


# ### log returns

# In[ ]:


lret = np.log(price) - np.log(price.shift(1))
lret = lret[1:]


# ## autocorrelation
#
# Use autocorrelation to get a sense of what lag to use for the autoregressive model.

# In[ ]:


from statsmodels.graphics.tsaplots import plot_acf


# In[ ]:


_ = plot_acf(lret, lags=10, title="log return autocorrelation")


# Since the sample series was simulated to have autoregressive properties, we also see autocorrelation between the current periods and the lags.
#
# Note that with actual stock data, there won't be much autocorrelation of returns from one day to the next.
# Stock returns (log returns and normal returns) can be described as a "random walk", in that each new period's value is more or less random.

# ## plot partial autocorrelation

# In[ ]:


from statsmodels.graphics.tsaplots import plot_pacf


# Notice how the partial autocorrelation of price shows that most of the correlation is found in the previous period.  Partial autocorrelation is different from autocorrelation in that it shows the influence of each period that is not attributed to the other periods leading up to the current period.  In other words, the two-day lag had a fairly strong correlation with the current value because it had a strong correlation with the one-day lag. However, the two-day lag's partial correlation with the current period that isn't attributable to the one-day lag is relatively small.

# In[ ]:


_ = plot_pacf(
    lret,
    lags=10,
    title="log return Partial Autocorrelation",
    color=sns.xkcd_rgb["crimson"],
)


# ## Discussion
#
# Notice that there isn't much correlation between previous periods with the current period.  In general, using past stock returns to predict future stock returns is rather difficult.  Volatility tends to have more of a correlation with past volatility.  We'll cover volatility in a later lesson within this module.

# ## Ljung-Box Test
#
# The Ljung-Box test helps us check whether the lag we chose gives autocorrelations that are significantly different from zero.  The null hypothesis is that the previous lags as a whole are not correlated with the current period.  If the p-value is small enough (say 0.05), we can reject the null and assume that the past lags have some correlation with the current period.
#
# ```
#
# returns:
# lbvalue (float or array) – test statistic
# pvalue (float or array) – p-value based on chi-square distribution
# ... (we'll ignore the other outputs, which are for another similar hypothesis test)
# ```

# In[ ]:


from statsmodels.stats.diagnostic import acorr_ljungbox


# In[ ]:


lb_test_stat, lb_p_value = acorr_ljungbox(lret, lags=20)
lb_p_value


# ## Discussion
#
# Since this series was simulated to have autoregressive properties, the Ljung-Box test shows p-values less than 0.05 for the 20 lag periods that we tested.

# ## Fit an ARMA model
#
# For the purpose of familiarizing ourselves with the ARMA model, we'll fit the model to our simulated return series.
#
# We'll just use one lag for the autoregression and one lag for the moving average.
# Check out the [statsmodel arma](https://www.statsmodels.org/dev/generated/statsmodels.tsa.arima_model.ARMA.html) documentation.

# In[ ]:


from statsmodels.tsa.arima_model import ARMA


# In[ ]:


AR_lag_p = 1
MA_lag_q = 1
order = (AR_lag_p, MA_lag_q)
arma_model = ARMA(lret.values, order=order)
arma_result = arma_model.fit()
arma_pred = pd.Series(arma_result.fittedvalues)


# ## View fitted predictions against actual values

# In[ ]:


plt.plot(lret, color=sns.xkcd_rgb["pale purple"])
plt.plot(arma_pred, color=sns.xkcd_rgb["dark sky blue"])
plt.title("Log returns and predictions using an ARMA(p=1,q=1) model")
print(
    f"Fitted AR parameter {arma_result.arparams[0]:.2f}, MA parameter {arma_result.maparams[0]:.2f}"
)


# ## Discussion
#
# In general, autoregressive moving average models are not able to forecast stock returns because stock returns are non-stationary and also quite noisy.
#
# There are other techniques that build upon the concepts of ARMA models, so the goal here was really to help you get familiar with these concepts, as they are the basis for other models that you'll see later in this module.

# ## Quiz: ARIMA
#
# Fit an autoregressive integrated moving average model.  Choose an order of integration of 1, autoregresion lag of 1, and moving average lag of 1.
#
# Check out the [stats model arima](http://www.statsmodels.org/0.6.1/generated/statsmodels.tsa.arima_model.ARMAResults.html) documentation to help you.

# In[ ]:


from statsmodels.tsa.arima_model import ARIMA


# In[ ]:


def fit_arima(lret):

    # TODO: choose autoregression lag of 1
    AR_lag_p = 1

    # TODO: choose moving average lag of 1
    MA_lag_q = 1

    # TODO: choose order of integration 1
    order_of_integration_d = 1

    # TODO: Create a tuple of p,d,q
    order = (AR_lag_p, MA_lag_q, order_of_integration_d)

    # TODO: create an ARIMA model object, passing in the values of the lret pandas series,
    # and the tuple containing the (p,d,q) order arguments
    arima_model = ARIMA(lret.values, order=order)
    arima_result = arima_model.fit()

    # TODO: from the result of calling ARIMA.fit(),
    # save and return the fitted values, autoregression parameters, and moving average parameters
    fittedvalues = arima_result.fittedvalues
    arparams = arima_result.arparams
    maparams = arima_result.maparams

    return fittedvalues, arparams, maparams


quiz_tests.test_fit_arima(fit_arima)


# In[ ]:


fittedvalues, arparams, maparams = fit_arima(lret)
arima_pred = pd.Series(fittedvalues)
plt.plot(lret, color=sns.xkcd_rgb["pale purple"])
plt.plot(arima_pred, color=sns.xkcd_rgb["jade green"])
plt.title("Log Returns and predictions using an ARIMA(p=1,d=1,q=1) model")
print(f"fitted AR parameter {arparams[0]:.2f}, MA parameter {maparams[0]:.2f}")


# If you're stuck, you can also check out the solution [here](autoregression_solution.ipynb)
