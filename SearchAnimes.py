import requests

class SearchAnimes:    
    def search_anime(self, name) -> None:
        self.name = name
        self.url = 'https://betteranime.net/autocompleteajax?term=' + self.name
        self.response = requests.get(self.url)
        self.json = self.response.json()
        self.animes = self.json

    def get_url(self) -> str:
        return self.url

    def get_animes(self) -> list:
        return self.animes

    def set_anime(self, anime) -> None:
        self.anime = anime

    def get_anime(self) -> list:
        return self.anime