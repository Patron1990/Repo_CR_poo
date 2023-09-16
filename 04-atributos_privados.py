#01 creamos la clase

class MiClase:
    def __init__(self):  #02 creamos el constructor
        self._atributo_privado = 42   #03 definimos atributos

    #04 creamos los metodos que vamos a necesitar de la clase
    def obtener_atributo(self):
        return self._atributo_privado
    
    def modificar_atributo(self,nuevo_valor):
        self._atributo_privado = nuevo_valor

#05 instanciamos la clase
objeto = MiClase()

#06 Probamos el funcionamiento de los metodos y atributos 

print(objeto._atributo_privado)
print(objeto.obtener_atributo())
objeto.modificar_atributo(100)
print(objeto.obtener_atributo())

