from functools import wraps
import time

# Wrapper to add timing information as a second return value
def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        tic = time.time()
        result = f(*args, **kwargs)
        toc = time.time()
        return f"\n########\n\nTaking {toc-tic:.6f}s, the {f.__name__} answer is" \
            f" {result}\n\n########\n"
    return wrapper