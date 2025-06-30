print('''
           mm###########mmm
        m####################m
      m#####`"#m m###"""'######m
     ######*"  "   "   "mm#######
   m####"  ,             m"#######m
  m#### m*" ,'  ;     ,   "########m
  ####### m*   m  |#m  ;  m ########
 |######### mm#  |####  #m##########|
  ###########|  |######m############
  "##########|  |##################"
   "#########  |## /##############"
     ########|  # |/ m###########
      "#######      ###########"
        """"""       """""""""
''')
print("Es un día común y decides visitar Tecomán, elije sabiamente tus decisiones 🥶")
print("Por donde quires llegar? ")
decision1 = input('''
  A) Tomo un avión
  B) Me voy por la salada
  C) Tomo casetas
                  
  Respuesta: ''').upper()

if decision1 == "A":
  print("Como va haber aviones para teco pa 😆")
elif decision1 == "C":
  print("Apoco si muy fino, pierdes por soberbio")
elif decision1 == "B":
  print("\nUn poco arriesgado de tu parte pero sigues vivo")

  print("Te topas con un par de soldados con tenis 🥶, que haces?")
  decision2 = input('''
    A) Me regreso
    B) Lo soborno
    C) Calma y elixir
                    
    Respuesta: ''').upper()
  
  if decision2 == "A":
    print("En tu intento de escape se te poncha una llanta y te cobran piso")
  elif decision2 == "B":
    print("Por querer pasarte de listo de balean")
  elif decision2 == "C":
    print("\nTu tranquilidad dió frutos y pasaste clean")

    print("Has llegado a teco, a donde quieres ir?")

    decision3 = input('''
    A) Citrojugos
    B) La playa
    C) Casa de Luis
                    
    Respuesta: ''').upper()

    if decision3 == "A":
      print("Que buena decisión Padrino has ganado el juego")
    elif decision3 == "B":
      print("No muy original de tu parte, pierdes por basado")
    elif decision3 == "C":
      print("Mejor mierda")
    else:
      print("Para tonto no se estudia, no hay esa opción")

  else:
    print("Para tonto no se estudia, no hay esa opción")

else:
  print("Para tonto no se estudia, no hay esa opción")

print("\nGracias por jugar lindura")