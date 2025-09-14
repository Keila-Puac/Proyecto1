#Inicio 

#Registrar Usuarios 

#Registrar Estudiantes y Profesores 

diccionario_usuarios =  {"Nombre":"carnet"}
lista_estudiantes = {}
lista_docentes = {}


class Registrar:
    def __init__(self, nombre, carnet):
        self.__nombre = nombre
        self.__carnet = carnet

    def registroEstudiante(self):
        try:
            self.__nombre = input("Ingrese su nombre y apellido")
            self.__carnet = input("Ingrese su carnet")
            lista_estudiantes[self.__carnet] = self.__nombre
            print(lista_estudiantes)
        except ValueError:
            print("Los valores ingresados no son correctos.")

    def registroDocente(self):
        try:
            self.__nombre = input("Ingrese su nombre y apellido")
            self.__carnet = input("Ingrese su carnet")

            
        except ValueError:
            print("Los valores ingresados son incorrectos")


usuario1 = Registrar("Paula", "12548")
usuario1.registroEstudiante()

