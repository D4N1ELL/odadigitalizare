#All extracts of data

def get_additional_data(file_path, table, field, conn, cursor):
    query = f"SELECT {field}_name FROM {table}"
    cursor.execute(query)
    data = [row[0] for row in cursor.fetchall()]

    with open(file_path, 'w') as file:
        file.write(f'export const {table} = [\n')
        for item in data:
            file.write(f'    "{item}",\n')
        file.write('];\n')

def get_personal_data(cursor, query, params):
    cursor.execute(query, params)
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

    return result

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
    return get_personal_data(cursor, query, (username,))

def get_personal_data_by_idnp(conn, idnp):
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
        pd.idnp = ?
    """
    return get_personal_data(cursor, query, (idnp,))

def get_personal_data_by_mail(conn, email):
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
        pd.email = ?
    """
    return get_personal_data(cursor, query, (email,))

def get_personal_data_by_phone(conn, phone_number):
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
        pd.phone_number = ?
    """
    return get_personal_data(cursor, query, (phone_number,))

def get_personal_data_by_city(conn, city):
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
        l.loc_name = ?
    """
    cursor.execute(query, (city,))
    rows = cursor.fetchall()
    
    results = []
    for row in rows:
        user_data = {
            "username": row[1],
            "idnp": row[2],
            "bday": row[3],
            "age": row[4],
            "phone_number": row[5],
            "email": row[6],
            "location": row[7],
            "program": row[8],
            "operator": row[9],
            "confirmation_date": row[10],
            "comment": row[11],
            "status": row[12],
            "certificate": row[13],
            "finance": row[14],
            "final_status": row[15],
            "exclusion": row[16],
        }
        results.append(user_data)
    
    return results

def get_personal_data_by_program(conn, program):
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
        p.program_name = ?
    """
    cursor.execute(query, (program,))
    rows = cursor.fetchall()
    
    results = []
    for row in rows:
        user_data = {
            "username": row[1],
            "idnp": row[2],
            "bday": row[3],
            "age": row[4],
            "phone_number": row[5],
            "email": row[6],
            "location": row[7],
            "program": row[8],
            "operator": row[9],
            "confirmation_date": row[10],
            "comment": row[11],
            "status": row[12],
            "certificate": row[13],
            "finance": row[14],
            "final_status": row[15],
            "exclusion": row[16],
        }
        results.append(user_data)
    
    return results

def get_personal_data_by_instructionGroup(conn, group):
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
    LEFT JOIN 
        instruction_group ig ON pd.id_user = ig.id_user
    WHERE 
        ig.group_name = ?
    """
    cursor.execute(query, (group,))
    rows = cursor.fetchall()
    
    results = []
    for row in rows:
        user_data = {
            "username": row[1],
            "idnp": row[2],
            "bday": row[3],
            "age": row[4],
            "phone_number": row[5],
            "email": row[6],
            "location": row[7],
            "program": row[8],
            "operator": row[9],
            "confirmation_date": row[10],
            "comment": row[11],
            "status": row[12],
            "certificate": row[13],
            "finance": row[14],
            "final_status": row[15],
            "exclusion": row[16],
        }
        results.append(user_data)
    
    return results
