load("@rules_python//python:defs.bzl", "py_binary")
load("@ai_for_trading_deps//:requirements.bzl", "requirement")

py_binary(
    name = "zipline_pipeline",
    srcs = [
        "zipline_pipeline.py",
    ],
    main = "zipline_pipeline.py",
    deps = [
        requirement("pandas"),
        requirement("graphviz"),
        requirement("zipline"),
    ],
)
