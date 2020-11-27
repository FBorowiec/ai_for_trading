"""
# Project 2: Breakout Strategy
## Instructions
Each problem consists of a function to implement and instructions on how to implement the function.
The parts of the function that need to be implemented are marked with a `# TODO` comment.
After implementing the function, run the cell to test it against the unit tests we've provided.
For each problem, we provide one or more unit tests from our `project_tests` package.
These unit tests won't tell you if your answer is correct, but will warn you of any major errors.
Your code will be checked for the correct solution when you submit it to Udacity.

## Packages
When you implement the functions, you'll only need to you use the packages you've used in the classroom,
like [Pandas](https://pandas.pydata.org/) and [Numpy](http://www.numpy.org/).
These packages will be imported for you.
We recommend you don't add any import statements, otherwise the grader might not be able to run your code.

The other packages that we're importing are `helper`, `project_helper`, and `project_tests`.
These are custom packages built to help you solve the problems.
The `helper` and `project_helper` module contains utility functions and graph functions.
The `project_tests` contains the unit tests for all the problems.
"""
import pandas as pd
import numpy as np
import helper
import project_helper
import project_tests

"""
## Market Data
### Load Data
While using real data will give you hands on experience, it's doesn't cover all the topics we try to condense in one project.
We'll solve this by creating new stocks. We've create a scenario where companies mining [Terbium](https://en.wikipedia.org/wiki/Terbium) are making huge profits.
All the companies in this sector of the market are made up. They represent a sector with large growth that will be used for demonstration latter in this project.
"""
df_original = pd.read_csv(
    "../../data/project_2/eod-quotemedia.csv", parse_dates=["date"], index_col=False
)

# Add TB sector to the market
df = df_original
df = pd.concat(
    [df] + project_helper.generate_tb_sector(df[df["ticker"] == "AAPL"]["date"]),
    ignore_index=True,
)

close = df.reset_index().pivot(index="date", columns="ticker", values="adj_close")
high = df.reset_index().pivot(index="date", columns="ticker", values="adj_high")
low = df.reset_index().pivot(index="date", columns="ticker", values="adj_low")

print("Loaded Data")

"""
### View Data
To see what one of these 2-d matrices looks like, let's take a look at the closing prices matrix.
"""
print(close)
