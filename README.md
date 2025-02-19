
# Data Validation and Standardization in Supply Chain Management

## Project Overview
This project aims to validate and standardize supplier data in supply chain management. The application identifies errors such as:
- Invalid or missing product codes
- Missing supplier names and prices
- Incorrect date formats (e.g., DD-MM-YYYY or MM/DD/YYYY)
- Delivery dates that precede order dates

The app is built using **Streamlit** for the frontend and **Pandas** for data processing.

---

## Project Structure

```bash
supply_chain_validation/
│
├── app.py                      # Main Streamlit app
├── data_validation.py          # Data validation and standardization logic
├── supplier_data.csv           # Sample input CSV
└── requirements.txt            # Python dependencies
```

---

## How It Works
1. The user uploads a CSV file containing supplier data.
2. The app validates the data for:
   - Missing supplier names and prices
   - Invalid product codes
   - Date inconsistencies (Order Date and Delivery Date)
3. Incorrect dates are standardized to `YYYY-MM-DD` format.
4. Product codes are standardized to `PROD-XXXX` format.
5. Errors are visualized through a bar chart.
6. The user can download the corrected CSV.

---

## Sample CSV (supplier_data.csv)
```csv
SupplierID,ProductCode,SupplierName,Price,OrderDate,DeliveryDate
101,abc123,Supplier A,100,01-01-2024,05-01-2024
102,12345,Supplier B,200,02/01/2024,30-12-2023
103,P6789,Supplier C,,2024-01-03,
104,XYZ987,Supplier D,150,2024-01-04,10/01/2024
105,abcd,Supplier E,250,INVALID,15-01-2024
```

---

## Installation
### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/supply-chain-validation.git
cd supply-chain-validation
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
streamlit run app.py
```

---

## How to Use the App
1. Open the app by running the command above.
2. Upload a CSV file (sample provided in the repository).
3. Review the raw data and identified errors.
4. Visualize the errors with the bar chart.
5. Download the standardized CSV.

---

## Requirements
```
streamlit
pandas
matplotlib
seaborn
```

---

## Output Example
```csv
SupplierID,ProductCode,SupplierName,Price,OrderDate,DeliveryDate
101,PROD-0123,Supplier A,100,2024-01-01,2024-01-05
102,PROD-1234,Supplier B,200,2024-01-02,2023-12-30
103,PROD-6789,Supplier C,,2024-01-03,0000-00-00
104,PROD-0987,Supplier D,150,2024-01-04,2024-01-10
105,PROD-0000,Supplier E,250,0000-00-00,2024-01-15
```

---

## Error Visualization (Example)
```
Invalid Product Code           | ███████        3
Delivery Before Order Date     | ███            1
Invalid Date Format            | ██             1
Missing Order Date             | █              1
```

---

## Next Steps
- **Highlight Errors**: Display errors directly in the uploaded table.
- **Custom Rules**: Allow for customizable validation rules (e.g., maximum delivery delay).
- **Date Correction UI**: Enable date correction via Streamlit widgets.

---



