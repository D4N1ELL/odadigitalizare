import sqlite3

database_path = "/home/liviu/ODA/database/main.db"

conn = sqlite3.connect(database_path)
cursor = conn.cursor()
query = "SELECT loc_name FROM location"
cursor.execute(query)
locations = [row[0] for row in cursor.fetchall()]
print(locations)
conn.close()