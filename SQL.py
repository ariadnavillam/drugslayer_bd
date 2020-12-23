import mysql.connector
from mysql.connector import errorcode
def contar_instancias(cursor, columna, tabla, header):
    """
    Función para contar todas las instancias de una tabla
    """
    query = str("SELECT COUNT(" + columna + ") FROM " + tabla)
    cursor.execute(query)
    for row in cursor:
       print("\n\t" + str(header) + str(row[0]))

def consultar_filas(cursor, query, header, params=None, title=None):
    """
    Funcion para obtener las filas tras una consulta con o sin parametros
    Se comprueba si el valor introducido es correcto según de resultado vacio o no
    """
    header.count("\t")
    cursor.execute(query, params)
    results = cursor.fetchall()
    count = len(results)
    if count == 0:
        print("\nEl valor introducido no existe en la base de datos")
    else:
        if title != None:
            print(title)
        print(header)
        for row in results:
            fila = str()
            for item in row:
                fila = fila + str(item) +"\t"
            print(fila)

def consultar_unico(cursor, query, header, params = None):
    """
    Funcion para obteneres valores concretos
    Se comprueba si el valor introducido es correcto según de resultado vacio o no
    """
    header.count("\t")
    cursor.execute(query, params)
    results = cursor.fetchall()
    count = len(results)
    if count == 0:
        print("\nEl valor introducido no existe en la base de datos")
    print("")
    for row in results:
        for i in range(len(header)):
            print(header[i] + " : " + str(row[i]))

def eliminar(cursor, query, params, db, n_rel):
    """
    Función para eliminar una entrada
    """
    #primero comprobamos que existe en la base de datos lo que ha introducido el usuario

    query_c = "SELECT * FROM drug_disease WHERE drug_id LIKE %s AND disease_id LIKE %s"
    cursor.execute(query_c, params)
    results = cursor.fetchall()
    if len(results) == 0:
        print("\nLa relacion no existe. ")
    else:
        try:
            cursor.execute(query,params)
            db.commit()
            print("\nSe he eliminado la relacion " + n_rel)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_CANT_DROP_FIELD_OR_KEY: 
                print("\nERROR: No se encuentra en la base de datos.")
                exit()
            else:
                print(err)
                exit()

def fuente_identificador(type_id):
    """
    Función para establecer el valor de "resource_id" según sea la fuente del id
    """
    if type_id.lower() == "a":
        resource_id = "72"
    if type_id.lower() == "b":
        resource_id = "75"
    return resource_id

def insertar(db, cursor, query_add_dis, query_add_drug_dis, disease_id, type_id, disease_name, drug_name, existe):
    """
    Funcion para insertar una el id y nombre de una enfermedad, ademas de un farmaco asociado
    """
    if existe == True:
        try:
            resource_id=fuente_identificador(type_id)
            db.start_transaction()
            cursor.execute(query_add_dis, (resource_id, disease_id, disease_name,))
            cursor.execute(query_add_drug_dis, (disease_id, drug_name,))
            db.commit()
            print("\nSe ha insertado la enfermedad con identificador " + disease_id + " y nombre " + disease_name)
            print("\nDicha enfermedad se ha asociado con el fármaco " + drug_name)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_DUP_ENTRY:
                print("\nERROR: El identificador introducido ya se encuentra en la base de datos")
                exit()
            elif err.errno == errorcode.ER_SUBQUERY_NO_1_ROW:
                print("\nERROR: La subconsulta retorna mas de una fila")
                exit()
            elif err.errno == errorcode.ER_DATA_TOO_LONG:
                print("\nERROR: La variable introducida es demasiado larga")
                exit()
            else:
                print(err)
                exit()

def modificar(cursor, query, valor_min):
    """
    Funcion para establecer a 0 el indice de asociacion por debajo de un valor introducido por teclado
    """
    query_contar= "SELECT COUNT(drug_id) FROM drug_phenotype_effect WHERE CAST(score AS DECIMAL (7, 4)) < %s AND CAST(score AS DECIMAL (7, 4)) > 0 AND phenotype_type LIKE 'SIDE EFFECT'"
    cursor.execute(query_contar, (valor_min,))
    for row in cursor:
        print("\nSe han modificado " + str(row[0]) + " filas.")
    cursor.execute(query, (valor_min,))


def comprobar(cursor, variable, columna, tabla):
    """
    Funcion para comprobar que el valor introducido existe en la base de datos
    """
    query = str("SELECT * FROM " + tabla + " WHERE " + columna + " LIKE " + "'" + variable + "'")
    cursor.execute(query)
    results = cursor.fetchall()
    count = len(results)
    if count == 0:
        print("\nEl valor introducido: " + variable + ", para la columna " + columna + " de la tabla " + tabla + " no existe en la base de datos.")
        var = False
    else:
        var = True
    return var

