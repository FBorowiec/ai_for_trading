load("@rules_python//python:defs.bzl", "py_binary")
load("@ai_for_trading_deps//:requirements.bzl", "requirement")

py_binary(
    name = "covariance_matrix",
    srcs = [
        "covariance_matrix.py",
        "covariance_matrix_quiz_tests.py",
        "covariance_matrix_tests.py",
    ],
    deps = [
        requirement("numpy"),
    ],
)

py_binary(
    name = "capm",
    srcs = [
        "capm.py",
    ],
    deps = [
        requirement("numpy"),
    ],
)
