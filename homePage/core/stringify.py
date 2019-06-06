# This program converts pdf to images and data from these images is extracted as string

import os
from pathlib import Path

from . import miner
from . import dictify
from . import record


def convert(file_path, firstPage, lastPage, data_dir):
    """
    Function to convert pdf pages into JPEG images and extract the data out of the images
    -> file_path = The pdf file (including extention) which has the data
    -> res = The resolution of the images generated (Default is 150)
    -> firstPage = The page number of the 1st page to start
    -> lastPage = The page number of the last page to stop
    """

    # Moving to data directory
    currentWD = Path.cwd()    
    os.chdir(data_dir)

    try:
        print("Starting pdf conversion...")
        pages = ','.join(str(e) for e in [n for n in range(firstPage, lastPage+1)])
        
        miner.main(["-o", "data.html","-p", pages, "-M","1.5","-W", "0.2", "-L", "0.1","-t", "html", file_path])

        print("-> Pdf conversion done!\nInitiating extraction...")
    except FileNotFoundError:
        print("Some file not found")
        return {}
    else:
        data, missed_records = dictify.data_to_dict(os.path.join(data_dir, 'data.html'))
        records_dict = record.create_records(data, missed_records)
        os.remove("data.html")
        return records_dict
    finally:
        os.chdir(currentWD)

if __name__ == "__main__":
    mainDir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    data_dir = os.path.join(mainDir, 'data')
    c = convert(file_path="RVP.pdf", firstPage=89, lastPage=91, data_dir=data_dir)
    print(c)
