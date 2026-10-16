import pytest

from app import calculate, get_password


@pytest.mark.parametrize(
    "a,b,operation,expected",
    [
        (2, 3, "add", 5),
        (5, 2, "subtract", 3),
        (4, 3, "multiply", 12),
        (10, 4, "divide", 2.5),
        (-2, 3, "add", 1),
        (0, 5, "multiply", 0),
    ],
)
def test_calculate(a, b, operation, expected):
    assert calculate(a, b, operation) == expected


def test_division_by_zero():
    with pytest.raises(ValueError, match="Division par zéro"):
        calculate(10, 0, "divide")


@pytest.mark.parametrize("operation", ["power", "__import__('os')", ""])
def test_unknown_operation(operation):
    with pytest.raises(ValueError, match="Opération non autorisée"):
        calculate(1, 2, operation)


def test_password_from_environment(monkeypatch):
    monkeypatch.setenv("APP_PASSWORD", "valeur-fictive-pour-le-tp")
    assert get_password() == "valeur-fictive-pour-le-tp"


@pytest.mark.parametrize("value", [None, ""])
def test_missing_password(monkeypatch, value):
    if value is None:
        monkeypatch.delenv("APP_PASSWORD", raising=False)
    else:
        monkeypatch.setenv("APP_PASSWORD", value)
    with pytest.raises(RuntimeError, match="APP_PASSWORD n'est pas configuré"):
        get_password()
