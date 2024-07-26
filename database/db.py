import sqlite3

# Database path 
db_path = '/home/liviu/ODA/database/main.db'

# Function to create tables in the single database
def create_tables(conn, create_table_sql):
    try:
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        conn.commit()
        print("Table created successfully")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

# SQL commands to create the tables
personal_data_sql = """
CREATE TABLE IF NOT EXISTS personal_data (
    id_user INTEGER PRIMARY KEY,
    id_loc INTEGER,
    id_program INTEGER,
    id_status INTEGER,
    id_operator INTEGER,
    id_fstatus INTEGER,
    username TEXT,
    idnp TEXT,
    bday DATE,
    age INTEGER,
    phone_number TEXT,
    email TEXT,
    confirmation_date DATE,
    comment TEXT,
    certificate TEXT,
    exclusion BOOLEAN,
    finance TEXT
);
"""

date_sql = """
CREATE TABLE IF NOT EXISTS date (
    id_user INTEGER,
    id_date INTEGER PRIMARY KEY,
    application_date DATE,
    FOREIGN KEY (id_user) REFERENCES personal_data (id_user)
);
"""

location_sql = """
CREATE TABLE IF NOT EXISTS location (
    id_loc INTEGER PRIMARY KEY,
    loc_name TEXT
);
"""

program_sql = """
CREATE TABLE IF NOT EXISTS program (
    id_program INTEGER PRIMARY KEY,
    program_name TEXT
);
"""

status_sql = """
CREATE TABLE IF NOT EXISTS status (
    id_status INTEGER PRIMARY KEY,
    status TEXT
);
"""

instruction_group_sql = """
CREATE TABLE IF NOT EXISTS instruction_group (
    id_user INTEGER,
    id_group INTEGER PRIMARY KEY,
    group_name TEXT,
    FOREIGN KEY (id_user) REFERENCES personal_data (id_user)
);
"""

operator_sql = """
CREATE TABLE IF NOT EXISTS operator (
    id_operator INTEGER PRIMARY KEY,
    operator TEXT
);
"""

final_status_sql = """
CREATE TABLE IF NOT EXISTS final_status (
    id_fstatus INTEGER PRIMARY KEY,
    final_status TEXT
);
"""

notice_sql = """
CREATE TABLE IF NOT EXISTS notice (
    id_user INTEGER,
    id_notice INTEGER PRIMARY KEY,
    phone_call DATE,
    email_call DATE,
    sms_call DATE,
    viber_call DATE,
    response TEXT,
    FOREIGN KEY (id_user) REFERENCES personal_data (id_user)
);
"""

conn = sqlite3.connect(db_path)

create_tables(conn, personal_data_sql)
create_tables(conn, date_sql)
create_tables(conn, location_sql)
create_tables(conn, program_sql)
create_tables(conn, status_sql)
create_tables(conn, instruction_group_sql)
create_tables(conn, operator_sql)
create_tables(conn, final_status_sql)
create_tables(conn, notice_sql)

conn.close()

print("All tables created successfully.")
