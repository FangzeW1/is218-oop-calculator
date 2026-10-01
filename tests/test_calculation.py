from calculator.calculation import Calculation, Add, Subtract
import pytest

def test_add():
    calculation = Add(10, 5)
    result = calculation.get_result()
    assert result == 15

def test_instances_have_their_own_operands():
    first = Add(10, 5)
    second = Add(100, 50)
    first.a = 20
    assert first.get_result() == 25
    assert second.a == 100
    assert second.b == 50
    assert second.get_result() == 150

def test_negative_operand():
    assert Add(-10, 5).get_result() == -5

def test_zero_operands():
    assert Add(0, 0).get_result() == 0

def test_add_positive_and_negative():
    calculation = Add(8, -3)
    result = calculation.get_result()
    assert result == 5
    assert calculation.a == 8
    assert calculation.b == -3

def test_subtract():
    assert Subtract(20, 7).get_result() == 13

def test_subtract_can_return_a_negative_result():
    assert Subtract(5, 10).get_result() == -5

def test_calculation_is_abstract():
    # Expecting an exception is a testable behavior, not a failed test.
    with pytest.raises(TypeError):
        Calculation(10, 5)

def test_polymorphism():
    calculations = [Add(10, 5), Subtract(20, 7)]
    results = []
    for calculation in calculations:
        results.append(calculation.get_result())
    assert results == [15, 13]

def test_multiple_calculations():
    calculations = [
        Add(4, 6),
        Subtract(3, 8),
        Add(10, -2),]
    results = []
    for calculation in calculations:
        results.append(calculation.get_result())
    assert results == [10, -5, 8]

def test_decimal_addition():
    # Decimal floats can have tiny representation differences.
    assert Add(0.1, 0.2).get_result() == pytest.approx(0.3)

def test_decimal_subtraction():
    assert Subtract(1.5, 0.25).get_result() == 1.25

def test_subtract_two_negative_operands():
    assert Subtract(-10, -5).get_result() == -5

def test_subtract_zero_operands():
    assert Subtract(0, 0).get_result() == 0