import matplotlib.pyplot as plt
import numpy as np

# Data
upazilas = ['Natore Sadar', 'Singra', 'Gurudaspur', 'Lalpur', 'Baraigram', 'Bagatipara']
areas = [401.29, 531, 199.40, 327.92, 299.6, 139.86]

# Colors
upazila_colors = {
    'Singra': '#55ff00',
    'Baraigram': '#ffff00',
    'Gurudaspur': '#ffaa00',
    'Lalpur': '#00c5ff',
    'Bagatipara': '#bfd999',
    'Natore Sadar': '#b53535'
}
colors = [upazila_colors[u] for u in upazilas]

# ==============================
# Pie Chart
# ==============================
plt.figure(figsize=(10,8))

# Pie with percentages inside
wedges, texts, autotexts = plt.pie(
    areas,
    labels=None,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    shadow=True,
    wedgeprops={'edgecolor':'black', 'linewidth':1.2},
    textprops={'fontsize':12, 'weight':'bold', 'color':'white'}
)

# Add legend inside the plot
legend_labels = [f"{upazilas[i]}: {areas[i]} sq.km" for i in range(len(upazilas))]
plt.legend(wedges, legend_labels, title="Upazilas & Area", loc='center', fontsize=11, title_fontsize=12, bbox_to_anchor=(0.5, -0.05), ncol=2)

# Title (moved slightly lower)
plt.title('Area Distribution of Natore Upazilas (sq.km)', fontsize=16, fontweight='bold', pad=10)

# Source & Copyright (italic, low opacity)
plt.figtext(0.01, -0.02, 'Source: Calculated from official sub-upazila area data', 
            horizontalalignment='left', fontsize=10, style='italic', alpha=0.6)
plt.figtext(0.99, -0.02, 'Prepared by Md. Khadem ali', 
            horizontalalignment='right', fontsize=10, style='italic', alpha=0.6)

plt.tight_layout()
plt.show()