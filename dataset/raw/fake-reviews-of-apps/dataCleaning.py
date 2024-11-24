import os
import pandas as pd

# Read the Excel file
df = pd.read_excel('./apps_fake_genuine_data.xlsx')

# Rename the label column to 'deceptive'
df.rename(columns={'label': 'class'}, inplace=True)
df.rename(columns={'review': 'text'}, inplace=True)

# Replace values in the 'deceptive' column
df.replace({'class': {'genuine': 'truthful', 'fake': 'deceptive'}}, inplace=True)

# Reset index to keep the original index as a column
df.reset_index(inplace=True, drop=False)

# Split the DataFrame into two based on the 'deceptive' column values
truthful_df = df[df['class'] == 'truthful']
deceptive_df = df[df['class'] == 'deceptive']

# Create the directory if it does not exist
output_dir = '../../clean/fake-reviews-of-apps'
os.makedirs(output_dir, exist_ok=True)

# Save each DataFrame into separate CSV files
truthful_file_path = f'{output_dir}/truthful.csv'
deceptive_file_path = f'{output_dir}/deceptive.csv'

truthful_df.to_csv(truthful_file_path, index=False)
deceptive_df.to_csv(deceptive_file_path, index=False)