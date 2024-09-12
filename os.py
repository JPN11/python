import os
import random

# Define the directory path
dir_path = "C:/path/to/your/directory"

# Get a list of all files in the directory
files = os.listdir(dir_path)

# Filter out only text files
text_files = [f for f in files if f.endswith(".txt")]

# Choose a random text file
random_file = random.choice(text_files)

# Get the full path to the random text file
random_file_path = os.path.join(dir_path, random_file)

print(random_file_path)
