import pandas as pd

# Load the scraped data from CSV file
data = pd.read_csv(r'C:\Users\HP\week 7\building_data_warehouse\data\scraped_data.csv')

# Data Cleaning
# Remove duplicates
data.drop_duplicates(inplace=True)

# Handle missing values (for simplicity, we'll fill missing values with an empty string)
data.fillna('', inplace=True)

# Standardize formats (for simplicity, we'll convert all text to lowercase)
data['Message'] = data['Message'].str.lower()

# Data Validation (for simplicity, we'll just ensure that 'ID' is unique)
assert data['ID'].is_unique, "ID column contains duplicate values!"

# Save the cleaned data to a new CSV file
cleaned_data_path = 'data/cleaned_scraped_data.csv'
data.to_csv(cleaned_data_path, index=False)

print(f"Data cleaning completed. Cleaned data saved to {cleaned_data_path}.")
