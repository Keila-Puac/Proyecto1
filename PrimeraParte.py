class Usuario:
    """
    Clase base para todos los usuarios del sistema académico.

    Atributos:
        nombre (str): Nombre del usuario.
        carnet (str): Identificador único del usuario.
    """
    def __init__(self, nombre, carnet):
        self.nombre = nombre
        self.carnet = carnet


class Estudiante(Usuario):
    """
    Representa a un estudiante dentro del sistema.

    Atributos:
        calificaciones (dict): Estructura que almacena las notas de cada curso.
                               {codigo_curso: {titulo_evaluacion: {"nota": valor, "extra": info}}}
    """
    def __init__(self, nombre, carnet):
        super().__init__(nombre, carnet)
        self.calificaciones = {}

    def registrar_nota(self, curso_codigo, evaluacion_titulo, nota, *args, **kwargs):
        """
        Registra o actualiza la nota de un estudiante en un curso específico.

        Args:
            curso_codigo (str): Código del curso.
            evaluacion_titulo (str): Nombre de la evaluación (ej. "Parcial 1").
            nota (int/float): Nota obtenida.
            *args: Argumentos adicionales (no obligatorios).
            **kwargs: Información extra (ejemplo: comentario="Buen trabajo").
        """
        try:
            if not isinstance(nota, (int, float)):
                raise ValueError("La nota debe ser numérica.")

            if curso_codigo not in self.calificaciones:
                self.calificaciones[curso_codigo] = {}

            self.calificaciones[curso_codigo][evaluacion_titulo] = {
                "nota": nota,
                "extra": kwargs
            }
        except Exception as e:
            print(f"Error al registrar la nota: {e}")

    def promedio_curso(self, curso_codigo):
        """
        Calcula el promedio de un curso específico.

        Args:
            curso_codigo (str): Código del curso.

        Returns:
            float | None: Promedio del curso o None si no hay notas.
        """
        try:
            if curso_codigo in self.calificaciones and self.calificaciones[curso_codigo]:
                notas = [data["nota"] for data in self.calificaciones[curso_codigo].values()]
                return sum(notas) / len(notas)
            return None
        except Exception as e:
            print(f"Error al calcular promedio del curso {curso_codigo}: {e}")
            return None

    def promedio_general(self):
        """
        Calcula el promedio general del estudiante en todos los cursos.

        Returns:
            float: Promedio general (0 si no hay calificaciones).
        """
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
    """
    Representa a un instructor del sistema.

    Atributos:
        cursos (list): Lista de códigos de cursos que imparte.
    """
    def __init__(self, nombre, carnet):
        super().__init__(nombre, carnet)
        self.cursos = []


class Actividad:
    """
    Clase base para actividades de un curso (ejemplo: Tarea, Evaluación).

    Atributos:
        titulo (str): Nombre de la actividad.
        fecha (str): Fecha de entrega/realización.
    """
    def __init__(self, titulo, fecha):
        self.titulo = titulo
        self.fecha = fecha

    def mostrar_info(self):
        """Devuelve una cadena con la información de la actividad."""
        return f"{self.titulo} - {self.fecha}"


class Tarea(Actividad):
    """
    Representa una tarea asignada a un curso.

    Atributos:
        descripcion (str): Detalle de la tarea.
    """
    def __init__(self, titulo, fecha, descripcion):
        super().__init__(titulo, fecha)
        self.descripcion = descripcion

    def mostrar_info(self):
        print(f"Tarea: {self.titulo}\nFecha: {self.fecha}\nDescripción: {self.descripcion}")


class Evaluacion(Actividad):
    """
    Representa una evaluación de un curso (ejemplo: examen, parcial).

    Atributos:
        puntaje (int/float): Valor total de la evaluación.
    """
    def __init__(self, titulo, fecha, puntaje):
        super().__init__(titulo, fecha)
        self.puntaje = puntaje

    def mostrar_info(self):
        print(f"Evaluación: {self.titulo}\nFecha: {self.fecha}\nPuntaje: {self.puntaje}")


class Curso:
    """
    Representa un curso dentro del sistema.

    Atributos:
        nombre (str): Nombre del curso.
        codigo (str): Código único del curso.
        instructor (Instructor): Instructor asignado.
        estudiantes (dict): Estudiantes inscritos {carnet: Estudiante}.
        actividades (list): Lista de actividades del curso.
    """
    def __init__(self, nombre, codigo, instructor: Instructor):
        self.nombre = nombre
        self.codigo = codigo
        self.instructor = instructor
        self.estudiantes = {}
        self.actividades = []

        instructor.cursos.append(codigo)

    def inscribir_estudiante(self, estudiante: Estudiante):
        """
        Inscribe un estudiante en el curso.

        Args:
            estudiante (Estudiante): Objeto estudiante a inscribir.
        """
        try:
            if estudiante.carnet not in self.estudiantes:
                self.estudiantes[estudiante.carnet] = estudiante
                print(f"{estudiante.nombre} inscrito en {self.nombre}")
            else:
                print(f"{estudiante.nombre} ya está inscrito en {self.nombre}")
        except Exception as e:
            print(f"Error al inscribir estudiante: {e}")

    def agregar_actividad(self, actividad: Actividad):
        """
        Agrega una actividad (Tarea o Evaluación) al curso.

        Args:
            actividad (Actividad): Objeto de tipo Tarea o Evaluacion.
        """
        try:
            self.actividades.append(actividad)
        except Exception as e:
            print(f"Error al agregar actividad: {e}")

    def listar_actividades(self):
        """Muestra todas las actividades registradas del curso."""
        try:
            if not self.actividades:
                print("No hay actividades registradas")
            else:
                for act in self.actividades:
                    act.mostrar_info()
        except Exception as e:
            print(f"Error al listar actividades: {e}")


class SistemaAcademico:
    """
    Clase principal que gestiona el sistema académico completo.

    Atributos:
        usuarios (dict): Diccionario de usuarios registrados {carnet: Usuario}.
        cursos (dict): Diccionario de cursos {codigo: Curso}.
    """
    def __init__(self):
        self.usuarios = {}
        self.cursos = {}

    # --------- Registro de usuarios ---------
    def registrar_usuario(self, tipo, *args, **kwargs):
        """
        Registra un nuevo usuario en el sistema.

        Args:
            tipo (str): "estudiante" o "instructor".
            *args: Argumentos posicionales (ejemplo: nombre, carnet).
            **kwargs: Argumentos con nombre (ejemplo: nombre="Ana", carnet="2025001").

        Returns:
            Usuario | None: El objeto creado o None si hay error.
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
        """
        Crea un curso nuevo y lo asigna a un instructor.

        Args:
            nombre (str): Nombre del curso.
            codigo (str): Código único del curso.
            carnet_instructor (str): Carnet del instructor.

        Returns:
            Curso | None: El curso creado o None si hay error.
        """
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
        """
        Genera un reporte de promedios de todos los estudiantes.

        Args:
            promedio_bajo (int): Umbral mínimo para considerar bajo rendimiento.

        Returns:
            list[dict]: Lista con reportes de estudiantes:
                        {"nombre": str, "promedio": float, "promedio_bajo": bool}
        """
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

def menu_inicio(sistema: SistemaAcademico):
    usuario_actual = None

    while not usuario_actual:
        print("\n=== INICIO DE SESIÓN ===")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo = input("Tipo (estudiante/instructor): ").strip().lower()
            nombre = input("Nombre: ")
            carnet = input("Carnet: ")
            usuario = sistema.registrar_usuario(tipo, nombre=nombre, carnet=carnet)
            if usuario:
                print("Registro exitoso. Ahora puede iniciar sesión.")
        elif opcion == "2":
            carnet = input("Ingrese su carnet: ")
            usuario_actual = sistema.usuarios.get(carnet)
            if not usuario_actual:
                print("Usuario no encontrado, regístrese primero.")
                usuario_actual = None
        elif opcion == "0":
            print("Saliendo...")
            exit()
        else:
            print("Opción inválida.")

    return usuario_actual


def menu_academico(sistema: SistemaAcademico, usuario_actual: Usuario):
    while True:
        print(f"\n=== MENÚ ACADÉMICO ({usuario_actual.nombre}) ===")
        print("1. Ver cursos disponibles")
        if isinstance(usuario_actual, Instructor):
            print("2. Crear curso")
            print("3. Inscribir estudiante en curso")
            print("4. Crear tarea/evaluación")
            print("5. Registrar calificación")
        elif isinstance(usuario_actual, Estudiante):
            print("2. Ver mis cursos inscritos")
            print("3. Ver mis calificaciones")
        print("6. Generar reporte de promedios")
        print("9. Cerrar sesión")

        opcion = input("Seleccione: ")

        # --- Opciones comunes ---
        if opcion == "1":
            for curso in sistema.cursos.values():
                print(f"{curso.codigo} - {curso.nombre} (Instructor: {curso.instructor.nombre})")

        elif opcion == "6":
            reporte = sistema.reporte_promedios()
            for r in reporte:
                estado = "Bajo rendimiento" if r["promedio_bajo"] else "Aceptable"
                print(f"{r['nombre']} - Promedio: {r['promedio']:.2f} {estado}")

        elif opcion == "9":
            print("Cerrando sesión...")
            break

        # --- Opciones de instructor ---
        elif isinstance(usuario_actual, Instructor):
            if opcion == "2":
                nombre = input("Nombre del curso: ")
                codigo = input("Código del curso: ")
                sistema.crear_curso(nombre, codigo, usuario_actual.carnet)

            elif opcion == "3":
                codigo = input("Código del curso: ")
                carnet_est = input("Carnet del estudiante: ")
                curso = sistema.cursos.get(codigo)
                estudiante = sistema.usuarios.get(carnet_est)
                if curso and isinstance(estudiante, Estudiante):
                    curso.inscribir_estudiante(estudiante)
                else:
                    print("Error: curso o estudiante no encontrado.")

            elif opcion == "4":
                codigo = input("Código del curso: ")
                curso = sistema.cursos.get(codigo)
                if not curso:
                    print("Curso no encontrado.")
                    continue

                tipo = input("¿Desea crear (tarea/evaluacion)? ").strip().lower()
                titulo = input("Título: ")
                fecha = input("Fecha (dd/mm/aaaa): ")

                if tipo == "tarea":
                    descripcion = input("Descripción: ")
                    tarea = Tarea(titulo, fecha, descripcion)
                    curso.agregar_actividad(tarea)
                elif tipo == "evaluacion":
                    puntaje = float(input("Puntaje total: "))
                    evaluacion = Evaluacion(titulo, fecha, puntaje)
                    curso.agregar_actividad(evaluacion)
                else:
                    print("Opción inválida.")

            elif opcion == "5":
                carnet_est = input("Carnet del estudiante: ")
                codigo = input("Código del curso: ")
                titulo = input("Título de la evaluación: ")
                nota = float(input("Nota obtenida: "))

                estudiante = sistema.usuarios.get(carnet_est)
                if isinstance(estudiante, Estudiante):
                    estudiante.registrar_nota(codigo, titulo, nota)
                    print("Nota registrada con éxito.")
                else:
                    print("Estudiante no encontrado.")

        # --- Opciones de estudiante ---
        elif isinstance(usuario_actual, Estudiante):
            if opcion == "2":
                cursos_inscritos = [curso for curso in sistema.cursos.values() if usuario_actual.carnet in curso.estudiantes]
                if cursos_inscritos:
                    for c in cursos_inscritos:
                        print(f"{c.codigo} - {c.nombre}")
                else:
                    print("No está inscrito en ningún curso.")

            elif opcion == "3":
                if usuario_actual.calificaciones:
                    for curso, evals in usuario_actual.calificaciones.items():
                        print(f"\nCurso {curso}:")
                        for titulo, datos in evals.items():
                            print(f"  {titulo}: {datos['nota']}")
                    print(f"\nPromedio general: {usuario_actual.promedio_general():.2f}")
                else:
                    print("No tiene calificaciones registradas.")

        else:
            print("Opción inválida.")


def main():
    sistema = SistemaAcademico()
    while True:
        usuario_actual = menu_inicio(sistema)
        menu_academico(sistema, usuario_actual)


if __name__ == "__main__":
    main()
