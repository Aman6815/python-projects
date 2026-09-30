from image import Image


image = Image("input/lake.png")

bright_image = image.brighten(1.5)
bright_image.save("output/lake_bright.png")

contrast_image = image.adjust_contrast(1.5)
contrast_image.save("output/lake_contrast.png")

print(f"Width: {image.width}")
print(f"Height: {image.height}")
print(f"Channels: {image.channels}")
print("Bright and contrast images saved.")