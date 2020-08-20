other=['.xml', '.log', '.recover', '.writingout']
PDF=['.pdf', '.pptx', '.docx']
Images=['.jpeg','.jpg','.svg','.png','.PNG','.mp4','.mp3', '.tif', '.JPG']
excels = ['.xlsx', 'xls', '.csv']
shapefiles = ['.gpkg', '.shp']
fme = ['.fmw']
qgis = ['.qgs','.qgz']

pdfLocation=r'C:\Users\AlexanderBurnett\Dropbox (MapStand)\MapStand Team Folder\Alex Burnett\PDFs'
shapeLocation=r'C:\Users\AlexanderBurnett\Dropbox (MapStand)\MapStand Team Folder\Alex Burnett\Shapefiles'
excelFilesLocation=r'C:\Users\AlexanderBurnett\Dropbox (MapStand)\MapStand Team Folder\Alex Burnett\Excels'
imageFilesLocation=r'C:\Users\AlexanderBurnett\Dropbox (MapStand)\MapStand Team Folder\Alex Burnett\Images'
fmeLocation=r'C:\Users\AlexanderBurnett\Dropbox (MapStand)\MapStand Team Folder\Alex Burnett\FME'
qgisLocation=r'C:\Users\AlexanderBurnett\Dropbox (MapStand)\MapStand Team Folder\Alex Burnett\QGIS'
otherLocation = r'C:\Users\AlexanderBurnett\Dropbox (MapStand)\MapStand Team Folder\Alex Burnett\Other'


def sorter(file):
    try:
        print(file)
#pdf
        if os.path.splitext(file)[1] in PDF:
            if(path.exists(pdfLocation)):
                shutil.move(file,pdfLocation)
            else:
                os.mkdir(pdfLocation)
                shutil.move(file,pdfLocation)
#shape
        if os.path.splitext(file)[1] in shapefiles:
            if(path.exists(shapeLocation)):
                shutil.move(file,shapeLocation)
            else:
                os.mkdir(shapeLocation)
                shutil.move(file,shapeLocation)
#excel
        if os.path.splitext(file)[1] in excels:
            if(path.exists(excelFilesLocation)):
                shutil.move(file,excelFilesLocation)
            else:
                os.mkdir(excelFilesLocation)
                shutil.move(file,excelFilesLocation)
#images
        if os.path.splitext(file)[1] in Images:
            if(path.exists(imageFilesLocation)):
                shutil.move(file,imageFilesLocation)
            else:
                os.mkdir(imageFilesLocation)
                shutil.move(file,imageFilesLocation)
#fme
        if os.path.splitext(file)[1] in fme:
            if(path.exists(fmeLocation)):
                shutil.move(file,fmeLocation)
            else:
                os.mkdir(fmeLocation)
                shutil.move(file,fmeLocation)

#QGIS
        if os.path.splitext(file)[1] in qgis:
            if(path.exists(qgisLocation)):
                shutil.move(file,qgisLocation)
            else:
                os.mkdir(qgisLocation)
                shutil.move(file,qgisLocation)
#other
        if os.path.splitext(file)[1] in other:
            if(path.exists(otherLocation)):
                shutil.move(file,otherLocation)
            else:
                os.mkdir(otherLocation)
                shutil.move(file,otherLocation)
    except:
        print('failed')
        pass
    

import os
import glob
import shutil
from os import path
desktop = glob.glob(r"C:\Users\AlexanderBurnett\Desktop\*")
dropbox = glob.glob(r"C:\Users\AlexanderBurnett\Dropbox (MapStand)\MapStand Team Folder\Alex Burnett\Various\*")


print("desktop")
for file in desktop:
    sorter(file)

print("dropbox")
for file in dropbox:
    sorter(file)

