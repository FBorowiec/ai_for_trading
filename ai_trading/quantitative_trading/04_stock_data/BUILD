load("@rules_python//python:defs.bzl", "py_binary")
load("@ai_for_trading_deps//:requirements.bzl", "requirement")

py_binary(
    name = "stock_data",
    srcs = [
        "stock_data.py",
    ],
    data = [
        "prices.csv",
        "prices_2017_09_22_2017-09-28.csv",
    ],
    imports = ["*"],
    deps = [
        requirement("pandas"),
        requirement("numpy"),
    ],
)

py_binary(
    name = "unit_tests",
    srcs = [
        "quiz_tests.py",
        "tests.py",
    ],
    main = "quiz_tests.py",
)
