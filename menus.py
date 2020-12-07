from os import system

def header(palabra):
    print(" -----------------------------------------------------------------------------------")
    print("|                                            %s                                     |" %palabra)
    print(" -----------------------------------------------------------------------------------")

def principal():
    system("cls")
    print(" -----------------------------------------------------------------------------------")
    print("|                                  BASE DE DATOS DE FARMACOS                        |")
    print(" -----------------------------------------------------------------------------------")

    print("Bienvenido a la base de datos 'disnet_drugslayer' del proyecto DISNET.")
    print("Cuenta con información sobre enfermedades a nivel fenotipico, biologico y fármacos.")
    print("\nPuede obtener diferentes tipos de información o funciones:")
    print("\n\t1. Información general")
    print("\n\t2. Información de los fármacos")
    print("\n\t3. Información de las enfermedades")
    print("\n\t4. Información de los efectos fenotipicos")
    print("\n\t5. Información de los targets")
    print("\n\t6. Borrados")
    print("\n\t7. Inserciones")
    print("\n\t8. Modificaciones")
    print("\n\t9. Salir")

def menu_1():
    system("cls")
    print(" --------------------------------------------------------------------------")
    print("|                        Información general                               | ")
    print(" --------------------------------------------------------------------------")
    print("En esta ventana puedes obtener varios tipos de información:")
    print("\n\t1. Número total")
    print("\n\t2. Primeras 10 instancias")

def menu_1_1():
    system("cls")
    print(" --------------------------------------------------------------------------")
    print("|                        Información general                               | ")
    print(" --------------------------------------------------------------------------")


def menu_1_2():
    system("cls")
    print(" --------------------------------------------------------------------------")
    print("|                        Información general                               | ")
    print(" --------------------------------------------------------------------------")
    print("En esta ventana puedes obtener las diez primeras instancias de:")
    print("\n\t1. Fármacos")
    print("\n\t2. Enfermedades")
    print("\n\t3. Efectos fenotipicos")
    print("\n\t4. Dianas")


def menu_2():
    system("cls")
    print(" --------------------------------------------------------------------------")
    print("|                     Información de los fármacos                          | ")
    print(" --------------------------------------------------------------------------")
    print("En esta ventana puedes obtener varios tipos de información:")
    print("\n\ta. Información general del fármaco")
    print("\n\tb. Sinónimos de un fármaco")
    print("\n\tb. Código ATC de un fármaco")

def menu_3():
    system("cls")
    print(" --------------------------------------------------------------------------")
    print("|                   Información de las enfermedades                        | ")
    print(" --------------------------------------------------------------------------")
    print("En esta ventana puedes obtener información sobre las enfermedades:")
    print("\n\t1. Fármacos para una enfermedad")
    print("\n\t2. Fármaco y enfermedad con el mayor score de asociación")

def menu_4():
    system("cls")
    print(" --------------------------------------------------------------------------")
    print("|                         Efectos fenotípicos                              | ")
    print(" --------------------------------------------------------------------------")
    print("En esta ventana podrá consultar información de los efectos fenotípicos \nasociados un fármaco.")
    print("Opciones: a. Indicaciones del fármaco: muestra los efectos fenotípicos \n"
          "             que sean indicaciones para las cuales se utiliza el fármaco.\n")
    print("          b. Efectos secundarios de un fármaco: muestra quellos efectos \n"
          "             fenotípicos categorizados como efectos secundarios generados\n"
          "             por el fármaco ordenados de forma descendiente en base a la \n"
          "             evidencia de esta asociación\n")

def menu_5():
    system("cls")
    print(" --------------------------------------------------------------------------")
    print("|                     Información de los targets                         | ")
    print(" --------------------------------------------------------------------------")
    print("En esta ventana puedes obtener información sobre las dianas de un fármaco:")
    print("\n\ta. Dianas de un tipo dado:")
    print("\n\tb. Organismo al cual se asocian un mayor número de dianas")


def menu_6():
    system("cls")
    print(" --------------------------------------------------------------------------")
    print("|                                Borrados                                  | ")
    print(" --------------------------------------------------------------------------")
    print("En esta ventana podrás Borrar asociación entre un fármaco y una enfermedad \n"
          "con un score muy bajo. En pantalla se muestran las 10 relaciones con un score\n "
          "más bajo. Escriba el nombre del fármaco y el nombre de la enfermedad separadas por un guión (-).")

def menu_7():
    system("cls")
    print(" --------------------------------------------------------------------------")
    print("|                              Inserciones                                 | ")
    print(" --------------------------------------------------------------------------")
    print("En esta ventana podrás añadir una nueva enfermedad con su fármaco asociado")

def menu_8():
    system("cls")
    print(" --------------------------------------------------------------------------")
    print("|                             Modificiones                                 | ")
    print(" --------------------------------------------------------------------------")
    print("En esta ventana podrás establecer como 0 el score")


