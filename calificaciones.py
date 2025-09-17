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

    class Sistem_Academico:
       def __init__(self):
          self.estudiantes = []
       def agregar_estudiante(self, estudiante):
          self.estudiante. append(estudiante)
#Funcion para agregar a un estudiante
def agregar_estudiante(self, estudiante):
   self.estudiantes.append(estudiante)
   #Funcion para consultar al estudiante y su respectivo promedio

def consultar_estudiantes(self):
   lista_nombres = []
   for estudiante in self.estudiantes:
      lista_nombres.append(estudiante.nombre)
      return lista_nombres
   # funcion para reporte de promedios
   def reporte_promedios(self):
      lista_reporte =[]
      for estudiante in self.estudiantes:
         lista_reporte.append((estudiante.nombre, estudiante.promedio_general()))
         return lista_reporte
      

    


