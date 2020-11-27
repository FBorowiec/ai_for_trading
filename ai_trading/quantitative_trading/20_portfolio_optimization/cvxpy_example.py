import cvxpy as cvx
import numpy as np

x = cvx.Variable(1)
objective = cvx.Minimize((x - 1) ** 2 + 1)
constraints = [x <= 0]
problem = cvx.Problem(objective, constraints)
result = problem.solve()
print("Optimal value of x: {:.2f}".format(x.value[0]))
print("Optimal value of the objective: {:.2f}".format(problem.value))
