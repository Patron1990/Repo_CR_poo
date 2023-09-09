#Crear un aplicacion que registre un alumno y sus calificaciones, que guarde sus califaciones en una lista, sus notas y promedios

#Definir las clases

class Alumno:
    #definir el contructor
    def __init__(self,nombre):
        self.nombre = nombre
        self.calificaciones = []

 #definicion de los metodos de la clase

    def agregar_calificacion(self,calificacion):
        self.calificaciones.append(calificacion)

    def calcular_promedio(self):
        if len(self.calificaciones)==0:
            return 0
        else:
            return sum(self.calificaciones)/len(self.calificaciones)

class RegistroAlumnos:
    def __init__(self):
        self.alumnos = []

        #definir metodos
    def agregar_alumno(self,nombre):
        alumno = Alumno(nombre)
        self.alumnos.append(alumno)

    def buscar_alumno(self,nombre):
        for alumno in self.alumnos:
            if alumno.nombre == nombre:
                return alumno
        return None     #none, no regresa ningun dato

    def mostrar_info(self):
        for alumno in self.alumnos:
            print(f'Nombre {alumno.nombre}')
            print("Calificaciones: ",alumno.calificaciones)
            print(f'Promedio de notas {alumno.calcular_promedio()}')
            print("")

registro = RegistroAlumnos()

while True:
    print("1.Agregar alumno")
    print("2.Agrega califiacacion a alumno")
    print ("3. Mostrar info de todos los almunos")
    print ("4.Salir")

    opcion = int(input("Seleccione una opcion"))

    if opcion == 1:
        nombre = input("Agregue el nombre del alumno: ")
        registro.agregar_alumno(nombre)

    elif opcion == 2:
        nombre = input("Ingrese el nombre del alumno: ")
        alumno = registro.buscar_alumno(nombre)
        if alumno: 
            calificacion = float(input("Ingrese la calificacion"))
            alumno.agregar_calificacion(calificacion)
        else:
            print("Alumno no encontrado")

    elif opcion == 3:
        registro.mostrar_info()

    elif opcion == 4:
        break

    else:
        print("opcion no valida")


    


