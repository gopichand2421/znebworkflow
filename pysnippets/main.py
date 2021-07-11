import os
import subprocess
from pathlib import Path
import shutil

rootDir = str(Path(__file__).resolve().parent.parent)

for file in os.listdir(rootDir):
    if file.endswith(".war"):
        filePath = os.path.join(rootDir,file)
        subprocess.run(f'echo {filePath}',shell=True)
        print(file+ ' is deleted successfully')

warFolder = str(os.path.join(rootDir,"source\kgcappliction\\target"))

for warfile in os.listdir(warFolder):
    if warfile.endswith(".war"):
        currentfile=str(os.path.join(warFolder,warfile))
        print(f'Source directory is: {currentfile}')
        print(f'Destination directory is {rootDir}')
        subprocess.call(f'copy {currentfile}  {rootDir}',shell=True)
        print("file is successfully copied")