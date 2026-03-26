import time
def measure_time(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f'\nTest {func.__name__}executed in {end-start::2f}seconds')
        return result
    return wrapper

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        # Only print if the test passes
        #if not hasattr(func, "_failed"):
        print(f"\nTest {func.__name__} executed in {end - start:.6f} seconds")
        #print(end-start)
        return result
    return wrapper