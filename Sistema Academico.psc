Algoritmo Sistema_Academico
	
    // ==== VECTORES ====
    Dimension cursoCodigo[50] //se usan para crear arreglos o matrices que almacenan múltiples datos bajo un mismo nombre.
    Dimension cursoNombre[50]
    Dimension cursoInstructor[50]
	
    Dimension usuarioID[500]
    Dimension usuarioNombre[500]
    Dimension usuarioTipo[500]
    Dimension usuarioPass[500]
	
    Dimension inscripcionEstudianteID[200]
    Dimension inscripcionCursoCodigo[200]
	
    Dimension evalCursoCodigo[200]
    Dimension evalNombre[200]
    Dimension evalPonderacion[200]
	
    Dimension notaEstudianteID[500]
    Dimension notaCursoCodigo[500]
    Dimension notaEvalNombre[500]
    Dimension notaValor[500]
	
    // ==== CONTADORES ====
    cursosCont <- 0
    usuariosCont <- 0
    inscripcionesCont <- 0
    evaluacionesCont <- 0
    notasCont <- 0
	
    // ==== VARIABLES ====
    Definir opcion, i, j, k, cuenta Como Entero
    Definir suma, promedio, nuevaNota Como Real
    Definir pausa, codigoCurso, nombreCurso, nombreInstructor, nombreEval, tipoValido, pass, tipoIngreso Como Caracter
    Definir idEstudiante, idInstructor Como Entero
    Definir duplicado, cursoValido, idValido, instructorValido, notaExistente Como Logico
	
    // ==== MENÚ PRINCIPAL ====
    Repetir
        Limpiar Pantalla
        Escribir "===== SISTEMA ACADEMICO ====="
        Escribir "1. Registrar usuario"
        Escribir "2. Crear curso (solo Instructor)"
        Escribir "3. Inscribir estudiante en curso"
        Escribir "4. Crear evaluación para un curso"
        Escribir "5. Registrar/Modificar calificación (solo Instructor)"
        Escribir "6. Consultas completas"
        Escribir "7. Reporte estudiantes con promedio bajo"
        Escribir "0. Salir"
        Leer opcion
		
        Segun opcion Hacer
			
				// ===== 1. Registrar usuario =====
            1:
                Repetir
                    Escribir "Nombre del usuario:"
                    Leer tipoValido
                    duplicado <- FALSO
                    
                    // CORRECCIÓN: Solo verificar duplicados si hay usuarios registrados
                    Si usuariosCont > 0 Entonces
                        Para k <- 1 Hasta usuariosCont
                            Si usuarioNombre[k] = tipoValido Entonces
                                duplicado <- VERDADERO
                            FinSi
                        FinPara
                    FinSi
                    
                    Si duplicado = VERDADERO Entonces
                        Escribir "Usuario ya existe. Ingrese otro."
                    FinSi
                Hasta Que duplicado = FALSO
				
                Escribir "Tipo (Estudiante/Instructor):"
                Leer nombreEval
				
                usuariosCont <- usuariosCont + 1
                usuarioID[usuariosCont] <- usuariosCont
                usuarioNombre[usuariosCont] <- tipoValido
                usuarioTipo[usuariosCont] <- nombreEval
				
                Escribir "Ingrese una contraseña para este usuario:"
                Leer usuarioPass[usuariosCont]
				
                Escribir "Usuario registrado con ID: ", usuariosCont
				
				// ===== 2. Crear curso (solo Instructor) =====
            2:
                Escribir "¿Es usted Estudiante o Instructor?"
                Leer tipoIngreso
				
                Si tipoIngreso = "Instructor" Entonces
                    Escribir "Ingrese su ID de usuario:"
                    Leer idInstructor
                    instructorValido <- FALSO
					
                    // CORRECCIÓN: Verificar solo si hay usuarios
                    Si usuariosCont > 0 Entonces
                        Para k <- 1 Hasta usuariosCont
                            Si usuarioID[k] = idInstructor Y usuarioTipo[k] = "Instructor" Entonces
                                Escribir "Ingrese contraseña:"
                                Leer pass
                                Si usuarioPass[k] = pass Entonces
                                    instructorValido <- VERDADERO
                                    Escribir "Acceso correcto. Bienvenido instructor ", usuarioNombre[k]
                                Sino
                                    Escribir "Contraseña incorrecta."
                                FinSi
                            FinSi
                        FinPara
                    FinSi
					
                    Si instructorValido = VERDADERO Entonces
                        Repetir
                            Escribir "Código del curso:"
                            Leer codigoCurso
                            duplicado <- FALSO
                            
                            // CORRECCIÓN: Solo verificar duplicados si hay cursos
                            Si cursosCont > 0 Entonces
                                Para k <- 1 Hasta cursosCont
                                    Si cursoCodigo[k] = codigoCurso Entonces
                                        duplicado <- VERDADERO
                                    FinSi
                                FinPara
                            FinSi
                            
                            Si duplicado = VERDADERO Entonces
                                Escribir "Código ya existe. Ingrese otro."
                            FinSi
                        Hasta Que duplicado = FALSO
						
                        Escribir "Nombre del curso:"
                        Leer nombreCurso
                        Escribir "Instructor del curso:"
                        Leer nombreInstructor
						
                        cursosCont <- cursosCont + 1
                        cursoCodigo[cursosCont] <- codigoCurso
                        cursoNombre[cursosCont] <- nombreCurso
                        cursoInstructor[cursosCont] <- nombreInstructor
						
                        Escribir "Curso registrado correctamente."
                    Sino
                        Escribir "Error: Solo un instructor válido puede crear cursos."
                    FinSi
                Sino
                    Escribir "Error: Esta opción solo está disponible para instructores."
                FinSi
				
				// ===== 3. Inscribir estudiante en curso =====
            3:
                
				Si usuariosCont = 0 Entonces
					Escribir "No hay estudiantes registrados."
				Sino
					repetirBusqueda <- VERDADERO
					Repetir
						Escribir "ID del estudiante (o 0 para regresar al menú):"
						Leer idEstudiante
						
						Si idEstudiante = 0 Entonces
							repetirBusqueda <- FALSO
						FinSi
						
						idValido <- FALSO
						Para k <- 1 Hasta usuariosCont
							Si usuarioID[k] = idEstudiante Y usuarioTipo[k] = "Estudiante" Entonces
								idValido <- VERDADERO
								Escribir "Estudiante encontrado: ", usuarioNombre[k]
							FinSi
						FinPara
						
						Si idValido = FALSO Y repetirBusqueda = VERDADERO Entonces
							Escribir "ID inválido o no corresponde a un estudiante. Ingrese 0 para regresar."
						FinSi
						
					Hasta Que idValido = VERDADERO O repetirBusqueda = FALSO
					
					// Si se decidió regresar, no continuar con la búsqueda de cursos
					Si repetirBusqueda = VERDADERO Entonces
						// Código para seleccionar curso y verificar duplicados...
						Si cursosCont = 0 Entonces
							Escribir "No hay cursos registrados."
						Sino
							Repetir
								Escribir "Código del curso:"
								Leer codigoCurso
								cursoValido <- FALSO
								Para k <- 1 Hasta cursosCont
									Si cursoCodigo[k] = codigoCurso Entonces
										cursoValido <- VERDADERO
										Escribir "Curso encontrado: ", cursoNombre[k]
									FinSi
								FinPara
								Si cursoValido = FALSO Entonces
									Escribir "Código de curso inválido."
								FinSi
							Hasta Que cursoValido = VERDADERO
							
							duplicado <- FALSO
							Si inscripcionesCont > 0 Entonces
								Para k <- 1 Hasta inscripcionesCont
									Si inscripcionEstudianteID[k] = idEstudiante Y inscripcionCursoCodigo[k] = codigoCurso Entonces
										duplicado <- VERDADERO
									FinSi
								FinPara
							FinSi
							
							Si duplicado = VERDADERO Entonces
								Escribir "Estudiante ya inscrito en este curso."
							Sino
								inscripcionesCont <- inscripcionesCont + 1
								inscripcionEstudianteID[inscripcionesCont] <- idEstudiante
								inscripcionCursoCodigo[inscripcionesCont] <- codigoCurso
								Escribir "Estudiante inscrito correctamente."
							FinSi
						FinSi
					FinSi
FinSi

				// ===== 4. Crear evaluación =====
            4:
                // CORRECCIÓN: Verificar que hay cursos antes de buscar
                Si cursosCont = 0 Entonces
                    Escribir "No hay cursos registrados."
                Sino
                    Repetir
                        Escribir "Código del curso para la evaluación:"
                        Leer codigoCurso
                        cursoValido <- FALSO
                        Para k <- 1 Hasta cursosCont
                            Si cursoCodigo[k] = codigoCurso Entonces
                                cursoValido <- VERDADERO
                                Escribir "Curso encontrado: ", cursoNombre[k]
                            FinSi
                        FinPara
                        Si cursoValido = FALSO Entonces
                            Escribir "Código de curso inválido."
                        FinSi
                    Hasta Que cursoValido = VERDADERO
					
                    Repetir
                        Escribir "Nombre de la evaluación:"
                        Leer nombreEval
                        duplicado <- FALSO
                        // CORRECCIÓN: Solo verificar evaluaciones si hay alguna
                        Si evaluacionesCont > 0 Entonces
                            Para k <- 1 Hasta evaluacionesCont
                                Si evalCursoCodigo[k] = codigoCurso Y evalNombre[k] = nombreEval Entonces
                                    duplicado <- VERDADERO
                                FinSi
                            FinPara
                        FinSi
                        Si duplicado = VERDADERO Entonces
                            Escribir "Evaluación ya registrada para este curso."
                        FinSi
                    Hasta Que duplicado = FALSO
					
                    evaluacionesCont <- evaluacionesCont + 1
                    evalCursoCodigo[evaluacionesCont] <- codigoCurso
                    evalNombre[evaluacionesCont] <- nombreEval
					
                    Repetir
                        Escribir "Ponderación (0 a 100):"
                        Leer evalPonderacion[evaluacionesCont]
                        Si evalPonderacion[evaluacionesCont] < 0 o evalPonderacion[evaluacionesCont] > 100 Entonces
                            Escribir "Valor inválido."
                        FinSi
                    Hasta Que evalPonderacion[evaluacionesCont] >= 0 Y evalPonderacion[evaluacionesCont] <= 100
					
                    Escribir "Evaluación registrada correctamente."
                FinSi
				
				// ===== 5. Registrar/Modificar calificación =====
            5:
                Escribir "¿Es usted Estudiante o Instructor?"
                Leer tipoIngreso
				
                Si tipoIngreso = "Instructor" Entonces
                    Escribir "Ingrese su ID de usuario:"
                    Leer idInstructor
                    instructorValido <- FALSO
					
                    // CORRECCIÓN: Verificar solo si hay usuarios
                    Si usuariosCont > 0 Entonces
                        Para k <- 1 Hasta usuariosCont
                            Si usuarioID[k] = idInstructor Y usuarioTipo[k] = "Instructor" Entonces
                                Escribir "Ingrese contraseña:"
                                Leer pass
                                Si usuarioPass[k] = pass Entonces
                                    instructorValido <- VERDADERO
                                    Escribir "Acceso correcto. Bienvenido instructor ", usuarioNombre[k]
                                Sino
                                    Escribir "Contraseña incorrecta."
                                FinSi
                            FinSi
                        FinPara
                    FinSi
					
                    Si instructorValido = VERDADERO Entonces
                        // CORRECCIÓN: Verificar que hay estudiantes
                        Si usuariosCont = 0 Entonces
                            Escribir "No hay estudiantes registrados."
                        Sino
                            Repetir
                                Escribir "ID del estudiante:"
                                Leer idEstudiante
                                idValido <- FALSO
                                Para k <- 1 Hasta usuariosCont
                                    Si usuarioID[k] = idEstudiante Y usuarioTipo[k] = "Estudiante" Entonces
                                        idValido <- VERDADERO
                                        Escribir "Estudiante encontrado: ", usuarioNombre[k]
                                    FinSi
                                FinPara
                                Si idValido = FALSO Entonces
                                    Escribir "ID inválido o no corresponde a un estudiante."
                                FinSi
                            Hasta Que idValido = VERDADERO
							
                            // CORRECCIÓN: Verificar que hay cursos
                            Si cursosCont = 0 Entonces
                                Escribir "No hay cursos registrados."
                            Sino
                                Repetir
                                    Escribir "Código del curso:"
                                    Leer codigoCurso
                                    cursoValido <- FALSO
                                    Para k <- 1 Hasta cursosCont
                                        Si cursoCodigo[k] = codigoCurso Entonces
                                            cursoValido <- VERDADERO
                                            Escribir "Curso encontrado: ", cursoNombre[k]
                                        FinSi
                                    FinPara
                                    Si cursoValido = FALSO Entonces
                                        Escribir "Código de curso inválido."
                                    FinSi
                                Hasta Que cursoValido = VERDADERO
								
                                // CORRECCIÓN: Verificar que hay evaluaciones
                                Si evaluacionesCont = 0 Entonces
                                    Escribir "No hay evaluaciones registradas para este curso."
                                Sino
                                    Repetir
                                        Escribir "Nombre de la evaluación:"
                                        Leer nombreEval
                                        duplicado <- FALSO
                                        Para k <- 1 Hasta evaluacionesCont
                                            Si evalCursoCodigo[k] = codigoCurso Y evalNombre[k] = nombreEval Entonces
                                                duplicado <- VERDADERO
                                            FinSi
                                        FinPara
                                        Si duplicado = FALSO Entonces
                                            Escribir "Evaluación no existe para este curso."
                                        FinSi
                                    Hasta Que duplicado = VERDADERO
									
                                    Repetir
                                        Escribir "Ingrese nota (0 a 100):"
                                        Leer nuevaNota
                                        Si nuevaNota <0 o nuevaNota>100 Entonces
                                            Escribir "Nota inválida."
                                        FinSi
                                    Hasta Que nuevaNota >=0 Y nuevaNota <=100
									
                                    notaExistente <- FALSO
                                    // CORRECCIÓN: Solo buscar notas si hay alguna
                                    Si notasCont > 0 Entonces
                                        Para k <- 1 Hasta notasCont
                                            Si notaEstudianteID[k] = idEstudiante Y notaCursoCodigo[k] = codigoCurso Y notaEvalNombre[k] = nombreEval Entonces
                                                notaValor[k] <- nuevaNota
                                                notaExistente <- VERDADERO
                                                Escribir "Nota modificada correctamente."
                                            FinSi
                                        FinPara
                                    FinSi
									
                                    Si notaExistente = FALSO Entonces
                                        notasCont <- notasCont + 1
                                        notaEstudianteID[notasCont] <- idEstudiante
                                        notaCursoCodigo[notasCont] <- codigoCurso
                                        notaEvalNombre[notasCont] <- nombreEval
                                        notaValor[notasCont] <- nuevaNota
                                        Escribir "Nota registrada correctamente."
                                    FinSi
                                FinSi
                            FinSi
                        FinSi
                    Sino
                        Escribir "Error: Solo un instructor válido puede gestionar calificaciones."
                    FinSi
                Sino
                    Escribir "Error: Esta opción solo está disponible para instructores."
                FinSi
				
				// ===== 6. Consultas completas =====
            6:
                Escribir "=== Cursos registrados ==="
                Si cursosCont > 0 Entonces
                    Para k <- 1 Hasta cursosCont
                        Escribir cursoCodigo[k], "-", cursoNombre[k], " (", cursoInstructor[k], ")"
                    FinPara
                Sino
                    Escribir "No hay cursos registrados."
                FinSi
				
                Escribir ""
                Escribir "=== Usuarios registrados ==="
                Si usuariosCont > 0 Entonces
                    Para k <- 1 Hasta usuariosCont
                        Escribir usuarioID[k], " ", usuarioNombre[k], " [", usuarioTipo[k], "]"
                    FinPara
                Sino
                    Escribir "No hay usuarios registrados."
                FinSi
				
                Escribir ""
                Escribir "=== Inscripciones ==="
                Si inscripcionesCont > 0 Entonces
                    Para k <- 1 Hasta inscripcionesCont
                        Para j <- 1 Hasta cursosCont
                            Si cursoCodigo[j] = inscripcionCursoCodigo[k] Entonces
                                Escribir "Estudiante ID: ", inscripcionEstudianteID[k], " Curso: ", inscripcionCursoCodigo[k], " - ", cursoNombre[j]
                            FinSi
                        FinPara
                    FinPara
                Sino
                    Escribir "No hay inscripciones registradas."
                FinSi
				
                Escribir ""
                Escribir "=== Evaluaciones ==="
                Si evaluacionesCont > 0 Entonces
                    Para k <- 1 Hasta evaluacionesCont
                        Escribir "Curso: ", evalCursoCodigo[k], " Evaluación: ", evalNombre[k], " Ponderación: ", evalPonderacion[k]
                    FinPara
                Sino
                    Escribir "No hay evaluaciones registradas."
                FinSi
				
                Escribir ""
                Escribir "=== Notas registradas ==="
                Si notasCont > 0 Entonces
                    Para k <- 1 Hasta notasCont
                        Para j <- 1 Hasta cursosCont
                            Si cursoCodigo[j] = notaCursoCodigo[k] Entonces
                                Escribir "Estudiante ID: ", notaEstudianteID[k], " Curso: ", notaCursoCodigo[k], " - ", cursoNombre[j], " Evaluación: ", notaEvalNombre[k], " Nota: ", notaValor[k]
                            FinSi
                        FinPara
                    FinPara
                Sino
                    Escribir "No hay notas registradas."
                FinSi
				
				// ===== 7. Reporte promedio bajo =====
            7:
                Escribir "=== Reporte: Promedio menor a 61 ==="
                Si usuariosCont > 0 Entonces
                    Para i <- 1 Hasta usuariosCont
                        Si usuarioTipo[i] = "Estudiante" Entonces
                            suma <- 0
                            cuenta <- 0
                            
                            // CORRECCIÓN PRINCIPAL: Solo procesar notas si existen
                            Si notasCont > 0 Entonces
                                Para j <- 1 Hasta notasCont
                                    Si notaEstudianteID[j] = usuarioID[i] Entonces
                                        suma <- suma + notaValor[j]
                                        cuenta <- cuenta + 1
                                    FinSi
                                FinPara
                            FinSi
                            
                            // Solo calcular promedio si hay notas
                            Si cuenta > 0 Entonces
                                promedio <- suma / cuenta
                                Si promedio < 61 Entonces
                                    Escribir "Estudiante: ", usuarioNombre[i], " Promedio: ", promedio
                                FinSi
                            FinSi
                        FinSi
                    FinPara
                Sino
                    Escribir "No hay estudiantes registrados."
                FinSi
				
				// ===== 0. Salir =====
            0:
                Escribir "Saliendo del sistema..."
        FinSegun
		
        Si opcion <> 0 Entonces
            Escribir "Presione ENTER para continuar..."
            Leer pausa
        FinSi

    Hasta Que opcion = 0

FinAlgoritmo
