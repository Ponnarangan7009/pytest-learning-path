import pytest

@pytest.fixture
def sample_resource():
    print("Set up resource")
    yield "resource ready"
    print("Clean up resource")