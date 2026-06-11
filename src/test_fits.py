import sunpy.map
import matplotlib.pyplot as plt
import numpy as np

from skimage.measure import label, regionprops
from skimage.morphology import remove_small_objects

file_path = r"DATA/raw/SUT_T24_0025_000016_Lev1.0_2024-01-07T00.04.50.320_0973NB04.fits"

# Load FITS file
smap = sunpy.map.Map(file_path)

# Convert to float
data = smap.data.astype(float)

# Normalize image
normalized = (data - np.min(data)) / (np.max(data) - np.min(data))

# Threshold for bright active regions
mask = normalized > 0.7

# Remove tiny noisy objects
mask = remove_small_objects(mask, min_size=100)

# Label connected regions
labels = label(mask)

# Create figure
fig, ax = plt.subplots(figsize=(8, 8))

ax.imshow(normalized, origin="lower", cmap="inferno")

count = 0

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

plt.title(f"Detected Active Regions: {count}")

# Save image automatically
plt.savefig(
    "RESULTS/images/active_regions_nb04.png",
    dpi=300,
    bbox_inches="tight"
)

print("Number of detected regions:", count)
print("Image saved in RESULTS/images")

plt.show()