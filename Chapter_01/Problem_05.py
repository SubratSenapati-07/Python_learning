import os

# Specify the directory path (use '.' for the current directory)
directory_path = "."

# List the contents of the directory
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
    print(item)
