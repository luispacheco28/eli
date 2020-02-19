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



            cover = resizeimage.resize_cover(image, [width, heigh])
            cover.save(dir2, image.format,optimize=True)
            print("exito")





