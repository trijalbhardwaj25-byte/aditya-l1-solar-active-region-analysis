import os
import sunpy.map
import numpy as np
import matplotlib.pyplot as plt

from skimage.measure import label, regionprops
from skimage.morphology import remove_small_objects

folder = r"part 3\data"

results = []

for filename in sorted(os.listdir(folder)):

    if not filename.endswith(".fits"):
        continue

    print(f"\nProcessing: {filename}")

    file_path = os.path.join(folder, filename)

    smap = sunpy.map.Map(file_path)

    data = smap.data.astype(float)

    normalized = (
        data - np.min(data)
    ) / (
        np.max(data) - np.min(data)
    )

    mask = normalized > 0.7

    mask = remove_small_objects(mask, 100)

    labels = label(mask)

    regions = regionprops(labels)

    region_count = len(regions)

    if region_count > 0:

        largest = max(regions, key=lambda r: r.area)

        area = largest.area

        coords = largest.coords

        mean_intensity = np.mean(
            normalized[
                coords[:, 0],
                coords[:, 1]
            ]
        )

    else:

        area = 0
        mean_intensity = 0

    filter_name = filename.split("0973")[-1].replace(".fits", "")

    results.append(
        [
            filter_name,
            region_count,
            area,
            mean_intensity
        ]
    )

    print(
        f"Filter={filter_name}"
    )

    print(
        f"Regions={region_count}"
    )

    print(
        f"Largest Area={area}"
    )

    print(
        f"Mean Intensity={mean_intensity:.4f}"
    )

print("\n===== FINAL RESULTS =====")

for row in results:
    print(row)