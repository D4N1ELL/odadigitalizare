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
            "id_user": user_id,
            "username": user_data[1],
            "idnp": user_data[2],
            "bday": user_data[3],
            "age": user_data[4],
            "phone_number": user_data[5],
            "email": user_data[6],
            "id_loc": user_data[7],
            "loc_name": user_data[8],
            "id_program": user_data[9],
            "program_name": user_data[10],
            "id_operator": user_data[11],
            "operator": user_data[12],
            "confirmation_date": user_data[13],
            "comment": user_data[14],
            "id_status": user_data[15],
            "status": user_data[16],
            "certificate": user_data[17],
            "finance": user_data[18],
            "id_final_status": user_data[19],
            "final_status": user_data[20],
            "exclusion": user_data[21]
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
        pd.id_loc, l.loc_name, pd.id_program, p.program_name, pd.id_operator, o.operator, 
        pd.confirmation_date, pd.comment, pd.id_status, s.status, pd.certificate, 
        pd.finance, pd.id_fstatus, fs.final_status, pd.exclusion
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
        pd.id_loc, l.loc_name, pd.id_program, p.program_name, pd.id_operator, o.operator, 
        pd.confirmation_date, pd.comment, pd.id_status, s.status, pd.certificate, 
        pd.finance, pd.id_fstatus, fs.final_status, pd.exclusion
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
        pd.id_loc, l.loc_name, pd.id_program, p.program_name, pd.id_operator, o.operator, 
        pd.confirmation_date, pd.comment, pd.id_status, s.status, pd.certificate, 
        pd.finance, pd.id_fstatus, fs.final_status, pd.exclusion
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
        pd.id_loc, l.loc_name, pd.id_program, p.program_name, pd.id_operator, o.operator, 
        pd.confirmation_date, pd.comment, pd.id_status, s.status, pd.certificate, 
        pd.finance, pd.id_fstatus, fs.final_status, pd.exclusion
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
    personal_data_query = """
    SELECT 
        pd.id_user, pd.username, pd.idnp, pd.bday, pd.age, pd.phone_number, pd.email, 
        pd.id_loc, l.loc_name, pd.id_program, p.program_name, pd.id_operator, o.operator, 
        pd.confirmation_date, pd.comment, pd.id_status, s.status, pd.certificate, 
        pd.finance, pd.id_fstatus, fs.final_status, pd.exclusion
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
    
    cursor.execute(personal_data_query, (city,))
    rows = cursor.fetchall()
    
    results = []
    for row in rows:
        user_data = {
            "id_user": row[0],
            "username": row[1],
            "idnp": row[2],
            "bday": row[3],
            "age": row[4],
            "phone_number": row[5],
            "email": row[6],
            "id_loc": row[7],
            "loc_name": row[8],
            "id_program": row[9],
            "program_name": row[10],
            "id_operator": row[11],
            "operator": row[12],
            "confirmation_date": row[13],
            "comment": row[14],
            "id_status": row[15],
            "status": row[16],
            "certificate": row[17],
            "finance": row[18],
            "id_final_status": row[19],
            "final_status": row[20],
            "exclusion": row[21]
        }
        
        query_dates = "SELECT application_date FROM date WHERE id_user = ?"
        cursor.execute(query_dates, (user_data["id_user"],))
        application_dates = [row[0] for row in cursor.fetchall()]
        
        query_groups = "SELECT group_name FROM instruction_group WHERE id_user = ?"
        cursor.execute(query_groups, (user_data["id_user"],))
        instruction_groups = [row[0] for row in cursor.fetchall()]
        
        query_notices = """
        SELECT phone_call, email_call, sms_call, viber_call, response 
        FROM notice WHERE id_user = ?
        """
        cursor.execute(query_notices, (user_data["id_user"],))
        notices = cursor.fetchall()
        
        results.append({
            "user_data": user_data,
            "application_dates": application_dates,
            "instruction_groups": instruction_groups,
            "notices": notices
        })
    
    return results

def get_personal_data_by_program(conn, program):
    cursor = conn.cursor()
    personal_data_query = """
    SELECT 
        pd.id_user, pd.username, pd.idnp, pd.bday, pd.age, pd.phone_number, pd.email, 
        pd.id_loc, l.loc_name, pd.id_program, p.program_name, pd.id_operator, o.operator, 
        pd.confirmation_date, pd.comment, pd.id_status, s.status, pd.certificate, 
        pd.finance, pd.id_fstatus, fs.final_status, pd.exclusion
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
    
    cursor.execute(personal_data_query, (program,))
    rows = cursor.fetchall()
    
    results = []
    for row in rows:
        user_data = {
            "id_user": row[0],
            "username": row[1],
            "idnp": row[2],
            "bday": row[3],
            "age": row[4],
            "phone_number": row[5],
            "email": row[6],
            "id_loc": row[7],
            "loc_name": row[8],
            "id_program": row[9],
            "program_name": row[10],
            "id_operator": row[11],
            "operator": row[12],
            "confirmation_date": row[13],
            "comment": row[14],
            "id_status": row[15],
            "status": row[16],
            "certificate": row[17],
            "finance": row[18],
            "id_final_status": row[19],
            "final_status": row[20],
            "exclusion": row[21]
        }
        
        query_dates = "SELECT application_date FROM date WHERE id_user = ?"
        cursor.execute(query_dates, (user_data["id_user"],))
        application_dates = [row[0] for row in cursor.fetchall()]
        
        query_groups = "SELECT group_name FROM instruction_group WHERE id_user = ?"
        cursor.execute(query_groups, (user_data["id_user"],))
        instruction_groups = [row[0] for row in cursor.fetchall()]
        
        query_notices = """
        SELECT phone_call, email_call, sms_call, viber_call, response 
        FROM notice WHERE id_user = ?
        """
        cursor.execute(query_notices, (user_data["id_user"],))
        notices = cursor.fetchall()
        
        results.append({
            "user_data": user_data,
            "application_dates": application_dates,
            "instruction_groups": instruction_groups,
            "notices": notices
        })
    
    return results

def get_personal_data_by_instructionGroup(conn, group):
    cursor = conn.cursor()
    personal_data_query = """
    SELECT 
        pd.id_user, pd.username, pd.idnp, pd.bday, pd.age, pd.phone_number, pd.email, 
        pd.id_loc, l.loc_name, pd.id_program, p.program_name, pd.id_operator, o.operator, 
        pd.confirmation_date, pd.comment, pd.id_status, s.status, pd.certificate, 
        pd.finance, pd.id_fstatus, fs.final_status, pd.exclusion
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
    cursor.execute(personal_data_query, (group,))
    rows = cursor.fetchall()
    
    results = []
    for row in rows:
        user_data = {
            "id_user": row[0],
            "username": row[1],
            "idnp": row[2],
            "bday": row[3],
            "age": row[4],
            "phone_number": row[5],
            "email": row[6],
            "id_loc": row[7],
            "loc_name": row[8],
            "id_program": row[9],
            "program_name": row[10],
            "id_operator": row[11],
            "operator": row[12],
            "confirmation_date": row[13],
            "comment": row[14],
            "id_status": row[15],
            "status": row[16],
            "certificate": row[17],
            "finance": row[18],
            "id_final_status": row[19],
            "final_status": row[20],
            "exclusion": row[21]
        }
        
        query_dates = "SELECT application_date FROM date WHERE id_user = ?"
        cursor.execute(query_dates, (user_data["id_user"],))
        application_dates = [row[0] for row in cursor.fetchall()]
        
        query_groups = "SELECT group_name FROM instruction_group WHERE id_user = ?"
        cursor.execute(query_groups, (user_data["id_user"],))
        instruction_groups = [row[0] for row in cursor.fetchall()]
        
        query_notices = """
        SELECT phone_call, email_call, sms_call, viber_call, response 
        FROM notice WHERE id_user = ?
        """
        cursor.execute(query_notices, (user_data["id_user"],))
        notices = cursor.fetchall()
        
        results.append({
            "user_data": user_data,
            "application_dates": application_dates,
            "instruction_groups": instruction_groups,
            "notices": notices
        })
    
    return results
