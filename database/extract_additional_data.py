@app.route('/update', methods=['POST'])
def update(cursor):
    data = request.json
    
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