# src/BUILD
load("@rules_python//python:py_library.bzl", "py_library")

# This py_library defines the 'ui_pages' Python package.
# Its srcs are relative to src/ (where this BUILD file is)
py_library(
    name = "ui_pages",
    srcs = [
        "ui_pages/__init__.py",    # The __init__.py for the ui_pages package
        "ui_pages/home_page.py",   # Your home_page module
        # Add any other .py files directly under src/ui_pages/
    ],
    visibility = ["//visibility:public"],
    # Add any external (pip) or internal (other //src/...) dependencies specific to ui_pages
    # e.g., if home_page.py imports from playwright:
    # deps = ["@pip//playwright"],
)

# This py_library defines the top-level 'src' Python package.
# It typically includes its own __init__.py and depends on its sub-packages.
py_library(
    name = "src",
    srcs = ["__init__.py"], # The __init__.py for the src package
    # If there are other .py files directly under src/ (e.g., src/utils.py), list them here:
    # srcs = ["__init__.py", "utils.py"],
    visibility = ["//visibility:public"],
    deps = [
        ":ui_pages", # The src package depends on the ui_pages sub-package
    ],
)