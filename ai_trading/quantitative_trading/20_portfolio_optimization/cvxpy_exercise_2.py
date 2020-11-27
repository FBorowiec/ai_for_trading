import cvxpy as cvx
import numpy as np


def optimize_portfolio(returns, index_weights, scale=0.00001):
    """
    Create a function that takes the return series of a set of stocks, the index weights,
    and scaling factor. The function will minimize a combination of the portfolio variance
    and the distance of its weights from the index weights.
    The optimization will be constrained to be long only, and the weights should sum to one.

    Parameters
    ----------
    returns : numpy.ndarray
        2D array containing stock return series in each row.

    index_weights : numpy.ndarray
        1D numpy array containing weights of the index.

    scale : float
        The scaling factor applied to the distance between portfolio and index weights

    Returns
    -------
    x : np.ndarray
        A numpy ndarray containing the weights of the stocks in the optimized portfolio
    """
    # TODO: Use cvxpy to determine the weights on the assets
    # that minimizes the combination of portfolio variance and distance from index weights

    # number of stocks m is number of rows of returns, and also number of index weights
    m = len(index_weights)

    # covariance matrix of returns
    cov = np.cov(returns)

    # x variables (to be found with optimization)
    x = cvx.Variable(m)

    # portfolio variance, in quadratic form
    portfolio_variance = cvx.quad_form(x, cov)

    # euclidean distance (L2 norm) between portfolio and index weights
    distance_to_index = cvx.norm(x - index_weights)

    # objective function
    objective = cvx.Minimize(portfolio_variance + scale * distance_to_index)

    # constraints
    constraints = [x >= 0, sum(x) == 1]

    # use cvxpy to solve the objective
    problem = cvx.Problem(objective, constraints)
    x_min = problem.solve()

    # retrieve the weights of the optimized portfolio
    x_values = x.value

    return x_values


def main():
    """Test with a 3 simulated stock return series"""
    days_per_year = 252
    years = 3
    total_days = days_per_year * years

    return_market = np.random.normal(loc=0.05, scale=0.3, size=days_per_year)
    return_1 = (
        np.random.uniform(low=-0.000001, high=0.000001, size=days_per_year)
        + return_market
    )
    return_2 = (
        np.random.uniform(low=-0.000001, high=0.000001, size=days_per_year)
        + return_market
    )
    return_3 = (
        np.random.uniform(low=-0.000001, high=0.000001, size=days_per_year)
        + return_market
    )
    returns = np.array([return_1, return_2, return_3])

    """simulate index weights"""
    index_weights = np.array([0.9, 0.15, 0.05])

    """try out your optimization function"""
    x_values = optimize_portfolio(returns, index_weights, scale=0.00001)
    print("The optimized weights are: ", x_values)
    print("The sum of the weights is: ", sum(x_values))


if __name__ == "__main__":
    # execute only if run as a script
    main()
