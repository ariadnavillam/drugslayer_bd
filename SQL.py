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
    """
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

def consultar_filas_imprimir(cursor, query, params, header, file):
    """
    Funcion para mostrar por pantalla solo las 10 primeras instancias y guadar todas en un archivo
    """
    f = open(file, "a")
    header.count("\t")
    cursor.execute(query, params)
    print(header)
    f.write("\nPhenotype ID\tPhenotype effect")
    count = 0
    for row in cursor:
        fila = str()
        for item in row:
            fila = fila + item +"\t"
        if count < 10:
            print(row[0] + "\t" + row[1])
            f.write(row[0] + "\t" + row[1])
        else:
            f.write(row[0] + "\t" + row[1])
        print(fila)

    f.close()

def consultar_unico(cursor, query, header, params = None):
    """
    Funcion para obtener el valor maximo o minimo
    """
    header.count("\t")
    cursor.execute(query, params)
    print("")
    for row in cursor:
        for i in range(len(header)):
            print(header[i] + " : " + str(row[i]))

def eliminar():
    query=""

def fuente_identificador(type_id):
    """
    Función para establecer el valor de "resource_id" según sea la fuente del id
    """
    if type_id.lower() == "a":
        resource_id = "72"
    if type_id.lower() == "b":
        resource_id = "75"
    return resource_id

def insertar(db, cursor, disease_id, type_id, disease_name, drug_name):
    """
    Funcion para insertar una el id y nombre de una enfermedad, ademas de un farmaco asociado
    """
    resource_id=fuente_identificador(type_id)
    query_add_dis="INSERT INTO disease VALUES (%s, %s, %s)"
    query_add_drug_dis="INSERT INTO drug_disease (disease_id, drug_id, source_id) VALUES (%s, (SELECT drug_id FROM drug WHERE drug_name=%s), 3)"

    db.start_transaction()
    cursor.execute(query_add_dis, (resource_id, disease_id, disease_name,))
    cursor.execute(query_add_drug_dis, (disease_id, drug_name,))
    db.commit()

def modificar(cursor, valor_min):
    """
    Funcion para establecer a 0 el indice de asociacion por debajo de un valor introducido por teclado
    """
    query="UPDATE drug_phenotype_effect SET score=0 WHERE score < %s AND phenotype_type LIKE 'SIDE EFFECT'"
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
        print("\nEl valor introducido: " + variable + ", para la columna " + columna + " de la tabla " + tabla + " es incorrecto")
        exit()
