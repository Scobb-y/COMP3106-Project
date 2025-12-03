from pathlib import Path
import json
from src.dataset import main as build_dataset

def test_dataset(tmp_path: Path):
    out = tmp_path / "data"
    build_dataset.callback(out=out, count=10)
    data = json.loads((out / "errors.json").read_text())
    assert len(data) == 10
    assert "text" in data[0] and "label" in data[0]
