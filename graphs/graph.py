import matplotlib.pyplot as plt

# Data for the charts
shots = ['Zero Shot', '20 Shots', '40 Shots']

# Polarity Positive
positive_accuracy = [61.60, 72.60, 71.60]
positive_precision = [76.00, 85.80, 77.80]
positive_recall = [37, 55, 61]

# Polarity Negative
negative_accuracy = [51.20, 51.40, 67.60]
negative_precision = [53.40, 24.20, 85.00]
negative_recall = [5, 13, 42]

# Create line charts
plt.figure(figsize=(10, 6))

# Positive Polarity
plt.subplot(2, 1, 1)
plt.plot(shots, positive_accuracy, marker='o', label='Accuracy', color='#ADD8E6')  # Light Blue
plt.plot(shots, positive_precision, marker='o', label='Precision', color='#0000FF')  # Blue
plt.plot(shots, positive_recall, marker='o', label='Recall', color='#00008B')  # Dark Blue
for i, txt in enumerate(positive_accuracy):
    plt.annotate(f'{txt}', (shots[i], positive_accuracy[i]))
for i, txt in enumerate(positive_precision):
    plt.annotate(f'{txt}', (shots[i], positive_precision[i]))
for i, txt in enumerate(positive_recall):
    plt.annotate(f'{txt}', (shots[i], positive_recall[i]))
plt.title('Polarity Positive Comparison')
plt.ylabel('Percentage')
plt.ylim(0, 100)
plt.legend()
plt.grid(True)

# Negative Polarity
plt.subplot(2, 1, 2)
plt.plot(shots, negative_accuracy, marker='o', label='Accuracy', color='#FFA07A')  # Light Red
plt.plot(shots, negative_precision, marker='o', label='Precision', color='#FF4500')  # Orange Red
plt.plot(shots, negative_recall, marker='o', label='Recall', color='#FF0000')  # Red
for i, txt in enumerate(negative_accuracy):
    plt.annotate(f'{txt}', (shots[i], negative_accuracy[i]))
for i, txt in enumerate(negative_precision):
    plt.annotate(f'{txt}', (shots[i], negative_precision[i]))
for i, txt in enumerate(negative_recall):
    plt.annotate(f'{txt}', (shots[i], negative_recall[i]))
plt.title('Polarity Negative Comparison')
plt.xlabel('Shots')
plt.ylabel('Percentage')
plt.ylim(0, 100)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()