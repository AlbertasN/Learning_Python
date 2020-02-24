#pip 3 install myaql-connector-python

import mysql.connector

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_studnet",
host = "188.167.148.122",
database = "ardit700_pn1database"   
)

cursor = con.cursor()

query = cursor.execute("SELECT * FROM Dictionary")
# norint rasti viena ("SELECT * FROM Dictionary WHERE Expression = 'zodis kurio ieskai')
result = cursor.fethcall()

print(result)