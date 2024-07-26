from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from extract_data import get_personal_data_by_name, get_personal_data_by_mail, get_personal_data_by_city, get_personal_data_by_idnp, get_personal_data_by_phone, get_personal_data_by_program, get_personal_data_by_instructionGroup, get_additional_data

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
    
if __name__ == '__main__':
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    for table, field, path in zip(tables, fields, paths):
        get_additional_data(path, table, field, conn, cursor)

    app.run(debug=True)
