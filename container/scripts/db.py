
#!/usr/bin/python3
import pymysql

# Connect to the database
connection = pymysql.connect(host='db', user='root', passwd='root', db='Minutesofmeeting' )
cursor=connection.cursor()

# Drop table if already exists
cursor.execute("DROP TABLE IF EXISTS MoM")

# Create table
cursor.execute("CREATE TABLE MoM(Username VARCHAR(255), Date VARCHAR(255), Minutes_of_meeting VARCHAR(255))")

# Create a new record 
cursor.execute("SET GLOBAL local_infile=1")
insert_data = "LOAD DATA INFILE '/var/lib/mysql-files/MoM.txt' INTO TABLE MoM COLUMNS TERMINATED BY '\t' LINES TERMINATED BY '\n'"
cursor.execute(insert_data)

# Connection is not autocommit by default. So we must commit to save our changes.
connection.commit()

# Execute query
sql = "SELECT * FROM MoM"
cursor.execute(sql)

# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)

# Close datbase connection
connection.close()
