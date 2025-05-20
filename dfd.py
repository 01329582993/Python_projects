import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis with transparent background
fig, ax = plt.subplots(figsize=(10, 6), facecolor='none')
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')

# Draw external entities
ax.add_patch(patches.Rectangle((0.5, 5.5), 2, 1, edgecolor='black', facecolor='lightblue'))
ax.text(1.5, 6, 'Student', ha='center', va='center')

ax.add_patch(patches.Rectangle((0.5, 1), 2, 1, edgecolor='black', facecolor='lightblue'))
ax.text(1.5, 1.5, 'Admin', ha='center', va='center')

# Draw process
ax.add_patch(patches.Circle((5, 3.5), 1, edgecolor='black', facecolor='lightgreen'))
ax.text(5, 3.5, 'Visualize\nAlgorithm', ha='center', va='center')

# Draw data store
ax.add_patch(patches.Rectangle((8, 2.5), 1.5, 2, edgecolor='black', facecolor='wheat'))
ax.text(8.75, 3.5, 'Data Store', ha='center', va='center')

# Arrows and labels
ax.annotate('', xy=(3.5, 6), xytext=(4, 4.5), arrowprops=dict(arrowstyle='->'))
ax.text(4, 5.2, 'Algorithm Selection\n+ Input Data', ha='center')

ax.annotate('', xy=(4, 2.5), xytext=(3.5, 1.5), arrowprops=dict(arrowstyle='->'))
ax.text(4, 2, 'Upload\nAlgorithms', ha='center')

ax.annotate('', xy=(6, 3.5), xytext=(7.9, 3.5), arrowprops=dict(arrowstyle='->'))
ax.text(7, 3.8, 'Store\nResults', ha='center')

ax.annotate('', xy=(7.9, 3), xytext=(6, 3), arrowprops=dict(arrowstyle='->'))
ax.text(7, 2.7, 'Retrieve\nData', ha='center')

ax.annotate('', xy=(4, 3.5), xytext=(2.6, 6), arrowprops=dict(arrowstyle='->'))
ax.text(3.2, 5.5, 'Animations +\nFeedback', ha='center')

plt.title('Context-Level DFD for Visual Algo', fontsize=14)
plt.tight_layout()
plt.show()
