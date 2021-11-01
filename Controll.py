import os
from Config import Config
from Fillers import Fillers

class Controll:
    def __init__(self):
        self.config = Config()
        self.path = self.config.get_config('path')

    def nextEpisode(self, anime, current) -> int:
        next_episode = int(current) + 1
        while (next_episode in Fillers(anime).get_fillers()):
            next_episode += 1

        return next_episode

    def create_dir(self, title) -> None:
        directory = self.path + '/' + title
        if not os.path.exists(directory):
            os.makedirs(directory)