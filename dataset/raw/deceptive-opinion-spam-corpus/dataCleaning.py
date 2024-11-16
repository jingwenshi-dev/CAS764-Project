import csv
import os

# Define the input and output file paths
input_file = './deceptive-opinion.csv'
output_dir = '../../clean/deceptive-opinion-spam-corpus'
output_files = {
    'deceptive_positive.csv': [],
    'deceptive_negative.csv': [],
    'truthful_positive.csv': [],
    'truthful_negative.csv': []
}

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Read the input CSV file
with open(input_file, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Read the header row
    header.remove('source')  # Remove the 'source' column from the header

    # Process each row in the CSV file
    for row in reader:
        label, hotel, polarity, source, review = row
        row_without_source = [label, hotel, polarity, review]  # Exclude the 'source' column
        if label == 'deceptive':
            if polarity == 'positive':
                output_files['deceptive_positive.csv'].append(row_without_source)
            elif polarity == 'negative':
                output_files['deceptive_negative.csv'].append(row_without_source)
        elif label == 'truthful':
            if polarity == 'positive':
                output_files['truthful_positive.csv'].append(row_without_source)
            elif polarity == 'negative':
                output_files['truthful_negative.csv'].append(row_without_source)

# Write the output files
for output_file, rows in output_files.items():
    with open(os.path.join(output_dir, output_file), 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)  # Write the header row
        writer.writerows(rows)  # Write the data rows