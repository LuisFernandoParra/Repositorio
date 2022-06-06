from decimal import DivisionByZero
from logging import exception


def dividir(a,b):
    operacion = a/b
    return operacion



while True:
    pregunta = input("Digite el dividendo: ")
    pregunta_2 = input("Digite el divisor:")
    try:
        pregunta = int(pregunta)
        pregunta_2 = int(pregunta_2)
        resultado = dividir(pregunta,pregunta_2) 
    except  ZeroDivisionError:
        print("No se puede dividir por cero:")
    except ValueError:
        print("porfavor ingrese un numero")
    except Exception as error:
        print("hubo un error",error)
    else:
        print("Felicadades ha completado el programa de forma exitosa su resultado es:",resultado)
        break

    


