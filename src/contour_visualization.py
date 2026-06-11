import sunpy.map
import matplotlib.pyplot as plt
import numpy as np

from skimage.morphology import remove_small_objects

file_path = r"DATA/raw/SUT_T24_0025_000016_Lev1.0_2024-01-07T00.04.50.320_0973NB04.fits"

# Load FITS file
smap = sunpy.map.Map(file_path)

# Convert to float
data = smap.data.astype(float)

# Normalize
normalized = (data - np.min(data)) / (np.max(data) - np.min(data))

# Create mask
mask = normalized > 0.7

# Remove small noisy regions
mask = remove_small_objects(mask, 100)

# Plot image
plt.figure(figsize=(8,8))

plt.imshow(
    normalized,
    origin="lower",
    cmap="inferno"
)

# Draw contours
plt.contour(
    mask,
    colors="cyan",
    linewidths=2
)

plt.title("Active Region Contours")

# Save image
plt.savefig(
    "RESULTS/images/contour_nb04.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()