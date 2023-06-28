# using the with keyword, tehre is no need to call file.close()
# with open('my_file.txt') as file:
#     contents = file.read()
#     print(contents)


with open('new_file.txt', mode='w') as file:
    file.write('\nNew textttttt.')