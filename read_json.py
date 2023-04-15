import json
import requests
from tqdm import tqdm
import os
import string
def modify_filename(original_filename, modification_function):
    # Get the file name without extension and the extension
    file_name, file_extension = os.path.splitext(original_filename)
    
    # Apply the modification function to the file name without extension
    new_file_name = modification_function(file_name)
    
    # Concatenate the new file name with the original file extension
    new_filename = new_file_name + file_extension
    
    return new_filename

# Define a custom modification function to remove illegal characters
def remove_illegal_characters(filename):
    # Set of allowed characters for filenames
    allowed_characters = set(string.ascii_letters + string.digits + "._-")
    
    # Filter out any illegal characters from the filename
    legal_filename = ''.join(c for c in filename if c in allowed_characters)
    
    return legal_filename

# Read JSON data from a file
with open('game.json', 'r') as file:
    data_list = json.load(file)

cnt=0
# Access and print JSON data from the list
for data in tqdm(data_list, desc="Processing URLs"):
    url=data['gameicon_urls']
    title=data['Name']
    response = requests.get(url)
    cnt=cnt+1
    if response.status_code == 200:
        title=modify_filename(title, remove_illegal_characters)
        with open('logo/{0}.jpg'.format(title), 'wb') as f:
            f.write(response.content)
    else:
        print('Error: Could not retrieve image.')
