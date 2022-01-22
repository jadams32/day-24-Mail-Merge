#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Create our letter
with open("starting_letter.txt", mode="r") as letter:
    letter = letter.read()

# Create a list of names to merge
with open("Mail Merge Project Start/Input/Names/invited_names.txt", mode="r") as name_data:
    names = name_data.readlines()

print(names)

# Save letter to a new file in the folder output
for name in names:
    with open(f"day/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as final_letter:
        # Replace text in letter with actual name
        final_letter.write(letter.replace("[name]", name))



        