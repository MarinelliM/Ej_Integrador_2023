import csv
from Menu import menu
from Alumnos import Alumno
from Materias import Materia
import numpy as np
if __name__ == "__main__":
    materias = []
    with open('materiasAprobadas.csv', 'r', encoding='utf8') as archivo:
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            materia = Materia(fila[0],fila[1],fila[2],fila[3],fila[4])
            materias.append(materia)
    archivo.close()
    for i in range(len(materias)):
        materias[i].mostrar()
    with open('alumnos.csv', 'r', encoding='utf8') as archivo:
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        i = sum(1 for fila in reader) # contar el número de filas restantes
        alumnos_np = np.empty(i, dtype=Alumno) # inicializar el arreglo numpy con el tamaño adecuado
        archivo.seek(0) # volver al principio del archivo
        next(reader) # omitir la primera fila de encabezado
        for a, fila in enumerate(reader):
            alumno = Alumno(fila[0], fila[1], fila[2], fila[3], fila[4])
            alumnos_np[a] = alumno
    archivo.close()
    for alumno in alumnos_np:
        alumno.mostraralumno()
    menu(alumnos_np,materias)
