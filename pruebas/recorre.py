import os
from pruebas import reducir_v2
from pruebas.reducir_v2 import reducir_v2
import threading

def recorre():

    y = 0
    x = 0

    i = 0
    aux = 0
    ruta_app =  r"C:\Users\SOPORTE\Desktop\imagenes pesadas"   #  os.getcwd()    C:\Users\SOPORTE\Desktop\VERSIONES DE CONTROL\ARCA DE PAPEL\htdocs"
    total = 0

    linea = '-' * 60
    for base, dirs, files in os.walk(ruta_app):

        for i in range(len(files)):

            if ".png" in files[i]:
                # aux=sum
                try:

                    reducir_v2(base+"\\"+files[i])

                except:
                    print("pass")








