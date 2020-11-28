load("@rules_python//python:defs.bzl", "py_binary")
load("@ai_for_trading_deps//:requirements.bzl", "requirement")

py_binary(
    name = "stock_data",
    srcs = [
        "quiz_tests.py",
        "stock_data.py",
        "tests.py",
    ],
    data = [
        "prices.csv",
        "prices_2017_09_22_2017-09-28.csv",
    ],
    deps = [
        requirement("pandas"),
        requirement("numpy"),
    ],
)
