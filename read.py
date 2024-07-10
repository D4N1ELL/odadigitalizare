import pandas as pd

# Load the Excel file
file_path = './excel/testdata.xlsx'
excel_data = pd.read_excel(file_path)

# Display the first few rows of the dataframe to understand its structure
print(excel_data.head())


