# Diccionarios para almacenar información
lista_estudiantes = {}  # Almacena estudiantes con formato {carnet: nombre}
lista_docentes = {}     # Almacena docentes con formato {carnet: nombre}
lista_cursos = {}       # Almacena cursos con formato {código: {"Nombre Curso": nombre, "Instructor": docente, "estudiantes": []}}


class Registrar:
    # Clase para registrar estudiantes y docentes en el sistema

    def registroEstudiante(self):
        # Registra un estudiante solicitando nombre y carnet
        # Almacena la información en el diccionario lista_estudiantes
        try:
            nombre = input("Ingrese su nombre y apellido: ")
            carnet = input("Ingrese su carnet: ")
            lista_estudiantes[carnet] = nombre
            print("Usuario registrado con éxito")
        except ValueError:
            print("Los valores ingresados no son correctos.")

    def registroDocente(self):
        # Registra un docente solicitando nombre y carnet
        # Almacena la información en el diccionario lista_docentes
        try:
            nombre = input("Ingrese su nombre y apellido: ")
            carnet = input("Ingrese su carnet: ")
            lista_docentes[carnet] = nombre
            print("Usuario registrado con éxito")
        except ValueError:
            print("Los valores ingresados son incorrectos")


class Cursos:
    # Clase para crear cursos, inscribir estudiantes y gestionar actividades

    def __init__(self):
        # Inicializa la lista de actividades del curso
        self.actividades = []

    def crear(self):
        # Crea un curso solicitando nombre, código y carnet del docente
        # Verifica que el curso y el docente existan antes de registrarlo
        try:
            nombre_curso = input("Ingrese el nombre del curso: ")
            código_curso = input("Ingrese el código del curso: ")
            carnet_docente = input("Ingrese el carnet del docente: ")

            if código_curso in lista_cursos:
                print("El curso ya existe")
                return

            if carnet_docente not in lista_docentes:
                print("El docente no está registrado")
                return

            lista_cursos[código_curso] = {
                "Nombre Curso": nombre_curso,
                "Instructor": lista_docentes[carnet_docente],
                "estudiantes": []
            }
            print(f"Curso '{nombre_curso}' creado exitosamente")
        except ValueError:
            print("Los datos ingresados no son válidos")

    def inscribir(self):
        # Inscribe un estudiante a un curso
        # Verifica que el estudiante y el curso existan
        # Evita inscribir al estudiante si ya está registrado en el curso
        carnet = input("Ingrese el carnet del estudiante: ")
        código_curso = input("Ingrese el código del curso: ")

        if carnet not in lista_estudiantes:
            print("El estudiante no está registrado")
            return

        if código_curso not in lista_cursos:
            print("El curso no existe")
            return

        if carnet in lista_cursos[código_curso]["estudiantes"]:
            print(f"{lista_estudiantes[carnet]} ya está inscrito en este curso")
        else:
            lista_cursos[código_curso]["estudiantes"].append(carnet)
            print(f"{lista_estudiantes[carnet]} inscrito en {lista_cursos[código_curso]['Nombre Curso']}")

    def agregar_actividad(self, actividad):
        # Agrega una actividad (Tarea o Evaluación) al curso
        self.actividades.append(actividad)

    def listar_actividades(self):
        # Lista todas las actividades registradas en el curso
        if not self.actividades:
            print("No hay actividades registradas")
        else:
            for act in self.actividades:
                act.mostrar_info()


class Actividad:
    # Clase base para representar una actividad de un curso

    def __init__(self, titulo, fecha):
        # Inicializa la actividad con un título y fecha
        self.titulo = titulo
        self.fecha = fecha

    def mostrar_info(self):
        # Devuelve la información básica de la actividad
        return f"{self.titulo} - {self.fecha}"


class Tarea(Actividad):
    # Subclase de Actividad que representa una tarea con descripción

    def __init__(self, titulo, fecha, descripción):
        # Inicializa la tarea con título, fecha y descripción
        super().__init__(titulo, fecha)
        self.descripción = descripción

    def mostrar_info(self):
        # Muestra la información completa de la tarea
        print(f"Tarea: {self.titulo}")
        print(f"Fecha: {self.fecha}")
        print(f"Descripción: {self.descripción}")


class Evaluación(Actividad):
    # Subclase de Actividad que representa una evaluación con puntaje

    def __init__(self, titulo, fecha, puntaje):
        # Inicializa la evaluación con título, fecha y puntaje máximo
        super().__init__(titulo, fecha)
        self.puntaje = puntaje

    def mostrar_info(self):
        # Muestra la información completa de la evaluación
        print(f"Evaluación: {self.titulo}")
        print(f"Fecha: {self.fecha}")
        print(f"Puntaje: {self.puntaje}")

class Estudiante:
    #  Clase que representa a un estudiante con registro de calificaciones por curso. Permite agregar notas y calcular promedios
    def __init__(self, nombre):
     self.nombre = nombre
     self. calificaciones =  {} ## Estructura: {curso: {evaluacion: nota}}
    def registrar_nota (self, curso, evaluacion, nota):
       if curso not in self.calificaciones:
          self.calificaciones[curso] ={}
          self.calificaciones[curso][evaluacion]=nota
#Funcion promedio
    def promedio_curso(self, curso): #Calcular el promedio de odas las notas de un curso.
     # Args: curso (str): Nombre dell curso
     # None: si no hay calificaciones para el curso 
     if curso in self.calificaciones and self.calificaciones[curso]:
        notas = self.calificaciones[curso ].values()
        return  sum(notas) / len (notas)
     return None

 # funcion de promedio general
    def promedio_general(self):
       if not self.calificaciones:
          return 0 # si no cuenta con cursos o con un promediode 0
       total= sum(self.promedio_curso(curso) for curso in self.calificaciones)
       return total / len (self.calificaciones)

# clase Sitema Academico para  consultar el promedio del estudiante y su rendimiento

class SistemaAcademico:
    #Clase que gestiona un sistema académico básico.
    #Permite registrar estudiantes, listarlos, consultar calificaciones  por curso y generar reportes de promedios.
    def __init__(self):
          self.estudiantes = []

#Funcion para agregar a un estudiante
    def agregar_estudiante(self, estudiante): 
            #Agrega un estudiante al sistema académico
            # Args: estudiante. objeto de la clase estudiante que sera agregado  
            self.estudiantes.append(estudiante)

    #Funcion que devuelve una lista de estudiantes 
    def listar_estudiantes(self): 
            #Devuelve una lista con los nombres de los estudiantes registrados 
            return [est.nombre for est in self.estudiantes]
    #Funcion para consultar al estudiante y su respectivo promedio

    def consultar_curso(self, curso):
        """Devuelve las evaluaciones y calificaciones de todos los estudiantes en un curso"""
        #Args: Curso nombre del curso a consultar
        resultado = {}
        for estudiante in self.estudiantes:
            if curso in estudiante.calificaciones:
                resultado[estudiante.nombre] = estudiante.calificaciones[curso]
        return resultado # diccionario con la estructura.

   # funcion para reporte de promedios
    def reporte_promedios(self, promedio_bajo=70):
        """Genera un reporte simple con promedios y alerta de promedio bajo"""
        #Args. list[dict]: Lista de diccionarios con la informacion por estudiante 
        reporte = []
        for estudiante in self.estudiantes:
            promedio = estudiante.promedio_general()
            alerta  = promedio < promedio_bajo
            reporte.append({
                'nombre': estudiante.nombre,
                'promedio': promedio,
                'promedio_bajo': alerta 
            })
        return reporte
