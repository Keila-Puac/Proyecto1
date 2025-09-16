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


#Cursos

class Cursos:
    def __init__(self, nombre_curso, código_curso, instructor):
        self.__nombre_curso = nombre_curso
        self.__código_curso = código_curso
        self.__instructor = instructor
        self.actividades = []

    def Crear(self):
        try:
            self.__nombre_curso = input("Ingrese el nombre del curso: ")
            self.__código_curso = input("Ingrese el código del curso: ")
            self.__instructor = input("Ingrese el carnet del instructor/docente: ")

            if self.__código_curso in lista_cursos:
                return "El curso ya existe"
            
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

#Inscribir estudiantes a cursos
    def Inscribir(self):
        try:
            carnet = input("Ingrese el carnet del estudiante: ")
            código = input("Ingrese el código del curso: ")

            if carnet not in lista_estudiantes:
                print("El estudiante no esta registrado.")

            if código not in lista_cursos:
                print("El curso no existe.")

            if "estudiantes" not in lista_cursos[código]:
                lista_cursos[código]["estudiantes"].append(carnet)
                print(f"{lista_estudiantes[carnet]} fue inscrito en {lista_cursos[código]["Nombre Curso"]}")

        except ValueError:
            print("Los datos ingresados no son validos")

    def agregar_actividad(self, actividad):
        self.actividades.append(actividad)

    def listar_actividades(self):
        if not self.actividades:
            print("No hay actividades registradas.")
        else:
            for act in self.actividades:
                print(act.mostrar_info())


class Actividad:
    def __init__(self, titulo, fecha):
        self.titulo = titulo
        self.fecha = fecha

    def mostrar_info(self):
        return f"{self.titulo} - {self.fecha}"
    
class Tarea(Actividad):
    def __init__(self, titulo, fecha, descripción):
        super().__init__(titulo, fecha)
        self.descripción = descripción

    def mostrar_info(self):
        print (f"Tarea: {self.titulo}")
        print (f"Fecha: {self.fecha}")
        print (f"Descripción:  {self.descripción}")

class Evaluacion(Actividad):
    def __init__(self, titulo, fecha, puntaje):
        super().__init__(titulo, fecha)
        self.puntaje = puntaje

    def mostrar_info(self):
        print(f"Evaluacion: {self.titulo}")
        print("Fecha: {self.fecha}")
        print("Puntaje: {self.puntaje}")
    