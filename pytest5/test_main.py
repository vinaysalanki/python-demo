import pytest
import time
from main import add, sub, even, maximum, swap

# Decorator for pytest-compatible timing
def measure_time(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f"\nTest {func.__name__} executed in {end - start:.6f} seconds")
        return result
    return wrapper

# -------------------------------
# Test Cases
# -------------------------------

@measure_time
def test_sub():
    assert sub(9,7) == 2

@measure_time
def test_even():
    assert even(6) == True

# Skip / skipif / xfail
@pytest.mark.skip(reason="Swap test skipped")
def test_swap_skip():
    assert swap(5,7) == [7,5]

@pytest.mark.skipif(True, reason="Maximum test condition not met")
def test_maximum_skipif():
    assert maximum([5,7,9]) == 9

@pytest.mark.xfail(reason="Intentional XFail example")
def test_add_xfail():
    assert add(5,7) == 11