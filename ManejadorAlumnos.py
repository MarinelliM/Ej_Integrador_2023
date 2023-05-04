import numpy as np
from Alumnos import Alumno
class ManejadorAlumnos:
    __cantidad = 0
    __dimension = 0
    __incremento = 5

    def __init__(self, dimension, incremento = 5) -> None:
        self.__alumnos = np.empty(dimension, dtype = Alumno)
        self.__dimension = dimension
        self.__cantidad = 0
        pass
    
    def agregaralumno(self, alum):
        if self.__cantidad == self.__dimension:
            self.__dimension+=self.__incremento
            self.__alumnos.resize(self.__dimension)
        self.__alumnos[self.__cantidad]=alum
        self.__cantidad+=1

    def getalumno(self, alum):
        return self.__alumnos[alum]
    
    def mostrar(self):
        for i in range(self.__cantidad):
            print(self.__alumnos[i].mostraralumno())
    
    def testManejadorAlumnos(self):
        a1 = Alumno(43839127,'Marinelli','Mauricio','POO',2023)
        a2 = Alumno(43839128,'Nicolas','Lloveras','POO',2023)
        a3 = Alumno(43839129,'Matias','Alvarez','PyE',2022)
        self.agregaralumno(a1)
        self.agregaralumno(a2)
        self.agregaralumno(a3)
        self.mostrar()

