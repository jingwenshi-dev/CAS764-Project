import os
import pandas as pd

# Read the Excel file
df = pd.read_excel('./multi-domain.xlsx')

df.columns = df.columns.str.lower()
df.replace({'class': {0: 'truthful', 1: 'deceptive'}}, inplace=True)

# Convert all values in the 'polarity' column to lowercase
df['polarity'] = df['polarity'].str.lower()

# Split the DataFrame into four based on the 'class' and 'polarity' column values
deceptive_negative_df = df[(df['class'] == 'deceptive') & (df['polarity'] == 'negative')]
deceptive_positive_df = df[(df['class'] == 'deceptive') & (df['polarity'] == 'positive')]
truthful_negative_df = df[(df['class'] == 'truthful') & (df['polarity'] == 'negative')]
truthful_positive_df = df[(df['class'] == 'truthful') & (df['polarity'] == 'positive')]

# Create the directory if it does not exist
output_dir = '../../clean/afrd-arabic-fake-reviews-detection'
os.makedirs(output_dir, exist_ok=True)

# Save each DataFrame into separate CSV files
deceptive_negative_file_path = f'{output_dir}/deceptive_negative.csv'
deceptive_positive_file_path = f'{output_dir}/deceptive_positive.csv'
truthful_negative_file_path = f'{output_dir}/truthful_negative.csv'
truthful_positive_file_path = f'{output_dir}/truthful_positive.csv'

deceptive_negative_df.to_csv(deceptive_negative_file_path, index=False)
deceptive_positive_df.to_csv(deceptive_positive_file_path, index=False)
truthful_negative_df.to_csv(truthful_negative_file_path, index=False)
truthful_positive_df.to_csv(truthful_positive_file_path, index=False)