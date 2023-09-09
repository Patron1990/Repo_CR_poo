class MiClase:
    def __init__(self,parametro01,parametro02):
        self.atrivuto01 = parametro01
        self.atributo02 = parametro02

    def metodo(self):
        return "Soy un metodo de la clase MiClase"

class Perro:
    def __init__(self,nombre,raza,edad,color,peso,altura):

        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.color = color
        self.peso = peso
        self.altura = altura

    def ladrar(self):
        return f'{self.nombre} esta ladrando'
    
    def dormir(self):
        return f'{self.nombre} esta durmiendo'
    
    def info_perro(self):
        return f'Hola me llamo {self.nombre},soy un perro de raza {self.raza},tengo {self.edad}años y soy de color {self.color}'
    
perro1 = Perro("Dino","Perrosaurio",5,"morado",1.25,1.75)

print(perro1.nombre)
print(perro1.ladrar())
print(perro1.info_perro())

perro2 = Perro("Mordisco","mixta",8,"canelo",35,1)

print("")
print(perro2.info_perro())
print(perro2.dormir())


    
