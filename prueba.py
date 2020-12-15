while True:
    "Esto es un bucle"
    var = input("Introduzca una variable: ")
    print(var)
    if var == "exit":
        exit()
    else:
        continue
    
except mysql.connector.Error as err:

    if err.errno == errorcode.ER_DUP_ENTRY: #inserciones
        print("\nERROR: El identificador introducido ya se encuentra en la base de datos")
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

    else:
        print(err)
        exit()
