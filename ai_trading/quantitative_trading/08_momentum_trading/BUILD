load("@rules_python//python:defs.bzl", "py_binary")
load("@ai_for_trading_deps//:requirements.bzl", "requirement")

py_binary(
    name = "data_types",
    main = "dtype.py",
    srcs = [
        "dtype.py",
        "dtype_project_tests.py",
        "dtype_tests.py",
    ],
    deps = [
        requirement("numpy"),
        requirement("pandas"),
    ],
)

py_binary(
    name = "top_and_bottom_performing",
    main = "top_and_bottom_performing.py",
    srcs = [
        "top_and_bottom_performing.py",
        "top_and_bottom_performing_project_tests.py",
        "top_and_bottom_performing_tests.py",
    ],
    deps = [
        requirement("numpy"),
        requirement("pandas"),
    ],
)
