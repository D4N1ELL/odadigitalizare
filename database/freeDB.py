import sqlite3

db_path = 'database/main.db'

table_names = [
    'personal_data',
    'date',
    'location',
    'program',
    'status',
    'instruction_group',
    'operator',
    'final_status',
    'notice'
]

def clear_data(db_path, table_names):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    for table_name in table_names:
        c.execute(f'DELETE FROM {table_name}')
    conn.commit()
    conn.close()

clear_data(db_path, table_names)