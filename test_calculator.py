
import pytes
import calculator
import math

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0

def test_subtract():
    assert calculator.sub(5, 3) == 2
    assert calculator.sub(0, 4) == -4

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.div(5, 0)

def test_logarithm():
    assert math.isclose(calculator.log(10, 100), 2)
    assert math.isclose(calculator.log(2, 8), 3)

def test_log_invalid_base():
    with pytest.raises(ValueError):
        calculator.log(1, 10)
    with pytest.raises(ValueError):
        calculator.log(-2, 8)
    with pytest.raises(ValueError):
        calculator.log(2, -8)

if __name__ == "__main__":
    unittest.main()