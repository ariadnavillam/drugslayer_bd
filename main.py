from os import system
import re
import mysql.connector
from mysql.connector import errorcode
import menus

def in_variable(texto, patron, texto_alt):
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
            print(texto_alt)
            continue
    return var


menus.principal()
system("cls")
print(" -----------------------------------------------------------------------------------")
print("|                              BASE DE DATOS DE FARMACOS                            |")
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

opcion = in_variable("\n¿Que función desea hacer? [Introduzca el número de la función deseada]", re.compile("[1-9]"), "Error. Introduzca un número.")


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

if int(opcion)==1:
    system("cls")
    print(" --------------------------------------------------------------------------")
    print("|                        Información general                               | ")
    print(" --------------------------------------------------------------------------")
    print("En esta ventana puedes obtener varios tipos de información:")
    print("\n\t1. Número total")
    print("\n\t2. Primeras 10 instancias")

    opcion2=input("\n¿Qué opción desea realizar? [Introduzca el número de la funcion deseada]")
    try:
        opcion2=int(opcion2)
        if opcion2<1 or opcion2>2:
            print("ERROR: Debe introducir un número entero del 1 al 2.")
            exit()
    except:
        print("ERROR: Debe introducir un número entero del 1 al 2.")
        exit()

    if opcion2==1:
        system("cls")
        print(" --------------------------------------------------------------------------")
        print("|                        Información general                               | ")
        print(" --------------------------------------------------------------------------")
        query1 = "SELECT COUNT(drug.drug_id) FROM drug"
        cursor.execute(query1)
        for row in cursor:
            count_drug = row[0]
            print("\n\t1. Número total de fármacos: %s" % count_drug)


        query2 = "SELECT COUNT(resource_id) FROM disease"
        cursor.execute(query2)
        for row in cursor:
            count_disease = row[0]
            print("\n\t2. Número total de enfermedades: %s " % count_disease)


        query3 = "SELECT COUNT(phenotype_id) FROM drug_phenotype_effect"
        cursor.execute(query3)
        for row in cursor:
            count_phenotype = row[0]
            print("\n\t3. Número total de efectos fenotípicos: %s " % count_phenotype)


        query4 = "SELECT COUNT(target_id) FROM drug_target"
        cursor.execute(query4)
        for row in cursor:
            count_target = row[0]
            print("\n\t4. Número total de targets diferentes: %s " % count_target)

        rep=input("\n¿Quiere hacer otra consulta? [S/N]")
        if rep=="S":
            system("python script1.py")
        else:
            exit()

    if opcion2==2:
        system("cls")
        print(" --------------------------------------------------------------------------")
        print("|                        Información general                               | ")
        print(" --------------------------------------------------------------------------")
        print("En esta ventana puedes obtener las diez primeras instancias de:")
        print("\n\t1. Fármacos")
        print("\n\t2. Enfermedades")
        print("\n\t3. Efectos fenotipicos")
        print("\n\t4. Dianas")

        opcion3=input("\n¿Qué opción desea realizar? [Introduzca el número de la funcion deseada]")

        try:
            opcion3=int(opcion3)
            if opcion3<1 or opcion3>4:
                print("ERROR: Debe introducir un número entero del 1 al 2.")
                exit()
        except:
            print("ERROR: Debe introducir un número entero del 1 al 2.")
            exit()

        if opcion3==1:
            query1 = "SELECT drug_id, drug_name, molecular_type, chemical_structure, inchi_key FROM drug WHERE drug_id IS NOT NULL AND drug_name IS NOT NULL AND molecular_type IS NOT NULL AND chemical_structure IS NOT NULL AND inchi_key IS NOT NULL LIMIT 10"
            cursor.execute(query1)
            print("PRIMERAS 10 INSTANCIAS DE MEDICAMENTOS")
            for row in cursor:
                drug_id = row[0]
                drug_name = row[1]
                molecular_type = row[2]
                chemical_structure = row[3]
                inchi_key = row[4]
                print(drug_id + "\t" + drug_name + "\t" + molecular_type + "\t" + chemical_structure + "\t" + inchi_key)

        if opcion3==2:
            query2 = "SELECT disease_id, disease_name FROM disease WHERE disease_id IS NOT NULL AND disease_name IS NOT NULL LIMIT 10"
            cursor.execute(query2)
            print("\nPRIMERAS 10 INSTANCIAS DE ENFERMEDADES")
            for row in cursor:
                disease_id = row[0]
                disease_name = row[1]
                print(disease_id + "\t" + disease_name)

        if opcion3==3:
            query3 = "SELECT phenotype_id, phenotype_name FROM phenotype_effect WHERE phenotype_id IS NOT NULL AND phenotype_name IS NOT NULL LIMIT 10"
            cursor.execute(query3)
            print("\nPRIMERAS 10 INSTANCIAS DE EFECTOS FENOTÍPICOS")
            for row in cursor:
                phenotype_id = row[0]
                phenotype_name = row[1]
                print(phenotype_id + "\t" + phenotype_name)

        if opcion3==4:
            query4 = "SELECT target_id, target_name_pref, target_type, target_organism FROM target WHERE target_id IS NOT NULL AND target_name_pref IS NOT NULL AND target_type IS NOT NULL AND target_organism IS NOT NULL LIMIT 10"
            cursor.execute(query4)
            print("\nPRIMERAS 10 INSTANCIAS DE TARGET")
            for row in cursor:
                target_id = row[0]
                target_name = row[1]
                target_type = row[2]
                target_organism = row[3]
                print(target_id + "\t" + target_name + "\t" + target_type + "\t" + target_organism)

#elif opcion == 2:

if opcion==3:
    system("cls")
    print(" --------------------------------------------------------------------------")
    print("|                   Información de las enfermedades                        | ")
    print(" --------------------------------------------------------------------------")
    print("En esta ventana puedes obtener información sobre las enfermedades:")
    print("\n\t1. Fármacos para una enfermedad")
    print("\n\t2. Fármaco y enfermedad con el mayor score de asociación")

    opcion2=input("\n¿Qué opción desea realizar? [Introduzca el número de la funcion deseada]")
    try:
        opcion2=int(opcion2)
        if opcion2<1 or opcion2>2:
            print("ERROR: Debe introducir un número entero del 1 al 2.")
            exit()
    except:
        print("ERROR: Debe introducir un número entero del 1 al 2.")
        exit()

    if opcion2==1:
        disease_name = input('Introduce el nombre de la enfermedad: ')

        query1 = "SELECT drug.drug_id, drug.drug_name FROM drug, drug_disease, disease WHERE disease.disease_name=%s AND drug.drug_id=drug_disease.drug_id AND disease.disease_id=drug_disease.disease_id"
        cursor.execute(query1, (disease_name,))
        for row in cursor:
            drug_id = row[0]
            drug_name = row[1]
            print("Drug_id: %s" % drug_id)
            print("Drug_name: %s" % drug_name)

    if opcion2==2:
        query2 = "SELECT disease.disease_name, drug.drug_name FROM disease, drug, drug_disease WHERE drug.drug_id=drug_disease.drug_id AND disease.disease_id=drug_disease.disease_id ORDER BY drug_disease.inferred_score DESC LIMIT 1"
        cursor.execute(query2)
        for row in cursor:
            disease_name = row[0]
            drug_name = row[1]
            print("Disease_name: %s" % disease_name)
            print("Drug_name: %s" % drug_name)

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

    opcion_letra = in_variable("Introduzca una opción: ", re.compile("[Aa]|[Bb]"), "Introduzca a o b")

    drug_id = in_variable("Introduzca Drug Id ChEMBL : ", re.compile("CHEMBL[1-9]+"), "Introduzca Drug ID: ")

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
    print("Fuente del identificador")
    print("\n\t1.OMIM")
    print("\n\t2.MESH")
    r_id=input("¿Cuál es la fuente del identificador introducido?")
    if r_id==1:
        resource_id="72"
    if r_id==2:
        resource_id="75"

    name_d=input("\n¿Qué nombre desea introducir?")
    name_f=input("\n¿Cuál es el nombre del fármaco asociado?")
    add_dis="INSERT INTO disease VALUES (%s, %s, %s)"
    add_drug_dis="INSERT INTO drug_disease (disease_id, drug_id, source_id) VALUES (%s, (SELECT drug_id FROM drug WHERE drug_name=%s), 3)"
    try:
        cursor.execute(add_dis, (resource_id, id_d, name_d))
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
