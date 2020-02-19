import os
import time

import queue
import threading

from pruebas_multithread.reducir_v3 import downgrade
def medir():

     tiempo_inicial = time.clock()

     tiempo_transcurrido = time.clock() - tiempo_inicial
     print("Tiempo transcurrido: %0.10f segundos." % tiempo_transcurrido)


def recorre2(cola):

    y = 0
    x = 0
    d=""
    d2 = ""
    i = 0
    aux = 0
    ruta_app = r"C:\Users\SOPORTE\Desktop\ARca\ARCA DE PAPEL\htdocs\view\exercises"   #  os.getcwd()    C:\Users\SOPORTE\Desktop\VERSIONES DE CONTROL\ARCA DE PAPEL\htdocs"
    total = 0

    linea = '-' * 60
    for base, dirs, files in os.walk(ruta_app):

        for i in range(len(files)):

            if ".png" in files[i]:
                # aux=sum
                try:

                    cola.put(base+"\\"+files[i])



                except:
                    print("pass")
    return cola





cola = queue.Queue()
cola2=recorre2(cola)
print("empezamos a comprimir")
for i in range(cola2.qsize()):
    t = threading.Thread(target=downgrade, args=(cola2,))
    t2 = threading.Thread(target=downgrade, args=(cola2,))
    t3 = threading.Thread(target=downgrade, args=(cola2,))
    t4 = threading.Thread(target=downgrade, args=(cola2,))
    t5 = threading.Thread(target=downgrade, args=(cola2,))
    t6 = threading.Thread(target=downgrade, args=(cola2,))
    t.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
medir()












