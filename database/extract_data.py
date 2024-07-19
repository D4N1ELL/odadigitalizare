from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

database_path = '/home/liviu/ODA/database/main.db'
locations_path = '/home/liviu/ODA/front/src/components/SearchForm/orase.js'

app = Flask(__name__)
CORS(app)

def get_all_locations(file_path):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    query = "SELECT loc_name FROM location"
    cursor.execute(query)
    locations = [row[0] for row in cursor.fetchall()]
    conn.close()

    with open(file_path, 'w') as file:
        file.write('export const cities = [\n')
        for location in locations:
            file.write(f'    "{location}",\n')
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

@app.route('/update', methods=['POST'])
def update():
    data = request.json
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    
    try:
        # Update personal_data table
        cursor.execute('''
            UPDATE personal_data SET
            username = ?,
            idnp = ?,
            bday = ?,
            age = ?,
            phone_number = ?,
            email = ?,
            loc_name = ?,
            program = ?,
            operator = ?,
            confirmation_date = ?,
            comment = ?,
            status = ?,
            certificate = ?,
            finance = ?,
            final_status = ?,
            exclusion = ?
            WHERE id_user = ?
        ''', (
            data['user_data']['username'],
            data['user_data']['idnp'],
            data['user_data']['bday'],
            data['user_data']['age'],
            data['user_data']['phone_number'],
            data['user_data']['email'],
            data['user_data']['location'],
            data['user_data']['program'],
            data['user_data']['operator'],
            data['user_data']['confirmation_date'],
            data['user_data']['comment'],
            data['user_data']['status'],
            data['user_data']['certificate'],
            data['user_data']['finance'],
            data['user_data']['final_status'],
            data['user_data']['exclusion'],
            data['user_data']['id_user']
        ))

        # Update date table
        cursor.execute('DELETE FROM date WHERE id_user = ?', (data['user_data']['id_user'],))
        for application_date in data['application_dates']:
            cursor.execute('INSERT INTO date (id_user, application_date) VALUES (?, ?)', (data['user_data']['id_user'], application_date))

        # Update instruction_group table
        cursor.execute('DELETE FROM instruction_group WHERE id_user = ?', (data['user_data']['id_user'],))
        for group_name in data['instruction_groups']:
            cursor.execute('INSERT INTO instruction_group (id_user, group_name) VALUES (?, ?)', (data['user_data']['id_user'], group_name))

        # Update notice table
        cursor.execute('DELETE FROM notice WHERE id_user = ?', (data['user_data']['id_user'],))
        for notice in data['notices']:
            cursor.execute('''
                INSERT INTO notice (id_user, phone_call, email_call, sms_call, viber_call, response)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (data['user_data']['id_user'], notice[0], notice[1], notice[2], notice[3], notice[4]))

        conn.commit()
        return jsonify({"success": True})
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
        return jsonify({"success": False, "error": str(e)})
    finally:
        conn.close()


@app.route('/search', methods=['POST'])
def search():
    data = request.json
    print(f"Received data: {data}")

    name = data.get('name')
    surname = data.get('surname')
    idnp = data.get('idnp')
    email = data.get('email')
    phone_number = data.get('phoneNumber')
    city = data.get('city')

    conn = sqlite3.connect(database_path)
    conn.execute("PRAGMA foreign_keys = ON")

    if name and surname:
        result = get_personal_data_by_name(conn, f"{name} {surname}")
    elif idnp:
        result = get_personal_data_by_idnp(conn, idnp)
    elif email:
        result = get_personal_data_by_mail(conn, email)
    elif phone_number:
        result = get_personal_data_by_phone(conn, phone_number)
    elif city:
        result = get_personal_data_by_city(conn, city)
    else:
        result = None

    conn.close()

    if result:
        print(f"Query result: {result}")
        return jsonify(result)
    else:
        return jsonify({"error": "No data found"}), 404

if __name__ == '__main__':
    get_all_locations(locations_path)
    app.run(debug=True)
