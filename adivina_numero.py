#Adivina el numero
import random

"""
Entrada:


"""
numero = int(input("""Adivina el numero del 1 al 100...
"""))

respuesta = "si"

while respuesta == "si":
    
    numero_random = random.randint(0,100)
    
    while numero != numero_random:
        
        if numero < numero_random:
            print("Es mayor...\n")

        elif numero > numero_random:
            print("Es Menor...\n")
            
        numero = int(input("Escribe otro numero... "))

    print(f"Felicidades!! Adivinaste el numero: {numero}!!")
    
    respuesta = input("\nDeseas volver a jugar? si|no: ")
    print("-----------------------------------------------------------------")
    numero = int(input("""Adivina el numero del 1 al 100...
"""))
    
print("\nEl juego ha terminado...")

