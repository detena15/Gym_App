from archivos import *  

class Historial():

    def __init__(self,path):

        self.tabla_historial = leer_archivo(path)
    

    def Guardar_Historial(self,path,archivo):

        escribir_archivo(path,archivo)

    
    def Añadir_Nueva_Sesion(self,tabla_plantilla,fecha_actual):
        self.tabla_historial[fecha_actual] = tabla_plantilla
        #print("CLASE TABLA PLANTILLA: ",tabla_plantilla)
        #print("CLASE TABLA HISTORIAL: ",self.tabla_historial)

    
    def Porcentaje(self):
        
        #leo de nuevo el historial, ahora con la ultima sesion añadida
        tabla_historial = leer_archivo("historial.json")

        #selecciono el ultimo item añadido
        series = tabla_historial[max(tabla_historial.keys())]
        #series = hist[fecha]
        #print(fecha)
        #series = self.tabla_historial[fecha]
        
        contador = {"1" : 0, "2" : 0, "3" : 0}

        for serie in series:

            for ejercicio in series[serie]:

               contador[serie] = contador[serie] + series[serie][ejercicio]
        
        porcentaje = str(round(((contador["1"] + contador["2"] + contador["3"])/27)*100)) + " %"

        return porcentaje
