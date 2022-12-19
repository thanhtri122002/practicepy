import zipfile as zip
import os
from pathlib import Path
# compress all file into dat file
def compress_allfile_into_dat():
    # create a zip file
    zip_file = zip.ZipFile("student.dat", "w")
    # get all file in current directory
    for file in os.listdir(os.getcwd()):
        # add file to zip file
        if file.endswith(".txt"):
            zip_file.write(file)
    #close the current file
    zip_file.close()
    
# decompress all file into dat file
def decompress_allfile_into_dat():# usingzipfile
   
    # create a zip file
    zip_file = zip.ZipFile("student.dat", "r")
    # get all file in current directory
    for file in zip_file.namelist():
        # add file to zip file
        zip_file.extract(file)
    # close zip file
    zip_file.close()

def pickle():
    pass