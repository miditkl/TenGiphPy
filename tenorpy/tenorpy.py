import requests
import json
import random


API_KEY = "J5UVWPVIM4A5"
API_ENDPOINT = 'https://api.tenor.co/v1/'
DEFAULT_SEARCH_LIMIT = 25
SAFE_SEARCH = 'off'


class TenorApiException(Exception):
    pass


class TenorImage(object):
    def __init__(self, data=None):
        if data:
            self.created = data.get('created')
            self.url = data.get('url')
            self.tags = data.get('tags')
            self.type = data.get('tupe')
            self.dims = ""
            self.preview = ""
            self.size = ""
            self.duration = ""


if __name__ == "__main__":
    class Tenor(object):
        def __init__(self):
            self.api_key = API_KEY

        def _get(self, **params):
            params['api_key'] = self.api_key

            response = requests.get('https://api.tenor.co/v1/search', params=params)

            results = json.loads(response.text)

            return results

        def search(self, tag, safesearch=False, limit=None):
            params = {'tag': tag}
            if safesearch:
                params['safesearch'] = safesearch
            if limit:
                params['limit'] = limit
            results = self._get(**params)
            return results

        def random(self, tag):
            search_results = self.search(tag=tag)
            random_entry = random.choice(search_results['results'])
            gif = random_entry['media'][0]['gif']['url']
            return gif
