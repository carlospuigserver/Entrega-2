import random
MIN=0
MAX=0

# Ahora se creará un menú con una selección de diversos niveles, que afectarán a la dificultad del juego

while True:
    nivel=input("Seleccione que nivel de dificultad quiere probar en esta partida, las opciones son:")
    ("nivel simple, nivel intermedio, nivel avandado y si te atreves nivel experto")
    try:
        if nivel== "nivel simple":
            MAX=100
            break
        elif nivel=="nivel intermedio":
            MAX=1000
            break
        elif nivel=="nivel avanzado":
            MAX=1000000
            break
        elif nivel== "nivel experto":
            MAX=1000000000000
            break
    except:
        pass


    # Ahora vamos a corroborar que el número elegido, es un número natural, y este...
    # .... se establece entre los intervalos de numeros naturales establecidos por el juego.  

    
    def pedir_numero (maximo=MIN, minimo=MAX):
        while True:
            elegido=input("Elige un número")
            try:
                elegido=int(elegido)
            except:
                pass
            if minimo<= elegido >=maximo:
                break
            elif elegido <=minimo or elegido>=maximo:
                print("El número que has elegido no pertenece a los intervalos definidos por el juego")
        return elegido        
                


# PARTE 1 
numero = pedir_numero("Introduzca el numero a adivinar") 
 
# PARTE 2 
while True: 
    intento = pedir_numero("Adivine el número") 
    if intento < numero: 
        print("Demasiado pequeño") 
    elif intento > numero: 
        print("Demasiado grande") 
    else: 
        print ("¡Ha ganado!" )
        break 

