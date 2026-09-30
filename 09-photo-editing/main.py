from image import Image


image = Image("input/lake.png")

bright_image = image.brighten(1.5)
bright_image.save("output/lake_bright.png")

print(f"Width: {image.width}")
print(f"Height: {image.height}")
print(f"Channels: {image.channels}")
print("Bright image saved.")