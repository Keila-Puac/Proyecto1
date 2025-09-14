#Inicio 

#Registrar Usuarios 

#Registrar Estudiantes y Profesores 

diccionario_usuarios =  {"Nombre":"carnet"}


class Registrar:
    def __init__(self, nombre, carnet):
        self.nombre = nombre
        self.carnet = carnet

        try:
            nombre_usuario = input("Ingrese su nombre")
            carnet_usuario = input("Ingrese su carnet")
        except ValueError:
            print("Los valores ingresados no son correctos.")

        

    