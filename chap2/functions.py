

def double(z):
    """ this is where you put an optional docstring that explains what the function does. for example,
    this function multiplies its input by 2"""
    return z * 2


def apply_to_one(f):
    """ calls the function f with 1 as its argument"""
    return f(1)

my_double = double
x = apply_to_one(my_double)
y = apply_to_one(lambda z: z + 4)
another_double_lambda = lambda z: 2 * z


def another_double(z):
    return 2 * z


def my_print(message="my default message"):
    print message


my_print("hello")
my_print()


def subtract(a=0, b=0):
    """
    """
    return a - b

subtract(10, 5)
subtract(0, 5)
subtract(b=5)
