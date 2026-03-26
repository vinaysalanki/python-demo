import pytest
from simple import add, sub, mul, even, odd
def test_add():
    assert add(2,3)==5
def test_sub():
    assert sub(5,4)==3
def test_mul():
    assert mul(2,7)==14
def test_even():
    assert even(5)==True
def test_odd():
    assert odd(10)==True  
