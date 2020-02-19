import time
from PIL import Image
import os

from resizeimage import resizeimage


def reducir(www):
    dir = www
    m=0
    t = len(dir)
    dir2 = dir[:t - 4] + ".png"
    #print(dir2)
    with open(dir, 'r+b') as f:
        with Image.open(f) as image:
            width, heigh = image.size



            cover = resizeimage.resize_cover(image, [width / 6, heigh / 6])
            cover.save(dir2, image.format)



def recorre():
    sizefile = 0
    y = 0
    x = 0
    sum = 0
    i = 0
    aux = 0
    ruta_app = r"C:\Users\SOPORTE\Desktop\VERSIONES DE CONTROL\ARCA DE PAPEL\htdocs"#os.getcwd()  #
    total = 0
    num_archivos = 0
    formato = '%d-%m-%y %H:%M:%S'
    linea = '-' * 60
    for base, dirs, files in os.walk(ruta_app):

        for i in range(len(files)):

            if ".png" in files[i]:

                aux=sum
                sizefile = os.path.getsize(base+"\\"+files[i])

                #sizefile = os.stat(files[i]).st_size


                sum=aux+sizefile
                y=y+1

    print(sum / (1024 * 1024))

#recorre()

