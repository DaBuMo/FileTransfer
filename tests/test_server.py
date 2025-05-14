# @pytest.fixture(scope="module")
import pytest


def test_smallbinaryfile(tmp_path):
    directory = tmp_path / "client_storage"
    directory.mkdir()

    file = directory / "xs.bin"
    file.write_text("HELLO WORLD", encoding="utf-8")

    assert file.read_text(encoding="utf-8") == "HELLO WORLD"
    assert len(list(tmp_path.iterdir())) == 1
