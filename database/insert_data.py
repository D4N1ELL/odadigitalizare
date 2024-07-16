import sqlite3
import json
import math

# Get last id from table or insert a new one
def get_id(conn, table, column, value):
    cursor = conn.cursor()

    # Check if the value is NaN and replace with "Necunoscut"
    if isinstance(value, float) and math.isnan(value):
        value = "Necunoscut"
    
    cursor.execute(f"SELECT rowid FROM {table} WHERE {column} = ?", (value,))
    row = cursor.fetchone()
    if row:
        return row[0]
    cursor.execute(f"INSERT INTO {table} ({column}) VALUES (?)", (value,))
    conn.commit()
    return cursor.lastrowid

# Insert data from JSON in table personal_data
def personal_data(conn, data, cursor):

    id_loc = get_id(conn, "location", "loc_name", data["location"])
    id_program = get_id(conn, "program", "program_name", data["program"])
    id_operator = get_id(conn, "operator", "operator", data["operator"])
    id_status = get_id(conn, "status", "status", data["statut"])
    id_fstatus = get_id(conn, "final_status", "final_status", data["final_statut"])

    insert_personal_data_sql = """
    INSERT INTO personal_data (username, idnp, bday, age, phone_number, email, id_loc, id_program, id_operator, confirmation_date, comment, id_status, certificate, finance, id_fstatus, exclusion)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    personal_data_values = (
        data["username"],
        data["idnp"],
        data["bday"],
        data["age"],
        data["phone_number"],
        data["email"],
        id_loc,
        id_program,
        id_operator,
        data["confirmation_date"],
        data["comment"],
        id_status,
        data["certificate"],
        data["finance"],
        id_fstatus,
        data["exclusion"]
    )

    cursor.execute(insert_personal_data_sql, personal_data_values)
    id_user = cursor.lastrowid
    conn.commit()
    return id_user

# Insert data from JSON in table date
def application_date(cursor, id_user, data):
    insert_application_date_sql = """
    INSERT INTO date (id_user, application_date)
    VALUES (?, ?)
    """
    application_dates = [(id_user, date) for date in data["application_date"]]
    cursor.executemany(insert_application_date_sql, application_dates)
    conn.commit()

# Insert data from JSON in table instruction_group
def instruction_group(cursor, id_user, data):
    insert_instruction_group_sql = """
    INSERT INTO instruction_group (id_user, group_name)
    VALUES (?, ?)
    """
    groups = [(id_user, group) for group in data["instruction_group"]]
    cursor.executemany(insert_instruction_group_sql, groups)
    conn.commit()

# Insert data from JSON in notice table
def notice(cursor, id_user, data):
    insert_notice_sql = """
    INSERT INTO notice (id_user, phone_call, email_call, sms_call, viber_call, response)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    notice_data = data["notice"]
    num_notices = len(notice_data["response"])
    notices = []

    for i in range(num_notices):
        phone_call = notice_data["phone_call"][i]
        email_call = notice_data["email_call"][i]
        sms_call = notice_data["sms_call"][i]
        viber_call = notice_data["viber_call"][i]
        response = notice_data["response"][i]

        notice_tuple = (id_user, phone_call, email_call, sms_call, viber_call, response)
        notices.append(notice_tuple)

    cursor.executemany(insert_notice_sql, notices)
    conn.commit()

db_path = '/home/liviu/ODA/database/main.db'
json_file_path = '/home/liviu/ODA/database/data.json'
conn = sqlite3.connect(db_path)
conn.execute("PRAGMA foreign_keys = ON")

with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

for obj in data:
    cursor = conn.cursor()
    id_user = personal_data(conn, obj, cursor)
    application_date(cursor, id_user, obj)
    instruction_group(cursor, id_user, obj)
    notice(cursor, id_user, obj)

conn.close()
print("Data inserted successfully.")
