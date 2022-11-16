# Posibles posiciones del jugador
# centro / izquierda / derecha / final

print("""Bienvenido a la mazmorra del PÁJARO CARPINTERO
OPCIONES:
- izquierda
- centro
- derecha""")

posicionDelJugador = input("En qué puerta quieres empezar? ")

tenemosLlave = False

puertaAbierta = False

#Esto se ejecuta de forma infinita
while True:

    #SALA CENTRAL
    if posicionDelJugador == "centro":
        print("ESTÁS EN LA SALA CENTRAL")
        print("- izquierda")
        print("- derecha")
        seleccion = input("Selecciona una puerta para avanzar: ")
        if seleccion == "izquierda":
            posicionDelJugador = "izquierda"
        elif seleccion == "derecha":
            posicionDelJugador = "derecha"
        else:
            print("Opción incorrecta")


    #SALA DE LA PUERTA
    elif posicionDelJugador == "derecha":
        print(""
              "ESTÁS EN LA SALA DE LA DERECHA")
        print("""- izquierda
- avanzar""")
        seleccion = input("Qué deseas hacer? ")
        if seleccion == "izquierda":
            posicionDelJugador = "centro"
        elif seleccion == "avanzar" and tenemosLlave == True:
            posicionDelJugador = "final"
        elif seleccion == "avanzar" and tenemosLlave == False:
            print("UPS! Parece que necesitas una llave para avanzar!")
        else:
            print("Opción incorrecta")


    #SALA DE LA LLAVE
    elif posicionDelJugador == "izquierda":
        print("ESTÁS EN LA SALA DE LA IZQUIERDA")
        print("- derecha")
        if tenemosLlave == False:
            print("- obtener [llave detectada!]")
        seleccion = input("Selecciona la opción: ")
        if seleccion == "derecha":
            posicionDelJugador = "centro"
        if seleccion == "obtener" and tenemosLlave == False:
            tenemosLlave = True
            print("Llave obtenida!")
        else:
            print("Opción incorrecta")

    #ÚLTIMA SALA
    elif posicionDelJugador == "final":
        print("Estás en la sala final")
        print("""Qué es lo que más le gusta a tu León bonito? CUIDADO! Si te equivocas se destruirá la mazmorra y no podrás escapar nunca!
        - chupa pija
        - meta quest 2""")
        seleccion = input("Selecciona una opción: ")
        if seleccion == "chupa pija":
            print("ENHORABUENA! HAS ESCAPADO DE LA MAZMORRA!")
            exit()
        elif seleccion == "meta quest 2":
            print("HAS MUERTO!")
            exit()

    #NO ES CORRECTA LA SALA
    else:
        print("Puerta incorrecta!")
        seleccion = input(" -escribe 'volver a intentar'")
        if seleccion == "volver a intentar":
            posicionDelJugador = "centro"