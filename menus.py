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

