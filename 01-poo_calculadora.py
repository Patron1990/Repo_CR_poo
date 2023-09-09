class Calculadora_Basica:
    def __init__(self,parametro1,parametro2):
        self.num1 = parametro1
        self.num2 = parametro2

    def sumar(self):
        return self.num1 + self.num2
    def restar(self):
        return self.num1 - self.num2
    def multiplicar(self):
        return self.num1 * self.num2
    def dividir(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "No se puede dividir entre 0"
        
numeros = Calculadora_Basica

print("suma: ",numeros.sumar())
print("suma: ",numeros.restar())
print("multiplicar: ",numeros.multiplicar())
print("dividir: ",numeros.dividir())


