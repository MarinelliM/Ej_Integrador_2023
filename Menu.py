def menu(arregloalu,listamat):
    print('a - Informar promedio con aplazos y sin aplazos de un alumno')
    print('b - Informar los alumnos que promocionaron en una materia')
    print('c - Obtener listado de alumnos ordenado por año que cursan y alfabeticamente')
    print('o - Salir del programa')
    op = str(input('Ingrese opcion:'))
    while op != 'o':
        if op == 'a':
            dni = str(input('Ingrese dni del alumno a buscar:'))
            opa(listamat,dni)
        elif op == 'b':
            materia = str(input('Ingrese el nombre de la materia a buscar:'))
            opb(listamat, materia, arregloalu)
        elif op == 'c':
            opc(arregloalu)
        print('a - Informar promedio con aplazos y sin aplazos de un alumno')
        print('b - Informar los alumnos que promocionaron en una materia')
        print('c - Obtener listado de alumnos ordenado por año que cursan y alfabeticamente')
        print('o - Salir del programa')
        op = str(input('Ingrese opcion:'))

def opa(lm,dni):
    i = 0
    a = 0
    b = 0
    promsinap = 0
    promconap = 0
    while i < len(lm):
        if lm[i].getdni() == dni:
            if lm[i] > '3':
                promsinap += int(lm[i].getnota()) 
                a += 1
                b += 1
                promconap += int(lm[i].getnota())
                i += 1
            else: 
                promconap += int(lm[i].getnota())
                b += 1
                i += 1
        else: i += 1
    print('Promedio sin aplazos: %.2f' % (promsinap/a))
    print('Promedio con aplazos: %.2f' % (promconap/b))


def opb(lm,materia,aa):
    i = 0
    a = 0
    la = []
    while i < len(lm):
        if lm[i].getnombre() == materia:
            if lm[i].getaprobacion() == 'P': #and lm[i].getnota() > 6:
                la.append(lm[i].getdni())
                i = len(lm)
        else:i += 1
    if not la:
        print('En la materia {}, no hubo alumnos que promocionaran o su nota fue menor a 7' .format(materia))
    else:
        print('DNI\tApellido y nombre\t\tAño que cursa')
        a = 0
        while a < len(la):
            dni = la[a]
            j = 0
            while j < len(aa):
                if aa[j].getdni() == dni:
                    alumno = aa[j]
                    print('{}\t{}\t{}'.format(alumno.getdni(), alumno.getapellido()+ '' +alumno.getnombre(), alumno.getañocar()))
                    j = len(aa)
                else: j+=1
            a += 
 def opc(aa):
     a = sorted(aa, reverse=False)
     for i in range(len(a)):
         a[i].mostraralumno()
