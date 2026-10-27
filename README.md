# Pytest Learning Path

A hands-on repository for learning pytest from the fundamentals through fixtures, parametrization, markers, test selection, failure handling, and reporting. Selenium provides a browser-automation practice area, with API testing planned as the next learning track.

## Learning folders

- `pracrtise_pytest/` — first assertions, test classes, and fixture injection.
- `pytest_fixture/` — fixture reuse through `conftest.py`, setup and cleanup with `yield`, and parametrized tests.
- `using_fixture/` — simple and nested fixtures, plus a file-resource teardown example.
- `run_test_and_debug/` — test selection, failures, and skip/xfail examples.
- `document-editor_pytest_mark/` — tests for a small class, markers, and exception checks.
- `hands-on/` — tests for order-processing rules, including discounts, stock, and invalid orders.
- `selenium_tests/` — a browser fixture, form interactions, explicit waits, a first Page Object, markers, and pytest reports.

See [LEARNING_ROADMAP.md](LEARNING_ROADMAP.md) for the progress and next steps.

## Set up the environment

From this repository folder, create and activate a virtual environment, then install the project dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## Run the examples

The learning folders are independent practice areas. Run pytest from the relevant folder so its local configuration and imports are used. For example:

```bash
cd pytest_fixture
python -m pytest -v
```

For the Selenium examples, run from `selenium_tests/`:

```bash
cd selenium_tests
python -m pytest
```

The Selenium exercises use Chrome and the Selenium practice form at `https://www.selenium.dev/selenium/web/web-form.html`.

To create a JUnit XML report from the Selenium tests:

```bash
python -m pytest --junitxml=test-results.xml
```

Some files intentionally demonstrate skipped, expected-failure, or command-line practice cases. Those outcomes are part of the lessons and may appear in the report.
