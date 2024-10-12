import os

PLACEHOLDER = "[name]"

# Ensure the output directory exists
output_dir = "Day 24/Mail Merge Project/Output/ReadyToSend"
os.makedirs(output_dir, exist_ok=True)


with open("Day 24/Mail Merge Project/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("Day 24/Mail Merge Project/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"{output_dir}/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
