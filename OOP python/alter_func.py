from functools import wraps


def logger(orig_func):
    import logging

    logging.basicConfig(filename=f"{orig_func.__name__}", level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(f"Ran with args: {args}, and kwargs {kwargs}")
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1

        print(f"{orig_func.__name__} ran in {t2} secs.")
        return result

    return wrapper


# def display():
#     print("display function ran")


import time


@logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print(f"display_info ran with arg({name}, {age})")


display_info("awesome", 18)
