from PIL import Image
import os

from resizeimage import resizeimage

def reducir(www):
    dir = www
    t = len(dir)
    dir2 = dir[:t - 4] + ".png"
    #print(dir2)
    with open(dir, 'r+b') as f:
        with Image.open(f) as image:
            width,heigh = image.size

            cover = resizeimage.resize_cover(image, [width/6, heigh/6])
            cover.save(dir2, image.format)


sizefile=0
y=0
x=0
sum=0
i = 0
aux=0
ruta_app =  r"D:\versiones de control\ARCA DE PAPEL" # os.getcwd()
total = 0
num_archivos = 0
formato = '%d-%m-%y %H:%M:%S'
linea = '-' * 60
print(os.getcwd())

for base, dirs, files in os.walk(ruta_app):

    for i in range(len(files)):



        if ".png" in files[i]:
            #aux=sum
            try:
                reducir(base+"\\"+files[i])
                print(1)
            except:
                print("pass")
            #sizefile = os.path.getsize(base+"\\"+files[i])
            #if sizefile > 700024:
              #  x=x+1
               #print(1)
            #sizefile = os.stat(files[i]).st_size

            #sum=aux+sizefile
            #y=y+1


print(sum/(1024*1024))