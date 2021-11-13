import random
MIN=0
MAX=0
maximo_intentos=0
contador=1
# Ahora se creará un menú con una selección de diversos niveles, que afectarán a la dificultad del juego

while True:
    nivel=input("Seleccione que nivel de dificultad quiere probar en esta partida, las opciones son:nivel simple, nivel intermedio, nivel avandado y si te atreves nivel experto   ")
    try:
    
        if nivel== "nivel simple":
            MAX=100
            maximo_intentos=5
            break
        elif nivel=="nivel intermedio":
            MAX=1000
            maximo_intentos=15
            break
        elif nivel=="nivel avanzado":
            MAX=1000000
            maximo_intento=25
            break
        elif nivel== "nivel experto":
            MAX=1000000000000
            maximo_intento=35
            break
    except:
            pass




    # Ahora vamos a corroborar que el número elegido, es un número natural, y este...
    # .... se establece entre los intervalos de numeros naturales establecidos por el juego.  

    
    def pedir_numero(minimo=MIN,maximo=MAX):
       
        while True:
            elegido=input("Elige un número:  ")  
            try:
                elegido=int(elegido)
            except:
                pass
            if minimo<= elegido <= maximo:
                break
            elif elegido<minimo or elegido>maximo:
                print("Has introducido un número que está fuera de los intervalos del juego, escribe otro")
        return elegido        
            
                
    
               
                


# Ahore llevaremos a cabo una complementación del juego, si el jugador no ve muy claro que vaya a poder ganar el juego..
# ... Le vamos a ofrecer la ayuda de decirle entre que intervalos está el número que busca, de esta manera el jugador...
#.., tendrá una referencia y una idea más clara del número que está buscando


def complementacion():
    pista= input("¿Quieres recibir una pista a cerca del nivel que estás jugando?  Responder afirmativo o negativo")
    try:
        if pista=="afirmativo":
            print(" el número está ccomprendido entre" +str(MIN))+ "y" + str(MAX)+":"
        elif pista=="negativo":
            print("No creo que vayas sobrado, pero si tienes confianza en ti mismo adelante")
    except:
        pass
    return pista



# Ahora procederemos a plantear las condiciones del ejercicio, el cual irá indicando como de encaminado...
#... vas en la partida que estás jugando, si has ganado, y si es el caso en cuantos intentos lo has hecho



numero=random.randint(MIN,MAX)
minimo=MIN
maximo=MAX
print("Has empezado el juego, escribe un número")

contador=1

while True:
    jugada =pedir_numero(minimo,maximo)
    if jugada<numero:
        contador=contador+1
        print("El número que has escrito es demasiado pequeño, sigue intentándolo")
    elif jugada>numero:
        contador=contador+1
        print("El número que has escrito es demasiado grande, sigue intentándolo")

    else:
        print("Ha ganado el juego eres un campeón")
        contador=contador+1
        print("Enhorabuena, has superado el juego, para esto has necesitado",contador,"intentos, no está mal para tu edad")
        break












