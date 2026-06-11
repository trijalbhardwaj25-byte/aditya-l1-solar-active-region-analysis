import os
import imageio.v2 as imageio

image_folder = "RESULTS/images"

files = sorted([
    f for f in os.listdir(image_folder)
    if f.endswith(".png")
    and "SUT_T24" in f
])

print("Frames being added:")

frames = []

for file in files:
    print(file)
    frames.append(
        imageio.imread(
            os.path.join(image_folder, file)
        )
    )

print("\nTotal frames:", len(frames))

imageio.mimsave(
    "RESULTS/animations/active_regions.gif",
    frames,
    duration=2
)

print("GIF created successfully")