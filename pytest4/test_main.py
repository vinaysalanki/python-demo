import pytest
import time
from main import palindrome, length, maximum, minimum, sort

# Time measuring decorator
def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"\nTest {func.__name__} executed in {end - start:.6f} seconds")
        return result
    return wrapper

# Fixed assertion for length
@measure_time
def test_length():
    assert length([1,2,3]) == 3   # ✅ Corrected

@measure_time    
def test_maximum():
    assert maximum([1,5,9,50]) == 50

@measure_time
def test_sort():
    assert sort([1,9,5,4]) == [1,4,5,9]

@pytest.mark.skip(reason="Feature not implemented")
def test_minimum_skip():
    assert minimum([6,8,9,2]) == 6

@pytest.mark.xfail(reason="Known issue with palindrome check")
def test_palindrome_xfail():
    assert palindrome("madam") == True