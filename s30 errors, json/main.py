

# try:
#     file = open('a_file.txt')
#     a_dictionary = {"key": "value"}
#     print(a_dictionary['non_existent_key']) 
# except FileNotFoundError:
#     file = open('a_file.txt', 'w') # create the file if there is an error
#     file.write('Something')
# except KeyError as error_message:
#     print(f'This key {error_message} does not exist.')
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError('This is an error that I made up.')

height = float(input('Height: '))
weight = int(input('Weight: '))

if height > 3:
    raise ValueError('This height is not acceptable!')

bmi = weight / height ** 2
print(bmi)


# JSON:
# updating (has to read first, load the data, update the data and then write the updated data):
with open('data.json', mode='r') as data_file:
                # Reading old data:
                data = json.load(data_file)
                # Updating old data with new data:
                data.update(new_data)
with open('data.json', 'w') as data_file:
    # Saving updated data:
    json.dump(data, data_file, indent=4)