import matplotlib.pyplot as plt
import pandas as pd
import math
data = {'Our Approach': {'min':97.38,"mean":97.38,"max":97.42}, 'Actual Approach': {"min":66.49, "mean":66.5, "max":66.79},}
df = pd.DataFrame(data)

ax=df.plot(kind='bar')
ax.set_xlabel("Metric")
ax.set_ylabel("Accuracy")
rects = ax.patches
labels = ["97.42%","97.38%","97.38%","66.75%","66.50%","66.49%"]
for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
            ha='center', va='bottom')
plt.show()
