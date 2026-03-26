import pytest
import time
from main import login,game,payment,email
def measure_time(func):
    def wrapper(*arg,**kwargs):
        start=time.time()
        result=func(*arg,**kwargs)
        end=time.time()
        
        print(f"\nTest {func.__name__} executed in{end-start:.6f} seconds")
        return result
    return wrapper
@measure_time   
def test_login():
    assert login("vinu","@123")==True
@measure_time
def test_game():
    assert game("pubg")==True
@measure_time
def test_payment():
    assert payment(600)==True
@measure_time
def test_email():
    assert email("amd.com")==True


