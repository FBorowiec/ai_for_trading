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
