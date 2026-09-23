import numpy as np
import matplotlib.pyplot as plt

salaries = np.array([45000,52000,120000,48000,55000])

sal_mean = salaries.mean()
sal_std = salaries.std()

scaled_salaries = (salaries - sal_mean) / sal_std

print("Standardized Salaries")
print(scaled_salaries)

fig, (ax1,ax2) = plt.subplots(1,2, figsize =(10,4))

ax1.plot(salaries, marker='o', color="red", linestyle = 'dashed')
ax1.set_title("Raw Salaries (Notice the massive spike)")
ax1.set_ylabel("Salaries in Rupees")

ax2.plot(scaled_salaries, marker ='o',color='green', linestyle = 'dashed')
ax2.set_title("Standardized Salaries (Z-Scores)")
ax2.set_ylabel("Standard Deviations")
ax2.axhline(0, color ='black', linewidth=1)

plt.tight_layout()
plt.show()



import pandas as pd
import os
import logging

# Configure terminal logs instead of basic print statements
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FinTechDataLoader:
    """
    Module 1: Data Acquisition Engine. 
    Ingests raw Hinglish banking reviews and enforces strict schema validation.
    """
    
    def __init__(self, file_path: str):
        self.file_path = file_path
        # The expected column names in your raw Google Play Store dataset
        self.text_col = "content"
        self.target_col = "score"

    def load_and_validate(self) -> pd.DataFrame:
        """Loads the CSV and prevents Ghost NaNs from crashing the pipeline."""
        
        # Guard Clause 1: Does the file actually exist?
        if not os.path.exists(self.file_path):
            logging.error(f"Dataset missing. Please ensure data exists at: {self.file_path}")
            raise FileNotFoundError(f"File not found: {self.file_path}")
            
        logging.info("Initializing Pandas ingestion engine...")
        df = pd.read_csv(self.file_path)
        
        # Guard Clause 2: Schema Validation
        if self.text_col not in df.columns or self.target_col not in df.columns:
            logging.error(f"Schema mismatch. Expected columns: '{self.text_col}' and '{self.target_col}'")
            raise KeyError("Critical columns missing from the dataset.")

        initial_rows = len(df)
        
        # Drop rows where the actual review text is entirely missing
        df = df.dropna(subset=[self.text_col, self.target_col])
        
        # Force the text column to be a strict String datatype (eliminates Ghost NaNs)
        df[self.text_col] = df[self.text_col].astype(str)
        
        dropped_rows = initial_rows - len(df)
        logging.info(f"Ingestion Complete: {len(df)} rows loaded. ({dropped_rows} empty records dropped).")
        
        return df

# Local execution test
if __name__ == "__main__":
    # Point this to where your scraped CSV is saved
    dataset_path = os.path.join(os.path.dirname(__file__), "..", "data", "raw", "bank_reviews.csv")
    
    loader = FinTechDataLoader(dataset_path)
    try:
        raw_dataframe = loader.load_and_validate()
        print(raw_dataframe.head())
    except Exception as e:
        print(f"Pipeline Halted: {e}")