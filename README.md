#parcial1
Parcial 1 DBZ
Resumen:
Lo que hago en este trabajo es crear un programa es gestionar la coleccion de personajes de Dragon Ball que nos es brindada en un archivo de formato CSV
Este lo separo por ID, nombre, raza, poderes, y habilidades.
Este programa me permite enlistar mediante razas, nombres y habilidades, ademas mediante estas mismas me permite buscar la informacion que quiera obtener.
Este es un ejemplo agrupado de todo lo que venimos viendo en clases con respecto al ordenamiento de datos en PYTHON

#ALUMNO
Matias Di Girolamo 
DIVISION: 1D
LEGAJO: 113597

#CONSIGNA

Necesitamos crear un programa para poder gestionar nuestra colección de personajes de Dragon Ball. Para
ello, disponemos de un archivo CSV con el siguiente formato:
Id, Nombre, Raza, Poder de pelea, Poder de ataque, Habilidades
Por ejemplo:
"1", "Goku", "Saiyan", "500000", "10000", "Kamehameha|$%Genki Dama|$%Super Saiyan"

Debes realizar un menú que permita al usuario trabajar con las siguientes opciones:
1. Traer datos desde archivo: guardará el contenido del archivo DBZ.csv en una colección. Tener en
cuenta que tanto razas y habilidades deben estar guardadas en algún tipo de colección debido a que
un personaje puede tener más de una raza y más de una habilidad.
2. Listar cantidad por raza: mostrará todas las razas indicando la cantidad de personajes que
corresponden a esa raza.
3. Listar personajes por raza: mostrará cada raza indicando el nombre y poder de ataque de cada
personaje que corresponde a esa raza. Dado que hay personajes que son cruza, los mismos podrán
repetirse en los distintos listados.
4. Listar personajes por habilidad: el usuario ingresa la descripción de una habilidad y el programa
deberá mostrar nombre, raza y promedio de poder entre ataque y defensa.
5. Jugar batalla: El usuario seleccionará un personaje. La máquina selecciona otro al azar. Gana la
batalla el personaje que más poder de ataque tenga. El personaje que gana la batalla se deberá
guardar en un archivo de texto, incluyendo la fecha de la batalla, el nombre del personaje que ganó y
el nombre del perdedor. Este archivo anexará cada dato.
6. Guardar Json: El usuario ingresa una raza y una habilidad. Generar un listado de los personajes que
cumplan con los dos criterios ingresados, los mismos se guardarán en un archivo Json. Deberíamos
guardar el nombre del personaje, el poder de ataque, y las habilidades que no fueron parte de la
búsqueda. El nombre del archivo estará nomenclado con la descripción de la habilidad y de la raza.
Por ejemplo: si el usuario ingresa Raza: Saiyan y Habilidad: Genki Dama
Nombre del archivo:
Saiyan_Genki_Dama.Json
Datos :
Goten - 3000 - Kamehameha + Tambor del trueno
Goku - 5000000 - Kamehameha + Super Saiyan 2
7. Leer Json: permitirá mostrar un listado con los personajes guardados en el archivo Json de la opción
6
8. Salir del programa.
