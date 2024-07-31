from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from extract_data import (
    get_personal_data_by_name, get_personal_data_by_mail, get_personal_data_by_city,
    get_personal_data_by_idnp, get_personal_data_by_phone, get_personal_data_by_program,
    get_personal_data_by_instructionGroup, get_additional_data
)

database_path = '/home/liviu/ODA/database/main.db'
locations_path = '/home/liviu/ODA/front/src/components/SearchForm/orase.js'
programs_path = '/home/liviu/ODA/front/src/components/SearchForm/programs.js'
instruction_groups_path = '/home/liviu/ODA/front/src/components/SearchForm/instructionGroups.js'

tables = ['location', 'program', 'instruction_group']
fields = ['loc', 'program', 'group']
paths = [locations_path, programs_path, instruction_groups_path]

app = Flask(__name__)
CORS(app)

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
    program = data.get('program')
    instructionGroup = data.get('instructionGroup')

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
    elif program:
        result = get_personal_data_by_program(conn, program)
    elif instructionGroup:
        result = get_personal_data_by_instructionGroup(conn, instructionGroup)
    else:
        result = None

    conn.close()

    if result:
        print(f"Query result: {result}")
        return jsonify(result)
    else:
        return jsonify({"error": "No data found"}), 404

def get_db():
    conn = sqlite3.connect(database_path)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/update', methods=['POST'])
def update_person():
    data = request.json
    conn = get_db()
    cursor = conn.cursor()

    try:
        print("Data received for update:", data)

        user_data = data['user_data']
        print("User data:", user_data)

        # Check if the program exists, and get its ID or insert a new program
        cursor.execute("SELECT id_program FROM program WHERE program_name = ?", (user_data['program_name'],))
        program_row = cursor.fetchone()

        if program_row:
            program_id = program_row[0]
            print("Existing program ID:", program_id)
        else:
            cursor.execute("INSERT INTO program (program_name) VALUES (?)", (user_data['program_name'],))
            program_id = cursor.lastrowid
            print("Inserted new program ID:", program_id)

        user_data['id_program'] = program_id

        # Check if the status exists, and get its ID or insert a new status
        cursor.execute("SELECT id_status FROM status WHERE status = ?", (user_data['status'],))
        status_row = cursor.fetchone()

        if status_row:
            status_id = status_row[0]
            print("Existing status ID:", status_id)
        else:
            cursor.execute("INSERT INTO status (status) VALUES (?)", (user_data['status'],))
            status_id = cursor.lastrowid
            print("Inserted new status ID:", status_id)

        user_data['id_status'] = status_id

        # Check if the final status exists, and get its ID or insert a new final status
        cursor.execute("SELECT id_fstatus FROM final_status WHERE final_status = ?", (user_data['final_status'],))
        final_status_row = cursor.fetchone()

        if final_status_row:
            final_status_id = final_status_row[0]
            print("Existing final status ID:", final_status_id)
        else:
            cursor.execute("INSERT INTO final_status (final_status) VALUES (?)", (user_data['final_status'],))
            final_status_id = cursor.lastrowid
            print("Inserted new final status ID:", final_status_id)

        user_data['id_final_status'] = final_status_id

        # Check if the location exists, and get its ID or insert a new location
        cursor.execute("SELECT id_loc FROM location WHERE loc_name = ?", (user_data['loc_name'],))
        location_row = cursor.fetchone()

        if location_row:
            location_id = location_row[0]
            print("Existing location ID:", location_id)
        else:
            cursor.execute("INSERT INTO location (loc_name) VALUES (?)", (user_data['loc_name'],))
            location_id = cursor.lastrowid
            print("Inserted new location ID:", location_id)

        user_data['id_loc'] = location_id

        # Check if the operator exists, and get its ID or insert a new operator
        cursor.execute("SELECT id_operator FROM operator WHERE operator = ?", (user_data['operator'],))
        operator_row = cursor.fetchone()

        if operator_row:
            operator_id = operator_row[0]
            print("Existing operator ID:", operator_id)
        else:
            cursor.execute("INSERT INTO operator (operator) VALUES (?)", (user_data['operator'],))
            operator_id = cursor.lastrowid
            print("Inserted new operator ID:", operator_id)

        user_data['id_operator'] = operator_id

        update_query = """
            UPDATE personal_data
            SET username = ?, idnp = ?, bday = ?, age = ?, phone_number = ?, email = ?, 
                id_loc = ?, id_program = ?, id_operator = ?, confirmation_date = ?, comment = ?, 
                id_status = ?, certificate = ?, finance = ?, id_fstatus = ?, exclusion = ?
            WHERE id_user = ?
        """
        update_values = (
            user_data['username'], user_data['idnp'], user_data['bday'], 
            int(user_data['age']), user_data['phone_number'], user_data['email'], 
            user_data['id_loc'], user_data['id_program'], user_data['id_operator'], user_data['confirmation_date'], 
            user_data['comment'], user_data['id_status'], user_data['certificate'], 
            user_data['finance'], user_data['id_final_status'], user_data['exclusion'], 
            user_data['id_user']
        )

        print("Executing update query:", update_query)
        print("With values:", update_values)

        cursor.execute(update_query, update_values)

        cursor.execute("DELETE FROM date WHERE id_user = ?", (user_data['id_user'],))
        for date in data['application_dates']:
            cursor.execute("INSERT INTO date (id_user, application_date) VALUES (?, ?)", (user_data['id_user'], date))

        cursor.execute("DELETE FROM instruction_group WHERE id_user = ?", (user_data['id_user'],))
        for group in data['instruction_groups']:
            cursor.execute("INSERT INTO instruction_group (id_user, group_name) VALUES (?, ?)", (user_data['id_user'], group))

        cursor.execute("DELETE FROM notice WHERE id_user = ?", (user_data['id_user'],))
        for notice in data['notices']:
            cursor.execute("""
                INSERT INTO notice (id_user, phone_call, email_call, sms_call, viber_call, response)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (user_data['id_user'], notice[0], notice[1], notice[2], notice[3], notice[4]))

        conn.commit()

        # Verify the update
        cursor.execute("SELECT * FROM personal_data WHERE id_user = ?", (user_data['id_user'],))
        updated_user = cursor.fetchone()
        print("Updated user data:", updated_user)

        return jsonify(success=True)
    except Exception as e:
        conn.rollback()
        print("Error during update:", e)
        return jsonify(success=False, error=str(e))
    finally:
        conn.close()



if __name__ == '__main__':
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    for table, field, path in zip(tables, fields, paths):
        get_additional_data(path, table, field, conn, cursor)

    app.run(debug=True)
