# Path to your local file
file_path = "./results/language-reverse/statistics"

# Read the file
with open(file_path, 'r') as file:
    file_content = file.readlines()

# Initialize metrics for all shot types
all_metrics = {
    "0-shot": {"Accuracy": [], "Precision": [], "Recall": []},
    "20-shot": {"Accuracy": [], "Precision": [], "Recall": []},
    "40-shot": {"Accuracy": [], "Precision": [], "Recall": []},
}

# Process the data for each shot type in each run
for i in range(5):
    start_index = i * 10
    # 0-shot
    all_metrics["0-shot"]["Accuracy"].append(float(file_content[start_index].split(":")[1].strip()))
    all_metrics["0-shot"]["Precision"].append(float(file_content[start_index + 1].split(":")[1].strip()))
    all_metrics["0-shot"]["Recall"].append(float(file_content[start_index + 2].split(":")[1].strip()))
    # 20-shot
    all_metrics["20-shot"]["Accuracy"].append(float(file_content[start_index + 3].split(":")[1].strip()))
    all_metrics["20-shot"]["Precision"].append(float(file_content[start_index + 4].split(":")[1].strip()))
    all_metrics["20-shot"]["Recall"].append(float(file_content[start_index + 5].split(":")[1].strip()))
    # 40-shot
    all_metrics["40-shot"]["Accuracy"].append(float(file_content[start_index + 6].split(":")[1].strip()))
    all_metrics["40-shot"]["Precision"].append(float(file_content[start_index + 7].split(":")[1].strip()))
    all_metrics["40-shot"]["Recall"].append(float(file_content[start_index + 8].split(":")[1].strip()))

# Calculate averages for each metric and each shot type
averages_all_shots = {
    shot: {metric: (sum(values) / len(values)) * 100 for metric, values in metrics.items()}
    for shot, metrics in all_metrics.items()
}

print(averages_all_shots)