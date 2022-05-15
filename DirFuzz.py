#!/usr/bin/python3
#Hola! este script fue creado por TheMV, el motivo por el cual lo cree, fue por aburrimiento, XD.
#Y porque me hacia ilusion tener mi propia herramienta para fuzzing XD

#Librerias
from pwn import * 
import requests
import argparse
import signal
import sys
import time
import pdb

def def_handler(sig, frame):
    print("\n[-] Saliendo...\n")
    sys.exit(1)

#Ctrl + C
signal.signal(signal.SIGINT, def_handler)

parser = argparse.ArgumentParser()
parser.add_argument('-u','--url', help="URL de la pagina web")
parser.add_argument('-w', '--wordlist', help="Ruta del diccionario para hacer fuzzing")
parser = parser.parse_args()

def fuzzing():
    url = parser.url
    path = parser.wordlist
    if os.path.isfile(path) == True:
        fuzzFile = open(path, 'r')
        p1 = log.progress("Iniciando Funzzing a la pagina", url)
        time.sleep(2)
        try:
            for ruta in fuzzFile.readlines():
                ruta = ruta.strip('\n')
                urlCom = url + "/" + ruta
                resp = requests.get(urlCom)

                if resp.status_code == 200:
                    print("\n"+urlCom + " -> " + str(resp.status_code,) + "OK")
        except:
            print("No se pudo conectar con la url, porque el programa fue interrumpido o la url esta mal escrita")
    elif os.path.isfile(path) == False:
        print("La ruta del diccionario es incorrecto o no existe")
if __name__ == '__main__':
    fuzzing()
