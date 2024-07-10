# import pandas as pd
# import json

# # Load the Excel file and skip the first two rows
# file_path = './excel/testdata.xlsx'
# df = pd.read_excel(file_path, skiprows=2)

# # Rename the columns to match the actual header row
# df.columns = ['ID', 'Name', 'Application Date', 'Repeated Application Date 1', 'Repeated Application Date 2', 
#               'IDNP', 'Birth Date', 'Age', 'Locality', 'Phone', 'Email', 'Program Applied', 'Caller', 
#               'Confirmation Date', 'Discussion Comment', 'Discussion Status', 'Phone Call 1', 'Email 1', 
#               'SMS 1', 'Viber 1', 'Response 1', 'Training Group Invited', 'Phone Call 2', 'Email 2', 
#               'SMS 2', 'Viber 2', 'Response 2', 'Phone Call 3', 'Email 3', 'SMS 3', 'Viber 3', 'Response 3', 
#               'Actual Training Group', 'Certificate', 'Funding Application', 'Evaluation Status', 'Database Exclusion']

# # Drop any columns or rows with all NaN values if necessary
# df.dropna(how='all', axis=1, inplace=True)
# df.dropna(how='all', axis=0, inplace=True)

# # Convert datetime columns to string
# datetime_columns = df.select_dtypes(include=['datetime']).columns
# for col in datetime_columns:
#     df[col] = df[col].astype(str)

# # Group the DataFrame by 'Program Applied'
# grouped_data = df.groupby('Program Applied').apply(lambda x: x.to_dict(orient='records')).to_dict()

# # Convert the grouped data to a JSON string with indentation
# json_data = json.dumps(grouped_data, indent=4, ensure_ascii=False)

# # Save the JSON data to a file
# json_file_path = './excel/testdata.xlsx'
# with open(json_file_path, 'w', encoding='utf-8') as json_file:
#     json_file.write(json_data)
    
# print("JSON file has been created:", json_file_path)

import pandas as pd
import json
from datetime import datetime

# Load the Excel file and skip the first two rows
file_path = './excel/testdata.xlsx'
df = pd.read_excel(file_path, skiprows=2)

# Rename the columns to match the actual header row
df.columns = ['ID', 'Name', 'Application Date', 'Repeated Application Date 1', 'Repeated Application Date 2', 
              'IDNP', 'Birth Date', 'Age', 'Locality', 'Phone', 'Email', 'Program Applied', 'Caller', 
              'Confirmation Date', 'Discussion Comment', 'Discussion Status', 'Phone Call 1', 'Email 1', 
              'SMS 1', 'Viber 1', 'Response 1', 'Training Group Invited', 'Phone Call 2', 'Email 2', 
              'SMS 2', 'Viber 2', 'Response 2', 'Phone Call 3', 'Email 3', 'SMS 3', 'Viber 3', 'Response 3', 
              'Actual Training Group', 'Certificate', 'Funding Application', 'Evaluation Status', 'Database Exclusion']

# Drop any columns or rows with all NaN values if necessary
df.dropna(how='all', axis=1, inplace=True)
df.dropna(how='all', axis=0, inplace=True)

# Convert datetime objects to strings
def convert_datetime(value):
    if isinstance(value, datetime):
        return value.isoformat()
    return value

df = df.applymap(convert_datetime)

# Group the DataFrame by 'Program Applied'
grouped_data = df.groupby('Program Applied').apply(lambda x: x.to_dict(orient='records')).to_dict()

# Convert the grouped data to a JSON string with indentation
json_data = json.dumps(grouped_data, indent=4, ensure_ascii=False)

# Save the JSON data to a file
json_file_path = './json/Registrul_aplicatiilor_grouped.json'
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)

print("JSON file has been created:", json_file_path)
