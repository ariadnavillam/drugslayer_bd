def contar_instancias(cursor, query, header):
    cursor.execute(query)
    for row in cursor:
        print("\n\t" + str(header) + str(row[0]))

def primeras_instancias(cursor, query, header, nombre_columnas):
    cursor.execute(query)
    print("\nPrimeras diez instancias de " + header)
    print(nombre_columnas.replace(", ", "\t"))
    for row in cursor:
        fila = str()
        for item in row:
            fila = fila + str(item) + "\t"
        print(fila)

def consultar_filas(cursor, query, params, header):
    header.count("\t")
    cursor.execute(query, params)
    print(header)
    for row in cursor:
        fila = str()
        for item in row:
            fila = fila + str(item) +"\t"
        print(fila)

def consultar_filas_imprimir(cursor, query, params, header, file):
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

def consultar_unico(cursor, query, params, header):
    header.count("\t")
    cursor.execute(query, params)
    print("")
    for row in cursor:
        for i in range(len(header)):
            print(header[i] + " : " + row[i])

def eliminar():
    query=""

def insertar():
    query=""

def modificar():
    query=""
