# AI for trading

This is the repository where I store the programs and projects I've done for the Udacity AI for trading nanodegree. The repository is focusing primarily on two aspects of trading:

- Quantitative trading
- AI algorithms in trading

## Quantitative analysis

Quantitative analysis is a research strategy that focuses on quantifying the collection and analysis of data including data processing, trading signal generation, and portfolio management. Using Python to work with historical stock data, develop trading strategies, and construct a multi-factor model with optimization.

Projects:

1. Trading with Momentum
2. Breakout Strategy
3. Portfolio Optimization
4. Alpha Research and Factor Modelling

## AI algorithms in trading

Analyzing alternative data and use machine learning to generate trading signals. Running a backtest to evaluate and combine top performing signals.

Projects:

1. Natural Language Processing on Financial Statements
2. Sentiment Analysis with Neural Networks
3. Combining Signals for enhanced Alpha
4. Backtesting

## How to run the code locally with *Bazel* already installed on host

You can use `jupyter-notebook` to check the ipython notebooks (`*.ipynb`) containing the projects.

For the project exercises I recommend either installing the *Bazel* build system or using my Docker image.

### Bazel installation

[Install Bazel](https://docs.bazel.build/versions/master/install.html)

Once you have successfully installed *Bazel* you can run the code using:

```bash
bazel run //ai_trading/quantitative_trading/04_stock_data:stock_data
```

## Run the code inside a container

You can use my following Docker image to instantiate a container locally with Ubuntu and Bazel already installed:

```bash
docker run -it --rm framaxwlad/ubuntu_dev:latest
```

There you can simply clone the repository:

```bash
git clone https://github.com/FBorowiec/ai_for_trading.git
cd ai_for_trading/
```

And use the aforementioned commands to run the program:

```bash
bazel run //ai_trading/quantitative_trading/04_stock_data:stock_data
```
