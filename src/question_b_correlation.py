import os
import sunpy.map
import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import pearsonr
from scipy.stats import spearmanr

from skimage.measure import label
from skimage.measure import regionprops
from skimage.morphology import remove_small_objects

folder = "DATA/temporal_evolution"

dates = []
areas = []
mean_intensities = []

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

    mask = normalized > 0.7

    mask = remove_small_objects(mask, 100)

    labels = label(mask)

    regions = regionprops(labels)

    if len(regions) == 0:

        area = 0
        mean_intensity = 0

    else:

        largest_region = max(
            regions,
            key=lambda r: r.area
        )

        area = largest_region.area

        coords = largest_region.coords

        mean_intensity = np.mean(
            normalized[
                coords[:, 0],
                coords[:, 1]
            ]
        )

    date = filename.split("_Lev1.0_")[1][:10]

    dates.append(date)
    areas.append(area)
    mean_intensities.append(mean_intensity)

    print(
        f"{date} | Area={area} | Mean Intensity={mean_intensity:.4f}"
    )

valid_indices = [
    i for i in range(len(areas))
    if areas[i] > 0
]

valid_areas = [
    areas[i]
    for i in valid_indices
]

valid_intensities = [
    mean_intensities[i]
    for i in valid_indices
]

pearson_corr, pearson_p = pearsonr(
    valid_areas,
    valid_intensities
)

spearman_corr, spearman_p = spearmanr(
    valid_areas,
    valid_intensities
)

print("\n===== CORRELATION RESULTS =====")

print(
    f"Pearson Correlation : {pearson_corr:.4f}"
)

print(
    f"Pearson p-value     : {pearson_p:.4f}"
)

print(
    f"Spearman Correlation: {spearman_corr:.4f}"
)

print(
    f"Spearman p-value    : {spearman_p:.4f}"
)

plt.figure(figsize=(7,5))

plt.scatter(
    valid_areas,
    valid_intensities
)

plt.xlabel(
    "Active Region Area (pixels)"
)

plt.ylabel(
    "Mean Intensity"
)

plt.title(
    "Area vs Mean Intensity"
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "area_intensity_correlation.png",
    dpi=300
)

plt.show()