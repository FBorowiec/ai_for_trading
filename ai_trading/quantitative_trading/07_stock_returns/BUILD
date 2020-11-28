load("@rules_python//python:defs.bzl", "py_binary")
load("@ai_for_trading_deps//:requirements.bzl", "requirement")

py_binary(
    name = "calculate_returns",
    srcs = [
        "calculate_returns.py",
        "quiz_tests.py",
        "tests.py",
    ],
    deps = [
        requirement("pandas"),
        requirement("numpy"),
    ],
)
