from image import Image


image = Image("input/does_not_exist.png")

print(f"Width: {image.width}")
print(f"Height: {image.height}")
print(f"Channels: {image.channels}")

