# Learning roadmap

## Completed foundations

- Pytest discovery, test naming, assertions, and reading pass/fail output.
- Running a file, class, or individual test; `-q` and `-v`.
- Fixtures that return values, fixture sharing through `conftest.py`, and fixture scope.
- Setup and cleanup with `yield`, including cleanup after a test fails.
- Parametrized tests with one or multiple inputs.
- Custom markers, `pytest.ini`, and selecting tests by marker.
- `skip`, `xfail`, and `xpass` outcomes.
- A Selenium browser fixture, locators, typing, clicking, explicit waits, and a basic Page Object.
- Test selection and troubleshooting with `-k`, `--collect-only`, `--lf`, `-x`, and `--tb=short`.
- Creating a JUnit XML report.

## Next: Selenium pytest mini-project

The learner will write the mini-project independently. Guidance will consist of requirements, milestones, and review of the learner's own implementation; no solution code or starter code will be supplied.

The project will practice organizing a small multi-page Selenium flow with pytest fixtures, Page Objects, useful assertions, parametrized data, and smoke/regression markers.

## After the mini-project: API testing basics

- What an API is and how a request and response work.
- HTTP methods, status codes, headers, and JSON.
- Writing API checks with Python, pytest, and an HTTP client.
- Positive and negative API cases.
- Common API testing interview questions and practice answers.
