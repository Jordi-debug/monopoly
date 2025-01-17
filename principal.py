import random

def inicioPartida():
    global jugadores
    listaJugadores = []

    for key in jugadores:
        listaJugadores.append(key)
    random.shuffle(listaJugadores)

    inicialesJugadores = []

    for jugadores in listaJugadores:
        if jugadores == "groc":
            inicialesJugadores.append("G")
        elif jugadores == "vermell":
            inicialesJugadores.append("V")
        elif jugadores == "blau":
            inicialesJugadores.append("B")
        elif jugadores == "taronja":
            inicialesJugadores.append("T")

    calles[12]['Ocupacion'].extend(inicialesJugadores) #calles[12] es la casilla de salida
    
    return None


def imprimir_tablero(calles):
    # Tablero inicial con posiciones que serán llenadas por los nombres de las calles

    tablero = [
        [calles[0]["Nombre"], calles[1]["Nombre"], calles[2]["Nombre"], calles[3]["Nombre"], calles[4]["Nombre"], calles[5]["Nombre"], calles[6]["Nombre"]],
        [calles[23]["Nombre"], "", "", "", "", "",calles[7]["Nombre"]],
        [calles[22]["Nombre"], "", "", "", "", "",calles[8]["Nombre"]],
        [calles[21]["Nombre"], "", "", "", "", "",calles[9]["Nombre"]],
        [calles[20]["Nombre"], "", "", "", "", "",calles[10]["Nombre"]],
        [calles[19]["Nombre"], "", "", "", "", "",calles[11]["Nombre"]],
        [calles[18]["Nombre"], calles[17]["Nombre"], calles[16]["Nombre"], calles[15]["Nombre"], calles[14]["Nombre"], calles[13]["Nombre"], calles[12]["Nombre"]],
    ]

    # Definir el tamaño de las casillas
    ancho_casilla = 12 #Solo funciona si es 12
    alto_casilla = 2 #No funciona bien si este valor no es 1 o 2.
    
    # Función auxiliar para crear bordes horizontales
    def crear_borde_horizontal(cantidad, fila): #Esta función se usa dentro del bucle for para crear las líneas horizontales
        if fila[0] != "" and fila[1] == "": #Si el primer valor del array de la iteración del bucle no es "" y el segundo valor es "", quiere decir que es uno de los arrays
                                            #que tiene que dejar huecos en medio
                                            
            if tablero.index(fila) <= len(tablero) -3: #Si el index de la fila (que es cada iteracion del bucle for), es menor o igual que la cantidad de arrays en tablero
                if tablero.index(fila) == len(tablero) - 3:
                    return "+" + ("-" * ancho_casilla + "+ ") + historial[2].ljust(63) + "+" + ("-" * ancho_casilla + "+")
                elif tablero.index(fila) == len(tablero) - 4:
                    return "+" + ("-" * ancho_casilla + "+ ") + historial[5].ljust(63) + "+" + ("-" * ancho_casilla + "+")
                elif tablero.index(fila) == len(tablero) - 5:
                    return "+" + ("-" * ancho_casilla + "+ ") + historial[8].ljust(63) + "+" + ("-" * ancho_casilla + "+")
                elif tablero.index(fila) == len(tablero) - 6:
                    return "+" + ("-" * ancho_casilla + "+ ") + historial[11].ljust(63) + "+" + ("-" * ancho_casilla + "+")
                
        return "+" + ("-" * ancho_casilla + "+") * cantidad
    

    # Función auxiliar para crear contenido de una fila
    def crear_fila_contenido(fila):
        resultado = ""
        barra = "|"
        iteracion = 0

        for elemento in fila:
            if elemento == "":
                elemento = " " * ancho_casilla  # Espacio vacío si no hay casilla
            else:
                elemento = elemento.ljust(ancho_casilla)  # Poner el nombre a la izquierda de la casilla
                if iteracion == 0:
                    nuevaString = elemento[:-1] + " |"
                else:
                    nuevaString = elemento[:-1] + "|"
                elemento = nuevaString
                elemento = nuevaString
            if fila[0] and fila[1] == "":
                resultado += barra #la barra se añade al principio, aunque luego igualmente es reemplazada por otra barra igual, pero si no estuviera se reemplazarían letras o espacios,
                                    #por lo que no cerraría bien el cuadrado
                if barra != "":     #Sí la variable barra no está vacía (ya que después en esta misma iteracion se vacía para que solo se use una vez en todo el bucle)
                    resultado += elemento + "".ljust(0)
                    
                else:
                    if elemento.replace(" ", "") != "":
                        if fila.index(elemento[:-1].replace(" ","")) <= len(fila) -1: #elemento[:-1].replace(" ","") es porque elemento sin modificaciones es "ejemplo           |", así que
                                                                                        #no lo encontraría en el array de fila al no coincidir con ninguno de los valores
                            resultado += "| " + elemento

                barra = ""
            else:
                resultado += " " + elemento
                
            iteracion += 1
                     
        nuevoEl = "|" + resultado[1:] #Esto lo que hace es una vez este el texto completo, reemplaza el primer valor del string con "|", para cerrar la caja.
        resultado = nuevoEl  


        
        return resultado
    
    # Imprimir la parte superior del tablero
    print(crear_borde_horizontal(len(tablero[0]), ["a", "a", "a"])) #Aquí el ["a", "a", "a"] es porque la funcion requiere un array como parámetro, pero no hace nada con el en esta ocasión
    
    # Imprimir las filas con contenido
    iteracion = 0
    histIt = 13
    for fila in tablero:
        
        for _ in range(alto_casilla):  # Altura de cada casilla (varias líneas por fila)
            if _ == 0:  # Contenido en la línea de arriba de la casilla
                if tablero.index(fila) >= 1 and tablero.index(fila) < 6:
                    txt = crear_fila_contenido(fila)
                    lineaSeparada = txt.split("|")
                    lineaSeparada[2] = historial[histIt]
                    histIt -= 3
                    lineaJunta = f"|" + f"{lineaSeparada[1]}" + "| " f"{lineaSeparada[2]}".ljust(65) + "|" + f"{lineaSeparada[3]}".ljust(12) + "|"
                    print(lineaJunta)
                else:
                    print(crear_fila_contenido(fila))
            else:  # Líneas vacías para la altura

                if iteracion == 0 or iteracion == 6:  #Según la iteracion del bucle for, añade barras verticales y la ocupacion de cada calle para la iteracion 0 y 6, es decir la primera y la última
                    if iteracion == 0:
                        txt = f"|" + f"".join(calles[0]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[1]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[2]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[3]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[4]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[5]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[6]['Ocupacion']).ljust(12) + f"|"
                    if iteracion == 6:
                        txt = f"|" + f"".join(calles[18]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[17]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[16]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[15]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[14]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[13]['Ocupacion']).ljust(12) + f"|" + f"".join(calles[12]['Ocupacion']).ljust(12) + f"|"
                    print(txt)
                    
                else:
                    if iteracion == 1:
                        txt = f"|" + f"".join(calles[23]['Ocupacion']).ljust(12) + f"| " + f"{historial[12]}".ljust(63) + f"|" + f"".join(calles[7]['Ocupacion']).ljust(12) + f"|"
                    if iteracion == 2:
                        txt = f"|" + f"".join(calles[22]['Ocupacion']).ljust(12) + f"| " + f"{historial[9]}".ljust(63) + f"|" + f"".join(calles[8]['Ocupacion']).ljust(12) + f"|"
                    if iteracion == 3:
                        txt = f"|" + f"".join(calles[21]['Ocupacion']).ljust(12) + f"| " + f"{historial[6]}".ljust(63) + f"|" + f"".join(calles[9]['Ocupacion']).ljust(12) + f"|"
                    if iteracion == 4:
                        txt = f"|" + f"".join(calles[20]['Ocupacion']).ljust(12) + f"| " + f"{historial[3]}".ljust(63) + f"|" + f"".join(calles[10]['Ocupacion']).ljust(12) + f"|"
                    if iteracion == 5:
                        txt = f"|" + f"".join(calles[19]['Ocupacion']).ljust(12) + f"| " + f"{historial[0]}".ljust(63) + f"|" + f"".join(calles[11]['Ocupacion']).ljust(12) + f"|"
                    
                    print(txt)
                iteracion += 1
        print(crear_borde_horizontal(len(fila), fila))  # Bordes inferiores de cada fila


calles = [
    {"Nombre": "Parking", "Ocupacion": ["G"]},         #0
    {"Nombre": "Urquinoa", "Ocupacion": ["V"]},        #1
    {"Nombre": "Fontan", "Ocupacion": ["B"]},          #2
    {"Nombre": "Sort", "Ocupacion": ["G"]},            #3
    {"Nombre": "Rambles", "Ocupacion": ["B"]},         #4
    {"Nombre": "Pl.Cat", "Ocupacion": ["G", "V"]},          #5
    {"Nombre": "Anr pró", "Ocupacion": ["R"]},         #6
    {"Nombre": "Angel", "Ocupacion": ["G"]},           #7
    {"Nombre": "Augusta", "Ocupacion": ["V"]},         #8
    {"Nombre": "Caixa", "Ocupacion": ["R"]},           #9
    {"Nombre": "Balmes", "Ocupacion": ["RV"]},          #10
    {"Nombre": "Gracia", "Ocupacion": ["G"]},          #11
    {"Nombre": "Sortida", "Ocupacion": []},         #12
    {"Nombre": "Lauria", "Ocupacion": ["R"]},          #13
    {"Nombre": "Rosell", "Ocupacion": []},          #14
    {"Nombre": "Sort2", "Ocupacion": []},           #15
    {"Nombre": "Marina", "Ocupacion": []},          #16
    {"Nombre": "Consell", "Ocupacion": []},         #17
    {"Nombre": "Presó", "Ocupacion": []},           #18
    {"Nombre": "Muntan", "Ocupacion": []},          #19
    {"Nombre": "Aribau", "Ocupacion": ["G"]},          #20
    {"Nombre": "Caixa2", "Ocupacion": []},          #21
    {"Nombre": "S.Joan", "Ocupacion": ["A"]},          #22
    {"Nombre": "Aragó", "Ocupacion": []}            #23
]

jugadores = {
    "blau":{
        "Carrers":None,
        "Diners":2000,
        "Carta Especial":None
        
    },
    "groc":{
        "Carrers":None,
        "Diners":2000,
        "Carta Especial":None
    },
    "taronja":{
        "Carrers":None,
        "Diners":2000,
        "Carta Especial":None
    },
    "vermell":{
        "Carrers":None,
        "Diners":2000,
        "Carta Especial":None
    }
}



# Mi idea con el historial es que siempre tenga este número de valores, aunque estén vacíos y parezca que no haya nada (""), porque en el caso de que se borren valores dará error
# al intentar buscar el valor en el index 13 por ejemplo y esté fuera del rango del array

historial = [
    "1.  Ejemplo alguien hace algo",
    "2.  Pasa esto",
    "3.  ABCD",
    "4.  Compra una casa",
    "5.  Vende una propiedad",
    "6.  Ha pasado por la salida",
    "7.  A Vermell no se le ocurren ejemplos",
    "8.  Ejemplo",
    "9.  Hola",
    "10. que",
    "11. Vermell compra un hotel",
    "12. Blau ha ganado 2000€",
    "13. Groc ha entrado en la prisión",
    "14. Taronja hace algo no se me ocurren más ejemplos"
]

inicioPartida()
imprimir_tablero(calles)


#Hay varios problemas con este tablero, el primero es que seguramente al poner qué jugador está en X casilla, toda la linea se moverá, desencajando el tablero, #SOLUCIONADO
#El segundo problema es que el hueco del medio no está "vacio", simplemente son espacios en blanco así que no sabría cómo hacer que saliera el historial por ahí. #Solucionado????
#El tercer problema es que es un código muy complicado y ni yo sé del todo por qué funciona bien, así que cualquier modificación por mínima que sea será muy difícil de hacer.