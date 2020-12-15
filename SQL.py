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

def consultar_filas(cursor, query, header, existe=True, params=None, title=None):
    """
    Funcion para obtener las filas tras una consulta con o sin parametros
    """
    if existe == True:
        header.count("\t")
        cursor.execute(query, params)
        if title != None:
            print(title)
        print(header)
        for row in cursor:
            fila = str()
            for item in row:
                fila = fila + str(item) +"\t"
            print(fila)

def consultar_unico(cursor, query, header, existe=True, params = None):
    """
    Funcion para obtener el valor maximo o minimo
    """
    if existe == True:
        header.count("\t")
        cursor.execute(query, params)
        print("")
        for row in cursor:
            for i in range(len(header)):
                print(header[i] + " : " + str(row[i]))

def eliminar(cursor, query, params):
    """
    Función para eliminar 
    """
    cursor.execute(query,params)

def fuente_identificador(type_id):
    """
    Función para establecer el valor de "resource_id" según sea la fuente del id
    """
    if type_id.lower() == "a":
        resource_id = "72"
    if type_id.lower() == "b":
        resource_id = "75"
    return resource_id

<<<<<<< HEAD
def insertar(db, cursor, query_add_dis, query_add_drug_dis, disease_id, type_id, disease_name, drug_name):
    """
    Funcion para insertar una el id y nombre de una enfermedad, ademas de un farmaco asociado
    """
    resource_id=fuente_identificador(type_id)
=======
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
>>>>>>> cfba93f6c1e3e6ad1ef0c819f4a61b68a36776de

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
    cursor.execute(query, (valor_min,))

def comprobar(cursor, variable, columna, tabla):
    """
    Funcion para comprobar que el valor introducido existe en la base de datos
    """
    query = str("SELECT * FROM " + tabla + " WHERE " + columna + " LIKE " + "'" + variable + "'")
    cursor.execute(query)
    count = 0
    for row in cursor:
        count = count + 1
    if count == 0:
<<<<<<< HEAD
        print("\nEl valor introducido: " + variable + ", para la columna " + columna + " de la tabla " + tabla + " no existe en la base de datos")
        exit()
=======
        print("\nEl valor introducido: " + variable + ", para la columna " + columna + " de la tabla " + tabla + " no existe en la base de datos.")
        var = False
    else:
        var = True
    
    return var
>>>>>>> cfba93f6c1e3e6ad1ef0c819f4a61b68a36776de
