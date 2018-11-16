from time import time

"""an example of decorator implementation

Decorators dynamically alter the functionality
of a function, method or class without having to
directly use subclasses.
"""


# a basic case
def foo(a, b):
    return a + b


before = time()
print("foo(1, 2):", foo(1, 2))
after = time()
print("elapsed:", after - before)

before = time()
print("foo(a, b):", foo("a", "b"))
after = time()
print("elapsed:", after - before)


# a wise solution using decorators
def timer(func):
    def f(*args, **kwargs):  # will work for any default function
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print("elapsed: ", after - before)
        return rv

    return f


@timer
def add(a, b):
    return a + b


print(add(10, 20))
