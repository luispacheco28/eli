from PIL import Image
import os

from resizeimage import resizeimage

def reducir_v2(www):
    dir = www
    t = len(dir)
    h=0
    w=0
    m=0
    d=1
    dir2 = dir[:t - 4] + ".png"
    #print(dir2)
    with open(dir, 'r+b') as f:
        with Image.open(f) as image:
            width,heigh = image.size

            if heigh>1000:
                m=width/heigh
                heigh=800
                width=m*800
            elif heigh>500:
                d=1.5
                heigh=heigh/d
                width=width/d
            else:
                d=1.3
                heigh = heigh / d
                width = width / d



            cover = resizeimage.resize_cover(image, [width, heigh])
            cover.save(dir2, image.format)




