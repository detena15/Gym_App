from pathlib import Path
import json, glob, random

def leer_archivo(path):

        with open(path) as file:

          archivo = json.load(file)
        
        return archivo

def escribir_archivo(path,archivo):

        with open(path,'w') as file:
             
          json.dump(archivo,file)