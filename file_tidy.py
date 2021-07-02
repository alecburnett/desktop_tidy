import os
import glob
import shutil
from os import path

#define buckets (include v_ prefix) 
v_other           = ['.xml', '.log', '.recover', '.writingout', '.crdownload']
v_pdf_documents   = ['.pdf', '.pptx', '.docx', '.txt']
v_images          = ['.jpeg','.jpg','.svg','.png','.PNG','.mp4','.mp3', '.tif', '.JPG']
v_excels          = ['.xlsx', 'xls', '.csv']
v_shapefiles      = ['.gpkg', '.shp']
v_python          = ['.py', '.pynb', '.ipynb']
v_sql             = ['.sql']
v_fme             = ['.fmw']
v_qgis            = ['.qgs','.qgz']
v_disk_images     = ['.dmg', '.app']
v_zip_files       = ['.zip']
v_vpn             = ['.ovpn']

#define your main location here:
main_location   = r'/Users/alexburnett/Downloads'



#sorter function
def sorter(file, value, folder):
    try:
        if os.path.splitext(file)[1] in value:
            if (path.exists(folder)):
                shutil.move(file, folder)
            else:
                os.mkdir(folder)
                shutil.move(file, folder)
    except:
      pass

#list files
files = glob.glob(str(main_location) + '''/*''')

#loop through files
for file in files:
  #loop through variables and pass files through sorter function
  for variable in dir():
    if variable.startswith('v_'):
      value = eval(variable)
      folder =  ( str(main_location) + '/' + str(variable).replace("v_", "") )
      sorter(file, value, folder)
