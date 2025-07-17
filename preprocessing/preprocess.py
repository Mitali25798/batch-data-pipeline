import pandas as pd
import os

INTERMEDIATE_PATH = '/app/data/intermediate/'

def preprocess_data():
    print("Preprocessing started...")
    for file in os.listdir(INTERMEDIATE_PATH):
        if file.startswith('clean_') and file.endswith('.csv'):
            df = pd.read_csv(os.path.join(INTERMEDIATE_PATH, file))

            # Drop NaNs
            df.dropna(inplace=True)

            # Parse date and cast values
            df['Date'] = pd.to_datetime(df['Date'])
            df['Value'] = df['Value'].astype(float)
            df['Transaction_count'] = df['Transaction_count'].astype(int)

            output_path = os.path.join(INTERMEDIATE_PATH, 'preprocessed_' + file)
            df.to_csv(output_path, index=False)
            print(f"Preprocessed: {file}")
    print("Preprocessing complete.")

if __name__ == "__main__":
    preprocess_data()
