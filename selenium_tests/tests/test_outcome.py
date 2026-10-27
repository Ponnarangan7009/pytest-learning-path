import pytest


@pytest.mark.skip(reason="Practice: learning how skipped tests are reported")
def test_skip_example():
    assert 1 == 2

@pytest.mark.xfail(reason="Practice: this failure is expected")
def test_expected_failure_example():
    assert 1 == 2

@pytest.mark.xfail(reason="Practice: this pass is expected")
def test_expected_failure_example_passed_scenario():
    assert 1 == 1