class Usuario:
    """Clase base para todos los usuarios del sistema"""
    def __init__(self, nombre, carnet):
        # Atributos comunes a todos los usuarios
        self.nombre = nombre
        self.carnet = carnet


class Estudiante(Usuario):
    """Subclase que representa a un estudiante"""
    def __init__(self, nombre, carnet):
        super().__init__(nombre, carnet)
        # Diccionario para almacenar las calificaciones
        # Estructura: {codigo_curso: {titulo_evaluacion: nota}}
        self.calificaciones = {}

    def registrar_nota(self, curso_codigo, evaluacion_titulo, nota, *args, **kwargs):
        """
        Registra o actualiza la nota de un estudiante en un curso específico.
        *args y **kwargs permiten flexibilidad, por ejemplo:
        registrar_nota("MAT101", "Parcial 1", 85, comentario="Bien hecho")
        """
        try:
            if not isinstance(nota, (int, float)):
                raise ValueError("La nota debe ser numérica.")

            if curso_codigo not in self.calificaciones:
                self.calificaciones[curso_codigo] = {}

            self.calificaciones[curso_codigo][evaluacion_titulo] = {
                "nota": nota,
                "extra": kwargs  # Guarda información extra opcional
            }
        except Exception as e:
            print(f"Error al registrar la nota: {e}")

    def promedio_curso(self, curso_codigo):
        """Calcula el promedio de un curso específico"""
        try:
            if curso_codigo in self.calificaciones and self.calificaciones[curso_codigo]:
                notas = [data["nota"] for data in self.calificaciones[curso_codigo].values()]
                return sum(notas) / len(notas)
            return None
        except Exception as e:
            print(f"Error al calcular promedio del curso {curso_codigo}: {e}")
            return None

    def promedio_general(self):
        """Calcula el promedio general de todas las asignaturas"""
        try:
            if not self.calificaciones:
                return 0
            total = sum(
                self.promedio_curso(curso)
                for curso in self.calificaciones
                if self.promedio_curso(curso) is not None
            )
            return total / len(self.calificaciones)
        except Exception as e:
            print(f"Error al calcular promedio general: {e}")
            return 0


class Instructor(Usuario):
    """Subclase que representa a un instructor"""
    def __init__(self, nombre, carnet):
        super().__init__(nombre, carnet)
        # Lista de cursos que imparte el instructor
        self.cursos = []

class Actividad:
    """Clase base para actividades de un curso"""
    def __init__(self, titulo, fecha):
        self.titulo = titulo
        self.fecha = fecha

    def mostrar_info(self):
        return f"{self.titulo} - {self.fecha}"


class Tarea(Actividad):
    """Subclase que representa una tarea"""
    def __init__(self, titulo, fecha, descripcion):
        super().__init__(titulo, fecha)
        self.descripcion = descripcion

    def mostrar_info(self):
        print(f"Tarea: {self.titulo}\nFecha: {self.fecha}\nDescripción: {self.descripcion}")


class Evaluacion(Actividad):
    """Subclase que representa una evaluación"""
    def __init__(self, titulo, fecha, puntaje):
        super().__init__(titulo, fecha)
        self.puntaje = puntaje

    def mostrar_info(self):
        print(f"Evaluación: {self.titulo}\nFecha: {self.fecha}\nPuntaje: {self.puntaje}")


class Curso:
    """Clase que representa un curso"""
    def __init__(self, nombre, codigo, instructor: Instructor):
        self.nombre = nombre
        self.codigo = codigo
        self.instructor = instructor
        self.estudiantes = {}   # {carnet: Estudiante}
        self.actividades = []   # Lista de actividades

        instructor.cursos.append(codigo)

    def inscribir_estudiante(self, estudiante: Estudiante):
        """Agrega un estudiante al curso"""
        try:
            if estudiante.carnet not in self.estudiantes:
                self.estudiantes[estudiante.carnet] = estudiante
                print(f"{estudiante.nombre} inscrito en {self.nombre}")
            else:
                print(f"{estudiante.nombre} ya está inscrito en {self.nombre}")
        except Exception as e:
            print(f"Error al inscribir estudiante: {e}")

    def agregar_actividad(self, actividad: Actividad):
        """Agrega una actividad (tarea o evaluación)"""
        try:
            self.actividades.append(actividad)
        except Exception as e:
            print(f"Error al agregar actividad: {e}")

    def listar_actividades(self):
        """Lista todas las actividades registradas"""
        try:
            if not self.actividades:
                print("No hay actividades registradas")
            else:
                for act in self.actividades:
                    act.mostrar_info()
        except Exception as e:
            print(f"Error al listar actividades: {e}")
            
class SistemaAcademico:
    """Clase que gestiona todo el sistema académico"""
    def __init__(self):
        self.usuarios = {}  # {carnet: Usuario}
        self.cursos = {}    # {codigo: Curso}

    # --------- Registro de usuarios ---------
    def registrar_usuario(self, tipo, *args, **kwargs):
        """
        Registra un nuevo usuario (estudiante o instructor).
        Uso flexible gracias a *args y **kwargs:
        registrar_usuario("estudiante", "Ana", "2025001")
        registrar_usuario("instructor", nombre="Carlos", carnet="INS101")
        """
        try:
            nombre = kwargs.get("nombre", args[0] if args else None)
            carnet = kwargs.get("carnet", args[1] if len(args) > 1 else None)

            if carnet in self.usuarios:
                print(f"El carnet {carnet} ya está registrado.")
                return None

            if tipo.lower() == "estudiante":
                usuario = Estudiante(nombre, carnet)
            elif tipo.lower() == "instructor":
                usuario = Instructor(nombre, carnet)
            else:
                raise ValueError("Tipo de usuario no válido.")

            self.usuarios[carnet] = usuario
            print(f"{tipo.title()} {nombre} registrado con éxito")
            return usuario
        except Exception as e:
            print(f"Error al registrar usuario: {e}")
            return None

    # --------- Gestión de cursos ---------
    def crear_curso(self, nombre, codigo, carnet_instructor, **kwargs):
        """Crea un curso nuevo y lo asocia a un instructor"""
        try:
            if codigo in self.cursos:
                raise ValueError("El curso ya existe.")

            if carnet_instructor not in self.usuarios or not isinstance(self.usuarios[carnet_instructor], Instructor):
                raise ValueError("Instructor no registrado.")

            curso = Curso(nombre, codigo, self.usuarios[carnet_instructor])
            self.cursos[codigo] = curso
            print(f"Curso '{nombre}' creado con éxito")
            return curso
        except Exception as e:
            print(f"Error al crear curso: {e}")
            return None

    # --------- Reportes ---------
    def reporte_promedios(self, promedio_bajo=70):
        """Genera un reporte de promedios de todos los estudiantes y alerta si es bajo"""
        try:
            reporte = []
            for usuario in self.usuarios.values():
                if isinstance(usuario, Estudiante):
                    promedio = usuario.promedio_general()
                    alerta = promedio < promedio_bajo
                    reporte.append({
                        "nombre": usuario.nombre,
                        "promedio": promedio,
                        "promedio_bajo": alerta
                    })
            return reporte
        except Exception as e:
            print(f"Error al generar reporte de promedios: {e}")
            return []

