import pytest
from division import divide

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
