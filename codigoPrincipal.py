## Funciones Matematicas

import unittest  ##importamos unittest  de error

import miModulo ## llamo al modulo logico

print("Funciones Matematicas")
print("Ingresa el primer número :")
num1=input()
num1=float(num1)
print("Ingresa el segundo número :")
num2=input()
num2=float(num2)
print ("La Suma es :" , miModulo.sumar(num1,num2))
print ("La Resta es :" , miModulo.restar(num1,num2))
print ("La Multiplicación es :" , miModulo.multiplicar(num1,num2))
print ("La División es :" , miModulo.dividir(num1,num2))

class Prueba(unittest.TestCase):  ## modulo de prueba de error 
    def tests_sumar(self):
        self .assertEqual(miModulo.sumar(3,7),10)
        self .assertEqual(miModulo.sumar(5,2),7)
        self .assertEqual(miModulo.sumar(1,8),9)
        self .assertEqual(miModulo.sumar(9,10),19)
    def tests_restar(self):
        self .assertEqual(miModulo.restar(3,7),-4)
        self .assertEqual(miModulo.restar(5,2),3)
        self .assertEqual(miModulo.restar(1,8),-7)
        self .assertEqual(miModulo.restar(9,10),-1)
    def tests_multiplicar(self):
        self .assertEqual(miModulo.multiplicar(3,7),21)
        self .assertEqual(miModulo.multiplicar(5,2),10)
        self .assertEqual(miModulo.multiplicar(1,8),8)
        self .assertEqual(miModulo.multiplicar(9,10),90)
    def tests_dividir(self):
        self .assertEqual(miModulo.dividir(3,1),3)
        self .assertEqual(miModulo.dividir(50,2),25)
        self .assertEqual(miModulo.dividir(10,5),2)
        self .assertEqual(miModulo.dividir(90,10),9)
if __name__=="__main__":
    unittest.main()
