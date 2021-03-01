import functools
import requests
import json
import random
from urllib.parse import urlencode


class Giphy(object):
    def __init__(self, token):
        self.token = token
        self.base = f"https://api.giphy.com/v1/gifs"

    def Post(self, endpoint=None, **kwargs):
        if endpoint:
            if kwargs:
                if "fmt" in kwargs:
                    del (kwargs["fmt"])
                params = urlencode(kwargs)
                url = f"{self.base}{endpoint}?api_key={self.token}&{params}"
            else:
                url = f"{self.base}{endpoint}?api_key={self.token}"
        else:
            if "fmt" in kwargs:
                kwargs["fmt"] = "json"

            params = urlencode(kwargs)
            url = f"{self.base}?api_key={self.token}&{params}"
        result = requests.get(url)
        return result.json()

    def gif_by_id(self, id):
        return self.Post(endpoint=f"/{id}")

    def gifs_by_id(self, ids):
        return self.Post(ids=','.join(ids))

    def __getattr__(self, attr):
        endpoint = f"/{attr}"
        return functools.partial(self.Post, endpoint)

    async def arandom(self, tag):
        return self.Post(endpoint=f'/random', tag=tag)


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


class Tenor(object):
    def __init__(self, token):
        self.api_key = token

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

    async def asearch(self, tag, safesearch=False, limit=None):
        params = {'tag': tag}
        if safesearch:
            params['safesearch'] = safesearch
        if limit:
            params['limit'] = limit
        results = self._get(**params)
        return results

    async def arandom(self, tag):
        search_results = self.search(tag=tag)
        random_entry = random.choice(search_results['results'])
        gif = random_entry['media'][0]['gif']['url']
        return gif
