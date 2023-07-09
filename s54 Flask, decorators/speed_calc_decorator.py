import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def wrapper_function():
        first_time = time.time()
        function()
        second_time = time.time()
        diff = second_time - first_time
        return diff
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i
        
@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_time = fast_function()
slow_time = slow_function()
print(f'fast function run speed: {fast_time}')
print(f'slow function run speed: {slow_time}')
