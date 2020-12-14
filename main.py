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
    Función para realizar otra consulta una vez se complete la anterior
    """
    rep=in_variable("\n¿Quiere hacer otra consulta? [S/N]", re.compile("[Ss]|[Nn]"),"\n¿Quiere hacer otra consulta? [S/N]")
    if rep.upper()=="S":
        ruta = getcwd()
        system("python " + ruta + "\main.py")
    else:
        menus.final(db)

def volver_menu(opcion_letra):
    """
    Funcion para volver al menu principal
    """
    if opcion_letra.lower() == "esc":
        ruta = getcwd()
        system("python " + ruta + "\main.py")

# CONEXION A LA BASE DE DATOS
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
        print("\nERROR: Hay un error en su nombre de usuario o contraseña.")
        exit()
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("\nERROR: La base de datos 'disnet_drugslayer' no existe.")
        exit()
    elif err.errno == errorcode.ER_WRONG_DB_NAME:
        print("\nERROR: El nombre de la base de datos es incorrecto")
        exit()
    elif err.errno == errorcode.ER_DBACCESS_DENIED_ERROR:
        print("\nERROR: Acceso denegado del usuario para acceder a la base de datos")
        exit()
    else:
        print(err)
        exit()

# REALIZACION CONSULTAS
menus.principal()

opcion = in_variable("\n¿Que función desea hacer? [Introduzca el número de la función deseada]", re.compile("[1-9]"), "Error. Introduzca un número.")

try:
    if int(opcion) == 1:
        menus.menu_1()

        opcion_letra = in_variable("\nIntroduzca una opción: ", re.compile("[Aa]|[Bb]|esc"), "Introduzca a o b.")
        volver_menu(opcion_letra)

        if opcion_letra.lower() == "a":
            menus.menu_1_1()

            SQL.contar_instancias(cursor, "drug_id", "drug", "1. Número total de fármacos: ")
            SQL.contar_instancias(cursor, "resource_id", "disease", "2. Número total de enfermedades: ")
            SQL.contar_instancias(cursor, "phenotype_id", "drug_phenotype_effect", "3. Número total de efectos fenotípicos: ")
            SQL.contar_instancias(cursor, "target_id", "drug_target", "4. Número total de targets diferentes: ")

            nueva_consulta()

        elif opcion_letra.lower() == "b":
            menus.menu_1_2()

            opcion_letra2 = in_variable("\nIntroduzca una opción: ", re.compile("[Aa]|[Bb]|[Cc]|[Dd]|esc"), "Introduzca a, b, c o d.")
            volver_menu(opcion_letra2)

            if opcion_letra2.lower() == "a":
                query = str("SELECT drug_id, drug_name, molecular_type, chemical_structure, inchi_key "
                            "FROM drug "
                            "WHERE drug_id IS NOT NULL "
                            "AND drug_name IS NOT NULL "
                            "AND molecular_type IS NOT NULL "
                            "AND chemical_structure IS NOT NULL "
                            "AND inchi_key IS NOT NULL "
                            "LIMIT 10")

                SQL.consultar_filas(cursor, query, "\nDrug ID\tDrug name\tMolecular type\tChemical structure\tInChi-key", title="\nPrimeras 10 instancias de fármacos:")

            elif opcion_letra2.lower() == "b":
                query = str("SELECT disease_id, disease_name "
                            "FROM disease "
                            "WHERE disease_id IS NOT NULL "
                            "AND disease_name IS NOT NULL "
                            "LIMIT 10")

                SQL.consultar_filas(cursor, query, ("\nDisease ID\tDisease name"), title="\nPrimeras 10 instancias de enfermedades:")

            elif opcion_letra2.lower() == "c":
                query = str("SELECT phenotype_id, phenotype_name "
                            "FROM phenotype_effect "
                            "WHERE phenotype_id IS NOT NULL "
                            "AND phenotype_name IS NOT NULL "
                            "LIMIT 10")

                SQL.consultar_filas(cursor, query, ("\nPhenotype ID\tPhenotype name"), title="\nPrimeras 10 instancias de efectos fenotípicos:")

            elif opcion_letra2.lower() == "d":
                query = str("SELECT target_id, target_name_pref, target_type, target_organism "
                            "FROM target WHERE target_id IS NOT NULL "
                            "AND target_name_pref IS NOT NULL "
                            "AND target_type IS NOT NULL "
                            "AND target_organism IS NOT NULL "
                            "LIMIT 10")

                SQL.consultar_filas(cursor, query, ("\nTarget ID\tTarget name pref\tTarget type\tTarget organism"), title="\nPrimeras 10 instancias de dianas:")

            nueva_consulta()

    elif int(opcion) == 2:
        menus.menu_2()

        opcion_letra = in_variable("\nIntroduzca una opción: ", re.compile("[Aa]|[Bb]|[Cc]|esc"), "Introduzca a o b.")
        volver_menu(opcion_letra)

        if opcion_letra.lower() == "a":
            drug_id = in_variable("\nIntroduzca el ID del farmaco: ", re.compile("CHEMBL[1-9]+"), "Drug ID: CHEMBL + número")
            SQL.comprobar(cursor, drug_id, "drug_id", "drug")
            query = str("SELECT drug_name, molecular_type, chemical_structure, inchi_key FROM drug WHERE drug_id= %s")
            SQL.consultar_unico(cursor, query, ("Drug Name", "Molecular type", "Chemical structure","InChi-Key"), params=(drug_id,))

        elif opcion_letra.lower() == "b":
            drug_name = in_variable("\nIntroduzca el nombre de un farmaco: ", re.compile(".+"), "")
            SQL.comprobar(cursor, drug_name, "drug_name", "drug")
            query = "SELECT synonymous_name FROM synonymous s, drug d WHERE s.drug_id=d.drug_id AND d.drug_name = %s"
            SQL.consultar_filas(cursor, query, ("\nSinónimos de " + drug_name + ":"), params=(drug_name,))

        elif opcion_letra.lower() == "c":
            drug_id = in_variable("\nIntroduzca el ID del farmaco: ", re.compile("CHEMBL[1-9]+"), "Drug ID: CHEMBL + número")
            SQL.comprobar(cursor, drug_id, "drug_id", "drug")
            query = "SELECT ATC_code_id FROM ATC_code WHERE drug_id = %s GROUP BY drug_id"
            try:
                SQL.consultar_filas(cursor, query, ("\nCódigos ATC asociados al fármaco " + drug_id + ":"), params=(drug_id,))
            except:
                print("\nNo existen ningun codigo ATC asociado al farmaco.")
                exit()

        nueva_consulta()

    elif int(opcion) == 3:
        menus.menu_3()

        opcion_letra = in_variable("\nIntroduzca una opción: ", re.compile("[Aa]|[Bb]|esc"), "Introduzca a o b.")
        volver_menu(opcion_letra)

        if opcion_letra.lower() == "a":
            disease_name = input('\nIntroduce el nombre de la enfermedad: ')
            SQL.comprobar(cursor, disease_name, "disease_name", "disease")
            query = str("SELECT dr.drug_id, dr.drug_name "
                        "FROM drug dr, drug_disease dr_di, disease di "
                        "WHERE di.disease_name=%s "
                        "AND dr.drug_id=dr_di.drug_id "
                        "AND di.disease_id=dr_di.disease_id")

            SQL.consultar_filas(cursor, query, "\nDrug ID\tDrug name", params=(disease_name,))

        elif opcion_letra.lower() == "b":
            query = str("SELECT di.disease_name, dr.drug_name "
                        "FROM disease di, drug dr, drug_disease dr_di "
                        "WHERE dr.drug_id=dr_di.drug_id "
                        "AND di.disease_id=dr_di.disease_id "
                        "ORDER BY dr_di.inferred_score DESC "
                        "LIMIT 1")

            SQL.consultar_unico(cursor, query, ("Disease name", "Drug name"))

        nueva_consulta()

    elif int(opcion) == 4:
        menus.menu_4()

        opcion_letra = in_variable("\nIntroduzca una opción: ", re.compile("[Aa]|[Bb]|esc"), "Introduzca a o b.")
        volver_menu(opcion_letra)

        drug_id = in_variable("\nIntroduzca el ID del farmaco: ", re.compile("CHEMBL[1-9]+"), "Drug ID: CHEMBL + número")
        SQL.comprobar(cursor, drug_id, "drug_id", "drug")

        if opcion_letra.lower() == "a":
            query = str("SELECT ph.phenotype_id, ph.phenotype_name "
                        "FROM phenotype_effect ph, drug_phenotype_effect dr_ph "
                        "WHERE dr_ph.drug_id = %s "
                        "AND dr_ph.phenotype_id = ph.phenotype_id "
                        "AND dr_ph.phenotype_type LIKE 'INDICATION'")

            SQL.consultar_filas(cursor, query, "\nPhenotype ID\tPhenotype effect" , params=(drug_id,))

        elif opcion_letra.lower() == "b":
            query = str("SELECT ph.phenotype_id, ph.phenotype_name "
                        "FROM phenotype_effect ph, drug_phenotype_effect dr_ph "
                        "WHERE dr_ph.drug_id = %s "
                        "AND dr_ph.phenotype_type LIKE 'SIDE EFFECT' "
                        "AND dr_ph.phenotype_id = ph.phenotype_id "
                        "ORDER BY dr_ph.score DESC")

            SQL.consultar_filas(cursor, query, "\nPhenotype ID\tPhenotype name\tScore", params=(drug_id,))

        nueva_consulta()

    elif int(opcion) == 5:
        menus.menu_5()

        opcion_letra = in_variable("\nIntroduzca una opción: ", re.compile("[Aa]|[Bb]|esc"), "Introduzca a o b.")
        volver_menu(opcion_letra)

        if opcion_letra.lower() == "a":
            target_type = in_variable("\nIntroduzca el tipo de diana: ", re.compile("[A-Z]|-+"),"" )
            SQL.comprobar(cursor, target_type, "target_type", "target")
            query = str("SELECT target_name_pref "
                        "FROM target "
                        "WHERE target_type = %s "
                        "ORDER BY target_name_pref ASC "
                        "LIMIT 20")

            SQL.consultar_filas(cursor, query, ("\nDianas de tipo " + target_type + ":"), params=(target_type,))

        elif opcion_letra.lower() == "b":

            query = str("SELECT target_organism, count(target_id) "
                        "FROM target group by target_organism "
                        "ORDER BY COUNT(target_organism) DESC "
                        "LIMIT 1")

            SQL.consultar_unico(cursor, query, ("Organismo con mayor número de dianas", "Número de dianas"))

        nueva_consulta()

    elif int(opcion) == 6:
        menus.menu_6()

        query = str("SELECT dr_di.inferred_score, dr.drug_id, dr.drug_name, di.disease_id, di.disease_name "
                    "FROM drug_disease dr_di, drug dr, disease di "
                    "WHERE dr_di.drug_id = dr.drug_id "
                    "AND dr_di.disease_id = di.disease_id "
                    "AND dr_di.inferred_score IS NOT null "
                    "ORDER BY inferred_score ASC "
                    "LIMIT 10")

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

    elif int(opcion) == 7:
        menus.menu_7()

        disease_id= in_variable("\nIntroduzca el identificador de la enfermedad:", re.compile("[1-9]+"), "Error. Introduzca un número.")

        menus.menu_7_1()

        type_id = in_variable("\n¿Cuál es la fuente del identificador introducido?", re.compile("[Aa]|[Bb]"), "Introduzca a o b")
        disease_name = in_variable("\nIntroduzca el nombre de la enfermedad: ", re.compile(".+"), "")
        drug_name = in_variable("\nIntroduzca el nombre del farmaco asociado: ", re.compile(".+"), "")
        SQL.comprobar(cursor, drug_name, "drug_name", "drug")

        SQL.insertar(db, cursor, disease_id, type_id, disease_name, drug_name)

        nueva_consulta()

    elif int(opcion) == 8:
        menus.menu_8()

        valor_min= in_variable("\nIntroduzca el valor minimo de score de asociacion que desea:", re.compile("[0-9]+"), "Error. Introduzca un número.")
        SQL.modificar(cursor, valor_min)

        nueva_consulta()

    elif int(opcion) == 9:
        menus.final(db)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_EMPTY_QUERY:
        print("\nERROR: La query introducida esta vacia")
        exit()
    elif err.errno == errorcode.ER_DUP_ENTRY:
        print("\nERROR: El identificador introducido ya se encuentra en la base de datos")
        exit()
    elif err.errno == errorcode.ER_NO_SUCH_TABLE:
        print("\nERROR: No existe la tabla indicada")
        exit()
    elif err.errno == errorcode.ER_SYNTAX_ERROR:
        print("\nERROR: Sintaxis incorrecta")
        exit()
    elif err.errno == errorcode.ER_WRONG_COLUMN_NAME:
        print("\nERROR: El nombre de la columna es incorrecto")
        exit()
    elif err.errno == errorcode.ER_WRONG_NUMBER_OF_COLUMNS_IN_SELECT:
        print("\nERROR: El número de columnas introducidas es incorrecto")
        exit()
    elif err.errno == errorcode.ER_WRONG_VALUE_FOR_VAR:
        print("\nERROR: No se puede establecer ese valor de la variable")
        exit()
    elif err.errno == errorcode.ER_SUBQUERY_NO_1_ROW:
        print("\nERROR: La subconsulta retorna mas de una fila")
        exit()
    elif err.errno == errorcode.ER_QUERY_INTERRUPTED:
        print("\nERROR: La query fue interrumpida")
        exit()
    elif err.errno == errorcode.ER_DATA_TOO_LONG:
        print("\nERROR: La variable introducida es demasiado larga")
        exit()
    else:
        print(err)
        exit()
