load("@rules_python//python:defs.bzl", "py_binary")
load("@ai_for_trading_deps//:requirements.bzl", "requirement")

py_binary(
    name = "autoregression",
    srcs = [
        "autoregression.py",
        "helper.py",
        "quiz_tests.py",
        "tests.py",
    ],
    main = "autoregression.py",
    deps = [
        requirement("matplotlib"),
        requirement("numpy"),
        requirement("pandas"),
        requirement("seaborn"),
        requirement("statsmodels"),
    ],
)
