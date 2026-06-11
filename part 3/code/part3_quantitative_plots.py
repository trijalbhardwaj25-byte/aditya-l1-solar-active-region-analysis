import matplotlib.pyplot as plt

filters = ["NB02", "NB03", "NB04", "NB05"]

areas = [39154, 2042, 2070, 62860]

intensities = [0.7772, 0.7954, 0.7890, 0.7784]

# ==========================
# AREA VS FILTER
# ==========================

plt.figure(figsize=(8,5))

plt.bar(filters, areas)

plt.title(
    "Active Region Area Across SUIT Filters"
)

plt.xlabel("Filter")

plt.ylabel("Largest Active Region Area (pixels)")

plt.grid(True, axis="y")

plt.tight_layout()

plt.savefig(
    r"part 3\figures\area_vs_filter.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ==========================
# INTENSITY VS FILTER
# ==========================

plt.figure(figsize=(8,5))

plt.plot(
    filters,
    intensities,
    marker="o",
    linewidth=2
)

plt.title(
    "Mean Active Region Intensity Across SUIT Filters"
)

plt.xlabel("Filter")

plt.ylabel("Mean Normalized Intensity")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    r"part 3\figures\intensity_vs_filter.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Plots saved successfully.")