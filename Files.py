import os
from time import sleep

class Files:
    path = '/home/vinicius/Downloads'

    def checkFile(self, file):
        if os.path.exists(self.path + '/' + file):
            return True
        else: 
            return False

    def renameFile(self, name, episode, file):
        sleep(5)
        while True:
            if self.checkFile(file):
                os.rename(file, f'{name} {episode}')
                break