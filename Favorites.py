class Favorites:
    def __init__(self):
        self.favorites = [{
            'title': 'Detective Conan',
            'url': 'https://betteranime.net/anime/legendado/detective-conan',
        }]

    def get_favorites(self) -> list:
        return self.favorites