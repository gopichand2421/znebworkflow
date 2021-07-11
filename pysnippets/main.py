import os,glob

from pathlib import Path
import shutil

rootDir = str(Path(__file__).resolve().parent.parent)

for file in os.listdir(rootDir):
    if file.endswith(".war"):
        os.remove(file)

warFolder = str(os.path.join(rootDir,"source\kgcappliction\\target"))

for warfile in os.listdir(warFolder):
    if warfile.endswith(".war"):
        currentfile=str(os.path.join(warFolder,warfile))
        shutil.copyfile(currentfile,rootDir)