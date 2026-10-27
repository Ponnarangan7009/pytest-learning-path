def test_failure_message():
    actual = "Welcome!"
    expected = "Welcome!"

    assert actual == expected

# python -m pytest tests/test_traceback_example.py --tb=short