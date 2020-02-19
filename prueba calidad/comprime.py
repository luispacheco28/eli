import  os, glob
from PIL import Image

cont = 0

### Configuracion
diri = "C:\\Users\\SOPORTE\\Desktop\\prubaim\\imagenes pesadas\\"  # directorio donde tendremos nuestras imagenes
qualityimg = 10  # calidad de salida de las imagenes
### termina configuracion
print ("comprimiendo...")
for img in glob.glob(diri + '*.jpg') + glob.glob(diri + '*.png') + glob.glob(diri + '*.gif'):
    try:
        namefile = os.path.basename(img)
        splitname = os.path.splitext(namefile)
        namefile = splitname[0]
        extens = splitname[1]
        i = Image.open(img)
        i.save(diri + "k" + namefile + extens, compress_level=9)
    except ValueError:
        print("no se pudo")
        cont = cont + 1
if cont > 0:
    print("Algunos archivos no se puedieron comprimir")
else:
    print("todos los ficheros fueron comprimidos con exito")