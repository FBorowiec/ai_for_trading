"""
Let’s say we want to construct a portfolio containing 2 stocks, Stock 1 and Stock 2.

Stock 1: Expected return=15%, Volatility=10%

Stock 2: Expected return=10%, Volatility=5%

Correlation between Stock A and B = 0.25

What weights on Stocks 1 and 2, x1​ and x2, will give the minimum variance portfolio?
"""

import numpy as np

# Expected returns
a_return = 0.15
b_return = 0.1

# Volatility
a_volatility = 0.1
b_volatility = 0.05

# Correlation between stocks
rho_ab = 0.25

# Portfolio variance
rho_p_squared = (
    np.power(a_return, 2) * np.power(a_volatility, 2)
    + np.power(b_return, 2) * np.power(b_volatility, 2)
    + 2 * a_return * b_return * a_volatility * b_volatility * rho_ab
)

# Weights for each stock for maximum portfolio variance
x_a = (np.power(b_volatility, 2) - a_volatility * b_volatility * rho_ab) / (
    np.power(a_volatility, 2)
    + np.power(b_volatility, 2)
    - 2 * a_volatility * b_volatility * rho_ab
)
x_b = 1 - x_a


print("Weight on stock A: {}\nWeight on stock B: {}".format(x_a, x_b))
