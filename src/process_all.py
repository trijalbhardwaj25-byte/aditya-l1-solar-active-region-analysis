import os
import sunpy.map
import matplotlib.pyplot as plt
import numpy as np

from skimage.measure import label, regionprops
from skimage.morphology import remove_small_objects

raw_folder = "DATA/raw"
results_folder = "RESULTS/images"

print("\nProcessing FITS files...\n")

summary = []

for filename in os.listdir(raw_folder):

    if not filename.endswith(".fits"):
        continue

    file_path = os.path.join(raw_folder, filename)

    print("Processing:", filename)

    # Load FITS file
    smap = sunpy.map.Map(file_path)

    # Normalize
    data = smap.data.astype(float)
    normalized = (data - np.min(data)) / (np.max(data) - np.min(data))

    # Threshold
    mask = normalized > 0.7

    # Remove noise
    mask = remove_small_objects(mask, min_size=100)

    # Label regions
    labels = label(mask)

    count = 0

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(normalized, origin="lower", cmap="inferno")

    for region in regionprops(labels):

        if region.area < 100:
            continue

        minr, minc, maxr, maxc = region.bbox

        rect = plt.Rectangle(
            (minc, minr),
            maxc - minc,
            maxr - minr,
            fill=False,
            edgecolor="cyan",
            linewidth=2
        )

        ax.add_patch(rect)
        count += 1

    plt.title(f"{filename}\nDetected Regions: {count}")

    save_name = filename.replace(".fits", ".png")

    plt.savefig(
        os.path.join(results_folder, save_name),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    summary.append([filename, count])

print("\n===== SUMMARY =====")

for row in summary:
    print(f"{row[0]}  -->  {row[1]} regions")

print("\nDone!")