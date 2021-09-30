"the way it is a bad zipper, because it has terrible reuseability"
"""Let's think about where to reprocess to make the code more robust
and make it more possible to be reuse
1. where can be reuse
    * unzip
    * (process)
    * zip
2. use (process) to make the mechanism more interchangeable
"""
import os 
import shutil
import zipfile
from abc import ABC, abstractmethod
from pathlib import Path


class ZipProcessor(ABC):
    def __init__(self, zipname):
        self.zipname = zipname
        self.temp_directory = Path(f"unzipped-{zipname[:-4]}")
    
    def process_zip(self):
        self.unzip_files()
        self.process_files()
        self.zip_files()

    def unzip_files(self):
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.zipname) as zip:
            zip.extractall(str(self.temp_directory))

    @abstractmethod
    def process_files():
        pass

    def zip_files(self):
        with zipfile.ZipFile(self.zipname, "w") as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)
        shutil.rmtree(str(self.temp_directory))