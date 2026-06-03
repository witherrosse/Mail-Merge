PLACEHOLDER = "[name]"

### Read all names from the invited names file ###

with open("./Input/Names/invited_names.txt", "r") as names_file:

    names = names_file.readlines()

### Read the starting letter template ###

with open("./Input/Letters/starting_letter.txt", "r") as letter_file:

    letter_contents = letter_file.read()

    ### Loop through each name and create a personalized letter ###

    for name in names:

        stripped_name = name.strip()   # Remove extra spaces or new lines


        ### Replace the placeholder [name] with the actual name ###

        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

        ### Save the new letter as a separate file ###

        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as completed_letter:

            completed_letter.write(new_letter)