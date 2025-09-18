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
