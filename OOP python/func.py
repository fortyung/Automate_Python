"""
First class function & Higher order function
"""


def square(x):
    return x * x


# f = square() # First class function


def my_map(func, arg_list):  # Higher order function
    result = []

    for i in arg_list:
        result.append(func(i))
    return result


lop = my_map(square, [1, 2, 3, 4, 5])

print(lop)
