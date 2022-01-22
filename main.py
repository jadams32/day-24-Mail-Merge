# On Day 24 of 100 days of code, the main topic learned was reading/writing to files, and file path structures.
# Here we use that knowledge by creating a mail merge program to send birthday letters out to friends.

# Create our letter
with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
    letter = letter.read()

# Create a list of names to merge
with open("./Input/Names/invited_names.txt", mode="r") as name_data:
    names = name_data.readlines()
    # Go through the names list and strip any spaces
    for name in names:
        formatted_name = name.strip()
        # Save letter to a new file in the folder output
        with open(f"./Output/ReadyToSend/letter_for_{formatted_name}.txt", mode="w") as final_letter:
            # Replace text in letter with actual name
            final_letter.write(letter.replace("[name]", formatted_name))
        