student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

df = pandas.read_csv('nato_phonetic_alphabet.csv')

NATO_dictionary = {row.letter:row.code for (index, row) in df.iterrows()}
# print(NATO_dictionary)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def convert_to_NATO():
    user_input = input('Input a word to convert to NATO phonetic dictionary:\n').upper()
    try:
        output = [NATO_dictionary[letter] for letter in user_input]
    except KeyError:
        print('Sorry, only letters are accepted.')
        convert_to_NATO()
    else: 
        print(output)
        convert_to_NATO()

convert_to_NATO()