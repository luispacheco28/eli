from PIL import Image
import queue

from resizeimage import resizeimage

def downgrade(cola=queue.Queue()):

    dir = cola.get()
    if (cola.empty() == True):
        print("SE ACABO")

    print(dir)

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
                heigh=900
                width=m*900
            elif heigh>500:
                m = width / heigh
                heigh = 400
                width = m * 400
            elif heigh>380:
                m = width / heigh
                heigh = 300
                width = m * 300



            cover = resizeimage.resize_cover(image, [width, heigh])
            cover.save(dir2, image.format,optimize=True)
            print("exito")





