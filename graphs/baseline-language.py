import matplotlib.pyplot as plt

# Data for line chart
shots = ['Zero Shot', '20 Shots', '40 Shots']

# Polarity Positive
positive_accuracy = [61.60, 72.60, 71.60]
positive_precision = [76.00, 85.80, 77.80]
positive_recall = [37.00, 55.00, 61.00]

# Polarity Negative
negative_accuracy = [51.20, 51.40, 67.60]
negative_precision = [53.40, 24.20, 85.00]
negative_recall = [5.00, 13.00, 42.00]

# Function to add data labels
def add_labels(x, y):
    for i in range(len(x)):
        plt.annotate(f'{y[i]}', (x[i], y[i]), textcoords="offset points", xytext=(0,5), ha='center')

# Set common y-axis limits
y_min = 0
y_max = 100

# Plot for Polarity Positive
plt.figure(figsize=(10, 6))
plt.plot(shots, positive_accuracy, marker='o', label='Accuracy', color='#ffaf00')
plt.plot(shots, positive_precision, marker='o', label='Precision', color='#f46920')
plt.plot(shots, positive_recall, marker='o', label='Recall', color='#f53255')

# Add labels
add_labels(shots, positive_accuracy)
add_labels(shots, positive_precision)
add_labels(shots, positive_recall)

plt.title('Polarity Positive Metrics by Shot Count')
plt.xlabel('Shot Count')
plt.ylabel('Percentage (%)')
plt.ylim(y_min, y_max)
plt.legend()
plt.grid(True, linestyle='dotted')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('../Paper/diagrams/polarity_positive_metrics.png')
plt.show()

# Plot for Polarity Negative
plt.figure(figsize=(10, 6))
plt.plot(shots, negative_accuracy, marker='o', label='Accuracy', color='#ffaf00')
plt.plot(shots, negative_precision, marker='o', label='Precision', color='#f46920')
plt.plot(shots, negative_recall, marker='o', label='Recall', color='#f53255')

# Add labels
add_labels(shots, negative_accuracy)
add_labels(shots, negative_precision)
add_labels(shots, negative_recall)

plt.title('Polarity Negative Metrics by Shot Count')
plt.xlabel('Shot Count')
plt.ylabel('Percentage (%)')
plt.ylim(y_min, y_max)
plt.legend()
plt.grid(True, linestyle='dotted')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('../Paper/diagrams/polarity_negative_metrics.png')
plt.show()