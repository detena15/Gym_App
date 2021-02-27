#librerias
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout

from datetime import datetime
from pathlib import Path
import json, glob, random

from archivos import * #modulo creado por Eduardo de Tena para el tratamiento de ficheros
from cl_sesion import Sesion
from cl_historial import Historial
from cl_ejercicios import Ejercicios


#----CLASES----
class HomePage(Screen):
    
    def entrenar(self):

        self.manager.transition.direction = "left"

        self.manager.current = "table_screen"

class TableScreen(Screen):

    def obtener_fecha(self): return fecha_actual
    
    def color(self, serie, ejercicio): return sesion.Cambiar_Color(serie,ejercicio)

    #aqui envia a la tabla los valores Peso y Repes por cada Ejercicio
    
    def on_enter(self):

        #toma los nombres de losejercicios de ejercicios.json y los manda a sus labels
        for ejercicio in zip(ejercicios.Get_Ejercicios(),ejercicios_ids):

            self.ids[ejercicio[1]].text = str(ejercicio[0])
            

        #toma los valores de peso y repeticiones de ejercicios.json y los manda a sus labels
        for ejercicio in zip(ejercicios.Get_Ejercicios(),repes_ids):

            self.ids[ejercicio[1]].text = str(ejercicios.Get_Repes(ejercicio[0]))
        
        for ejercicio in zip(ejercicios.Get_Ejercicios(),pesos_ids):

            self.ids[ejercicio[1]].text = str(ejercicios.Get_Peso(ejercicio[0]))

    def done(self, serie, ejercicio, id):
    
        sesion.Cambiar_Valor(serie,ejercicio)
        
        self.ids[id].background_color = sesion.Cambiar_Color(serie,ejercicio)

    
    def volver(self):

        self.manager.transition.direction = "right"

        self.manager.current = "home_page"
        
    def submit(self):

        if fecha_actual in historial.tabla_historial:

            self.ids.infor.text = "¡Ya has entrenado este día!"

        else:

            historial.Añadir_Nueva_Sesion(sesion.tabla_plantilla,fecha_actual)
            
            historial.Guardar_Historial(tabla_historial_path,historial.tabla_historial)

            self.manager.transition.direction = "left"

            self.manager.current = "submitted_screen"

           
    def resetear(self):      
        
        sesion.Todo_Cero()

        sesion.Guardar_Sesion(tabla_plantilla_path,sesion.tabla_plantilla)

        for i in serie_ejercicio:

            self.ids[i].background_color = color0

        self.ids.infor.text = ""
    

    def ir_a_modificar(self,ejercicio):

        #guardo el ejercicio para saber cual voy a modificar en el widget ModificarEjercicio()
        ejercicios.Guardar_Ejercicio(ejercicio)

        self.manager.transition.direction = "left"

        self.manager.current = "modificar_ejercicio"

class SubmittedScreen(Screen):
    
    def volver_a_inicio(self):

        self.manager.transition.direction = "right"

        self.manager.current = "home_page"
    
    def on_enter(self):

        ratio = 0

        for serie in sesion.Series_Count():

            self.ids[serie].text = "Serie " + serie + " ---> " +str(historial.Ratio_Serie(serie)) + " / 9"
            
            ratio = ratio + historial.Ratio_Serie(serie)
        
        self.ids.ratio_sesion.text = "Sesión ---> " + str(ratio) + " / 27"

        self.ids.porcentaje.text = str(round(((ratio/27)*100),2)) + " %"


class ModificarEjercicio(Screen):
    
    def volver_a_sesion(self):

        self.manager.transition.direction = "right"

        self.manager.current = "table_screen"
    
    def modificar_valor(self):

        ejercicios.Modificar_Repes(ejercicios.ejercicio,int(self.ids.repes.text))
        
        ejercicios.Modificar_Peso(ejercicios.ejercicio,int(self.ids.peso.text))

        ejercicios.Guardar_Ejercicios(ejercicios_path,ejercicios.ejercicios)

        self.manager.transition.direction = "right"

        self.manager.current = "table_screen"
        


class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):

        return RootWidget()

#----MAIN----
Builder.load_file('frontend.kv')

#paths
ejercicios_path = "Files/ejercicios.json"
tabla_plantilla_path = "Files/tabla_plantilla.json"
tabla_historial_path = "Files/historial.json"

#creacion de los objetos
ejercicios = Ejercicios(ejercicios_path)
sesion = Sesion(tabla_plantilla_path)
historial = Historial(tabla_historial_path)

#variables globales
fecha_actual = datetime.now().strftime("%Y-%m-%d")

color0 = [0.1, 0.7, 1, 0.2]
color1 = [0.1, 0.7, 1, 1]

#ids de los elementos de frontend.kv
serie_ejercicio = ["serie_1_eje_1","serie_1_eje_2","serie_1_eje_3","serie_1_eje_4","serie_1_eje_5","serie_1_eje_6","serie_1_eje_7","serie_1_eje_8","serie_1_eje_9",
        "serie_2_eje_1","serie_2_eje_2","serie_2_eje_3","serie_2_eje_4","serie_2_eje_5","serie_2_eje_6","serie_2_eje_7","serie_2_eje_8","serie_2_eje_9",
        "serie_3_eje_1","serie_3_eje_2","serie_3_eje_3","serie_3_eje_4","serie_3_eje_5","serie_3_eje_6","serie_3_eje_7","serie_3_eje_8","serie_3_eje_9"]

ejercicios_ids = ["ejercicio_1","ejercicio_2","ejercicio_3",
                "ejercicio_4","ejercicio_5","ejercicio_6",
                "ejercicio_7","ejercicio_8","ejercicio_9",]

repes_ids = ["repes_1","repes_2","repes_3",
        "repes_4","repes_5","repes_6",
        "repes_7","repes_8","repes_9"]

pesos_ids = ["peso_1","peso_2","peso_3",
        "peso_4","peso_5","peso_6",
        "peso_7","peso_8","peso_9"]


#se lanza la interfaz
if __name__ == '__main__':
    MainApp().run()