import scrapy
from tqdm import tqdm
import logging
import requests
logging.getLogger('scrapy').propagate = False
class BoardgameSpiderSpider(scrapy.Spider):
    name = 'boardgame_spider'
    allowed_domains = ['boardgamegeek.com']
    start_page = 1
    num_pages = 5
    start_urls = [f'https://boardgamegeek.com/browse/boardgame/page/{i}' for i in range(start_page, start_page + num_pages)]
    def parse(self, response):
        # Extract game titles
        titles = response.css('.collection_objectname a::text').getall()

        # Extract game ratings
        ratings = response.css('td.collection_bggrating::text').getall()
        ratings = [rating.strip() for rating in ratings if rating.strip()]

        normal_ratings = ratings[0::3]
        avg_ratings = ratings[1::3]
        num_voters = ratings[2::3]

        # Extract game URLs
        game_urls = response.css('.collection_objectname a::attr(href)').getall()

        # Combine titles, ratings, and game URLs into a list of dictionaries
        games = [{'Name': title, 'Geek Rating': normal_rating, 'Avg Rating': avg_rating, 'Num_voters': voter, 'url': response.urljoin(url)} for title, normal_rating, avg_rating, voter, url in zip(titles, normal_ratings, avg_ratings, num_voters, game_urls)]

        # Visit each game page to extract shop price information
        for game in games:
            yield scrapy.Request(game['url'], callback=self.parse_game_page, meta={'game': game})
    pbar = tqdm(total=num_pages, desc='Downloading Pages')
    def parse_game_page(self, response):
        game = response.meta['game']

        # Extract price information
        price_section = response.css('.gameplay')

        # Extract Amazon link if available
        amazon_link = price_section.css('a[href*="amazon.com"]::attr(href)').get()

        # Update game dictionary with Amazon link
        game['Amazon Link'] = amazon_link

        yield game
    def closed(self, reason):
        # Close the progress bar when the spider finishes
        self.pbar.close()
