import matplotlib.pyplot as plt

# Data for line chart
shots = ['Zero Shot', '20 Shots', '40 Shots']

# Eng-Arb metrics
eng_arb_accuracy = [52.00, 55.00, 56.80]
eng_arb_precision = [22.80, 50.20, 59.00]
eng_arb_recall = [16.00, 39.00, 47.00]

# Arb-Eng metrics
arb_eng_accuracy = [51.80, 50.00, 52.20]
arb_eng_precision = [51.80, 50.00, 51.80]
arb_eng_recall = [52.00, 50.00, 54.00]


# Function to add data labels
def add_labels(x, y):
    for i in range(len(x)):
        plt.annotate(f'{y[i]:.1f}%', (x[i], y[i]), textcoords="offset points", xytext=(0, 5), ha='center')


# Set common y-axis limits
y_min = 0
y_max = 100

# Plot for Eng-Arb metrics
plt.figure(figsize=(10, 6))
plt.plot(shots, eng_arb_accuracy, marker='o', label='Accuracy', color='#cbe4f4')
plt.plot(shots, eng_arb_precision, marker='o', label='Precision', color='#6794b6')
plt.plot(shots, eng_arb_recall, marker='o', label='Recall', color='#2d5468')

# Add labels
add_labels(shots, eng_arb_accuracy)
add_labels(shots, eng_arb_precision)
add_labels(shots, eng_arb_recall)

plt.title('English to Arabic Metrics by Shot Count')
plt.xlabel('Shot Count')
plt.ylabel('Percentage (%)')
plt.ylim(y_min, y_max)
plt.legend()
plt.grid(True, linestyle='dotted')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('../Paper/diagrams/eng_arb_metrics.png')
plt.show()

# Plot for Arb-Eng metrics
plt.figure(figsize=(10, 6))
plt.plot(shots, arb_eng_accuracy, marker='o', label='Accuracy', color='#ffaf00')
plt.plot(shots, arb_eng_precision, marker='o', label='Precision', color='#f46920')
plt.plot(shots, arb_eng_recall, marker='o', label='Recall', color='#f53255')

# Add labels
add_labels(shots, arb_eng_accuracy)
add_labels(shots, arb_eng_precision)
add_labels(shots, arb_eng_recall)

plt.title('Arabic to English Metrics by Shot Count')
plt.xlabel('Shot Count')
plt.ylabel('Percentage (%)')
plt.ylim(y_min, y_max)
plt.legend()
plt.grid(True, linestyle='dotted')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('../Paper/diagrams/arb_eng_metrics.png')
plt.show()
