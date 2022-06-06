numero_1 = float(input("Digite su primer numero: "))
numero_2 = float(input("Digite su segundo numero: "))
opcion_1 = 'Si desea que se sumen porfavor digite "A"'
print(opcion_1)
opcion_2 = 'Si desea que se resten porfavor digite "B"'
print(opcion_2)
opcion_3 = 'Si desea que se multipliquen porfavor digite "C"'
print(opcion_3)
opcion_4 = 'Si desea que el programa finalice porfavor digite "D"'
print(opcion_4)
respuesta = input("Porfavor digite su respuesta: ")
print(respuesta)

if respuesta == "A":
    resultado = numero_1 + numero_2
    print(resultado)

elif respuesta == "B":
    resultado = numero_1 - numero_2
    print(resultado)

elif respuesta == "C":
    resultado = numero_1 * numero_2
    print(resultado)

elif respuesta == "D":
    print("El programa ha finalizado")

else:
    print("Usted ha introducido una opcion incorrecta")



