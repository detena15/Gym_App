#librerias
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

from datetime import datetime
from pathlib import Path
from pathlib import Path

import json, glob, random

#rutas

#clases

class TableScreen(Screen):

    def obtener_fecha(self):

        return datetime.now().strftime("%Y-%m-%d")
    
    def leer_archivo(self,path):

        with open(path) as file:
            archivo = json.load(file)
        
        return archivo
    
    def escribir_archivo(self,path,archivo):

        with open(path,'w') as file:
            json.dump(archivo,file)

    def done(self, serie, ejercicio, id):
        
        tabla_plantilla = self.leer_archivo("tabla_plantilla.json")
        
        if tabla_plantilla[serie][ejercicio] == 1:
            tabla_plantilla[serie][ejercicio] = 0 #Undone
        else:
            tabla_plantilla[serie][ejercicio] = 1 #Done
        
        self.escribir_archivo("tabla_plantilla.json",tabla_plantilla)
        
        self.ids[id].background_color = self.color(serie, ejercicio)
       
    def color(self, serie, ejercicio):

        color0 = [0.1, 0.7, 1, 1]
        color1 = [0.8, 0.2, 1, 1]

        tabla_plantilla = self.leer_archivo("tabla_plantilla.json")

        if tabla_plantilla[serie][ejercicio] == 1:
            return color1
        else:
            return color0

    def resetear(self):

        color0 = [0.1, 0.7, 1, 1]
        serie_ejercicio = ["serie_1_eje_1","serie_1_eje_2","serie_1_eje_3","serie_1_eje_4","serie_1_eje_5","serie_1_eje_6","serie_1_eje_7","serie_1_eje_8","serie_1_eje_9",
        "serie_2_eje_1","serie_2_eje_2","serie_2_eje_3","serie_2_eje_4","serie_2_eje_5","serie_2_eje_6","serie_2_eje_7","serie_2_eje_8","serie_2_eje_9",
        "serie_3_eje_1","serie_3_eje_2","serie_3_eje_3","serie_3_eje_4","serie_3_eje_5","serie_3_eje_6","serie_3_eje_7","serie_3_eje_8","serie_3_eje_9"]

        tabla_plantilla = self.leer_archivo("tabla_plantilla.json")

        for serie in tabla_plantilla:
            for ejercicio in tabla_plantilla[serie]:
                tabla_plantilla[serie][ejercicio] = 0
                self.color(serie,ejercicio)
        
        for i in serie_ejercicio:
            self.ids[i].background_color = color0
                
        with open("tabla_plantilla.json",'w') as file:
                json.dump(tabla_plantilla,file)
        
    def submit(self): #al hacer submit, se carga el tabla_plantilla.json al historial.json
        
        #tabla_historial = self.leer_archivo("historial.json")

        #tabla_plantilla = self.leer_archivo("tabla_plantilla.json")
        
        #tabla_historial[datetime.now().strftime("%Y-%m-%d")] = tabla_plantilla
        
        #self.escribir_archivo("historial.json",tabla_historial)

        #self.resetear()

        tabla_historial = self.leer_archivo("historial.json")
        
        if self.obtener_fecha() in tabla_historial:
            print("Ya has subido este dia")
        else:
            tabla_plantilla = self.leer_archivo("tabla_plantilla.json")       
            tabla_historial[self.obtener_fecha()] = tabla_plantilla
            self.escribir_archivo("historial.json",tabla_historial)

        self.resetear()






class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

#main
Builder.load_file('frontend.kv')

if __name__ == '__main__':
    MainApp().run()