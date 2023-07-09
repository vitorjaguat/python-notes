import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
        function()
        print('Done!')
    return wrapper_function

@delay_decorator
def say_hello():
    print('Hello')

@delay_decorator
def say_bye():
    print('Bye')

say_hello()