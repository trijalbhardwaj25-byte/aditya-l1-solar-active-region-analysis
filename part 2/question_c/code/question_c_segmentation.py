import os
import sunpy.map
import numpy as np

from skimage.filters import threshold_otsu
from skimage.filters import threshold_local

from skimage.measure import label, regionprops
from skimage.morphology import remove_small_objects

data_folder = "DATA/raw"

print("\n===== SEGMENTATION COMPARISON =====\n")

for filename in sorted(os.listdir(data_folder)):

    if not filename.endswith(".fits"):
        continue

    file_path = os.path.join(data_folder, filename)

    smap = sunpy.map.Map(file_path)

    data = smap.data.astype(float)

    normalized = (
        data - np.min(data)
    ) / (
        np.max(data) - np.min(data)
    )

    # Fixed Threshold

    fixed_mask = normalized > 0.7
    fixed_mask = remove_small_objects(
        fixed_mask,
        100
    )

    fixed_regions = len(
        regionprops(
            label(fixed_mask)
        )
    )

    # Otsu

    otsu_value = threshold_otsu(
        normalized
    )

    otsu_mask = normalized > otsu_value

    otsu_mask = remove_small_objects(
        otsu_mask,
        100
    )

    otsu_regions = len(
        regionprops(
            label(otsu_mask)
        )
    )

    # Adaptive

    adaptive_thresh = threshold_local(
        normalized,
        block_size=51
    )

    adaptive_mask = normalized > adaptive_thresh

    adaptive_mask = remove_small_objects(
        adaptive_mask,
        100
    )

    adaptive_regions = len(
        regionprops(
            label(adaptive_mask)
        )
    )

    print(
        f"{filename[-11:-5]}  |  "
        f"Fixed={fixed_regions}  "
        f"Otsu={otsu_regions}  "
        f"Adaptive={adaptive_regions}"
    )