#librerias
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

from datetime import datetime
from pathlib import Path
import json, glob, random

from archivos import * #modulo creado por Eduardo de Tena para el tratamiento de ficheros
from cl_sesion import Sesion
from cl_historial import Historial


#----CLASES----
class HomePage(Screen):
    
    def entrenar(self):

        self.manager.transition.direction = "left"

        self.manager.current = "table_screen"

class TableScreen(Screen):

    def obtener_fecha(self): return fecha_actual
    
    def color(self, serie, ejercicio): 
        
        return sesion.Cambiar_Color(serie,ejercicio)

    def done(self, serie, ejercicio, id):
    
        sesion.Cambiar_Valor(serie,ejercicio)
        
        self.ids[id].background_color = sesion.Cambiar_Color(serie,ejercicio)

    def resetear(self):      
        
        sesion.Todo_Cero()

        sesion.Guardar_Sesion(tabla_plantilla_path,sesion.tabla_plantilla)

        for i in serie_ejercicio:

            self.ids[i].background_color = color0

        self.ids.infor.text = ""
        
    def submit(self):

        if fecha_actual in historial.tabla_historial:

            self.ids.infor.text = "¡Ya has entrenado este día!"

        else:

            historial.Añadir_Nueva_Sesion(sesion.tabla_plantilla,fecha_actual)

            #print("sesion TABLA PLANTILLA: ", sesion.tabla_plantilla)
            
            historial.Guardar_Historial(tabla_historial_path,historial.tabla_historial)

            sesion.Todo_Cero()

            #print("HISTORIAL: ",historial.tabla_historial)

            #print("PORCENTAJE: ",historial.Porcentaje(fecha_actual))
            
            #print("Ultima fecha: ",max(historial.tabla_historial.keys()))

            #print("ULTIMA SESION: ",historial.tabla_historial[max(historial.tabla_historial.keys())])

            self.manager.transition.direction = "left"

            self.manager.current = "submitted_screen"

        #QUITAR ESTAS DOS LINEAS LUEGO ------- !!!!
        self.manager.transition.direction = "left"
        self.manager.current = "submitted_screen"

class SubmittedScreen(Screen):
    
    def volver_a_inicio(self):

        self.manager.transition.direction = "right"

        self.manager.current = "home_page"

    def status(self):

        self.ids.porcentaje.text = historial.Porcentaje()

        return "hola"


class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):

        return RootWidget()

#----MAIN----
Builder.load_file('frontend.kv')

#paths
tabla_plantilla_path = "tabla_plantilla.json"
tabla_historial_path = "historial.json"

sesion = Sesion(tabla_plantilla_path)
historial = Historial(tabla_historial_path)

#variables globales
fecha_actual = datetime.now().strftime("%Y-%m-%d")

color0 = [0.1, 0.7, 1, 1]
color1 = [0.8, 0.2, 1, 1]

serie_ejercicio = ["serie_1_eje_1","serie_1_eje_2","serie_1_eje_3","serie_1_eje_4","serie_1_eje_5","serie_1_eje_6","serie_1_eje_7","serie_1_eje_8","serie_1_eje_9",
        "serie_2_eje_1","serie_2_eje_2","serie_2_eje_3","serie_2_eje_4","serie_2_eje_5","serie_2_eje_6","serie_2_eje_7","serie_2_eje_8","serie_2_eje_9",
        "serie_3_eje_1","serie_3_eje_2","serie_3_eje_3","serie_3_eje_4","serie_3_eje_5","serie_3_eje_6","serie_3_eje_7","serie_3_eje_8","serie_3_eje_9"]

contador = {"1" : 0, "2" : 0, "3" : 0}
        
series_id = ["serie_1_stats","serie_2_stats","serie_3_stats"]



#se lanza la interfaz
if __name__ == '__main__':
    MainApp().run()