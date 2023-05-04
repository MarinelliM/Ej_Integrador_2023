def menu(MA,MM):
    print('a - Informar promedio con aplazos y sin aplazos de un alumno')
    print('b - Informar los alumnos que promocionaron en una materia')
    print('c - Obtener listado de alumnos ordenado por año que cursan y alfabeticamente')
    print('o - Salir del programa')
    op = str(input('Ingrese opcion:'))
    while op != 0:
        if op == 'a':
            dni = int(input('Ingrese dni del alumno a buscar:'))
            MM.buscarpromedio(dni)
        elif op == 'b':
            materia = str(input('Ingrese el nombre de la materia a buscar:'))
            MM.buscarmaterias(materia, MA)
        elif op == 'c':
            MA.crearorden()
        else:
            print('a - Informar promedio con aplazos y sin aplazos de un alumno')
            print('b - Informar los alumnos que promocionaron en una materia')
            print('c - Obtener listado de alumnos ordenado por año que cursan y alfabeticamente')
            print('o - Salir del programa')
            op = str(input('Ingrese opcion:'))