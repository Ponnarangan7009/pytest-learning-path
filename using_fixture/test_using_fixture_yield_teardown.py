import pytest

@pytest.fixture
def handle_files_content(tmp_path):
    path = tmp_path / "sample_text.txt"
    path.write_text("this is the sample line\n", encoding="utf-8")
    yield path
    path.unlink()

def test_read_content(handle_files_content):
    with open(handle_files_content, "r", encoding="utf-8") as file:
        file_content = file.read()
    assert file_content == "this is the sample line\n"

def test_write_content(handle_files_content):
    with open(handle_files_content, "a", encoding="utf-8") as file:
        file.write("this is second line")
    with open(handle_files_content, "r", encoding="utf-8") as file:
        file_content = file.read()
    assert file_content == "this is the sample line\nthis is second line"
