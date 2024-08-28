from sistema_facultad import Estudiante, Curso

def menu():

    estudiantes = []
    cursos = []

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar estudiante")
        print("2. Registrar curso")
        print("3. Inscribir estudiante en curso")
        print("4. Ver estado de cursos")
        print("5. Ver estado de estudiantes")
        print("0. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == '1':
            dni = input("DNI del estudiante: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            numero_matricula = input("Número de Matrícula: ")
            carrera = input("Carrera: ")

            try:
                nuevo_estudiante = Estudiante(dni, nombre, apellido, numero_matricula, carrera)
                estudiantes.append(nuevo_estudiante)
                print(f"Estudiante {nombre} {apellido} registrado con éxito.")
            except ValueError as e:
                print(e)

        elif opcion == '2':
            nombre_curso = input("Nombre del curso: ")
            codigo = input("Código del curso: ")
            profesor = input("Profesor encargado: ")
            capacidad_maxima = int(input("Capacidad máxima del curso: "))

            nuevo_curso = Curso(nombre_curso, codigo, profesor, capacidad_maxima)
            cursos.append(nuevo_curso)
            print(f"Curso {nombre_curso} registrado con éxito.")

        elif opcion == '3':

            matricula = input("Número de Matrícula del estudiante: ")
            codigo_curso = input("Código del curso: ")

            estudiante = None
            for e in estudiantes:
                if e.numero_matricula == matricula:
                    estudiante = e
                    break

            curso = None
            for c in cursos:
                if c.codigo == codigo_curso:
                    curso = c
                    break  

            if estudiante and curso:
                estudiante.inscribir_curso(curso)
            else:
                print("Estudiante o curso no encontrado.")

        elif opcion == '4':
            for curso in cursos:
                print(curso)

        elif opcion == '5':
            for estudiante in estudiantes:
                print(estudiante)

        elif opcion == '0':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    menu()




