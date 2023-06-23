#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open('./Input/Letters/starting_letter.txt') as starting_letter:
    starting_letter_content = starting_letter.read()

with open('./Input/Names/invited_names.txt') as invited_names:
    invited_names_content = invited_names.readlines()

print(starting_letter_content)
print(invited_names_content)

for name in invited_names_content:
    # strip all spaces and \n from the beginning and the and of a string:
    name_without_line = name.strip() 
    content_to_write = starting_letter_content.replace('[name]', name_without_line)
    with open(f'./Output/ReadyToSend/{name}.txt', 'w') as ready:
        ready.write(content_to_write)