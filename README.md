# PyGuardQA: Comprehensive Web QA with Playwright & Bazel 🚀

## Project Overview

PyGuardQA is an automated Quality Assurance (QA) framework designed for robust web application testing. It leverages the power of **Playwright** for efficient end-to-end UI testing and **Pytest** for flexible API and unit testing. The entire test suite is orchestrated by **Bazel**, ensuring hermetic, reproducible, and fast builds.

---

## Features

* **End-to-End UI Testing:** Automates user interactions with web interfaces using Playwright.
* **API Testing:** Verifies backend service functionality and data integrity (needs implementation).
* **Unit Testing:** Supports granular testing of individual code components.
* **Bazel Build System:** Provides a highly optimized and consistent build and test environment.
* **Code Coverage Integration:** Measures test effectiveness to identify untested code paths (needs configuration).

---

## Directory Structure 📁

Understanding the project layout is crucial, especially for a Bazel-driven project.

PyGuardQA/
├── .bazelrc                   # (Recommended) Bazel configuration flags for consistent builds.
├── .gitignore                 # Specifies files and directories to be ignored by Git.
├── BUILD                      # (Review) Root-level Bazel BUILD file. Its necessity should be reviewed.
├── conftest.py                # Pytest plugin file for shared fixtures and hooks.
├── MODULE.bazel               # Defines external Bazel dependencies (e.g., rules_python).
├── MODULE.bazel.lock          # Bazel-generated lock file for module dependencies.
├── README.md                  # This project overview and guide.
├── requirements.txt           # Lists all Python package dependencies with pinned versions.
├── WORKSPACE.bak              # (To be removed) Backup of an old Bazel WORKSPACE file.
├── .pytest_cache/             # Pytest cache directory (ignored by Git).
├── fixtures/                  # Placeholder for test data or reusable test components.
├── src/                       # Contains core application logic or Page Object Models.
│   ├── BUILD                  # Bazel BUILD file defining Python libraries within 'src'.
│   ├── init.py            # Marks 'src' as a Python package.
│   ├── ui_pages/              # Contains Page Object models for UI elements.
│   │   ├── home_page.py       # Example Page Object for the Home page.
│   │   └── init.py        # Marks 'ui_pages' as a Python sub-package.
│   └── utils/                 # Placeholder for utility functions.
└── tests/                     # Houses all test cases.
├── BUILD                  # Bazel BUILD file defining test targets.
└── ui/                    # Directory for UI (End-to-End) tests.
└── test_home_page.py  # Example UI test script for the Home page.


---

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

* **Bazel:** Ensure Bazel is installed on your system.
    * [Bazel Installation Guide](https://bazel.build/install)
* **Python:** Python 3.13 (as indicated by your `venv`'s `__pycache__` files) or higher is recommended.
    * [Python Downloads](https://www.python.org/downloads/)
* **Playwright Browsers:** Install the necessary browser binaries for Playwright.
    ```bash
    playwright install
    ```

### Clone the Repository

```bash
git clone [https://github.com/your-username/PyGuardQA.git](https://github.com/your-username/PyGuardQA.git)
cd PyGuardQA
Install Dependencies
Bazel automatically manages Python dependencies defined in requirements.txt via MODULE.bazel and rules_python. You typically don't need to run pip install manually for Bazel builds.

Running Tests 🏃‍♂️
Use Bazel commands to execute the test suite.

Run All Tests
Bash

bazel test //...
Run Specific UI Test
Bash

bazel test //tests/ui:test_home_page
Running UI Tests with Browser Visibility (for debugging)
For visual debugging, you might need to launch Playwright in a non-headless mode. This typically involves setting an environment variable that your Playwright test code can read.

Example (within your Python test code):

Python

# In your test_home_page.py or a fixture, import os and sync_playwright
import os
from playwright.sync_api import sync_playwright

def my_test_function(page):
    if os.getenv("PW_HEADLESS", "1") == "0": # Default to headless, set PW_HEADLESS=0 for visible
        # Example of launching non-headless if needed, this would override a fixture
        # Usually, fixtures handle this more cleanly.
        print("Running in non-headless mode for debugging.")
        # Your Playwright setup would determine if this is effective
    # ... rest of your test steps
Then run from the command line:

Bash

PW_HEADLESS=0 bazel test //tests/ui:test_home_page
Note: Directly setting environment variables like PWDEBUG might be more geared towards Node.js Playwright. For Python, it's generally more reliable to configure this within your Python code or Bazel test environment setup.

Code Coverage (Future)
To generate code coverage reports (requires lcov installed locally for HTML reports):

Bash

bazel coverage //...
After running coverage, you can generate an HTML report using genhtml:

Bash

# Ensure 'lcov' is installed on your system for genhtml
genhtml bazel-out/_coverage/_coverage_report.dat --output-directory coverage_html
# Then open coverage_html/index.html in your browser
Contributing
We welcome contributions! Please refer to our CONTRIBUTING.md (if you create one) for guidelines on how to contribute.

License
This project is licensed under the MIT License.

Contact
For any questions or support, please open an issue in the GitHub repository.