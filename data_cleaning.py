import pandas as pd
import streamlit as st
import os

df = pd.read_csv("1- mental-illnesses-prevalence.xls", encoding="latin-1")

# print(df.head())

def extract(file_path):
    try:
        df = pd.read_csv(
            file_path,
            encoding="latin-1",
            on_bad_lines="skip"
        )
        print(f"Loaded {len(df)} rows and {len(df.columns)} columns")
        return df
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Extraction failed: {e}")
    
    return None

# df = extract("1- mental-illnesses-prevalence.xls")
# print(df.head())

def transform(df):
    try:
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_" )
        df = df.drop_duplicates()
        
        df = df.dropna()
        
        df = df.reset_index(drop=True)

        print("Data transformed successfully")
        return df

    except Exception as e:
        print(f"Transformation failed: {e}")
        return None

    
    
def load(df, output_path):
    try:
        if os.path.exists(output_path):
            print("File exists — updating it...")
        else:
            print("File does not exist — creating it...")

        df.to_csv(output_path, index=False)
        print(f"Data saved to {output_path}")

    except Exception as e:
        print(f"Loading failed: {e}")
    
def main():
    df = extract("1- mental-illnesses-prevalence.xls")

    if df is not None:
        df = transform(df)

        if df is not None:
            load(df, "cleaned_data.csv")


if __name__ == "__main__":
    main()