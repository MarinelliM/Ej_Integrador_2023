class Alumno:
    __dni: int
    __apellido: str
    __nombre: str
    __carrera: str
    __año_carrera: int

    def __init__(self, dni, apellido, nombre, carrera, año) -> None:
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__año_carrera = año
        pass

    def __str__(self) -> str:
        return "%8d %s %s %s %4d" % (self.__dni, self.__apellido, self.__nombre, self.__carrera, self.__año_carrera)
        pass

    def getdni(self):
        return self.__dni
    
    def getañocar(self):
        return self.__año_carrera
    
    def mostraralumno(self):
        return print('Alumno: {} {}. Dni: {}. Carrera: {}. Año de cursado: {}' .format(self.__nombre,self.__apellido,self.__dni,self.__carrera,self.__año_carrera))
    
    def __gt__(self, otro):
        return self.getañocar() > otro.getañocar()
    
    
