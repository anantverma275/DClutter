import os
import pandas as pd
from pathlib import Path

def getFiles(mypath):
    return [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
def stripColumn(fileformat):
    try:
        return fileformat.strip()
    except AttributeError:
        pass
        
def getFolder(fileformat):
    for column in db.columns:
        db[column] = db[column].apply(stripColumn)
        if fileformat in list(db[column]):
            return column
    return None

def getIndexedFileName(foldername, filename, fileformat):
    files = getFiles(mypath+"\\" + foldername)
    files = [m for m in files if filename in m]
    for i in range(2, len(files)+1):
        if filename + f" - Copy ({i})" + fileformat not in files:
            return filename + f" - Copy ({i})"
        
mypath = input()
files = getFiles(mypath)
db = pd.read_csv("database.csv")

for file in files:
    filename = os.path.splitext(file)[0] 
    fileformat = os.path.splitext(file)[1].strip()
    foldername = getFolder(fileformat)
    if foldername is not None:
        Path(mypath+"\\"+foldername).mkdir(parents=True, exist_ok=True)
        try:
            os.rename(mypath+"\\"+file, mypath+"\\" + foldername + "\\" + file)
        except FileExistsError:
            n = int(input(file + " already exists in " + foldername +".\n" + "Choose:\n1. Replace\n2. Append index\n3. Skip\n"))
            if n == 1:
                os.replace(mypath+"\\"+file, mypath+"\\" + foldername + "\\" + file)
            if n == 2:
                try:
                    os.rename(mypath+"\\"+file, mypath+"\\" + foldername + "\\" + filename + " - Copy" + fileformat)
                except FileExistsError:
                    filename = getIndexedFileName(foldername, filename, fileformat) 
                    os.rename(mypath+"\\"+file, mypath+"\\" + foldername + "\\" + filename + fileformat)    