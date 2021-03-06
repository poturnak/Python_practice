#! /library/Frameworks/Python.framework/Versions/3.5/python3.5


import time


def timing_function(some_function):

    """
    Outputs the time a function takes to execute.
    """

    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        return "Time it took to run the function: " + str((t2 - t1)) + "\n"
    return wrapper


@timing_function
def my_function():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print("\nSum of all the numbers: " + str((sum(num_list))))


print(my_function())

# ________________________________________________________________________________

from time import sleep


def sleep_decorator(function):

    """
    Limits how fast the function is called.
    """

    def wrapper(*args, **kwargs):
        sleep(2)
        function(*args, **kwargs)
    return wrapper


@sleep_decorator
def print_number(num1):
    print(num1)

print_number(222)

for num in range(1, 6):
    print_number(num)

# ________________________________________________________________________________
from functools import wraps
from flask import g, request, redirect, url_for


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/secret')
@login_required
def secret():
    pass
# ________________________________________________________________________________

