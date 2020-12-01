load("@rules_python//python:defs.bzl", "py_binary")
load("@ai_for_trading_deps//:requirements.bzl", "requirement")

py_binary(
    name = "pairs_candidates",
    srcs = [
        "pairs_candidates.py",
        "quiz_tests.py",
        "tests.py",
    ],
    deps = [
        requirement("numpy"),
        requirement("pandas"),
        requirement("statsmodels"),
        requirement("scikit-learn"),
        requirement("matplotlib"),
    ],
)
