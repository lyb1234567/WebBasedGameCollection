import json
import requests
from tqdm import tqdm
# Read JSON data from a file
with open('output2.json', 'r') as file:
    data_list = json.load(file)

# Access and print JSON data from the list
for data in tqdm(data_list, desc="Processing URLs"):
    url=data['gameicon_urls']
    title=data['Name']
    response = requests.get(url)
    if response.status_code == 200:
        with open('logo/{0}.jpg'.format(title), 'wb') as f:
            f.write(response.content)
    else:
        print('Error: Could not retrieve image.')
