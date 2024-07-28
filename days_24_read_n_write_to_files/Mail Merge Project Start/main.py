#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names_path = "./Input/Names/invited_names.txt"
letter_path = "./Input/Letters/starting_letter.txt"
replace_string = "[name]"

with open(names_path, "r") as names: # Reads names in the file into a list
    invited_names = names.readlines()

# Gets hold of each name and put in a true list
names_list = [] 
for line in invited_names:
    names_list.append(line.strip("\n")) # Removes backslash and 'n'

# Read through the invite content into a list.
with open(letter_path, "r") as letter:
    start_letter = letter.read() # reads the whole text in the starting_letter.

# Loops through the list of names and compares if there is a '[name]' value and replace it.   
for name in names_list:
    if replace_string in start_letter:
        mod_content = start_letter.replace(replace_string, name)
    # Creates a new file according to the person's name in the loop.
    with open(f"./Output/ReadyToSend/invitation_{name}.txt", "w") as final_letter:
        final_letter.write(mod_content)


## Antie Angela's code
# with open("./Input/Names/invited_names.txt") as names_file: # Reads names in the file into a list
#     names = names_file.readlines()

# with open("./Input/Letters/starting_letter.txt") as letter_file:
#     letter_contents = letter_file.read()
#     for name in names:
#         stripped_name = name.strip("\n")
#         new_letter = letter_contents.replace(replace_string, stripped_name)
#         print(new_letter)
#         with open(f"./Output/ReadyToSend/invitation_{stripped_name}.txt", "w") as final_letter:
#             final_letter.write(new_letter)




## Using enumerate to change a single value in a phrase inside a list.
# with open(letter_path) as letter:
#     starting_letter = letter.readlines()
#     for i, line in enumerate(starting_letter):
#         if '[name]' in line:
#             starting_letter[i] = line.replace('[name]', invited_names[0])