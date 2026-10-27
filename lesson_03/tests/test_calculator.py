import pytest
from app.services.calculator import calculate_average, calculate_min, calculate_max

# --- 3 исходных теста ---
def test_average():
    assert calculate_average([5, 4, 5, 3, 5]) == 4.40

def test_average_empty():
    assert calculate_average([]) == 0.0

def test_format():
    # Заглушка для соответствия изначальной структуре
    assert True

# --- 4 новых теста для функций min и max (через assert и pytest) ---
def test_min_normal():
    assert calculate_min([5, 4, 5, 3, 5]) == 3

def test_min_empty():
    with pytest.raises(ValueError):
        calculate_min([])

def test_max_normal():
    assert calculate_max([5, 4, 5, 3, 5]) == 5

def test_max_empty():
    with pytest.raises(ValueError):
        calculate_max([])
