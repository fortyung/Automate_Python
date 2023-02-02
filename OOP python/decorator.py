def prefix_deco(prefix):
    def decorator_func(original_func):
        def wrapper_func(*args, **kwargs):
            print(f"{prefix}: This was printed before {original_func.__name__}")
            return original_func(*args, **kwargs)

        return wrapper_func

    return decorator_func


# @decorator_func
# def display():
#     print("display function ran")


@prefix_deco("Testing...")
def display_info(name, age):
    print(f"display_info ran with arg({name}, {age})")


display_info("john", 55)
# print("---------")
# display()
