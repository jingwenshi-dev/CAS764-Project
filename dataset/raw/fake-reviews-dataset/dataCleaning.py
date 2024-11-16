import os
import pandas as pd

# Define the input and output file paths
input_file = './fake reviews dataset.csv'

# Read the input CSV file
df = pd.read_csv(input_file)

df.rename(columns={'label': 'class'}, inplace=True)
df.rename(columns={'text_': 'text'}, inplace=True)
df.rename(columns={'rating': 'polarity'}, inplace=True)
df.replace({'class': {'OR': 'truthful', 'CG': 'deceptive'}}, inplace=True)
df['polarity'] = df['polarity'].replace({1: 'negative', 2: 'negative', 3: 'negative', 4: 'positive', 5: 'positive'})

# Split the DataFrame into four based on the 'class' and 'polarity' column values
deceptive_negative_df = df[(df['class'] == 'deceptive') & (df['polarity'] == 'negative')]
deceptive_positive_df = df[(df['class'] == 'deceptive') & (df['polarity'] == 'positive')]
truthful_negative_df = df[(df['class'] == 'truthful') & (df['polarity'] == 'negative')]
truthful_positive_df = df[(df['class'] == 'truthful') & (df['polarity'] == 'positive')]

# Create the directory if it does not exist
output_dir = '../../clean/fake-reviews-dataset'
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
