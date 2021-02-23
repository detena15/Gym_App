from archivos import *

class Ejercicios():

    def __init__(self,path): 
        self.ejercicios = leer_archivo(path)


    def Guardar_Ejercicios(self,path,archivo):  
        escribir_archivo(path,archivo)


    def Guardar_Ejercicio(self,ejercicio):
        self.ejercicio = ejercicio


    def Get_Repes(self,ejercicio):
        return self.ejercicios[ejercicio]["Repeticiones"]


    def Get_Peso(self,ejercicio):
        return self.ejercicios[ejercicio]["Peso"]
    

    def Get_Ejercicio(self,ejercicio):
        return self.ejercicios[ejercicio]


    def Get_Ejercicios(self):
        return [ejercicio for ejercicio in self.ejercicios]


    def Modificar_Repes(self,ejercicio,repes):    
        self.ejercicios[ejercicio]["Repeticiones"] = repes


    def Modificar_Peso(self,ejercicio,peso):       
        self.ejercicios[ejercicio]["Peso"] = peso
    

    

    
    

    
    
