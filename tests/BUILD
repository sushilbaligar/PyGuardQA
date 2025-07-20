# tests/BUILD
load("@rules_python//python:py_test.bzl", "py_test")

py_test(
    name = "test_home_page",
    srcs = ["UI/test_home_page.py"],
    python_version = "3.10",
    # --- Add these attributes ---
    size = "enormous", # Or "large", "medium" based on typical runtime
    timeout = "300s",  # Or more, e.g., "600s" (10 minutes) if needed for complex tests
    # ---------------------------
    deps = [
        "@pip//pytest",
        "@pip//playwright",
        "//src",
    ],
)