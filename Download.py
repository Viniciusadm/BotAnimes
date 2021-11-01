import urllib.request
from Config import Config

class Download:
    def __init__(self, url, title, title_file):
        self.url = url
        self.title = title
        self.title_file = title_file
        self.config = Config()
        self.path = self.config.get_config('path')
        self.download()

    def download(self) -> str:
        urllib.request.urlretrieve(self.url, self.path + self.title + '/' + self.title_file)
        return f'{self.title_file} baixado com sucesso!'