load("@rules_python//python:defs.bzl", "py_binary")
load("@ai_for_trading_deps//:requirements.bzl", "requirement")

py_binary(
    name = "breakout_strategy",
    srcs = [
        "breakout_strategy.py",
        "helper.py",
        "project_helper.py",
    ],
    main = "main.py",
    deps = [
        requirement("pandas"),
        requirement("numpy"),
    ],
)

py_binary(
    name = "unit_tests",
    srcs = [
        "project_tests.py",
        "tests.py",
    ],
    main = "project_tests.py",
)
