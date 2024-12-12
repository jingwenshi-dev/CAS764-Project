import numpy as np
import matplotlib.pyplot as plt

# Data
metrics = ['Accuracy', 'Precision', 'Recall']
zero_shot = [51.60, 51.60, 53.75]
twenty_shots = [53.60, 52.60, 57.00]
forty_shots = [64.80, 68.25, 57.00]

# Plot
x = np.arange(len(metrics))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots(figsize=(10, 6))  # Adjust figure size
bars1 = ax.bar(x - width, zero_shot, width, label='Zero Shot', color='#cbe4f4')
bars2 = ax.bar(x, twenty_shots, width, label='20 Shots', color='#6794b6')
bars3 = ax.bar(x + width, forty_shots, width, label='40 Shots', color='#2d5468')

# Add labels, title, and custom x-axis tick labels
ax.set_ylabel('Percentage (%)', fontsize=14)
ax.set_title('Baseline Performance Metrics by Shot Count', fontsize=16)
ax.set_xticks(x)
ax.set_xticklabels(metrics, fontsize=12)
ax.legend(fontsize=12)

# Set y-axis limits
ax.set_ylim(0, 100)

# Add grid lines
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Show percentage values above bars
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}%',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 5),  # 5 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10)

# Tight layout and display the plot
plt.tight_layout()
plt.savefig('../Paper/diagrams/baseline.png')
plt.show()