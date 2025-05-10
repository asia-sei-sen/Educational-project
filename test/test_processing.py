import pytest

from src.processing import (
    sort_by_date,
)


@pytest.fixture
def transaction_set():
    return [
        {"date": "2023-08-20T12:00:00", "amount": 100},
        {"date": "2022-05-15T08:30:00", "amount": 200},
        {"date": "2023-01-10T16:45:00", "amount": 300},
        {"date": "invalid_date", "amount": 400},
        {"date": None, "amount": 500}
    ]


@pytest.fixture
def edge_cases():
    return [
        [],
        [{"date": "2023-01-01T00:00:00"}],
        [{"amount": 100}],
        [{"date": None}]
    ]


@pytest.mark.parametrize("reverse, expected", [
    (True, ["2023-08-20", "2023-01-10", "2022-05-15"]),
    (False, ["2022-05-15", "2023-01-10", "2023-08-20"])
])
def test_sort_by_date_parametrized(transaction_set, reverse, expected):
    result = sort_by_date([t for t in transaction_set if t["date"] not in ("invalid_date", None)], reverse)
    assert [r["date"][:10] for r in result] == expected


def test_sort_with_fixtures(transaction_set, edge_cases):
    # Тест с некорректными датами
    result = sort_by_date(transaction_set)
    assert all(t["date"] in ("invalid_date", None) for t in result[-2:])  # последние элементы должны быть некорректными

    # Тест крайних случаев
    for case in edge_cases:
        if case and "date" in case[0]:
            assert sort_by_date(case) == case
        else:
            assert sort_by_date(case) == []


def test_sort_empty_list():
    assert sort_by_date([]) == []


def test_sort_with_only_invalid_dates():
    invalid_transactions = [
        {"date": "invalid_date"},
        {"date": None}
    ]
    assert sort_by_date(invalid_transactions) == invalid_transactions