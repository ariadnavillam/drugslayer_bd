from os import system
import mysql.connector

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

opcion=input("\n¿Que función desea hacer? [Introduzca el número de la función deseada]")

try:
    opcion=int(opcion)
    if int(opcion)<0 or int(opcion)>9:
        print("ERROR: El número introducido debe ser un numero entero del 1 al 9")
        exit()

except:
    print("ERROR: Debe introducir un número entero del 1 al 9")
    exit()

config = {
    'user': 'drugslayer',
    'passwd': 'drugslayer_pwd',
    'host': '127.0.0.1',
    'db': 'disnet_drugslayer',
    }

db=mysql.connector.connect(**config)
db.autocommit=True
cursor=db.cursor()

if int(opcion)==7:
    system("cls")
    print(" --------------------------------------------------------------------------")
    print("|                              Inserciones                                 | ")
    print(" --------------------------------------------------------------------------")
    print("En esta ventana podrás añadir una nueva enfermedad con su fármaco asociado")

    id_d=input("\n¿Qué identificador desea introducir?")
    name_d=input("\n¿Qué nombre desea introducir?")
    name_f=input("\n¿Cuál es el nombre del fármaco asociado?")
    add_dis="INSERT INTO disease VALUES (%s, %s, %s)"
    add_drug_dis="INSERT INTO drug_disease (disease_id, drug_id, source_id) VALUES (%s, (SELECT drug_id FROM drug WHERE drug_name=%s), 3)"
    try:
        cursor.execute(add_dis, (72, id_d, name_d))
        cursor.execute(add_drug_dis, (id_d, name_f))
        print("\n - Inserción realizada con éxito - ")
    except:
        print("\nHa ocurrido un error")
        exit()

    rep=input("\n¿Quiere hacer otra consulta? [S/N]")
    if rep=="S":
        system("python script1.py")
    else:
        exit()

if int(opcion)==8:
    system("cls")
    print(" --------------------------------------------------------------------------")
    print("|                             Modificiones                                 | ")
    print(" --------------------------------------------------------------------------")
    print("En esta ventana podrás establecer como 0 el score")

    valor_min=input("\n¿Cuál es el valor minimo que de score de asociacion que desea?")
    upd="UPDATE drug_phenotype_effect SET score=0 WHERE score < %s AND phenotype_type LIKE 'SIDE EFFECT'"
    try:
        cursor.execute(upd, (valor_min,))
        print("\n - Modificación realizada con éxito - ")
    except:
        print("\nHa ocurrido un error")
        exit()

    rep=input("\n¿Quiere hacer otra consulta? [S/N]")
    if rep=="S":
        system("python script1.py")
    else:
        exit()

if int(opcion)==9:
    exit()

db.close()
