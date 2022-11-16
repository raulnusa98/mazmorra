
#mazmorrita!!

troncho = False
porrito = False
tenemosLlave1 = False

print("BIENVENIDO A LA MAZMORRA DEL PRIMITO LUCAS!")  
print("""Qué posición quieres empezar?
- izquierda
- centro
- derecha""")

posicionJugador = input("Selecciona una opción: ")

while(True):
#SALA IZQUIERDA  

  if posicionJugador == "Izquierda":
    print("""ESTAS EN LA SALA DE LA IZQUIERDA
    - Bajar
    - Derecha""")
    if troncho == False:
      print("    - porrito [Gorila Glue]")
    respuesta = input("Cómo deseas continuar?")
    if respuesta == "Derecha":
      posicionJugador = "Centro"
    elif respuesta == "Bajar":
       posicionJugador = "Sotano"
    elif respuesta == "Porrito":
      troncho = True   
    else:
      print("Opción incorrecta!")

#SALA CENTRAL

  elif posicionJugador == "Centro":
    print("ESTÁS EN LA SALA CENTRAL!")
    respuesta = input("""Cómo deseas continuar?
    - Izquierda
    - Derecha""")
    if respuesta == "Izquierda":
      posicionJugador = "Izquierda"
    elif respuesta == "Derecha":
      posicionJugador = "Derecha"
    else:
      print("Opción incorrecta!")

#SALA DERECHA

  elif posicionJugador == "Derecha":
    print("""ESTÁS EN LA SALA DE LA DERECHA
    - Abrir
    - Izquierda""")
    respuesta = input("Cómo deseas continuar?")
    if respuesta == "Abrir" and tenemosLlave1 == False:
      print("UPS! PARECE QUE NECESITAS UNA LLAVE PARA AVANZAR")
      posicionJugador = "Derecha"
    elif respuesta == "Abrir" and tenemosLlave1 == True:
      posicionJugador = "Final"
    elif respuesta == "Izquierda":
      posicionJugador = "Centro"
    else:
      print("Opción incorrecta!")

#SOTANOwqerw2r234r23r23r2

  elif posicionJugador == "Sotano":
    print("ESTÁS EN EL SÓTANO!")
    print("- Subir")
    if porrito == False:
      print("- Coger [porrito Rirri]")
    if tenemosLlave1 == False:
      print("- Obtener [Llave detectada!]")
    respuesta = input("Qué deseas hacer?") 
    if respuesta == "Coger":
      porrito = True     
      fumar = input("""Quieres fumártelo?
      - Si
      - No""")
      if fumar == "Si":
        print("FUMAR ES MALO!!!!")
        posicionJugador = "Sotano"
      elif fumar == "No":
        print("BIEN HECHO! FUMAR ES MALO!!")
        posicionJugador = "Sotano"
    elif respuesta == "Obtener":
      tenemosLlave1 = True
      posicionJugador = "Sotano"
    elif respuesta == "Subir":
      posicionJugador = "Izquierda"
    else:
      print("Opción incorrecta!")

#SALA FINAL

  elif posicionJugador == "Final":
    if troncho == True and porrito == True:
      print("ESTÁS EN LA SALA FINAL! CUIDADO! EL PRIMITO LUCAS TE ESTÁ ESPERANDO Y ES MUY AGRESIVO!")
      print("PARECE QUE LLEVAS ALGO QUE PUEDE CALMARLO!")
      print("- Gorila [darle porrito Gorila]")
      print("- Rirri [darle porrito Rirri]")
      print("- Calmar [intentar calmar al primito con palabras]")
      accion = input("- Qué deseas hacer ")
      if accion == "Gorila":
        print("BIEN! PARECE QUE LE HA GUSTADO! TE HA DEJADO MARCHAR!")
        exit()
      elif accion == "Rirri":
        print("NO ES SU HIERBA FAVORITA! PERO PARECE QUE TE DA OTRA OPORTUNIDAD!")
        print("- Gorila [dale porrito Gorila]")
        print("- Calmar [intentar calmar al primito con palabras]")
        segundo = input("Qué deseas hacer?")
        if segundo == "Gorila":
          print("ENHORABUENA! LE HA ENCANTADO AL PRIMITO Y TE HA DEJADO ESCAPAR!")
          exit()
        elif segundo == "Calmar":
          print("HAS MUERTO!")
          exit()
        else:
          print("Opción incorrecta!")
      elif accion == "Calmar":
        print("EL PRIMITO NO SE CALMA CON PALABRAS! TE HA MATADO! :(")
        exit()
      else:
        print("Opción incorrecta!")
        posicionJugador == "Sotano"
    elif troncho == False and porrito == True:
      print("Parece que te falta algún objeto que puede ayudarte en la sala final!")
      print("Deseas continuar?")
      respuesta = input("""- Si
- No""")
      if respuesta == "Si":
        print("- Rirri [darle porrito Rirri]")
        print("- Calmar [intentar calmar al primito con palabras]")
        respuesta = input("Qué deseas hacer? ")
        if respuesta == "Rirri":
          print("Parece que no es su hierba favorita! Pero te perdona y te da otra oportunidad!")
          print("Volver más tarde?")
          respuesta = input("Si o no?")
          if respuesta == "Si":
            posicionJugador = "derecha"
          if respuesta == "No":
            print("Calmar")
            respuesta = input("Qué deseas hacer? ")
            if respuesta == "calmar":
              print("HAS MUERTO! EL PRIMITO SOLO QUIERE GORILA GLUE!")
              exit()
      elif respuesta == "No":
        posicionJugador = "Sotano"
    elif troncho == True and porrito == False:
      print("Parece que te falta algún objeto que puede ayudarte en la sala final!")
      print("Deseas continuar?")
      respuesta = input("""- Si
- No""")
      if respuesta == "Si":
        print("- Gorila [darle porrito Gorila Glue]")
        print("- Calmar [intentar calmar al primito con palabras]")
        respuesta = input("Qué deseas hacer? ")
        if respuesta == "Gorila":
          print("ENHORABUENA! AL PRIMITO LUCAS LE HA ENCANTADO Y TE HA DEJADO ESCAPAR!")
        if respuesta == "Calmar":
          print("HAS MUERTO! EL PRIMITO SOLO QUERÍA SU GORILA GLUE!")
  
  else:
    print("Opción incorrecta! Por lo que aparecerás en una sala aleatoria!")
    posicionJugador = "Centro"