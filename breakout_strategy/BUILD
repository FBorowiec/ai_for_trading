load("@rules_python//python:defs.bzl", "py_binary")
load("@ai_for_trading_deps//:requirements.bzl", "requirement")

py_binary(
    name = "breakout_strategy",
    srcs = [
        "helper.py",
        "project_2_starter.py",
        "project_helper.py",
        "project_tests.py",
        "tests.py",
    ],
    data = ["eod-quotemedia.csv"],
    main = "project_2_starter.py",
    deps = [
        requirement("colour"),
        requirement("pandas"),
        requirement("numpy"),
        requirement("scipy"),
        requirement("plotly"),
    ],
)
