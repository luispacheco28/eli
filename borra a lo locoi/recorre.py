import os
import time
from shutil import rmtree
import queue
import threading

from pruebas_multithread.reducir_v3 import downgrade



def encola(cola):

    y = 0
    x = 0
    d=""
    d2 = ""
    i = 0
    aux = 0
    ruta_app = r"C:\Users\SOPORTE\Desktop\ARca\ARCA DE PAPEL\htdocs\view\matematica"   #  os.getcwd()    C:\Users\SOPORTE\Desktop\VERSIONES DE CONTROL\ARCA DE PAPEL\htdocs"
    total = 0

    linea = '-' * 60
    for base, dirs, files in os.walk(ruta_app):

        for i in range(len(files)):

            if "img" in dirs:
                # aux=sum
                try:
                    print(dirs)
                    rmtree(base+"\\img")
                    print("Borrado")



                except:
                    print("pass")
    return cola
cola = queue.Queue()
print("eliminando archivos")
encola(cola)
print("eliminados con exito")