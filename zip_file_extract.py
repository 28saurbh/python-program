# importing required modules
from zipfile import ZipFile

# specifying the zip file name
file_name = "name.zip"

# opening the zip file in Read Mode

with ZipFile(file_name, 'r') as zip:
    # printing all the contents of the zip
    zip.printdir()
    
    # extracting all the files
    print('Extracting all the files now...')
    zip.extractall()
    print('Done!')
