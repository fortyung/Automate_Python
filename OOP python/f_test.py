import logging

logging.basicConfig(filename="example.log", level=logging.DEBUG)


def logger(func):
    def log_fun(*args):
        logging.info(f"Running {func.__name__} with arguments {args}")
        print(func(*args))

    return log_fun


@logger
def add(a, b):
    return a + b


@logger
def sub(a, b):
    return a - b


# add_log = logger(add)
# sub_log = logger(sub)

add(2, 3)
sub(3, 2)
