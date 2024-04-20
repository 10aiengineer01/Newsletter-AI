from agency_swarm.tools import BaseTool
from pydantic import Field
import json
import requests

class GetScrapeUrls(BaseTool):
    """
    Retrieves URLs related to the provided news content topics using the DuckDuckGo Instant Answer API.
    Each news content string is considered a query for which URLs will be found.
    """
    
    query: list[str] = Field(
        ..., description="List of topics to search URLs for. Each topic should be just one word."
    )

    def run(self) -> str:
        """
        Searches for URLs related to each topic in query using the DuckDuckGo Instant Answer API
        and compiles the results into a structured, serialized JSON object.
        """
        compiled_data = {'results': []}
        
        for query in self.query:
            urls = self._search_duckduckgo(query)
            compiled_data['results'].append({"query": query, "urls": urls})
        
        return json.dumps(compiled_data, ensure_ascii=False)

    def _search_duckduckgo(self, query):
        url = 'https://api.duckduckgo.com/'
        params = {
            'q': query,
            'format': 'json'
        }
        
        response = requests.get(url, params=params)
        urls = []

        if response.status_code == 200:
            data = response.json()
            related_topics = data.get('RelatedTopics', [])
            for topic in related_topics:
                if 'FirstURL' in topic:
                    urls.append(topic['FirstURL'])
        
        return urls
