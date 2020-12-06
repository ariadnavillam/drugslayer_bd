#CONSULTA 3A
import mysql.connector

config = {
    'host':'localhost',
    'port':'3306',
    'user':'drugslayer',
    'password':'drugslayer_pwd',
    'database':'disnet_drugslayer'
}


db = mysql.connector.connect(**config)

cursor = db.cursor()

try:
    disease_name = input('Introduce el nombre de la enfermedad: ')
    
    query1 = "SELECT drug.drug_id, drug.drug_name FROM drug, drug_disease, disease WHERE disease.disease_name=%s AND drug.drug_id=drug_disease.drug_id AND disease.disease_id=drug_disease.disease_id"
    cursor.execute(query1, (disease_name,))
    for row in cursor:
        drug_id = row[0]
        drug_name = row[1]
        print("Drug_id: %s" % drug_id)
        print("Drug_name: %s" % drug_name)
        
except ValueError:
    print("Error: el nombre de la enfermedad no existe")

finally:
    db.close()


#CONSULTA 3B
import mysql.connector

config = {
    'host':'localhost',
    'port':'3306',
    'user':'drugslayer',
    'password':'drugslayer_pwd',
    'database':'disnet_drugslayer'
}

try:
    
    query2 = "SELECT disease.disease_name, drug.drug_name FROM disease, drug, drug_disease WHERE drug.drug_id=drug_disease.drug_id AND disease.disease_id=drug_disease.disease_id ORDER BY drug_disease.inferred_score DESC LIMIT 1"
    cursor.execute(query2)
    for row in cursor:
        disease_name = row[0]
        drug_name = row[1]
        print("Disease_name: %s" % drug_id)
        print("Drug_name: %s" % drug_name)
        
except ValueError:
    print("Error: algo ha ido mal")

finally:
    db.close()
    print("Connection closed")