import os
from time import sleep

class Files:
    def __init__(self, old_path, new_path, quantity):
        self.new_path = new_path
        self.old_path = old_path
        self.quantity = quantity

    def get_path(self) -> str:
        return self.path

    def checkFile(self, file) -> bool:
        if os.path.exists(f'{self.old_path}/{file}'):
            return True
        else: 
            return False

    def create_dir(self) -> None:
        if not os.path.exists(self.new_path):
            os.makedirs(self.new_path)

    def list_dir(self) -> list:
        return os.listdir(self.old_path)

    def get_time(self, file) -> float:
        return os.path.getmtime(f'{self.old_path}/{file}')

    def create_list_files(self) -> None:
        files_list = self.list_dir()
        files_list.sort(key=self.get_time, reverse=True)
        self.files_list = files_list[:self.quantity]
    
    def move_file(self, file, name, episode) -> str:
        path = f'{self.new_path}/{name} {episode}'
        if self.checkFile(file):
            os.rename(f'{self.old_path}/{file}', path)
        return path

    def check_downloaded(self) -> list:
        self.create_list_files()
        for file in self.files_list:
            if file[-10:] == 'crdownload':
                print(f'{file} ainda está sendo baixado')
                sleep(10)
                self.create_list_files()
                self.check_downloaded()
        return self.files_list