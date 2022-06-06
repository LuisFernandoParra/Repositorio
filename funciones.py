def ano_bisiesto(a):
    while not a.isdigit():
        a = input("El caracter digitado no es un numero porfavor digite un numero:")
    if a.isdigit():
         a = int(a) 
    if ((a % 4 == 0) or (a % 400 == 0)) and  ( a !=100):
            return "el año es bisiesto"
    else:
            return "el año no es bisiesto"
    
pregunta = input("Porfavor digite el año que desee saber si es bisiesto: ")
resultado = ano_bisiesto(pregunta)
print(resultado)

    