# Pytest Revision Guide

A focused review of the pytest concepts practiced in this repository.

## 1. Test discovery

By default, pytest discovers files named `test_*.py` or `*_test.py`.

- Test functions and methods start with `test_`.
- Test classes start with `Test` and should not define an `__init__` method.
- Check the folder you run pytest from and `testpaths` in `pytest.ini` if no tests are collected.

## 2. Assertions and results

Use `assert` to compare an actual result with what you expect. If the condition is true, the test passes. If false, pytest reports the failing line and shows the compared values.

```python
def test_error_message():
    actual = "Invalid password"
    expected = "Invalid password"

    assert actual == expected
```

## 3. Run and select tests

Run commands from the project folder with its virtual environment active.

```bash
python -m pytest                              # Run discovered tests
python -m pytest -v                           # Show test names and outcomes
python -m pytest -q                           # Keep output brief
python -m pytest tests/test_messages.py       # Run one file
python -m pytest tests/test_messages.py::test_error_message -v
python -m pytest -k message -v                # Select by name/keyword
python -m pytest -m smoke -v                  # Select by marker
python -m pytest --collect-only               # List tests without running them
python -m pytest --lf -v                     # Rerun tests that failed last time
python -m pytest -x                           # Stop at the first failure
python -m pytest --tb=short                   # Show a concise traceback
```

`python -m pytest` runs pytest using the active Python interpreter. `-k` matches names and related keywords; `-m` selects tests by marker.

## 4. Test classes

A class groups related tests. Pytest discovers class methods that start with `test_` in a class named `Test...`.

```python
class TestLoginMessages:
    def test_error_message(self):
        assert "Invalid password" == "Invalid password"
```

Use `self` for test methods inside a class. Plain test functions outside a class do not need `self`.

## 5. Fixtures

A fixture provides a value or resource that a test needs. Pytest matches the fixture name to a test parameter and supplies it automatically.

```python
import pytest


@pytest.fixture
def expected_message():
    return "Invalid password"


def test_message(expected_message):
    assert expected_message == "Invalid password"
```

A fixture can use `yield` to separate setup from cleanup:

```python
@pytest.fixture
def resource():
    item = create_resource()
    yield item
    clean_up(item)
```

Setup runs before the test uses the fixture. Cleanup runs after the test, including when its assertion fails.

### Fixture scope

- `function` is the default: pytest creates and cleans up a fixture for each test that requests it.
- `class` keeps one fixture instance for tests in a class.
- `module` keeps one fixture instance for tests in one file.
- `session` keeps one fixture instance for the test session.

Choose a scope based on how long the resource should be shared. Function scope gives tests the most isolation.

### `conftest.py`

Put fixtures shared by multiple test files in `conftest.py`. Tests in that folder and its subfolders can request those fixtures by name; they do not import `conftest`.

## 6. Parametrize test data

Use `@pytest.mark.parametrize` to call the same test with multiple data sets. Import pytest first with `import pytest`.

For one argument, give a list of values:

```python
@pytest.mark.parametrize("status", ["PASS", "FAIL"])
def test_status_is_known(status):
    assert status in ["PASS", "FAIL"]
```

For multiple arguments, provide one tuple of values per case, in the same order as the argument names:

```python
@pytest.mark.parametrize(
    ("actual", "expected"),
    [
        ("Invalid password", "Invalid password"),
        ("Please check your password", "Please check your password"),
    ],
)
def test_message(actual, expected):
    assert actual == expected
```

Each row creates a separate test case. A fixture and parametrized values can be requested by the same test.

## 7. Configuration and markers

`pytest.ini` is optional. It stores pytest settings for the project. Paths such as `testpaths` are relative to the directory containing the configuration file.

```ini
[pytest]
testpaths = tests
addopts = -v
markers =
    smoke: quick checks of key functionality
    regression: broader checks of existing functionality
```

A marker labels a test so it can be selected as a group:

```python
@pytest.mark.smoke
def test_important_check():
    assert True
```

Run that group with `python -m pytest -m smoke -v`. Register custom marker names in `pytest.ini` to document them and avoid unknown-marker warnings.

## 8. Skip and expected failures

- **skip**: pytest does not run the test because it does not apply or a requirement is unavailable.
- **xfail**: pytest runs the test, but a failure is expected, often because of a known issue.
- **xpass**: an `xfail` test unexpectedly passes. Review the mark because the issue may have been fixed.

## 9. Failure reports and XML output

The terminal summary reports passed, failed, skipped, xfailed, and xpassed tests. Use `--tb=short` for a compact traceback; pytest still shows the test name, failing line, and useful assertion details.

Create a JUnit XML report for CI tools with:

```bash
python -m pytest --junitxml=test-results.xml
```

In the XML report, an expected failure is represented as a skipped case with type `pytest.xfail`. An unexpected pass appears as a passing case. Generated reports are ignored by Git in this repository.

## 10. Common troubleshooting clues

- **No tests collected:** check filenames, function names, current folder, and `testpaths`. Use `--collect-only` to inspect discovery.
- **Fixture not found:** check the fixture spelling and whether its `conftest.py` is in the test folder’s parent path.
- **Need to focus on a recent failure:** use `--lf`; use `-x` to stop at the first failing test.
- **A long failure traceback is hard to scan:** use `--tb=short`.
