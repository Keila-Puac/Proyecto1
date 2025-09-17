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
    

