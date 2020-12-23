# Script con los menus y submenus que se mostraran por pantalla

from os import system

def header(titulo):
    long = 80
    long_palabra = len(titulo)
    print(" " + "-" * long)
    esp = (long - long_palabra)/2
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
    print("\nIntroduzca 'esc' para volver al menu principal.")

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
    print("\nIntroduzca 'esc' para volver al menu principal.")

def menu_2():
    system("cls")
    header("Informacion de los farmacos")
    print("En esta ventana puedes obtener varios tipos de informacion:")
    print("\n\ta. Informacion general del farmaco")
    print("\n\tb. Sinonimos de un farmaco")
    print("\n\tc. Código ATC de un farmaco")
    print("\nIntroduzca 'esc' para volver al menu principal.")

def menu_3():
    system("cls")
    header("Informacion de las enfermedades")
    print("En esta ventana puedes obtener informacion sobre las enfermedades:")
    print("\n\ta. Farmacos para una enfermedad")
    print("\n\tb. Farmaco y enfermedad con el mayor score de asociacion")
    print("\nIntroduzca 'esc' para volver al menu principal.")

def menu_4():
    system("cls")
    header("Informacion de los efectos fenotipicos")
    print("En esta ventana podra consultar información de los efectos fenotípicos \n"
          "asociados un farmaco. Opciones:\n")
    print("\ta. Indicaciones del farmaco: muestra los efectos fenotipicos \n"
          "\tque sean indicaciones para las cuales se utiliza el farmaco.\n")
    print(" \tb. Efectos secundarios de un fármaco: muestra aquellos efectos \n"
          "\tfenotipicos categorizados como efectos secundarios generados\n"
          "\tpor el farmaco ordenados de forma descendiente en base a la \n"
          "\tevidencia de esta asociacion.")
    print("\nIntroduzca 'esc' para volver al menu principal.")

def menu_5():
    system("cls")
    header("Informacion de los targets")
    print("En esta ventana puedes obtener informacion sobre las dianas de un farmaco:")
    print("\n\ta. Dianas de un tipo dado")
    print("\n\tb. Organismo al cual se asocian un mayor numero de dianas")
    print("\nIntroduzca 'esc' para volver al menu principal.")

def menu_6():
    system("cls")
    header("Borrados")
    print("En esta ventana podras borrar asociacion entre un farmaco y una enfermedad \n"
          "con un score muy bajo. En pantalla se muestran las 10 relaciones con un score\n"
          "mas bajo. Si introduce una relación que no se encuentra entre las mostradas en\n"
          "pantalla también se borrara, siempre que exista.")

def menu_7():
    system("cls")
    header("Inserciones")
    print("En esta ventana podras añadir una nueva enfermedad con su farmaco asociado.")

def menu_7_1():
    print("\nHay dos posibles fuentes del identificador introducido:")
    print("\n\ta. OMIM")
    print("\n\tb. MESH")

def menu_8():
    system("cls")
    header("Modificaciones")
    print("En esta ventana podrás establecer como 0 el score de aquellas asociaciones \n"
          "entre farmacos y efectos secundarios por debajo del valor deseado.")

def final(database):
    header("Adios")
    print("¡Que tenga un buen dia!")
    database.close()
    exit()
