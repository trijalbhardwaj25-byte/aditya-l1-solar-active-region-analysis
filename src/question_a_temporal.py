import os
import sunpy.map
import numpy as np
import matplotlib.pyplot as plt

from skimage.measure import label
from skimage.measure import regionprops
from skimage.morphology import remove_small_objects

folder = "DATA/temporal_evolution"

dates = []
areas = []

for filename in sorted(os.listdir(folder)):

    if not filename.endswith(".fits"):
        continue

    file_path = os.path.join(folder, filename)

    print(f"Processing: {filename}")

    smap = sunpy.map.Map(file_path)

    data = smap.data.astype(float)

    normalized = (
        data - np.min(data)
    ) / (
        np.max(data) - np.min(data)
    )

    # Fixed Threshold Segmentation
    mask = normalized > 0.7

    mask = remove_small_objects(mask, 100)

    labels = label(mask)

    regions = regionprops(labels)

    if len(regions) == 0:
        area = 0
    else:
        largest_region = max(
            regions,
            key=lambda r: r.area
        )
        area = largest_region.area

    date = filename.split("_Lev1.0_")[1][:10]

    dates.append(date)
    areas.append(area)

    print(f"Date: {date} Area: {area}")

print("\nDates:")
print(dates)

print("\nAreas:")
print(areas)

# Plot
plt.figure(figsize=(8, 5))

plt.plot(
    dates,
    areas,
    marker="o",
    linewidth=2
)

plt.title("Active Region Area vs Time")

plt.xlabel("Date")

plt.ylabel("Largest Active Region Area (pixels)")

plt.xticks(rotation=45)

plt.grid(True)

plt.tight_layout()

# SAVE GRAPH
plt.savefig(
    "part 2/question_a/figures/area_vs_time.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nGraph saved successfully.")
# ==========================
# TEMPORAL EVOLUTION METRICS
# ==========================

valid_areas = [a for a in areas if a > 0]

print("\n===== STATISTICS =====")

print("Maximum Area :", max(valid_areas))

print("Minimum Area :", min(valid_areas))

print("Average Area :", round(sum(valid_areas)/len(valid_areas), 2))

print("\n===== GROWTH / DECAY =====")

for i in range(1, len(areas)):

    previous = areas[i-1]
    current = areas[i]

    if previous == 0:
        print(
            f"{dates[i-1]} → {dates[i]} : Cannot compute (previous area = 0)"
        )
        continue

    change = ((current - previous) / previous) * 100

    print(
        f"{dates[i-1]} → {dates[i]} : {change:.2f}%"
    )