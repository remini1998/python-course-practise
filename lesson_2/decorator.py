import time
from functools import wraps
from typing import Callable


def timer(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time() * 1000
        result = func(*args, **kwargs)
        end = time.time() * 1000
        print("\n===================================")
        print("===================================")
        print("Function Name\t: %s" % func.__name__)
        print("Used Time\t\t: %.3f ms" % (end - start))
        print("===================================")
        print("===================================\n")
        return result
    return wrapper
