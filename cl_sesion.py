from archivos import * 

class Sesion():

    def __init__(self,path):

        self.tabla_plantilla = leer_archivo(path)

    def Guardar_Sesion(self,path,archivo):

        escribir_archivo(path,archivo)


    def Todo_Cero(self):

        for serie in self.tabla_plantilla:

            for ejercicio in self.tabla_plantilla[serie]:

                self.tabla_plantilla[serie][ejercicio] = 0
    
    def Cambiar_Valor(self,serie,ejercicio):

        if self.tabla_plantilla[serie][ejercicio] == 1:

            self.tabla_plantilla[serie][ejercicio] = 0 #Undone
            
        else:

            self.tabla_plantilla[serie][ejercicio] = 1 #Done
    
    def Cambiar_Color(self,serie,ejercicio):

        color0 = [0.1, 0.7, 1, 1]

        color1 = [0.8, 0.2, 1, 1]

        if self.tabla_plantilla[serie][ejercicio] == 1:

            return color1

        else:

            return color0
    
    def Series_Count(self):

        return [serie for serie in self.tabla_plantilla]
        

