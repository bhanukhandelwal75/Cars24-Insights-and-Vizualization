import pandas as pd

df = pd.read_csv('cars24_delhi-ncr.csv')

# Display the first few rows of the DataFrame
print(df.head())

# Get a summary of the DataFrame
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Define a function to clean and convert the "KM Driven" column
def convert_km_to_int(km_str):
    km_str = km_str.replace(' km', '').replace(',', '')
    return int(km_str)

# Apply the function to the "KM Driven" column
df['KM driven'] = df['KM driven'].apply(convert_km_to_int)

# Remove the word "owner" from the "Owner Type" column
df['Owner Type'] = df['Owner Type'].str.replace(' owner', '', regex=False)

def convert_emi_to_int(emi_str):
    emi_str = emi_str.replace('₹', '').replace(',', '').replace('/month', '')
    return int(emi_str.strip())

# Apply the function to the "Monthly EMI" column
df['Monthly EMI'] = df['Monthly EMI'].apply(convert_emi_to_int)

# Define a function to clean and convert the "Car Price" column
def convert_price_to_int(price_str):
    if pd.isnull(price_str):  # Handle missing values
        return 0
    price_str = price_str.replace('₹', '').replace(' Lakh', '').replace(',', '')
    price_value = float(price_str.strip()) * 100000
    return int(price_value)

# Apply the function to the "Car Price" column
df['Car Price'] = df['Car Price'].apply(convert_price_to_int)

# Define a simple function to clean and convert the "Downpayment Amount" column
def convert_downpayment_to_int(dp_str):
    if pd.isnull(dp_str) or 'Zero' in dp_str or 'zero' in dp_str:  # Check for missing values or 'Zero' in the string
        return 0
    dp_str = dp_str.split()[0].replace('₹', '').replace(',', '')
    return int(dp_str)

# Apply the function to the "Downpayment Amount" column
df['Downpayment Amount'] = df['Downpayment Amount'].apply(convert_downpayment_to_int)

# Define a function to extract the city from the location and update the Location column
def clean_location(location):
    parts = location.split(', ')
    if len(parts) == 2:
        return parts[0]
    else:
        return location

# Apply the function to update the "Location" column and create a new "City" column
df['Location'] = df['Location'].apply(clean_location)

df['City'] = 'Delhi'

# Drop the original "Location" column if you no longer need it
df.drop(columns=['Car Variant'], inplace=True)

# Display the first few rows of the DataFrame
print(df.head())

# Get a summary of the DataFrame
print(df.info())

df.to_csv('cleaned_cars24_delhi-ncr.csv', index=False)