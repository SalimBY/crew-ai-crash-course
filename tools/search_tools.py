import json
import os
import requests
from crewai.tools import BaseTool


class SearchTool(BaseTool):
    name: str = "Search Tool"
    description: str = "Useful to search the internet about a given topic and return relevant results"
    
    def _run(self, query: str):
        """Execute the search with the given query"""
        import json
        import requests
        
        top_result_to_return = 4
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY': "1472ed9069a6945a2b0aaa61b6320e590ee48a94",
            'content-type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        # check if there is an organic key
        if 'organic' not in response.json():
            return "Sorry, I couldn't find anything about that, there could be an error with your serper api key."
        else:
            results = response.json()['organic']
            string = []
            for result in results[:top_result_to_return]:
                try:
                    string.append('\n'.join([
                        f"Title: {result['title']}", f"Link: {result['link']}",
                        f"Snippet: {result['snippet']}", "\n-----------------"
                    ]))
                except KeyError:
                    continue

            return '\n'.join(string)
