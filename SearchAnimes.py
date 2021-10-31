import requests

class SearchAnimes:
    def __init__(self, name):
        self.name = name
        self.url = 'https://betteranime.net/autocompleteajax?term=' + self.name
        self.response = requests.get(self.url)
        self.json = self.response.json()
        self.animes = self.json
    
    def get_url(self):
        return self.url

    def get_animes(self):
        return self.animes

    def set_anime(self, anime):
        self.anime = anime

    def get_anime(self):
        return self.anime