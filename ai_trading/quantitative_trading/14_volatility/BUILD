load("@rules_python//python:defs.bzl", "py_binary")
load("@ai_for_trading_deps//:requirements.bzl", "requirement")

py_binary(
    name = "volatility",
    srcs = ["volatility.py"],
    data = ["prices.csv"],
    deps = [
        requirement("numpy"),
        requirement("pandas"),
    ],
)

py_binary(
    name = "rolling_windows",
    srcs = [
        "quiz_tests.py",
        "rolling_windows.py",
        "tests.py",
    ],
    deps = [
        requirement("numpy"),
        requirement("pandas"),
    ],
)

py_binary(
    name = "estimate_volatility",
    srcs = ["estimate_volatility.py"],
    data = ["data.csv"],
    deps = [
        requirement("numpy"),
        requirement("pandas"),
    ],
)
