#  new_list = [new_item for item in list]

numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = 'Jaguat'
letters = [letter for letter in name]
print(letters)

range_list = range(1,5)
double_list = [num * 2 for num in range_list]
print(double_list)


# list_with_test = [new_item for item in list if test]
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Freddie']

short_names = [name for name in names if len(name) < 5]
print(short_names)

uppercase_large_names = [name.upper() for name in names if len(name) > 5]
print(uppercase_large_names)


# new_dict = {new_key:new_value for item in list}
# new_dict2 = {new_key:new_value for (key,value) in dict.items()}


