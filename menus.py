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
    header("Información general")
    print("En esta ventana puedes obtener varios tipos de información:")
    print("\n\ta. Número total")
    print("\n\tb. Primeras 10 instancias")

def menu_1_1():
    system("cls")
    header("Información general")

def menu_1_2():
    system("cls")
    header("Información general")
    print("En esta ventana puedes obtener las diez primeras instancias de:")
    print("\n\ta. Fármacos")
    print("\n\tb. Enfermedades")
    print("\n\tc. Efectos fenotipicos")
    print("\n\td. Dianas")


def menu_2():
    system("cls")
    header("Información de los fármacos")
    print("En esta ventana puedes obtener varios tipos de información:")
    print("\n\ta. Información general del fármaco")
    print("\n\tb. Sinónimos de un fármaco")
    print("\n\tc. Código ATC de un fármaco")

def menu_3():
    system("cls")
    header("Información de las enfermedades")
    print("En esta ventana puedes obtener información sobre las enfermedades:")
    print("\n\ta. Fármacos para una enfermedad")
    print("\n\tb. Fármaco y enfermedad con el mayor score de asociación")

def menu_4():
    system("cls")
    header("Información de los efectos fenotípicos")
    print("En esta ventana podrá consultar información de los efectos fenotípicos \nasociados un fármaco.")
    print("Opciones: a. Indicaciones del fármaco: muestra los efectos fenotípicos \n"
          "             que sean indicaciones para las cuales se utiliza el fármaco.\n")
    print("          b. Efectos secundarios de un fármaco: muestra quellos efectos \n"
          "             fenotípicos categorizados como efectos secundarios generados\n"
          "             por el fármaco ordenados de forma descendiente en base a la \n"
          "             evidencia de esta asociación\n")

def menu_5():
    system("cls")
    header("Información de los targets")
    print("En esta ventana puedes obtener información sobre las dianas de un fármaco:")
    print("\n\ta. Dianas de un tipo dado:")
    print("\n\tb. Organismo al cual se asocian un mayor número de dianas")


def menu_6():
    system("cls")
    header("Borrados")
    print("En esta ventana podrás Borrar asociación entre un fármaco y una enfermedad \n"
          "con un score muy bajo. En pantalla se muestran las 10 relaciones con un score\n "
          "más bajo. Escriba el nombre del fármaco y el nombre de la enfermedad separadas por un guión (-).")

def menu_7():
    system("cls")
    header("Inserciones")
    print("En esta ventana podrás añadir una nueva enfermedad con su fármaco asociado")

def menu_8():
    system("cls")
    header("Modificaciones")
    print("En esta ventana podrás establecer como 0 el score")

def final(database):
    header("Adios")
    print("Sus consultas se han guardado en el archivo 'Resultados.txt'")
    database.close()       
    exit()


