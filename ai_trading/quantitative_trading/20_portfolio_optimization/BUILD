load("@rules_python//python:defs.bzl", "py_binary")
load("@ai_for_trading_deps//:requirements.bzl", "requirement")

py_binary(
    name = "portfolio_optimization_with_two_stocks",
    srcs = [
        "portfolio_optimization_with_two_stocks.py",
    ],
    main = "portfolio_optimization_with_two_stocks.py",
    deps = [
        requirement("numpy"),
    ],
)

py_binary(
    name = "cvxpy_example",
    srcs = [
        "cvxpy_example.py",
    ],
    main = "cvxpy_example.py",
    deps = [
        requirement("cvxpy"),
        requirement("numpy"),
    ],
)

py_binary(
    name = "cvxpy_basic",
    srcs = [
        "cvxpy_basic.py",
        "quiz_tests.py",
        "tests.py",
    ],
    main = "cvxpy_basic.py",
    deps = [
        requirement("cvxpy"),
        requirement("numpy"),
        requirement("pandas"),
    ],
)

py_binary(
    name = "cvxpy_advanced",
    srcs = [
        "cvxpy_advanced.py",
        "quiz_tests.py",
        "tests.py",
    ],
    main = "cvxpy_advanced.py",
    deps = [
        requirement("cvxpy"),
        requirement("numpy"),
        requirement("pandas"),
    ],
)

py_binary(
    name = "cvxpy_exercise_1",
    srcs = [
        "cvxpy_exercise_1.py",
    ],
    main = "cvxpy_exercise_1.py",
    deps = [
        requirement("cvxpy"),
        requirement("numpy"),
    ],
)

py_binary(
    name = "cvxpy_exercise_2",
    srcs = [
        "cvxpy_exercise_2.py",
    ],
    main = "cvxpy_exercise_2.py",
    deps = [
        requirement("cvxpy"),
        requirement("numpy"),
    ],
)
