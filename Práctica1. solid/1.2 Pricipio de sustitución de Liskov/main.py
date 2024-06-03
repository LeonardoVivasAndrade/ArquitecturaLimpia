from cuadrado import Cuadrado
from rectangulo import Rectangulo

cuadrado = Cuadrado(20)
print("Cuadrado de lados: " + str(cuadrado.lado))
print("Área: " + str(cuadrado.area()))
print("Perímetro: " + str(cuadrado.perimetro()))
print("")
rectangulo = Rectangulo(50,200)
print("Rectangulo " + str(rectangulo.base) + "x" + str(rectangulo.altura))
print("Área: " + str(rectangulo.area()))
print("Perímetro: " + str(rectangulo.perimetro()))