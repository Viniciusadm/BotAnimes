import os
from time import sleep

class Files:
    path = '/home/vinicius/Downloads'

    def checkFile(self, file):
        if os.path.exists(f'{self.path}/{file}'):
            return True
        else: 
            return False

    def renameFile(self, name, episode, file):
        sleep(1)
        while True:
            if self.checkFile(file):
                os.rename(f'{self.path}/{file}', f'{self.path}/{name} {episode}')
                break