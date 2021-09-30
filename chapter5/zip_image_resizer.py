from zipfile import ZipExtFile
from zip_processor_templete import ZipProcessor
import sys
import os 
from PIL import Image


class ScaleZip(ZipExtFile):
    def processfile(self):
        for filename in self.temp_directory.iterdir():
            im = Image.open(str(filename))
            scaled = im.read.resize((640, 480))
            scaled.save(str(filename))


if __name__ == "__main__":
    ScaleZip(*sys.argv[1:4]).process_zip()
