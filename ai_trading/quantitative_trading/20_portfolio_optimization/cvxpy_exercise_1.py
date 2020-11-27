import numpy as np
import cvxpy as cvx


def optimize_twoasset_portfolio(varA, varB, rAB):
    """Create a function that takes in the variance of Stock A, the variance of
    Stock B, and the correlation between Stocks A and B as arguments and returns
    the vector of optimal weights

    Parameters
    ----------
    varA : float
        The variance of Stock A.

    varB : float
        The variance of Stock B.

    rAB : float
        The correlation between Stocks A and B.

    Returns
    -------
    x : np.ndarray
        A 2-element numpy ndarray containing the weights on Stocks A and B,
        [x_A, x_B], that minimize the portfolio variance.

    """
    # TODO: Use cvxpy to determine the weights on the assets in a 2-asset
    # portfolio that minimize portfolio variance.

    cov = varA * varB * rAB
    x = cvx.Variable(2)
    P = np.array(
        [
            [varA, np.sqrt(varA) * np.sqrt(varB) * rAB],
            [np.sqrt(varA) * np.sqrt(varB) * rAB, varB],
        ]
    )
    portfolio_variance = cvx.quad_form(x, P)
    objective = cvx.Minimize(portfolio_variance)
    constraints = [sum(x) == 1]
    problem = cvx.Problem(objective, constraints)
    result = problem.solve()
    min_value = x.value[0]
    xA, xB = min_value, 1 - min_value

    return xA, xB


def main():
    varA, varB, rAB = 0.1, 0.2, 0.25
    xA, xB = optimize_twoasset_portfolio(varA, varB, rAB)
    print("xA = {:.3f}, xB = {:.3f}".format(xA, xB))


if __name__ == "__main__":
    # execute only if run as a script
    main()
