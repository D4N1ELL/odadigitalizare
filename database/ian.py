import sqlite3

def get_personal_data_by_name(conn, username):
    cursor = conn.cursor()
    query = """
    SELECT 
        pd.id_user, pd.username, pd.idnp, pd.bday, pd.age, pd.phone_number, pd.email, 
        l.loc_name, p.program_name, o.operator, pd.confirmation_date, pd.comment, 
        s.status, pd.certificate, pd.finance, fs.final_status, pd.exclusion
    FROM 
        personal_data pd
    LEFT JOIN 
        location l ON pd.id_loc = l.rowid
    LEFT JOIN 
        program p ON pd.id_program = p.rowid
    LEFT JOIN 
        operator o ON pd.id_operator = o.rowid
    LEFT JOIN 
        status s ON pd.id_status = s.rowid
    LEFT JOIN 
        final_status fs ON pd.id_fstatus = fs.rowid
    WHERE 
        pd.username = ?
    """
    cursor.execute(query, (username,))
    user_data = cursor.fetchone()

    if not user_data:
        return None

    user_id = user_data[0]

    query_dates = "SELECT application_date FROM date WHERE id_user = ?"
    cursor.execute(query_dates, (user_id,))
    application_dates = [row[0] for row in cursor.fetchall()]

    query_groups = "SELECT group_name FROM instruction_group WHERE id_user = ?"
    cursor.execute(query_groups, (user_id,))
    instruction_groups = [row[0] for row in cursor.fetchall()]

    query_notices = """
    SELECT phone_call, email_call, sms_call, viber_call, response 
    FROM notice WHERE id_user = ?
    """
    cursor.execute(query_notices, (user_id,))
    notices = cursor.fetchall()

    result = {
        "user_data": {
            "username": user_data[1],
            "idnp": user_data[2],
            "bday": user_data[3],
            "age": user_data[4],
            "phone_number": user_data[5],
            "email": user_data[6],
            "location": user_data[7],
            "program": user_data[8],
            "operator": user_data[9],
            "confirmation_date": user_data[10],
            "comment": user_data[11],
            "status": user_data[12],
            "certificate": user_data[13],
            "finance": user_data[14],
            "final_status": user_data[15],
            "exclusion": user_data[16],
        },
        "application_dates": application_dates,
        "instruction_groups": instruction_groups,
        "notices": notices,
    }
    print(result)
    return result

conn = sqlite3.connect('/home/liviu/ODA/database/main.db')
conn.execute("PRAGMA foreign_keys = ON")
name = "Ana"
lastname = "Maria"

result = get_personal_data_by_name(conn, name+" "+lastname)