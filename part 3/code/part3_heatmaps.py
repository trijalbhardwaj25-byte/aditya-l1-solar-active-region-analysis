import os
import sunpy.map
import numpy as np
import matplotlib.pyplot as plt

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

    filter_name = filename.split("0973")[-1].replace(".fits", "")

    ax = axes[idx]

    heatmap = ax.imshow(
        normalized,
        cmap="hot",
        origin="lower"
    )

    ax.set_title(f"{filter_name} Heatmap")

    ax.axis("off")

    plt.colorbar(
        heatmap,
        ax=ax,
        fraction=0.046,
        pad=0.04
    )

plt.suptitle(
    "Active Region Heatmap Comparison Across SUIT Filters",
    fontsize=16
)

plt.tight_layout()

plt.savefig(
    r"part 3\figures\multifilter_heatmaps.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Heatmap figure saved successfully.")