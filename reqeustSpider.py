from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from PIL import Image
import requests
from tqdm import tqdm
import json
import re
def return_extra(url):
    # Configure headless mode for Chrome
    chrome_options = Options()
    chrome_options.add_argument('--headless')

    # Replace the path with the actual path to your Chrome WebDriver executable
    chrome_driver_path = '/path/to/chromedriver'

    # Initialize the WebDriver with a Service object
    service = Service(executable_path=chrome_driver_path)

    chrome_options = webdriver.ChromeOptions()

# Bypass SSL check (use this option with caution)
    chrome_options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)

    # Get the page source
    content = driver.page_source

    # Create a Beautiful Soup object
    soup = BeautifulSoup(content, 'html.parser')

    css_age_selector='#mainbody > div.global-body-content-container.container-fluid > div > div.content.ng-isolate-scope > div:nth-child(2) > ng-include > div > ng-include > div > div.game-header > div.game-header-body > div.game-header-gameplay.hidden-game-header-collapsed.ng-scope > gameplay-module > div > div > ul > li:nth-child(3) > div.gameplay-item-primary > span'
    css_description_selector='#mainbody > div.global-body-content-container.container-fluid > div > div.content.ng-isolate-scope > div:nth-child(2) > ng-include > div > div > ui-view > ui-view > div > overview-module > description-module > div > div.panel-body > div > div.game-description > div.panel.panel-condensed.panel-expandable.ng-scope.ng-isolate-scope.expandable > div.expandable-envelope > div > article > div > p:nth-child(1)'
    css_weight_selector='#mainbody > div.global-body-content-container.container-fluid > div > div.content.ng-isolate-scope > div:nth-child(2) > ng-include > div > ng-include > div > div.game-header > div.game-header-body > div.game-header-gameplay.hidden-game-header-collapsed.ng-scope > gameplay-module > div > div > ul > li:nth-child(4) > div.gameplay-item-primary > span.ng-isolate-scope'
    css_publishyear_selector='#mainbody > div.global-body-content-container.container-fluid > div > div.content.ng-isolate-scope > div:nth-child(2) > ng-include > div > ng-include > div > div.game-header > div.game-header-body > div.game-header-title-container > div > div.game-header-title-info > h1 > span'
    css_publisher_selector='#mainbody > div.global-body-content-container.container-fluid > div > div.content.ng-isolate-scope > div:nth-child(2) > ng-include > div > ng-include > div > div.game-header > div.game-header-body > div.game-header-credits.hidden-game-header-collapsed > ng-include > div > ul > li:nth-child(3) > popup-list > span.ng-scope > a'
    age= soup.select_one(css_age_selector)
    try:
        age=age.get_text(strip=True)
    except:
        age=None
    description=soup.select_one(css_description_selector)
    try:
        description=description.get_text(strip=True)
    except:
        description=None
    weight=soup.select_one(css_weight_selector)
    try:
        weight=weight.get_text(strip=True)
        weight= re.search(r'\d+\.\d+/\s*5', weight).group()
    except:
        weight=None
    year=soup.select_one(css_publishyear_selector)
    try:
        year=year.get_text(strip=True)[1:-1]
    except:
        year=None
    publisher=soup.select_one(css_publisher_selector)
    try:
        publisher=publisher['title']
    except:
        publisher=None
    driver.quit()
    return [age,description,weight,year,publisher]
    

url = 'https://boardgamegeek.com/browse/boardgame/page/1'


# Configure headless mode for Chrome
chrome_options = Options()
chrome_options.add_argument('--headless')

# Replace the path with the actual path to your Chrome WebDriver executable
chrome_driver_path = '/path/to/chromedriver'

# Initialize the WebDriver with a Service object
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

pirce_lst=[]
Normal_Rating_lst=[]
Avg_Rating_lst=[]
Num_Voter_lst=[]
title_lst=[]
url_lst=[]
age_lst=[]
description_lst=[]
logo_urls_lst=[]
weight_lst=[]
publishyear_lst=[]
publisher_lst=[]
# Fetch the web page
driver.get(url)

# Get the page source
content = driver.page_source

# Create a Beautiful Soup object
soup = BeautifulSoup(content, 'html.parser')

# CSS selector to find the game titles
css_price_selector = '#row_ > td.collection_shop'
css_title_selector='.collection_objectname a'
css_ratings_selector='td.collection_bggrating'
css_urls_selector='.collection_objectname a '
css_logo_selector='#row_ > td.collection_thumbnail > a > img'
# Find elements using the CSS selector
game_prices = soup.select(css_price_selector)
titles=soup.select(css_title_selector)
ratings=soup.select(css_ratings_selector)
urls=soup.select(css_urls_selector)
logos=soup.select(css_logo_selector)
for url in urls:
    url_lst.append('https://boardgamegeek.com/'+url['href'])
for title in titles:
    title=title.get_text(strip=True)
    title_lst.append(title)
for rating in ratings[0::3]:
    rating=rating.get_text(strip=True)
    Normal_Rating_lst.append(rating)

for rating in ratings[1::3]:
    rating=rating.get_text(strip=True)
    Avg_Rating_lst.append(rating)

for rating in ratings [2::3]:
    rating=rating.get_text(strip=True)
    Num_Voter_lst.append(rating)
pattern = r"Amazon:\$(\d+\.\d{2})"
# Print the text content of each game title
for price in game_prices:
    price=price.get_text(strip=True)
    match = re.search(pattern, price)
    if match:
            amazon_price = match.group(1)
            pirce_lst.append(amazon_price)
    else:
            pirce_lst.append('Amazon:Unavailable')
for url in logos:
    logo_urls_lst.append(url['src'])
# Close the WebDriver
for url in tqdm(url_lst, desc="Processing URLs"):
    extra_lst=return_extra(url)
    age_lst.append(extra_lst[0])
    description_lst.append(extra_lst[1])
    weight_lst.append(extra_lst[2])
    publishyear_lst.append(extra_lst[3])
    publisher_lst.append(extra_lst[4])

zipped = zip(title_lst, Normal_Rating_lst, Avg_Rating_lst, Num_Voter_lst, age_lst, description_lst,pirce_lst,logo_urls_lst,weight_lst,publishyear_lst,publisher_lst)

# Create a list of dictionaries
combined_list = [
    {
        "Name": item[0],
        "Geek Rating": item[1],
        "Avg Rating": item[2],
        "Num Voter": item[3],
        "Age": item[4],
        "Description": item[5],
        "gamePrice":item[6],
        "gameicon_urls":item[7],
        "gameRate":item[8],
        "gamePublishDate":item[9],
        "publisher":item[10]
    }
    for item in zipped
]

# Write the dictionaries to a JSON file
with open("output2.json", "w") as outfile:
    json.dump(combined_list, outfile)


for i in range(len(logo_urls_lst)):
    url=logo_urls_lst[i]
    title=title_lst[i]
    response = requests.get(url)
    if response.status_code == 200:
        with open('logo/{0}.jpg'.format(title), 'wb') as f:
            f.write(response.content)
    else:
        print('Error: Could not retrieve image.')
driver.quit()
