from os import system
import re
import mysql.connector
from mysql.connector import errorcode
def in_variable(texto, patron):
    """
    Esta función sirve para introducir variables sin errores
    """
    
    while True:
        var = input(texto)
        if patron.match(var):
            break

        elif var == "exit":
            exit()
        else:
            continue
    return var
    


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

#opcion=input("\n¿Que función desea hacer? [Introduzca el número de la función deseada]")
opcion = in_variable("\n¿Que función desea hacer? [Introduzca el número de la función deseada]", re.compile("[1-9]"))
# try:
#     opcion=int(opcion)
#     if int(opcion)<0 or int(opcion)>9:
#         print("ERROR: El número introducido debe ser un numero entero del 1 al 9")
#         exit()

# except:
#     print("ERROR: Debe introducir un número entero del 1 al 9")
#     exit()

config = {
    'user': 'drugslayer',
    'passwd': 'drugslayer_pwd',
    'host': 'localhost',
    'db': 'disnet_drugslayer',
    }

try:
    db=mysql.connector.connect(**config)
    db.autocommit=True
    cursor=db.cursor()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

finally:
    db.close()
    print("Data in file x.txt")

#if opcion == 1:
    
#elif opcion == 2:

#elif opcion == 3:

if int(opcion) == 4:
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
    
    opcion_letra = in_variable("Introduzca una opción: ", re.compile("[Aa]|[Bb]"))

    drug_id = in_variable("Introduzca Drug Id ChEMBL : ", re.compile("CHEMBL[1-9]+")) 
    
    # while True:
    #     pattern = re.compile("CHEMBL[1-9]+")
    #     drug_id = input("Introduzca Drug Id ChEMBL : ")
    #     if pattern.match(drug_id):
    #         break
    #     else:
    #         print("Drug id: CHEMBL + número.")

    f = open("resultados.txt", "a")
    if opcion_letra.lower() == "a":
        query = str("SELECT phenotype_effect.phenotype_id, phenotype_effect.phenotype_name "
                    "FROM phenotype_effect, drug_phenotype_effect "
                    "WHERE drug_phenotype_effect.drug_id = %s AND drug_phenotype_effect.phenotype_id = phenotype_effect.phenotype_id "
                    )
        params = (drug_id,)
        cursor.execute(query, params)
        print("\nPhenotype ID\tPhenotype effect")
        f.write("\nPhenotype ID\tPhenotype effect")
        count = 0
        for row in cursor:
            if count < 10:
                print(row[0] + "\t" + row[1])
                f.write(row[0] + "\t" + row[1])
            else:
                f.write(row[0] + "\t" + row[1])
    
    elif opcion_letra.lower() == "b":
        query = str("SELECT phenotype_effect.phenotype_id, phenotype_effect.phenotype_name, drug_phenotype_effect.score "
                    "FROM phenotype_effect, drug_phenotype_effect "
                    "WHERE drug_phenotype_effect.drug_id = %s "
                    "AND drug_phenotype_effect.phenotype_type LIKE 'SIDE EFFECT' "
                    "AND drug_phenotype_effect.phenotype_id = phenotype_effect.phenotype_id "
                    "ORDER BY drug_phenotype_effect.score DESC")
        cursor.execute(query, (drug_id,))            
        print("\nPhenotype ID\tPhenotype name")
        f.write("\nPhenotype ID\tPehnotype name")
        count = 0
        for row in cursor:
            if count < 10:
                print(row[0] + "\t" + row[1] + "\t" + row[2])
                f.write(row[0] + "\t" + row[1] + "\t" + row[2])
            else:
                f.write(row[0] + "\t" + row[1] + "\t" + row[2])
    f.close()
    
    rep=input("\n¿Quiere hacer otra consulta? [S/N]")
    if rep=="S":
        system("python script1.py")
    else:
        exit()

#elif int(opcion) == 5:

elif int(opcion) == 6:
    system("cls")
    print(" --------------------------------------------------------------------------")
    print("|                                Borrados                                  | ")
    print(" --------------------------------------------------------------------------")
    print("En esta ventana podrás Borrar asociación entre un fármaco y una enfermedad \n"
          "con un score muy bajo. En pantalla se muestran las 10 relaciones con un score\n "
          "más bajo. Escriba el nombre del fármaco y el nombre de la enfermedad separadas por un guión (-).")
   
    query = str("SELECT drug_disease.inferred_score, drug.drug_id, drug.drug_name, disease.disease_id, disease.disease_name "
                "FROM drug_disease, drug, disease "
                "WHERE drug_disease.drug_id = drug.drug_id "
                "AND drug_disease.disease_id = disease.disease_id "
                "AND drug_disease.inferred_score IS NOT null "
                "ORDER BY inferred_score ASC LIMIT 10")
    
    cursor.execute(query)

    drug_name_id = dict()
    disease_name_id = dict()
    print("\nScore\tDrug name\tDisease name")
    for row in cursor:
        drug_name_id[row[2]] = row[1]
        disease_name_id[row[4]] = row[3]
        print(row[0], row[2], row[4])
    
    while True:
        var_in = input("Introduzca nombre de la relacion a eliminar : ")
        if var_in == "exit":
            exit()  

        dd = var_in.split("-")
        if dd[0] in drug_name_id and dd[1] in disease_name_id:
            drug_id = drug_name_id[dd[0]]
            disease_id = disease_name_id[dd[1]]
            break
        else:
            print("Relacion no valida")
    
    query = str("SELECT * FROM drug_disease "
                "WHERE drug_id=%s AND disease_id=%s")
    #query = "DELETE FROM drug_disease "
    #        "WHERE drug_id='%s' AND disease_id='%s'" %(drug_id,disease_id)
    cursor.execute(query,(drug_id, disease_id,))

    for row in cursor:
        print (row) 

elif int(opcion)==7:
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

elif int(opcion)==8:
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

elif int(opcion)==9:
    exit()

#else:
#    print("Introduzca un número del 1 al 9.")

