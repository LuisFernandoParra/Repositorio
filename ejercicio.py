esp_2_ing = {"rojo":"red","verde":"green","azul":"blue"}
ing_2_esp = {"red":"rojo","green":"verde","blue":"azul"}



while True:
    print("0- para salir")
    print("1- Español -> Inglés")
    print("2- Inglés -> Español ")
    pregunta = input(">>> ")
    try:
        pregunta = int(pregunta)
    except ValueError:
        print("No ingresaste una opcion valida")
    except Exception as error:
        print(error)
    if pregunta == 0:
        break
    elif pregunta == 1:
        pregunta_2 = input("Palabra: ")
        if pregunta_2 == "rojo":
           print(">>>",esp_2_ing["rojo"])
        elif pregunta_2 == "verde":
             print(">>>",esp_2_ing["verde"])
        elif pregunta_2 == "azul":
            print(">>>",esp_2_ing["azul"])
        else:
            print("No sabemos la traduccion")
    elif pregunta == 2:
         pregunta_3 = input("word:")
         if pregunta_3 == "red":
           print(">>>",ing_2_esp["red"])
         elif pregunta_3 == "green":
             print(">>>",ing_2_esp["green"])
         elif pregunta_3 == "blue":
            print(">>>",ing_2_esp["green"])
         else:
            print("No sabemos la traduccion")
        
            
    

