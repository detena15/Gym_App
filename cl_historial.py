from archivos import *

class Historial():

    def __init__(self,path):

        self.tabla_historial = leer_archivo(path)
    

    def Guardar_Historial(self,path,archivo):

        escribir_archivo(path,archivo)


    def Añadir_Nueva_Sesion(self,tabla_plantilla,fecha_actual):

        self.tabla_historial[fecha_actual] = tabla_plantilla
        
    
    def Ratio_Serie(self,serie):

        contador = 0

        self.serie = self.tabla_historial[max(self.tabla_historial.keys())][serie]

        for ejercicio in self.serie:
            
            contador = contador + self.serie[ejercicio]
        
        return contador
    
    def Fechas_Hist(self):

        return [fecha for fecha in self.tabla_historial]
        
        


    