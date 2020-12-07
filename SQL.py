def consultar_filas(cursor, query, params, header):
    header.count("\t")
    cursor.execute(query, params)
    print(header)
    for row in cursor:
        fila = str()
        for item in row:
            fila = fila + item +"\t"
        print(fila)

def consultar_unico(cursor, query, params, header):
    header.count("\t")
    cursor.execute(query, params)
    print("")
    for row in cursor:
        for i in range(len(header)):
            print(header[i] + " : " + row[i])
        

def insertar():
    query=""

def modificar():
    query=""

def eliminar():
    query=""
