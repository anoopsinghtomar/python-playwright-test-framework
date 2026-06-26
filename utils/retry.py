from functools import wraps
import time


def retry(attempts=3, delay=1):
    """
    Retry a function a specified number of times.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None

            for _ in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    last_exception = exc
                    time.sleep(delay)

            raise last_exception

        return wrapper

    return decorator