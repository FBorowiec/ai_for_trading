import numpy as np

"""
What is the return and the beta of a 3 stock portfolio with the following information:
rf=2%
rm=10%
βA=1.2, βB=1.8, βC=0.5
wA=0.4, wB=0.4, wC=0.2
"""

beta = [1.2, 1.8, 0.5]
w = [0.4, 0.4, 0.2]
rf = 0.02
rm = 0.1

portfolio_beta = np.sum(np.array(beta) * np.array(w))
portfolio_return = np.sum(np.array(w) * (rf + np.array(beta) * (rm - rf)))

print(
    "Porfolio Beta: {beta}\nPortfolio return: {returns}".format(
        beta=portfolio_beta, returns=portfolio_return
    )
)
