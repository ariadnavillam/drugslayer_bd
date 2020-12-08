from os import system, getcwd
import re
import mysql.connector
from mysql.connector import errorcode
import SQL
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

def nueva_consulta():
    """
    Función para realizar otra consulta una vez completada otra
    """
    rep=in_variable("\n¿Quiere hacer otra consulta? [S/N]", re.compile("[Ss]|[Nn]"),"\n¿Quiere hacer otra consulta? [S/N]")
    if rep.upper()=="S":
        ruta = getcwd()
        system("python " + ruta + "\main.py")
    else:
        menus.final(db)

menus.principal()

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
        print("Hay un error en su nombre de usuario o contraseña.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base de datos 'disnet_drugslayer' no existe.")
    else:
        print(err)

if int(opcion) == 1:
    menus.menu_1()

    opcion_letra = in_variable("\nIntroduzca una opción: ", re.compile("[Aa]|[Bb]|"), "Introduzca a o b.")

    if opcion_letra.lower() == "a":
        menus.menu_1_1()

        db.start_transaction()

        query = "SELECT COUNT(drug.drug_id) FROM drug"
        SQL.contar_instancias(cursor, query, "1. Número total de fármacos: ")

        query = "SELECT COUNT(resource_id) FROM disease"
        SQL.contar_instancias(cursor, query, "2. Número total de enfermedades: ")

        query = "SELECT COUNT(phenotype_id) FROM drug_phenotype_effect"
        SQL.contar_instancias(cursor, query, "3. Número total de efectos fenotípicos: ")

        query = "SELECT COUNT(target_id) FROM drug_target"
        SQL.contar_instancias(cursor, query, "4. Número total de targets diferentes: ")

        db.commit()

        nueva_consulta()

    elif opcion_letra.lower() == "b":
        menus.menu_1_2()

        opcion_letra2 = in_variable("\nIntroduzca una opción: ", re.compile("[Aa]|[Bb]|[Cc]|[Dd]"), "Introduzca a, b, c o d.")
        if opcion_letra2.lower() == "a":
            query = "SELECT drug_id, drug_name, molecular_type, chemical_structure, inchi_key FROM drug WHERE drug_id IS NOT NULL AND drug_name IS NOT NULL AND molecular_type IS NOT NULL AND chemical_structure IS NOT NULL AND inchi_key IS NOT NULL LIMIT 10"
            SQL.consultar_filas(cursor, query, "\nDrug ID\tDrug name\tMolecular type\tChemical structure\tInChi-key", title="\nPrimeras 10 instancias de fármacos:")

        elif opcion_letra2.lower() == "b":
            query = "SELECT disease_id, disease_name FROM disease WHERE disease_id IS NOT NULL AND disease_name IS NOT NULL LIMIT 10"
            SQL.consultar_filas(cursor, query, ("\nDisease ID\tDisease name"), title="\nPrimeras 10 instancias de enfermedades:")

        elif opcion_letra2.lower() == "c":
            query = "SELECT phenotype_id, phenotype_name FROM phenotype_effect WHERE phenotype_id IS NOT NULL AND phenotype_name IS NOT NULL LIMIT 10"
            SQL.consultar_filas(cursor, query, ("\nPhenotype ID\tPhenotype name"), title="\nPrimeras 10 instancias de efectos fenotípicos:")

        elif opcion_letra2.lower() == "d":
            query = "SELECT target_id, target_name_pref, target_type, target_organism FROM target WHERE target_id IS NOT NULL AND target_name_pref IS NOT NULL AND target_type IS NOT NULL AND target_organism IS NOT NULL LIMIT 10"
            SQL.consultar_filas(cursor, query, ("\nTarget ID\tTarget name pref\tTarget type\tTarget organism"), title="\nPrimeras 10 instancias de dianas:")

        nueva_consulta()

elif int(opcion) == 2:
    menus.menu_2()

    opcion_letra = in_variable("\nIntroduzca una opción: ", re.compile("[Aa]|[Bb]|[Cc]"), "Introduzca a, b o c.")

    if opcion_letra.lower() == "a":
        drug_iden = in_variable("\nIntroduzca el ID del farmaco: ", re.compile("CHEMBL[1-9]+"), "Drug ID: CHEMBL + número")
        query = str("SELECT drug_name, molecular_type, chemical_structure, inchi_key from drug where drug_id= %s")
        SQL.consultar_unico(cursor, query, ("Drug Name", "Molecular type", "Chemical structure","InChi-Key"), params=(drug_iden,))

    elif opcion_letra.lower() == "b":
        drug_nom = in_variable("\nIntroduzca el nombre de un farmaco: ", re.compile(".+"), "")
        query = "SELECT synonymous_name FROM synonymous, drug WHERE synonymous.drug_id=drug.drug_id AND drug.drug_name = %s"
        SQL.consultar_filas(cursor, query, ("\nSinónimos de " + drug_nom + ":"), params=(drug_nom,))

    elif opcion_letra.lower() == "c":
        drug_id = in_variable("\nIntroduzca el ID del farmaco: ", re.compile("CHEMBL[1-9]+"), "Drug ID: CHEMBL + número")
        query = "SELECT ATC_code.ATC_code_id from ATC_code, drug WHERE drug.drug_id = %s GROUP BY drug.drug_id"
        SQL.consultar_filas(cursor, query, ("\nCódigos ATC asociados al fármaco " + drug_id + ":"), params=(drug_id,))

    nueva_consulta()

if int(opcion) ==3:
    menus.menu_3()

    opcion_letra = in_variable("\nIntroduzca una opción: ", re.compile("[Aa]|[Bb]|"), "Introduzca a o b.")

    if opcion_letra.lower() == "a":
        disease_name = input('Introduce el nombre de la enfermedad: ')

        query = "SELECT drug.drug_id, drug.drug_name FROM drug, drug_disease, disease WHERE disease.disease_name=%s AND drug.drug_id=drug_disease.drug_id AND disease.disease_id=drug_disease.disease_id"
        params=(disease_name,)
        SQL.consultar_filas(cursor, query, "\nDrug ID\tDrug name", params=params)

    elif opcion_letra.lower() == "b":
        query = "SELECT disease.disease_name, drug.drug_name FROM disease, drug, drug_disease WHERE drug.drug_id=drug_disease.drug_id AND disease.disease_id=drug_disease.disease_id ORDER BY drug_disease.inferred_score DESC LIMIT 1"
        SQL.consultar_unico(cursor, query, ("Disease name: ", "Drug name: "))

    nueva_consulta()

if int(opcion) == 4:
    menus.menu_4()
    opcion_letra = in_variable("Introduzca una opción: ", re.compile("[Aa]|[Bb]"), "Introduzca a o b")
    drug_id = in_variable("\nIntroduzca Drug Id ChEMBL : ", re.compile("CHEMBL[1-9]+"), "Introduzca Drug ID: ")

    if opcion_letra.lower() == "a":
        query = str("SELECT phenotype_effect.phenotype_id, phenotype_effect.phenotype_name "
                    "FROM phenotype_effect, drug_phenotype_effect "
                    "WHERE drug_phenotype_effect.drug_id = %s AND drug_phenotype_effect.phenotype_id = phenotype_effect.phenotype_id "
                    )
        params = (drug_id,)
        SQL.consultar_filas(cursor, query, "\nPhenotype ID\tPhenotype effect" , params=params)
        cursor.execute(query, params)

    elif opcion_letra.lower() == "b":
        query = str("SELECT phenotype_effect.phenotype_id, phenotype_effect.phenotype_name, drug_phenotype_effect.score "
                    "FROM phenotype_effect, drug_phenotype_effect "
                    "WHERE drug_phenotype_effect.drug_id = %s "
                    "AND drug_phenotype_effect.phenotype_type LIKE 'SIDE EFFECT' "
                    "AND drug_phenotype_effect.phenotype_id = phenotype_effect.phenotype_id "
                    "ORDER BY drug_phenotype_effect.score DESC")

        SQL.consultar_filas(cursor, query, "\nPhenotype ID\tPhenotype name\tScore", params=(drug_id,))

    nueva_consulta()

elif int(opcion) == 5:
    menus.menu_5()

    opcion_letra = in_variable("\nIntroduzca una opción: ", re.compile("[Aa]|[Bb]"), "Introduzca a o b")
    if opcion_letra.lower() == "a":
        target_type = in_variable("\nIntroduzca el tipo de diana: ", re.compile("[A-Z]|-+"),"" )

        query = "SELECT target_name_pref FROM target WHERE target_type = %s ORDER BY target_name_pref ASC LIMIT 20"

        SQL.consultar_filas(cursor, query, ("\nDianas de tipo " + target_type + ":"), params=(target_type,))

    elif opcion_letra.lower() == "b":

        query = str("SELECT target_organism, count(target_id) "
                    "FROM target group by target_organism "
                    "ORDER BY COUNT(target_organism) DESC LIMIT 1")
        SQL.consultar_unico(cursor, query, ("Organismo con mayor número de dianas: ", "Número de dianas : "))

    nueva_consulta()


elif int(opcion) == 6:
    menus.menu_6()

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
    menus.menu_7()

    id_d= in_variable("\n¿Qué identificador desea introducir?", re.compile("[1-9]+"), "Error. Introduzca un número.")
    print("\nHay dos posibles fuentes del identificador introducido:")
    print("\n\t1. OMIM")
    print("\n\t2. MESH")
    resource_id = in_variable("\n¿Cuál es la fuente del identificador introducido?", re.compile("[1-2]"), "Error. Introduzca un número.")
    if int(resource_id)==1:
        resource_id=72
    if int(resource_id)==2:
        resource_id=75
        
    name_d=input("\n¿Qué nombre desea introducir?")
    name_f=input("\n¿Cuál es el nombre del fármaco asociado?")
    add_dis="INSERT INTO disease VALUES (%s, %s, %s)"
    add_drug_dis="INSERT INTO drug_disease (disease_id, drug_id, source_id) VALUES (%s, (SELECT drug_id FROM drug WHERE drug_name=%s), 3)"
    db.start_transaction()
    cursor.execute(add_dis, (resource_id, id_d, name_d))
    cursor.execute(add_drug_dis, (id_d, name_f))
    db.commit()

    nueva_consulta()

elif int(opcion)==8:
    menus.menu_8()

    valor_min=input("\n¿Cuál es el valor minimo que de score de asociacion que desea?")
    query="UPDATE drug_phenotype_effect SET score=0 WHERE score < %s AND phenotype_type LIKE 'SIDE EFFECT'"
    cursor.execute(query, (valor_min,))

    nueva_consulta()

elif int(opcion)==9:
    menus.final(db)
