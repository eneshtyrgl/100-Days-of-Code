import os

# Create 100 directories named 'Day 1', 'Day 2', ..., 'Day 100'
for day in range(1, 101):
    directory_name = f"Day {day}"
    print(f"Creating directory: {directory_name}")
    try:
        os.mkdir(directory_name)
    except FileExistsError:
        print(f"Directory {directory_name} already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{directory_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
