# Script con los menus y submenus que se mostraran por pantalla

from os import system

def header(titulo):
    long=80
    long_palabra=len(titulo)
    print(" " + "-" * long)
    esp=(long-long_palabra)/2
    print("|" + " " * int(esp) + titulo + " " * int(esp) + " |")
    print(" " + "-" * long)

def principal():
    system("cls")
    header("BASE DE DATOS")
    print("Bienvenido a la base de datos 'disnet_drugslayer' del proyecto DISNET.")
    print("Cuenta con informacion sobre enfermedades a nivel fenotipico, biologico y farmacos.")
    print("\nPuede obtener diferentes tipos de informacion o funciones:")
    print("\n\t1. Informacion general")
    print("\n\t2. Informacion de los farmacos")
    print("\n\t3. Informacion de las enfermedades")
    print("\n\t4. Informacion de los efectos fenotipicos")
    print("\n\t5. Informacion de los targets")
    print("\n\t6. Borrados")
    print("\n\t7. Inserciones")
    print("\n\t8. Modificaciones")
    print("\n\t9. Salir")

def menu_1():
    system("cls")
    header("Informacion general")
    print("En esta ventana puedes obtener varios tipos de informacion:")
    print("\n\ta. Numero total")
    print("\n\tb. Primeras 10 instancias")

def menu_1_1():
    system("cls")
    header("Informacion general")

def menu_1_2():
    system("cls")
    header("Informacion general")
    print("En esta ventana puedes obtener las diez primeras instancias de:")
    print("\n\ta. Farmacos")
    print("\n\tb. Enfermedades")
    print("\n\tc. Efectos fenotipicos")
    print("\n\td. Dianas")

def menu_2():
    system("cls")
    header("Informacion de los farmacos")
    print("En esta ventana puedes obtener varios tipos de informacion:")
    print("\n\ta. Informacion general del farmaco")
    print("\n\tb. Sinonimos de un farmaco")
    print("\n\tc. Código ATC de un farmaco")

def menu_3():
    system("cls")
    header("Informacion de las enfermedades")
    print("En esta ventana puedes obtener informacion sobre las enfermedades:")
    print("\n\ta. Farmacos para una enfermedad")
    print("\n\tb. Farmaco y enfermedad con el mayor score de asociacion")

def menu_4():
    system("cls")
    header("Informacion de los efectos fenotipicos")
    print("En esta ventana podra consultar información de los efectos fenotípicos \nasociados un farmaco:")
    print("Opciones: a. Indicaciones del farmaco: muestra los efectos fenotipicos \n"
          "             que sean indicaciones para las cuales se utiliza el farmaco.\n")
    print("          b. Efectos secundarios de un fármaco: muestra quellos efectos \n"
          "             fenotípicos categorizados como efectos secundarios generados\n"
          "             por el farmaco ordenados de forma descendiente en base a la \n"
          "             evidencia de esta asociacion.\n")

def menu_5():
    system("cls")
    header("Informacion de los targets")
    print("En esta ventana puedes obtener informacion sobre las dianas de un farmaco:")
    print("\n\ta. Dianas de un tipo dado")
    print("\n\tb. Organismo al cual se asocian un mayor numero de dianas")

def menu_6():
    system("cls")
    header("Borrados")
    print("En esta ventana podras borrar asociacion entre un farmaco y una enfermedad \n"
          "con un score muy bajo. En pantalla se muestran las 10 relaciones con un score\n "
          "mas bajo. Escriba el nombre del farmaco y el nombre de la enfermedad separadas por un guión (-).")

def menu_7():
    system("cls")
    header("Inserciones")
    print("En esta ventana podras añadir una nueva enfermedad con su farmaco asociado.")

def menu_8():
    system("cls")
    header("Modificaciones")
    print("En esta ventana podrás establecer como 0 el score de aquellas asociaciones \n"
          "entre fármacos y efectos secundarios por debajo del valor deseado.")

def final(database):
    header("Adios")
    print("Sus consultas se han guardado en el archivo 'Resultados.txt'.")
    database.close()
    exit()
