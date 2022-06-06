pregunta = int(input("Porfavor digite un numero del 0 al 9: "))
numeros = [1,3,6,9]
while  pregunta < 0 or pregunta >= 10:
    error = int(input("El numero digitado es incorrecto porfavor digite un numero del 0 al 9: "))
    if 0 <= pregunta and pregunta < 10:
        break
if pregunta in numeros:
        print("El numero digitado se encuentra en la lista")
else:
        print("El numero digitado no se encuentra en la lista")




