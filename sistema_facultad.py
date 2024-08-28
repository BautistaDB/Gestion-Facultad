class Estudiante:
    
    matriculas_registradas = set()  
    dni_registrados = set()

    def __init__(self, dni, nombre, apellido, numero_matricula, carrera):

        if dni in Estudiante.dni_registrados:
            raise ValueError(f"El número de dni {dni} ya está registrado.")
        
        if numero_matricula in Estudiante.matriculas_registradas:
            raise ValueError(f"El número de matrícula {numero_matricula} ya está registrado.")
        
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.numero_matricula = numero_matricula
        self.carrera = carrera
        self.cursos_inscriptos = []

        Estudiante.matriculas_registradas.add(numero_matricula) 
        Estudiante.dni_registrados.add(dni)

    def inscribir_curso(self, curso):
        if curso.inscribir_estudiante(self):
            self.cursos_inscriptos.append(curso)

    def __str__(self):
        cursos = ", ".join(self.nombre for self.curso in self.cursos_inscriptos) if self.cursos_inscriptos else "Ninguno"
        return (f"DNI: {self.dni}, Nombre: {self.nombre} {self.apellido}, "
                f"Número de Matrícula: {self.numero_matricula}, Carrera: {self.carrera}, "
                f"Cursos Inscriptos: {cursos}")


class Curso:
    
    nombre_cursos_registrados = set()
    codigo_cursos_registrados = set()


    def __init__(self, nombre, codigo, profesor, capacidad_maxima):

        if nombre in Curso.nombre_cursos_registrados:
                raise ValueError(f"El nombre del curso {nombre} ya está registrado.")
        
        if codigo in Curso.codigo_cursos_registrados:
                raise ValueError(f"El codigo del curso {codigo} ya está registrado.")
        
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        self.capacidad_maxima = capacidad_maxima
        self.estudiantes_inscriptos = []

    def inscribir_estudiante(self, estudiante):
        if len(self.estudiantes_inscriptos) < self.capacidad_maxima:
            self.estudiantes_inscriptos.append(estudiante)
            print(f"Estudiante {self.nombre} inscripto en el curso {self.nombre}.")
            return True
        else:
            print(f"No hay cupos disponibles en el curso {self.nombre}.")
            return False

    def __str__(self):
        inscriptos = len(self.estudiantes_inscriptos)
        return (f"Curso: {self.nombre}, Código: {self.codigo}, Profesor: {self.profesor}, "
                f"Capacidad: {self.capacidad_maxima}, Inscriptos: {inscriptos}")
