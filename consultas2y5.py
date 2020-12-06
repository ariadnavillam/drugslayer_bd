config = {
		'host':"%",
		'port':"3306",
		'user':"drugslayer",
		'passwd':"drugslayer_pwd",
		'db':"disnet_drugslayer"
		}
	
import mysql.connector
db = mysql.connector.connect(**config)
cursor = db.cursor()


#Ejercicio 2
#a)
try:
	drug_iden = input("Introduce the identifier of the drug: ")
	print(" ")
	query = "SELECT drug_name, molecular_type, chemical_structure, inchi_key from drug where drug_id= %s"
	cursor.execute(query,(drug_iden,))
	for row in cursor:
		names=row[0]
		type=row[1]
		struct=row[2]
		inchi_k=row[3]
		print("Name of drug: %s" % names)\t
		print("Molecular type: %s" % type)\t
		print("Chemical structure: %s" % struct)\t
		print("Inchi key: %s" % inchi_k)
except ValueError:
	print("El drug_id que has introducido no es correcto o no se encuentra en la BD")

finally:
	db.close()
	print(" ")
	print("Connection closed")

#b)
try:
	drug_nam = input("Introduce the name of the drug: ")
	query = "SELECT synonymous_name FROM synonymous, drug WHERE synonymous.drug_id=drug.drug_id AND drug.drug_name = %s"
	cursor.execute(query, (drug_nam,))
	print("The synonymous names of drug are: ")
	for row in cursor:
		syn_name=row[0]
		print("%s" %syn_name)

except ValueError:
	print("El drug_id que has introducido no es correcto o no se encuentra en la BD")

finally:
	db.close()
	print(" ")
	print("Connection closed")


#c)
try:
	drug_id = input("Introduce the identifier of the drug: ")
	query = "SELECT ATC_code.ATC_code_id from ATC_code, drug WHERE drug.drug_id = %s GROUP BY drug.drug_id"
	cursor.execute(query,(drug_id,))
	for row in cursor:
		code=row[0]
		print("ATC code of drug: %s" % code)

except ValueError:
	print("ATC code not found in DB")

else:
	db.close()
	print(" ")
	print("Connection closed")



#Ejercicio 5
#a)

try:
	drug_tar = input("Introduce the target type to show: ")
	query = "SELECT target_name_pref FROM target WHERE target_type = %s ORDER BY target_name_pref ASC LIMIT 20"
	cursor.execute(query,(drug_tar,))
	for row in cursor:
		name_tar=row[0]
		print("Name of the target type: %s" % name_tar)
 	
except ValueError:
	print("The target type introduced is not correct or is not in DB")
	
else:
	db.close()
	print(" ")
	print("Connection closed")

#b)

try:
	query = "SELECT target_id, target_organism, COUNT(target_organism) FROM target GROUP BY tax_id ORDER BY count(target_organism) desc LIMIT 1"
	cursor.execute(query)
	for row in cursor:
		taxa=row[0]
		org=row[1]
		cont=row[2]
		print(" ")
		print("The identifier of taxa is: %s" % taxa)
		print("The organism with greater number of targets: %s" % org)
		print("Organism associated with greather number of targets: %s" % cont)

except ValueError:
	print("Something went wrong with this organism")
	
else:
	db.close()
	print(" ")
	print("Everything ok! Connection closed")