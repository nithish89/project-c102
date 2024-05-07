import os
import shutil

source="C:/Users/acer/Desktop/f"
destination="C:/Users/acer/Downloads"

source=source + '/'
destination=destination + '/' 


list_of_files = os.listdir(source)
for file in list_of_files:
    shutil.move((source+file), destination)

