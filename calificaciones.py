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
    
