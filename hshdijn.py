import math
def area_circulo(r):
    resultado = r**2 *math.pi
    return resultado

radio = int(input("Porfavor digite el radio de su circulo:"))
area = area_circulo(radio)
print(area)