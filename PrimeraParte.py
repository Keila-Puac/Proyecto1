#Inicio 

#Registrar Usuarios 

#Registrar Estudiantes y Profesores 

lista_estudiantes = {}
lista_docentes = {}
lista_cursos = {}
#lista_cursos = {"Código Curso":{"Nombre Curso":"Instructor"}}

class Registrar:
    def __init__(self, nombre, carnet):
        self.__nombre = nombre
        self.__carnet = carnet

    def registroEstudiante(self):
        try:
            self.__nombre = input("Ingrese su nombre y apellido: ")
            self.__carnet = input("Ingrese su carnet: ")
            lista_estudiantes[self.__carnet] = self.__nombre
            print("Usuario Registrado con éxito")
        except ValueError:
            print("Los valores ingresados no son correctos.")

    def registroDocente(self):
        try:
            self.__nombre = input("Ingrese su nombre y apellido: ")
            self.__carnet = input("Ingrese su carnet: ")
            lista_docentes[self.__carnet] = self.__nombre
            print("Usuario Registrado con éxito")

            
        except ValueError:
            print("Los valores ingresados son incorrectos")


#Inscribir a estudiantes en cursos

class Cursos:
    def __init__(self, nombre_curso, código_curso, instructor):
        self.__nombre_curso = nombre_curso
        self.__código_curso = código_curso
        self.__instructor = instructor

    def Crear(self):
        try:
            self.__nombre_curso = input("Ingrese el nombre del curso: ")
            self.__código_curso = input("Ingrese el código del curso: ")
            self.__instructor = input("Ingrese el nombre del instructor/docente: ")
            
            if self.__instructor in lista_docentes:
                lista_cursos[self.__código_curso] = {
                    "Nombre curso": self.__nombre_curso,
                    "Instructor": lista_docentes[self.__instructor]
                }
                print("Curso creado exitosamente")
                print(lista_cursos)
            else:
                print("El docente no esta registrado")


        except ValueError:
            print("Los datos ingresados no son validos")


        

Curso1 = Cursos("", "", "")
Curso1.Crear()