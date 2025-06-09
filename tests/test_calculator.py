import pytest

from app.calculator import calculate_expression, calculate_operation

# --- Tests for Expression Evaluation ---


def test_simple_expression():
    assert calculate_expression("2 + 3 * 4") == 14


def test_parentheses_expression():
    assert calculate_expression("(2 + 3) * 4") == 20


def test_math_function():
    assert calculate_expression("sqrt(16)") == 4.0


def test_invalid_expression():
    with pytest.raises(ValueError):
        calculate_expression("2 + * 3")


# --- Tests for Structured Operation ---


def test_add_operation():
    assert calculate_operation(5, 3, "add") == 8.0


def test_subtract_operation():
    assert calculate_operation(10, 4, "subtract") == 6.0


def test_divide_operation():
    assert calculate_operation(9, 3, "divide") == 3.0


def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculate_operation(5, 0, "divide")


def test_unknown_operation():
    with pytest.raises(ValueError):
        calculate_operation(2, 2, "invalid")
