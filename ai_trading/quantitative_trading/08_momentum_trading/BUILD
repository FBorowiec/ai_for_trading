load("@rules_python//python:defs.bzl", "py_binary")
load("@ai_for_trading_deps//:requirements.bzl", "requirement")

py_binary(
    name = "data_types",
    srcs = [
        "dtype.py",
        "dtype_project_tests.py",
        "dtype_tests.py",
    ],
    main = "dtype.py",
    deps = [
        requirement("numpy"),
        requirement("pandas"),
    ],
)

py_binary(
    name = "top_and_bottom_performing",
    srcs = [
        "top_and_bottom_performing.py",
        "top_and_bottom_performing_project_tests.py",
        "top_and_bottom_performing_tests.py",
    ],
    main = "top_and_bottom_performing.py",
    deps = [
        requirement("numpy"),
        requirement("pandas"),
    ],
)

py_binary(
    name = "statistical_test",
    srcs = [
        "statistical_test.py",
    ],
    data = ["net_returns.csv"],
    deps = [
        requirement("numpy"),
        requirement("pandas"),
        requirement("scipy"),
    ],
)
