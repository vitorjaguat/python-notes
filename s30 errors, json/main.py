

try:
    file = open('a_file.txt')
except FileNotFoundError:
    file = open('a_file.txt', 'w') # create the file if there is an error
