import re
import random
import datetime
import json
from os import system
system("cls")
def traer_datos_archivo(path:str)->list:
    """
Brief: La función traer_datos_archivo recibe como parámetro un path que indica la ubicación del archivo a leer, y retorna una lista de diccionarios, donde cada diccionario representa a un guerrero y contiene la información de su id, nombre, raza, poder de pelea, poder de ataque y habilidades.
Parameters:path: una cadena de caracteres que indica la ubicación del archivo a leer.
Return:lista_guerrero: una lista de diccionarios, donde cada diccionario representa a un guerrero y contiene la información de su id, nombre, raza, poder de pelea, poder de ataque y habilidades. 
    """
    with open(path, "r", encoding="utf-8") as archivo:     
        lista_guerrero = []
        dicc = {}
        for line in archivo:
            info = re.split(",", line)
            dicc = {'id': info[0], 'nombre': info[1],'raza': info[2],'poder_pelea': info[3],'poder_ataque': info[4],'habilidades': info[5]}
            lista_guerrero.append(dicc)
            for i in range(len(lista_guerrero)):
                lista_guerrero[i]['habilidades'] = re.sub("[$%\\n]+","",lista_guerrero[i]['habilidades'])
                lista_guerrero[i]['habilidades'] = re.sub(" \|","|",lista_guerrero[i]['habilidades'])
        return lista_guerrero

#######################################################################################################################
def crear_lista_algo(clave:str,path:str)->list:
    """ 
Brief  Esta función toma una clave y una ruta de archivo como entrada y devuelve una lista de valores correspondientes a la clave en cada diccionario de la lista.
Parameters:

clave (str): Una cadena que representa la clave del diccionario que se quiere extraer.
path (str): Una cadena que contiene la ruta del archivo que se quiere leer.
Returns:

lista_algo_creada (list): Una lista de valores extraídos de cada diccionario de la lista que corresponden a la clave proporcionada.
    """
    lista_algo = traer_datos_archivo(path)
    lista_algo_creada = []
    for guerrero in lista_algo:
        algo  = guerrero[clave]
        lista_algo_creada.append(algo) 
    return lista_algo_creada

def setear_lista(clave:str)->set:
    """ 
Parámetros: clave: una cadena de caracteres que indica la clave que se va a utilizar para crear la lista.
Brief: setea la lista que recibe
Return: lista_filtrada: una lista seteadad del valor que reciba el path.
    """
    lista_recibe = crear_lista_algo(clave, "DBZ.csv")
    lista_filtrada = set(lista_recibe)
    return lista_filtrada
def listar_cantidad_por_raza(clave:str)->None:
    """ 
    Parámetros:clave (str): clave que se utilizará para filtrar la información del archivo.
                path (str): ruta del archivo que se va a leer.
Brief: Esta función recibe una clave y una ruta de archivo, utiliza la función traer_datos_archivo y crear_lista_algo para crear una lista con la información que corresponde a la clave recibida. Luego, crea un diccionario con la cantidad de guerreros por raza y finalmente imprime la cantidad de guerreros por cada raza.

Return: None
    """
    lista_info = crear_lista_algo(clave,"DBZ.csv")
    dicc = {}
    for contador_raza in lista_info:
        if contador_raza in dicc:
            dicc[contador_raza] += 1
        else:
            dicc[contador_raza] = 1
    for raza,cantidad in dicc.items():
        print(f"{raza}: {cantidad}")
                    

#listar_cantidad_por_raza(lista_guerrero,'raza')

def listar_personajes_por_raza(clave:str,lista:list)->None:
    """ 
    Parametros:
clave (str): la clave del diccionario que se usará para hacer la búsqueda.
path (str): la ruta del archivo .csv que contiene la información de los personajes.
Brief:
La función recibe una clave y una ruta de archivo. Luego, se crea una lista de los personajes a partir de los datos del archivo y se filtra la lista de acuerdo con la clave recibida. Después, se itera sobre la lista filtrada para imprimir los nombres y poderes de ataque de los personajes que pertenecen a cada raza en la lista.

Return:
La función no retorna nada, ya que solo imprime la información solicitada.
    """
    lista_filtrada = setear_lista(clave)
    for raza in lista_filtrada:
        print(raza)
        for guerreros in lista:
            if raza in guerreros[clave]:
                print(f"\tNombre: {guerreros['nombre']} -> Poder de ataque: {guerreros['poder_ataque']}")
        print("----------------------------------------------------------------")
            
#listar_personajes_por_raza(lista_guerrero,'raza')
###############################################################################################################################################


def crear_lista_habilidades(path:str)->list:
    """ 
Parameters:path: una cadena de caracteres que indica la ruta del archivo que contiene los datos.
Brief:La función "crear_lista_habilidades" recibe como parámetro una ruta de archivo, lee los datos del archivo y crea una lista con todas las habilidades de los personajes.
Return:La función retorna una lista de habilidades.
    """
    lista = traer_datos_archivo(path)
    lista_habilidades = []
    for i in lista:
        habilidad = i['habilidades'].split('|')
        lista_habilidades.extend(habilidad)   
    return lista_habilidades
def mostrar_habilidades(lista_info:list)->None:
    """ 
Parameters:lista_info (list): una lista de habilidades.
Brief:La función recibe una lista de habilidades y muestra por pantalla las habilidades sin repetir.
Return:La función no retorna nada (None).
    """
    for habilidades in set(lista_info):
        print(habilidades)

def ingresar_habilidad(path:str) ->str:
    """ 
Parameters:path: ruta del archivo donde se encuentran los datos de los personajes.

Brief: Esta función permite al usuario ingresar una habilidad y valida que esa habilidad se encuentre en la lista de habilidades obtenida del archivo de datos. Si la habilidad es válida, la función la retorna como un string.

Return:habilidad_ingresada: la habilidad ingresada por el usuario, si es válida y se encuentra en la lista de habilidades.
    """
    lista_habilidades = crear_lista_habilidades(path)
    validacion = True
    while validacion == True:
        habilidad_ingresada = input("Ingrese una habilidad: ")
        if habilidad_ingresada.capitalize() in lista_habilidades:
            validacion = False
            return habilidad_ingresada
        else:
            print("Error esa habilidad no existe")

def listar_personajes_por_habilidad(lista:list,path:str)->None:
    """ 
Parameters:path (str): la ruta del archivo que contiene los datos de los personajes.
    
Brief:La función "listar_personajes_por_habilidad" muestra los personajes que tienen una habilidad específica y su promedio de poder. Primero, se carga la lista de personajes y la lista de habilidades. Luego, se muestra al usuario la lista de habilidades disponibles y se le solicita que ingrese una habilidad. A continuación, se recorre la lista de personajes y se verifica si el personaje tiene la habilidad elegida. Si es así, se calcula el promedio de poder y se muestra el nombre del personaje junto con el promedio de poder.

Return:None. La función imprime por pantalla la información solicitada.
    """
    lista_habilidades = crear_lista_habilidades(path)
    mostrar_habilidades(lista_habilidades)
    habilidad_elegida = ingresar_habilidad(path)
    habilidad_elegida = habilidad_elegida.capitalize()
    for personaje in lista:
        if habilidad_elegida in personaje['habilidades']:
            poder_ataque = int(personaje['poder_ataque'])
            poder_pelea = int(personaje['poder_pelea'])
            promedio_poder = (poder_ataque + poder_pelea) / 2
            print(f"\tNombre: {personaje['nombre']} -> Promedio de poder: {promedio_poder}")



#listar_personajes_por_habilidad(lista_guerrero)
#######################################################
def mostrar_personajes(path:str):
    """ 
Parámetros:path: una cadena que indica la ruta del archivo que contiene los datos de los personajes.
Brief: Esta función lee los datos de un archivo CSV y muestra los nombres de los personajes en la consola.
Return: Esta función no retorna ningún valor.
    """
    lista = traer_datos_archivo(path)
    print("--------------PERSONAJES--------------")
    for personaje in lista:
        print(personaje['nombre'])
        
def ingresar_personaje(path:str) ->str:
    """ 
Parameters:path: una cadena de caracteres que indica la ruta del archivo de donde se leerán los datos.

Brief: La función permite al usuario ingresar un nombre de personaje y verificar si se encuentra en la lista de personajes del archivo. Si el personaje existe, la función devuelve su nombre.

Return:Una cadena de caracteres que indica el nombre del personaje ingresado por el usuario si se encuentra en la lista de personajes. Si el personaje no existe, la función no devuelve nada (None).
    """
    lista = traer_datos_archivo(path)
    mostrar_personajes(path)  
    validacion = True
    while validacion == True:
        nombre_personaje = input("Ingrese personaje: ")
        for i in lista:
            if nombre_personaje.lower() == i['nombre'].lower():
                validacion = False
                return nombre_personaje
                

def generar_personaje_random(path:str) ->str:
    """ 
Parameters:path : str
La ruta del archivo CSV que contiene la información de los personajes.
Brief:La función generar_personaje_random() genera aleatoriamente un personaje a partir de la lista de personajes que se encuentra en el archivo CSV.
Return:personaje_aleatorio['nombre']El nombre del personaje generado aleatoriamente.
    """
    lista = traer_datos_archivo(path)
    personaje_aleatorio = random.choice(lista)
    return personaje_aleatorio['nombre']


def comenzar_batalla(lista:list):
    """ 
    Parameters: 
        recibe la lista con los personajes y su informacion

    Brief:
        Esta función permite simular una batalla entre dos personajes, elegidos por el usuario y de manera aleatoria.
        Luego de realizar la batalla, se guarda el resultado en un archivo de texto, junto con la fecha y hora en que se realizó.

    Returns:
        bool: Retorna True si el usuario no desea continuar con la batalla, y False si desea seguir peleando.

    """
    opcion = False
    while opcion == False:
        fecha = datetime.datetime.now().strftime("%x - %X")
        nombre_personaje = ingresar_personaje("DBZ.csv")
        personaje_aleatorio = generar_personaje_random("DBZ.csv")
        for personaje in lista:
            if personaje['nombre'].lower() == nombre_personaje.lower():
                poder_ataque_elegido = int(personaje['poder_ataque'])
            if personaje['nombre'].lower() == personaje_aleatorio.lower():
                poder_ataque_aleatorio = int(personaje['poder_ataque'])
        with open("GANADORES_BATALLAS.txt","a", encoding="UTF-8") as archivo:
            if poder_ataque_aleatorio > poder_ataque_elegido:        
                archivo.writelines(f"El personaje: {personaje_aleatorio} ha ganado, poder: {poder_ataque_aleatorio}, {nombre_personaje} es el perdedor, poder: {poder_ataque_elegido}:(---{fecha}\n")
                print(f"El personaje: {personaje_aleatorio} ha ganado! SU PODER ES DE {poder_ataque_aleatorio}, {nombre_personaje} es un perderdor con un poder de {poder_ataque_elegido}:(---{fecha}\n")
            elif poder_ataque_elegido > poder_ataque_aleatorio:
                archivo.writelines(f"El personaje: {nombre_personaje} es el ganador, poder: {poder_ataque_elegido}, {personaje_aleatorio} es el perdedor,poder: {poder_ataque_aleatorio}---{fecha}\n")
                print(f"El personaje: {nombre_personaje} es el ganador!!, CON UN PODER DE {poder_ataque_elegido}, {personaje_aleatorio} es el perdedor JI JI JI JA con un poder de {poder_ataque_aleatorio}---{fecha}\n")
            else:
                archivo.writelines(f"{nombre_personaje} y {personaje_aleatorio} han empatado con un poder de {poder_ataque_elegido}----{fecha}\n")
                print(f"{nombre_personaje} y {personaje_aleatorio} han empatado con un poder de {poder_ataque_elegido}----{fecha}\n")
        respuesta = input("¿Desea continuar? (S/N) ")
        respuesta = respuesta.lower()
        if respuesta == 's':
            pass
        else:
            opcion = True
            return opcion
        
            
            
##################################################################################################################################################
def validar_entero(numero:str)->bool:
    """ 
    recibe como parametro un str y lo pasa a entero y lo devuelve
    """
    confirmacion = False
    if numero.isdigit() == True: 
        confirmacion = True    
        
    return confirmacion
def imprimir_menu()->None:
    """ 
    no recibe nada y se utiliza para crear el menu de opciones y imprimirlo
    """
    menu = ["-------","1.Traer datos","2.Listar cantidad de heroes por raza","3.Listar personajes de cada raza",
            "4.Buscar que personajes tienen una habilidad","5.Jugar batalla de personajes",
            "6.Guardar Json",
            "7.Leer Json","8.Borras historial","9.Salir","10.Otorgar poder"]
    for i in menu:
        print(i)
        
def mostrar_menu_principal()->int:
    """ 
    Parameters:
    Brief:mprime el menu principal y pide al usuario ingresar una opcion, luego la valida con la funcion validar_entero y la devuelve
    Return: pedir_opcion que es la opcion validada
    """
    print("Menu principal")
    imprimir_menu()
    pedir_opcion = input("Elija una opcion: ")
    validacion_int = validar_entero(pedir_opcion)
    if validacion_int == True:
        pedir_opcion = int(pedir_opcion)
        return pedir_opcion
    else:
        return -1 
    
    #################################################################################################
def guardar_json(path:str)->str:
    """ 
Parameters: path: Es un parámetro de tipo string que representa la ruta del archivo que se utilizará para cargar los datos de los personajes.
brief:su principal función es crear un archivo JSON con los personajes que cumplen con ciertos criterios de selección, cargando un diccionario con el nombre el poder 
y las habilidades de los que cumplen esa funcion. Sin embargo, en caso de existir algún error en la ejecución volvera al menu de inicio
return: de retorno se guarda el nombre del archivo.json para dsp poder leerlo en otra funcion
    """
    personajes = traer_datos_archivo(path)
    lista_raza = crear_lista_algo('raza', path)
    lista_habilidades = crear_lista_habilidades(path)
    diccionario_personajes = {}
    habilidad_ingresada = []
    diccionario_personajes['personaje'] = []
    validacion = True
    while validacion == True:
        print("================RAZAS================")
        for i in set(lista_raza):
            print(i)
        raza_ingresada = input("Ingresar una raza: ")
        print("================HABILIDADES================")
        for x in (lista_habilidades):
            print(x)
        habilidad_ingresada = input("Ingresar una habilidad: ") 
        for personaje in personajes:
            if habilidad_ingresada.lower() in personaje['habilidades'].lower() and raza_ingresada.lower() in personaje['raza'].lower():
                print(personaje['nombre'])
                habilidades = personaje['habilidades'].split("|")
                habilidades_filtradas = [habilidad for habilidad in habilidades if habilidad.lower() != habilidad_ingresada.lower()]
                print(habilidades_filtradas)
                diccionario_personajes['personaje'].append({'nombre':personaje['nombre'],'poder_de_ataque':personaje['poder_ataque'],'habilidades':habilidades_filtradas})
                nombre_archivo_guardado = f'{raza_ingresada.replace(" ","_")}_{habilidad_ingresada.replace(" ","_")}.json'
                with open(nombre_archivo_guardado,'w',encoding='utf-8') as file:
                    json.dump(diccionario_personajes,file,indent= 4,ensure_ascii=False)         
                    print("El archivo se guardo de forma correcta")     
                validacion = False
                
            else:
                pass
    return nombre_archivo_guardado 
    
    
def leer_json(guardado) ->None:
    """ 
    parameters: Recibe como parametro guardado el nombre del json
    breef: lo lee el json para mostrar que contiene
    return no retorna nada muestra directamente
    """
    with open(guardado,encoding='utf-8') as file:
        guardado = json.load(file)
        for personaje in guardado['personaje']:
            print(f"{personaje['nombre']}---Poder de ataque->{personaje['poder_de_ataque']}---Habilidades: {personaje['habilidades']}")
            
            
            
            
def agregar_poder_ataque(lista:list)->None:
    """ 
    parameters: recibe como parametro la lista la cual traemos del csv en la funcion de menu
    breef agrega un 50% de poder de pelea y un 70% de poder de ataque a los saiyan
    return no retorna nada ya que imprime por pantalla al ejecutarse
    """
    for saiyan in lista:
        if 'Saiyan' in saiyan['raza']:
            print(f"{saiyan['nombre']}")
            saiyan['poder_pelea']=float(saiyan['poder_pelea'])
            print(f"Poder pelea anterior: {saiyan['poder_pelea']}")
            saiyan['poder_pelea']= saiyan['poder_pelea'] * 1.5
            print(f"Poder pelea actua:{saiyan['poder_pelea']}")
            saiyan['poder_ataque']=float(saiyan['poder_ataque'])
            print(f"Poder ataque anterior: {saiyan['poder_ataque']}")
            saiyan['poder_ataque']= saiyan['poder_ataque'] * 1.7
            print(f"Poder ataque actua: {saiyan['poder_ataque']}")
            saiyan['habilidades'] += '| Transformacion nivel dios'
            print(f"Habilidades: {saiyan['habilidades'].split('|')}")
            with open("saiyan_cambiados.csv", "a", encoding= "utf-8") as archivo:
                archivo.writelines(f"Nombre: {saiyan['nombre']}, Poder de pelea---{saiyan['poder_pelea']},Poder ataque:--{saiyan['poder_ataque']}--{saiyan['habilidades'].split('|')}\n") 

def aplicacion_DBZ(path:str):

    """ 
    esta es la funcion principal la cual recibe la lista de heroes
    en base a la opcion que elija el usuario reutiliza las funciones creadas y pide que se muestre lo que el usuario desee
    no devuelve nada
    """
    opcion = mostrar_menu_principal()
    while opcion != 1:
        system("cls")
        print("Error, debe guardar los datos primero con la opcion 1")
        opcion = mostrar_menu_principal()
    else:
        while opcion != -1:
            match opcion:
                case 1:
                    lista_guerreros = traer_datos_archivo(path)
                    system("cls")
                    print("Datos importados correctamente")
                case 2:
                    listar_cantidad_por_raza('raza')
                case 3:
                    listar_personajes_por_raza('raza',lista_guerreros)
                case 4:
                    listar_personajes_por_habilidad(lista_guerreros,path)
                case 5:
                    seguir = comenzar_batalla(lista_guerreros)
                    if seguir == True:
                        pass
                case 6:
                    guardado = guardar_json("DBZ.csv")
                case 7:
                    if guardado == None:
                        print("No hay datos guardados")
                    else:
                        leer_json(guardado)
                case 8:
                    system("cls")
                case 9:
                    break
                case 10:
                    agregar_poder_ataque(lista_guerreros)
            opcion = mostrar_menu_principal()
            