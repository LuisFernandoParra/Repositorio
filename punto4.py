numeros_a_introducir = int(input("Digite la cantidad de numeros que desee introducir: "))
lista = []
for x in range(0,numeros_a_introducir):
    pregunta = int(input("Digite los numeros que desee que se sumen: "))
    lista.append(pregunta)

media_aritmetica = sum(lista)/numeros_a_introducir
print(media_aritmetica)
    
    
