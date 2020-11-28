#!/usr/bin/env python
# coding: utf-8

# # Testing if a Distribution is Normal

# ## Imports

# In[ ]:


import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import test_normality_quiz_tests

# Set plotting options
# get_ipython().run_line_magic("matplotlib", "inline")
plt.rc("figure", figsize=(16, 9))


# ## Create normal and non-normal distributions

# In[ ]:


# Sample A: Normal distribution
sample_a = stats.norm.rvs(loc=0.0, scale=1.0, size=(1000,))

# Sample B: Non-normal distribution
sample_b = stats.lognorm.rvs(s=0.5, loc=0.0, scale=1.0, size=(1000,))


# ## Boxplot-Whisker Plot and Histogram
#
# We can visually check if a distribution looks normally distributed.  Recall that a box whisker plot lets us check for symmetry around the mean.  A histogram lets us see the overall shape.  A QQ-plot lets us compare our data distribution with a normal distribution (or any other theoretical "ideal" distribution).

# In[ ]:


# Sample A: Normal distribution
sample_a = stats.norm.rvs(loc=0.0, scale=1.0, size=(1000,))
fig, axes = plt.subplots(2, 1, figsize=(16, 9), sharex=True)
axes[0].boxplot(sample_a, vert=False)
axes[1].hist(sample_a, bins=50)
axes[0].set_title("Boxplot of a Normal Distribution")


# In[ ]:


# Sample B: Non-normal distribution
sample_b = stats.lognorm.rvs(s=0.5, loc=0.0, scale=1.0, size=(1000,))
fig, axes = plt.subplots(2, 1, figsize=(16, 9), sharex=True)
axes[0].boxplot(sample_b, vert=False)
axes[1].hist(sample_b, bins=50)
axes[0].set_title("Boxplot of a Lognormal Distribution")


# In[ ]:


# Q-Q plot of normally-distributed sample
plt.figure(figsize=(10, 10))
plt.axis("equal")
stats.probplot(sample_a, dist="norm", plot=plt)


# In[ ]:


# Q-Q plot of non-normally-distributed sample
plt.figure(figsize=(10, 10))
plt.axis("equal")
stats.probplot(sample_b, dist="norm", plot=plt)


# ## Testing for Normality
# ### Shapiro-Wilk
#
# The Shapiro-Wilk test is available in the scipy library.  The null hypothesis assumes that the data distribution is normal.  If the p-value is greater than the chosen p-value, we'll assume that it's normal. Otherwise we assume that it's not normal.
# https://docs.scipy.org/doc/scipy-0.19.0/reference/generated/scipy.stats.shapiro.html

# In[ ]:


def is_normal(sample, test=stats.shapiro, p_level=0.05, **kwargs):
    """Apply a normality test to check if sample is normally distributed."""
    t_stat, p_value = test(sample, **kwargs)
    print("Test statistic: {}, p-value: {}".format(t_stat, p_value))
    print("Is the distribution Likely Normal? {}".format(p_value > p_level))
    return p_value > p_level


# Using Shapiro-Wilk test (default)
print("Sample A:-")
is_normal(sample_a)
print("Sample B:-")
is_normal(sample_b)


#

# ## Kolmogorov-Smirnov
#
# The Kolmogorov-Smirnov is available in the scipy.stats library.  The K-S test compares the data distribution with a theoretical distribution.  We'll choose the 'norm' (normal) distribution as the theoretical distribution, and we also need to specify the mean and standard deviation of this theoretical distribution.  We'll set the mean and stanadard deviation of the theoretical norm with the mean and standard deviation of the data distribution.
#
# https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.kstest.html

# # Quiz
#
# To use the Kolmogorov-Smirnov test, complete the function `is_normal_ks`.
#
# To set the variable normal_args, create a tuple with two values.  An example of a tuple is `("apple","banana")`
# The first is the mean of the sample. The second is the standard deviation of the sample.
#
# **hint:** Hint: Numpy has functions np.mean() and np.std()

# In[ ]:


def is_normal_ks(sample, test=stats.kstest, p_level=0.05, **kwargs):
    """
    sample: a sample distribution
    test: a function that tests for normality
    p_level: if the test returns a p-value > than p_level, assume normality

    return: True if distribution is normal, False otherwise
    """
    normal_args = (np.mean(sample), np.std(sample))

    t_stat, p_value = test(sample, "norm", normal_args, **kwargs)
    print("Test statistic: {}, p-value: {}".format(t_stat, p_value))
    print("Is the distribution Likely Normal? {}".format(p_value > p_level))
    return p_value > p_level


test_normality_quiz_tests.test_is_normal_ks(is_normal_ks)


# In[ ]:


# Using Kolmogorov-Smirnov test
print("Sample A:-")
is_normal_ks(sample_a)
print("Sample B:-")
is_normal_ks(sample_b)
