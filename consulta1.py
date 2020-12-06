#CONSULTA 1A
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
    query1 = "SELECT COUNT(drug.drug_id) FROM drug"
    cursor.execute(query1)
    for row in cursor:
        count_drug = row[0]
        print("1) Número total de fármacos: %s" % count_drug)
    
    
    query2 = "SELECT COUNT(resource_id) FROM disease"
    cursor.execute(query2)
    for row in cursor:
        count_disease = row[0]
        print("2) Número total de enfermedades: %s " % count_disease)
    
    
    query3 = "SELECT COUNT(phenotype_id) FROM drug_phenotype_effect"
    cursor.execute(query3)
    for row in cursor:
        count_phenotype = row[0]
        print("3) Número total de efectos fenotípicos: %s " % count_phenotype)
    
    
    query4 = "SELECT COUNT(target_id) FROM drug_target"
    cursor.execute(query4)
    for row in cursor:
        count_target = row[0]
        print("4) Número total de targets diferentes: %s " % count_target)
   

        
except ValueError:
    print("Something goes wrong")

finally:
    db.close()
    print("Connection closed")



#CONSULTA 1B
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
    query1 = "SELECT drug_id, drug_name, molecular_type, chemical_structure, inchi_key FROM drug WHERE drug_id IS NOT NULL AND drug_name IS NOT NULL AND molecular_type IS NOT NULL AND chemical_structure IS NOT NULL AND inchi_key IS NOT NULL LIMIT 10"
    cursor.execute(query1)
    print("PRIMERAS 10 INSTANCIAS DE MEDICAMENTOS")
    for row in cursor:
        drug_id = row[0]
        drug_name = row[1]
        molecular_type = row[2]
        chemical_structure = row[3]
        inchi_key = row[4]
        #print("PRIMERA INSTANCIA:")
        #print("Identificador: %s" % drug_id)
        #print("Nombre: %s" % drug_name)
        #print("Tipo molecular: %s" % molecular_type)
        #print("Estructura química: %s" % chemical_structure)
        #print("InChy-key: %s" % inchi_key)
        print(drug_id + "\t" + drug_name + "\t" + molecular_type + "\t" + chemical_structure + "\t" + inchi_key)
    
    
    query2 = "SELECT disease_id, disease_name FROM disease WHERE disease_id IS NOT NULL AND disease_name IS NOT NULL LIMIT 10"
    cursor.execute(query2)
    print("\nPRIMERAS 10 INSTANCIAS DE ENFERMEDADES")
    for row in cursor:
        disease_id = row[0]
        disease_name = row[1]
        #print("Identificador: %s " % disease_id)
        #print("Nombre: %s" % disease_name)
        print(disease_id + "\t" + disease_name)
    
    query3 = "SELECT phenotype_id, phenotype_name FROM phenotype_effect WHERE phenotype_id IS NOT NULL AND phenotype_name IS NOT NULL LIMIT 10"
    cursor.execute(query3)
    print("\nPRIMERAS 10 INSTANCIAS DE EFECTOS FENOTÍPICOS")
    for row in cursor:
        phenotype_id = row[0]
        phenotype_name = row[1]
        #print("Identificador: %s " % phenotype_id)
        #print("Nombre: %s" % phenotype_name)
        print(phenotype_id + "\t" + phenotype_name)
    
    query4 = "SELECT target_id, target_name_pref, target_type, target_organism FROM target WHERE target_id IS NOT NULL AND target_name_pref IS NOT NULL AND target_type IS NOT NULL AND target_organism IS NOT NULL LIMIT 10"
    cursor.execute(query4)
    print("\nPRIMERAS 10 INSTANCIAS DE TARGET")
    for row in cursor:
        target_id = row[0]
        target_name = row[1]
        target_type = row[2]
        target_organism = row[3]
        #print("Identificador: %s " % target_id)
        #print("Nombre: %s" % target_name)
        #print("Tipo: %s" % target_type)
        #print("Nombre del organismo: %s" % target_organism)
        print(target_id + "\t" + target_name + "\t" + target_type + "\t" + target_organism)

        
except ValueError:
    print("Something goes wrong")

finally:
    db.close()
    print("Connection closed")