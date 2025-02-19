import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
from data_validation import validate_data, standardize_product_codes

st.title("Supply Chain Data Validation & Standardization")

uploaded_file = st.file_uploader("Upload Supplier CSV", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Raw Data")
    st.dataframe(df)

    # Validate Data
    errors = validate_data(df)
    st.write("### Validation Errors")
    st.write(errors)

    # Visualization
    st.write("### Error Visualization")
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 5))
    
    error_names = list(errors.keys())
    error_counts = list(errors.values())
    
    ax = sns.barplot(x=error_names, y=error_counts, palette="muted")
    ax.set_ylabel("Number of Errors")
    ax.set_xlabel("Error Type")
    
    for i, count in enumerate(error_counts):
        plt.text(i, count + 0.1, str(count), ha='center', va='bottom')
    
    st.pyplot(plt)

    # Standardize Product Codes
    cleaned_df = standardize_product_codes(df)
    st.write("### Standardized Data")
    st.dataframe(cleaned_df)
    
    # Download Cleaned Data
    output = BytesIO()
    cleaned_df.to_csv(output, index=False)
    output.seek(0)
    
    st.download_button(
        label="Download Cleaned Data",
        data=output,
        file_name="standardized_supplier_data.csv",
        mime="text/csv"
    )
