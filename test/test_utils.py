import pytest
import json
from unittest.mock import mock_open, patch
from src.utils import load_json_file  # ← исправлен импорт


def test_load_json_file_valid_json():
    mock_data = json.dumps([
        {"id": 1, "amount": 100, "currency": "USD"},
        {"id": 2, "amount": 200, "currency": "RUB"}
    ])

    with patch("builtins.open", mock_open(read_data=mock_data)), \
         patch("os.path.exists", return_value=True):
        result = load_json_file("fake_path.json")  # ← исправлено имя функции

    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["amount"] == 100


def test_load_json_file_file_not_found():
    with patch("os.path.exists", return_value=False):
        result = load_json_file("nonexistent.json")  # ← исправлено
    assert result == []


def test_load_json_file_invalid_json():
    with patch("builtins.open", mock_open(read_data="invalid json")), \
         patch("os.path.exists", return_value=True):
        result = load_json_file("invalid.json")  # ← исправлено
    assert result == []


def test_load_json_file_not_a_list():
    mock_data = json.dumps({"id": 1, "amount": 100})
    with patch("builtins.open", mock_open(read_data=mock_data)), \
         patch("os.path.exists", return_value=True):
        result = load_json_file("notalist.json")  # ← исправлено
    assert result == []
