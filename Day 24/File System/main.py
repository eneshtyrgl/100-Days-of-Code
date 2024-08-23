# How to Open, Read, and Write to Files using the "with" Keyword


# Open and Read File

file = open("100 Days of Code\Day 24\File System\my_file.txt")
contents = file.read()
print(contents)
file.close()

with open("100 Days of Code\Day 24\File System\my_file.txt") as file:
    contents = file.read()
    print(contents)


# Write on File   # modes:  r=read, w=write, a=append

with open("100 Days of Code\Day 24\File System\my_file.txt", mode="w") as file:
    file.write("New text.")

with open("100 Days of Code\Day 24\File System\my_file.txt", mode="a") as file:
    file.write("\nOther text.")


# Create New File
with open("100 Days of Code\Day 24\File System\other_file.txt", mode="w") as file:
    file.write("New file created.")