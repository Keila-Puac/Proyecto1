class Usuario:
    """Clase base para todos los usuarios del sistema"""
    def __init__(self, nombre, carnet):
        # Atributos comunes a todos los usuarios
        self.nombre = nombre
        self.carnet = carnet


class Estudiante(Usuario):
    """Subclase que representa a un estudiante"""
    def __init__(self, nombre, carnet):
        # Llamada al constructor de la clase base Usuario
        super().__init__(nombre, carnet)
        # Diccionario para almacenar las calificaciones
        # Estructura: {codigo_curso: {titulo_evaluacion: nota}}
        self.calificaciones = {}

    def registrar_nota(self, curso_codigo, evaluacion_titulo, nota):
        """Registra o actualiza la nota de un estudiante en un curso específico"""
        if curso_codigo not in self.calificaciones:
            self.calificaciones[curso_codigo] = {}  # Crear registro si no existe
        self.calificaciones[curso_codigo][evaluacion_titulo] = nota  # Guardar nota

    def promedio_curso(self, curso_codigo):
        """Calcula el promedio de un curso específico"""
        if curso_codigo in self.calificaciones and self.calificaciones[curso_codigo]:
            notas = self.calificaciones[curso_codigo].values()
            return sum(notas) / len(notas)  # Promedio simple
        return None  # Retorna None si no hay notas

    def promedio_general(self):
        """Calcula el promedio general de todas las asignaturas"""
        if not self.calificaciones:
            return 0  # Retorna 0 si no tiene cursos registrados
        total = sum(
            self.promedio_curso(curso)
            for curso in self.calificaciones
            if self.promedio_curso(curso) is not None
        )
        return total / len(self.calificaciones)  # Promedio general


class Instructor(Usuario):
    """Subclase que representa a un instructor"""
    def __init__(self, nombre, carnet):
        super().__init__(nombre, carnet)
        # Lista de cursos que imparte el instructor
        self.cursos = []







# ========================
# CURSOS Y ACTIVIDADES
# ========================
class Actividad:
    """Clase base para actividades de un curso"""
    def __init__(self, titulo, fecha):
        self.titulo = titulo  # Nombre de la actividad
        self.fecha = fecha    # Fecha de entrega o realización

    def mostrar_info(self):
        # Retorna información básica de la actividad
        return f"{self.titulo} - {self.fecha}"


class Tarea(Actividad):
    """Subclase que representa una tarea"""
    def __init__(self, titulo, fecha, descripcion):
        super().__init__(titulo, fecha)
        self.descripcion = descripcion  # Información adicional específica de la tarea

    def mostrar_info(self):
        # Muestra información detallada de la tarea
        print(f"Tarea: {self.titulo}\nFecha: {self.fecha}\nDescripción: {self.descripcion}")


class Evaluacion(Actividad):
    """Subclase que representa una evaluación"""
    def __init__(self, titulo, fecha, puntaje):
        super().__init__(titulo, fecha)
        self.puntaje = puntaje  # Puntaje máximo de la evaluación

    def mostrar_info(self):
        # Muestra información detallada de la evaluación
        print(f"Evaluación: {self.titulo}\nFecha: {self.fecha}\nPuntaje: {self.puntaje}")


class Curso:
    """Clase que representa un curso"""
    def __init__(self, nombre, codigo, instructor: Instructor):
        self.nombre = nombre          # Nombre del curso
        self.codigo = codigo          # Código único del curso
        self.instructor = instructor  # Instructor que imparte el curso
        self.estudiantes = {}         # Diccionario de estudiantes {carnet: Estudiante}
        self.actividades = []         # Lista de tareas y evaluaciones

        # Agrega automáticamente el curso a la lista de cursos del instructor
        instructor.cursos.append(codigo)

    def inscribir_estudiante(self, estudiante: Estudiante):
        """Agrega un estudiante al curso"""
        if estudiante.carnet not in self.estudiantes:
            self.estudiantes[estudiante.carnet] = estudiante
            print(f"{estudiante.nombre} inscrito en {self.nombre}")
        else:
            print(f"{estudiante.nombre} ya está inscrito en {self.nombre}")

    def agregar_actividad(self, actividad: Actividad):
        """Agrega una tarea o evaluación al curso"""
        self.actividades.append(actividad)

    def listar_actividades(self):
        """Imprime todas las actividades del curso"""
        if not self.actividades:
            print("No hay actividades registradas")
        else:
            for act in self.actividades:
                act.mostrar_info()







# ========================
# SISTEMA ACADÉMICO
# ========================
class SistemaAcademico:
    """Clase que gestiona todo el sistema académico"""
    def __init__(self):
        # Diccionarios para manejar usuarios y cursos por su identificador
        self.usuarios = {}  # {carnet: Usuario}
        self.cursos = {}    # {codigo: Curso}

    # --------- Registro de usuarios ---------
    def registrar_usuario(self, tipo, nombre, carnet):
        """Registra un nuevo usuario (estudiante o instructor)"""
        if carnet in self.usuarios:
            print(f"El carnet {carnet} ya está registrado.")
            return None

        # Determina el tipo de usuario
        if tipo.lower() == "estudiante":
            usuario = Estudiante(nombre, carnet)
        elif tipo.lower() == "instructor":
            usuario = Instructor(nombre, carnet)
        else:
            print("Tipo de usuario no válido")
            return None

        # Guardar usuario en el diccionario
        self.usuarios[carnet] = usuario
        print(f"{tipo.title()} {nombre} registrado con éxito")
        return usuario

    # --------- Gestión de cursos ---------
    def crear_curso(self, nombre, codigo, carnet_instructor):
        """Crea un curso nuevo y lo asocia a un instructor"""
        if codigo in self.cursos:
            print("El curso ya existe")
            return None

        # Verifica que el instructor esté registrado
        if carnet_instructor not in self.usuarios or not isinstance(self.usuarios[carnet_instructor], Instructor):
            print("Instructor no registrado")
            return None

        # Crear y almacenar curso
        curso = Curso(nombre, codigo, self.usuarios[carnet_instructor])
        self.cursos[codigo] = curso
        print(f"Curso '{nombre}' creado con éxito")
        return curso

    # --------- Reportes ---------
    def reporte_promedios(self, promedio_bajo=70):
        """Genera un reporte de promedios de todos los estudiantes y alerta si es bajo"""
        reporte = []
        for usuario in self.usuarios.values():
            if isinstance(usuario, Estudiante):
                promedio = usuario.promedio_general()
                alerta = promedio < promedio_bajo  # Marca si el promedio es inferior al umbral
                reporte.append({
                    "nombre": usuario.nombre,
                    "promedio": promedio,
                    "promedio_bajo": alerta
                })
        return reporte

