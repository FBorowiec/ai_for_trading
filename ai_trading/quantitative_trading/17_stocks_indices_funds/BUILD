load("@rules_python//python:defs.bzl", "py_binary")
load("@ai_for_trading_deps//:requirements.bzl", "requirement")

py_binary(
    name = "cumsum_and_cumprod",
    srcs = [
        "cumsum_and_cumprod.py",
        "quiz_tests.py",
        "tests.py",
    ],
    deps = [
        requirement("numpy"),
        requirement("pandas"),
        requirement("matplotlib"),
    ],
)
