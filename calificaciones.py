class Estudiante:
    def __init__(self, nombre):
     self.nombre = nombre
     self. calificaciones =  {}
    def registrar_nota (self, curso, evaluacion, nota):
       if curso not in self.calificaciones:
          self.calificaciones[curso] ={}
          self.calificaciones[curso][evaluacion]=nota
#Funcion promedio
    def promedio_curso(self, curso):
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
       def __init__(self):
          self.estudiantes = []

#Funcion para agregar a un estudiante
def agregar_estudiante(self, estudiante):
   self.estudiantes.append(estudiante)






 #Funcion que devuelve una lista de estudiantes 
       def listar_estudiantes(self):
        return [est.nombre for est in self.estudiantes]
   #Funcion para consultar al estudiante y su respectivo promedio

       def consultar_curso(self, curso):
        """Devuelve las evaluaciones y calificaciones de todos los estudiantes en un curso"""
        resultado = {}
        for estudiante in self.estudiantes:
            if curso in estudiante.calificaciones:
                resultado[estudiante.nombre] = estudiante.calificaciones[curso]
        return resultado

   # funcion para reporte de promedios
       def reporte_promedios(self, promedio_bajo=70):
        """Genera un reporte simple con promedios y alerta de promedio bajo"""
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

