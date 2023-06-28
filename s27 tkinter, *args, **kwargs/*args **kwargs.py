# *args: are stored in the form of a tuple
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(2,3,2,3,2,4,3))

# **kwargs: are stored in the form of a dictionary
def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

calculate(2, add=3, multiply=5)