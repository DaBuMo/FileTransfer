from pathlib import Path
import pytest
from src.lib.download import Download
from src.lib.constants import DEFAULT_PORT, LOCALHOST

@pytest.fixture
def storages(tmp_path) -> list[Path]:
  client_storage = tmp_path / "client_storage"
  client_storage.mkdir()

  server_storage = tmp_path / "server_storage"
  server_storage.mkdir()

  xs_file = server_storage / "xs.bin"
  xs_file.write_text("HELLO WORLD", encoding="utf-8")

  return [client_storage, server_storage]

  
def test_download_xs(storages):
  client = Download.Download(LOCALHOST, DEFAULT_PORT)
  client.start("xs.bin")

  client_storage = storages[0]

  downloaded_file = client_storage / "xs.bin"

  assert downloaded_file.exists(follow_symlinks=False)
  assert downloaded_file.read_text(encoding="utf-8") == "HELLO WORLD"