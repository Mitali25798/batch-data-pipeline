import pandas as pd
import os

RAW_PATH = '/app/data/raw/'
INTERMEDIATE_PATH = '/app/data/intermediate/'

def ingest_excel_to_csv():
    print("Ingestion started...")
    for file in os.listdir(RAW_PATH):
        if file.endswith('.xlsx'):
            df = pd.read_excel(os.path.join(RAW_PATH, file))
            filename = file.replace('.xlsx', '.csv')
            output_path = os.path.join(INTERMEDIATE_PATH, 'clean_' + filename)
            df.to_csv(output_path, index=False)
            print(f"Converted {file} → {output_path}")
    print("Ingestion complete.")

if __name__ == "__main__":
    ingest_excel_to_csv()
