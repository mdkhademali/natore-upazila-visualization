import matplotlib.pyplot as plt

# Upazila data
upazilas = ['Natore Sadar', 'Singra', 'Gurudaspur', 'Lalpur', 'Baraigram', 'Bagatipara']
latitudes = [24.4167, 24.5, 24.3681, 24.185, 24.3075, 24.35]
longitudes = [88.9256, 89.1333, 89.2475, 88.9708, 89.1667, 88.9333]
upazila_colors = ['#b53535', '#55ff00', '#ffaa00', '#00c5ff', '#ffff00', '#bfd999']

plt.figure(figsize=(12,8))

# Scatter plot
plt.scatter(longitudes, latitudes, s=200, c=upazila_colors, edgecolors='black', alpha=0.9)

# Offset for annotations to avoid overlap with the dot
x_offset = 0.008  # horizontal offset
y_offsets = [0, 0, -0.003, -0.003, 0, -0.003]  # vertical adjustments per point

# Annotate each point
for i, name in enumerate(upazilas):
    plt.text(longitudes[i]+x_offset, latitudes[i]+y_offsets[i],
             f"{name}\n({latitudes[i]}, {longitudes[i]})",
             fontsize=11, weight='bold', va='center', ha='left',
             bbox=dict(facecolor='white', alpha=0.6, edgecolor='gray'))

# Title & labels
plt.title('Approximate Locations of Natore Upazilas', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Longitude', fontsize=12)
plt.ylabel('Latitude', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)

# Source & Prepared by
plt.figtext(0.01, -0.02, 'Source: Calculated from official sub-upazila coordinates', 
            horizontalalignment='left', fontsize=10, style='italic', alpha=0.6)
plt.figtext(0.99, -0.02, 'Prepared by Md. Khadem Ali', 
            horizontalalignment='right', fontsize=10, style='italic', alpha=0.6)

plt.tight_layout()
plt.show()