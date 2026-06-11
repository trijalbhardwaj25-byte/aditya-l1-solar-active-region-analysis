import os
import sunpy.map
import numpy as np
import matplotlib.pyplot as plt

from skimage.measure import label, regionprops
from skimage.morphology import remove_small_objects

folder = r"part 3\data"

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes = axes.flatten()

for idx, filename in enumerate(sorted(os.listdir(folder))):

    if not filename.endswith(".fits"):
        continue

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

        largest = max(
            regions,
            key=lambda r: r.area
        )

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

    ax = axes[idx]

    ax.imshow(
        normalized,
        cmap="inferno",
        origin="lower"
    )

    ax.set_title(filter_name)

    ax.text(
        20,
        40,
        f"Regions: {region_count}\nArea: {int(area)}\nIntensity: {mean_intensity:.3f}",
        color="white",
        fontsize=10,
        bbox=dict(facecolor="black", alpha=0.7)
    )

    ax.axis("off")

plt.suptitle(
    "Multi-Wavelength Active Region Comparison",
    fontsize=16
)

plt.tight_layout()

plt.savefig(
    r"part 3\figures\multifilter_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print(
    "Dashboard saved successfully."
)