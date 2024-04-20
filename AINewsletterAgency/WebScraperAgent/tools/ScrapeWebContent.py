from agency_swarm.tools import BaseTool
from pydantic import Field
import requests
import json
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
grandparent_dir = os.path.dirname(parent_dir)
sys.path.append(grandparent_dir)

class ScrapeWebContent(BaseTool):
    """
    Extracts text content from a list of URLs using BeautifulSoup.
    The extracted content is returned as a list of text pieces, one for each URL.
    """

    urls: list[str] = Field(
        ..., description="List of URLs to scrape."
    )

    def scrape_url(self, url):
        from agency import browserless_api
        api_url = "https://chrome.browserless.io/scrape?token="+browserless_api
        headers = {'Content-Type': 'application/json'}
        data = json.dumps({
            "url": url,
            "elements": [
                {"selector": "p"}
            ]
        })
        
        response = requests.post(api_url, headers=headers, data=data)
        
        if response.status_code == 200:
            content = response.json()
            
            text_contents = []
            for result in content['data'][0]['results']:
                text_contents.append(result['text'])
            return text_contents
        else:
            print(f"Issue while scraping these: {url}, Code {response.status_code}")
            return ""

    def run(self) -> list[str]:
        """
        Performs web scraping on the provided URLs, extracting text content.
        """
        extracted_texts = []
        for url in self.urls:
            paragraph_texts = self.scrape_url(url)
            if paragraph_texts:
                full_text = ' '.join(paragraph_texts)
                extracted_texts.append(full_text)
            else:
                extracted_texts.append("Issue while scraping the the url")
        return extracted_texts
