import pandas as pd
import re
from datetime import datetime

# Validate and Standardize Dates
def validate_data(df):
    errors = {
        "Missing Supplier Name": 0,
        "Missing Price": 0,
        "Invalid Product Code": 0,
        "Missing Order Date": 0,
        "Delivery Before Order Date": 0,
        "Invalid Date Format": 0
    }
    
    # Check for missing supplier names and prices
    errors["Missing Supplier Name"] = df['SupplierName'].isnull().sum()
    errors["Missing Price"] = df['Price'].isnull().sum()
    
    # Validate Product Code Format
    pattern = re.compile(r'^PROD-\d{4}$')
    for code in df['ProductCode']:
        if not pattern.match(str(code)):
            errors["Invalid Product Code"] += 1
    
    # Validate and Standardize Dates
    for index, row in df.iterrows():
        try:
            if pd.isnull(row['OrderDate']):
                errors["Missing Order Date"] += 1
            else:
                df.at[index, 'OrderDate'] = standardize_date(row['OrderDate'])
                
            if pd.notnull(row['DeliveryDate']):
                df.at[index, 'DeliveryDate'] = standardize_date(row['DeliveryDate'])
                
                order_date = pd.to_datetime(df.at[index, 'OrderDate'])
                delivery_date = pd.to_datetime(df.at[index, 'DeliveryDate'])
                
                if delivery_date < order_date:
                    errors["Delivery Before Order Date"] += 1
        
        except Exception:
            errors["Invalid Date Format"] += 1
    
    return errors

# Date Standardization Function
def standardize_date(date_str):
    formats = ['%d-%m-%Y', '%m/%d/%Y', '%Y-%m-%d']
    
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).strftime('%Y-%m-%d')
        except (ValueError, TypeError):
            continue
    # Return default if invalid
    return '0000-00-00'

# Standardize Product Codes
def standardize_product_codes(df):
    standardized_codes = []
    
    for code in df['ProductCode']:
        digits = re.findall(r'\d+', str(code))
        if digits:
            standardized_code = f"PROD-{digits[0].zfill(4)}"
        else:
            standardized_code = "PROD-0000"
        standardized_codes.append(standardized_code)
    
    df['ProductCode'] = standardized_codes
    return df
