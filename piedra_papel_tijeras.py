#Programa de piedra papel o tijeras

import random

juego = ["piedra", "papel", "tijeras"]

pregunta = "si"

while pregunta == "si":
    
    print("Juego de piedra papel o tijeras")
    respuesta = input("Cual elijes? : ")
    
    palabra_aleatoria = random.choice(juego)
    
    
    #piedra
    if respuesta == "piedra" and palabra_aleatoria == "piedra":
        print(f"La computadora elije: {palabra_aleatoria}")
        print("Empatan")
    
    elif respuesta == "piedra" and palabra_aleatoria == "papel":
        print(f"La computadora elije: {palabra_aleatoria}")
        print("Perdiste ")
    
    elif respuesta == "piedra" and palabra_aleatoria == "tijeras":
        print(f"La computadora elije: {palabra_aleatoria}")
        print("Ganaste! ")

    #papel
    elif respuesta == "papel" and palabra_aleatoria == "piedra":
        print(f"La computadora elije: {palabra_aleatoria}")
        print("Ganaste!")
    
    elif respuesta == "papel" and palabra_aleatoria == "papel":
        print(f"La computadora elije: {palabra_aleatoria}")
        print("Empataste")
    
    elif respuesta == "papel" and palabra_aleatoria == "tijeras":
        print(f"La computadora elije: {palabra_aleatoria}")
        print("Perdiste")

    #tijeras
    elif respuesta == "tijeras" and palabra_aleatoria == "piedra":
        print(f"La computadora elije: {palabra_aleatoria}")
        print("Perdiste")
    
    elif respuesta == "tijeras" and palabra_aleatoria == "papel":
        print(f"La computadora elije: {palabra_aleatoria}")
        print("Ganaste!")
        
    elif respuesta == "tijeras" and palabra_aleatoria == "tijeras":
        print(f"La computadora elije: {palabra_aleatoria}")
        print("Empataste")
        
    else:
        print("No elejiste correctamente ")
    
    print("\n")
    pregunta = input("Deseas seguir jungando? si|no: ")
    print("\n")

print("El juego ha terminado..")
    
    