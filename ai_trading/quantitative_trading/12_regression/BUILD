load("@rules_python//python:defs.bzl", "py_binary")
load("@ai_for_trading_deps//:requirements.bzl", "requirement")

py_binary(
    name = "visualize_distributions",
    srcs = [
        "visualize_distributions.py",
    ],
    main = "visualize_distributions.py",
    deps = [
        requirement("matplotlib"),
        requirement("pandas"),
    ],
)

py_binary(
    name = "test_normality",
    srcs = [
        "quiz_tests.py",
        "test_normality.py",
        "tests.py",
    ],
    main = "test_normality.py",
    deps = [
        requirement("matplotlib"),
        requirement("numpy"),
        requirement("pandas"),
        requirement("scipy"),
    ],
)
