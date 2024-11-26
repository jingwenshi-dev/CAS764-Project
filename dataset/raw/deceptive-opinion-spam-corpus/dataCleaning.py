import csv
import os
import pandas as pd

# Define the input and output file paths
input_file = './deceptive-opinion.csv'
output_dir = '../../clean/deceptive-opinion-spam-corpus'

df = pd.read_csv(input_file)
df.rename(columns={'deceptive': 'class'}, inplace=True)

# Reset index to keep the original index as a column
df.reset_index(inplace=True, drop=False)

# Split the DataFrame into four based on the 'class' column values
deceptive_negative_df = df[(df['class'] == 'deceptive') & (df['polarity'] == 'negative')]
deceptive_positive_df = df[(df['class'] == 'deceptive') & (df['polarity'] == 'positive')]
truthful_negative_df = df[(df['class'] == 'truthful') & (df['polarity'] == 'negative')]
truthful_positive_df = df[(df['class'] == 'truthful') & (df['polarity'] == 'positive')]

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