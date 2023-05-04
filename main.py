from ManejadorAlumnos import ManejadorAlumnos
import csv
from Menu import menu
from ManejadorMaterias import ManejadorMaterias

if __name__ == "__main__":
    ma = ManejadorAlumnos(3,10)
    ma.testManejadorAlumnos()
    archivo = open('alumnos.csv')
    reader = csv.reader(archivo,delimiter=';')
    next(reader)
    i = len(list(reader))
    ma = ManejadorAlumnos(i,i*2)
    ma.initman()
    mm = ManejadorMaterias()
    mm.initmm()
    menu(ma,mm)
