with open("C:/Users/ns/Desktop/new_file.txt", mode="w") as file:
    file.write("New file created.")

with open("/Users/ns/Desktop/new_file.txt") as file:
    contents = file.read()
    print(contents)