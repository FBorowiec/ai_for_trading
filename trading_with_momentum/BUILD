load("@rules_python//python:defs.bzl", "py_binary")
load("@ai_for_trading_deps//:requirements.bzl", "requirement")

py_binary(
    name = "trading_with_momentum",
    srcs = [
        "helper.py",
        "project_1_starter.py",
        "project_helper.py",
        "project_tests.py",
        "tests.py",
    ],
    data = [
        "eod-quotemedia.csv",
    ],
    main = "project_1_starter.py",
    deps = [
        requirement("pandas"),
        requirement("plotly"),
        requirement("numpy"),
        requirement("tqdm"),
    ],
)
