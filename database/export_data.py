import pandas as pd

def export_to_excel(query_result, output_path):
    # Extract user data
    user_data = query_result['user_data']
    application_dates = query_result['application_dates']
    instruction_groups = query_result['instruction_groups']
    notices = query_result['notices']

    # Create DataFrames
    user_df = pd.DataFrame([user_data])
    application_dates_df = pd.DataFrame(application_dates, columns=["Application Dates"])
    instruction_groups_df = pd.DataFrame(instruction_groups, columns=["Instruction Groups"])
    notices_df = pd.DataFrame(notices, columns=["Phone Calls", "Email Calls", "SMS Calls", "Viber Calls", "Response"])

    # Create a Pandas Excel writer using openpyxl as the engine
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        user_df.to_excel(writer, sheet_name='User Data', index=False)
        application_dates_df.to_excel(writer, sheet_name='Application Dates', index=False)
        instruction_groups_df.to_excel(writer, sheet_name='Instruction Groups', index=False)
        notices_df.to_excel(writer, sheet_name='Notices', index=False)

# Example usage
query_result = {
    'user_data': {
        'username': 'Ana Maria',
        'idnp': '1535657895985',
        'bday': '01/03/1995',
        'age': 28,
        'phone_number': '37312345678',
        'email': 'anamaria@gmail.com',
        'location': 'or. Ialoveni',
        'program': 'Ecologizare IMM',
        'operator': 'O.Constantinova',
        'confirmation_date': '01/03/2023',
        'comment': 'așteaptă instruire',
        'status': 'lista de așteptare',
        'certificate': 'PEA/SB/632 din 13.10.2023',
        'finance': 'PARE 23/II-100 DIN 13.06.2023',
        'final_status': 'Necunoscut',
        'exclusion': 1
    },
    'application_dates': ['18/07/2023', '18/09/2024'],
    'instruction_groups': ['GR 2 - 0 ZILE', 'GR 8 - 0 ZILE', 'GR 13 - 0 ZILE'],
    'notices': [
        ('01/03/1995', None, None, None, 'Confirm'),
        (None, '01/04/1995', None, None, 'Confirm'),
        (None, None, '01/05/1995', '01/06/1995', 'Confirm')
    ]
}

output_path = 'query_result.xlsx'
export_to_excel(query_result, output_path)
print(f"Data exported to {output_path}")
