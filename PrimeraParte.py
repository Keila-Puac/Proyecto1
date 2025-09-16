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
