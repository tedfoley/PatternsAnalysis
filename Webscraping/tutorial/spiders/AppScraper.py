from pathlib import Path

import scrapy

class AlternativeToSpider(scrapy.Spider):
    name = 'alternativeto'
    start_urls = []

    # List of app names to scrape
    app_names = ["spotify", "fantastical", "finder"]

    # List to store descriptions
    descriptions = []

    def start_requests(self):
        # Generate URLs for each app name
        for app_name in self.app_names:
            url = f"https://alternativeto.net/browse/search/?q={app_name}"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                'Referer': 'https://www.google.com/',  # Add a valid referer here
            }
            yield scrapy.Request(url, callback=self.parse, meta={'app_name': app_name}, headers=headers)
    
    def parse(self, response):
        app_name = response.meta['app_name']
        description = response.css('span.AppListItem_description__wtODK > p::text').get()

        if description:
            self.descriptions.append(f'{app_name}: {description.strip()}')

        self.log(f'Scraped {app_name}: {description}')

    def closed(self, reason):
        # Save all descriptions to a single file
        with open('all_descriptions.txt', 'w', encoding='utf-8') as file:
            file.write('\n'.join(self.descriptions))
