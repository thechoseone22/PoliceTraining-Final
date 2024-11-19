from pathlib import Path
import pandas as pd

# directory of files
directory = Path(r"C:\Users\jasmi\Projects\Final Project")

# find all .csv
csv_files = [file for file in directory.iterdir() if file.suffix == ".csv"]

# combine all .csv 
dataframes = [pd.read_csv(file) for file in csv_files]
combined_df = pd.concat(dataframes, ignore_index=True)

# save 
output_path = directory / "combined_dataset.csv"
combined_df.to_csv(output_path, index=False)

print("success")
