# def decorator_func(original_func):
#     def wrapper_func(*args, **kwargs):
#         print(f"This was printed before {original_func.__name__}")
#         return original_func(*args, **kwargs)

#     return wrapper_func


class decorator_class(object):
    def __init__(self, original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        print(f"The call method was printed before {self.original_func.__name__}")
        return self.original_func(*args, **kwargs)


@decorator_class
def display():
    print("display function ran")


@decorator_class
def display_info(name, age):
    print(f"display_info ran with arg({name}, {age})")


display_info("john", 55)
print("---------")
display()
