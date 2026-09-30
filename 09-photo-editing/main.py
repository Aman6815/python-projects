from image import Image


image = Image("input/lake.png")

bright_image = image.brighten(1.5)
bright_image.save("output/lake_bright.png")

contrast_image = image.adjust_contrast(1.5)
contrast_image.save("output/lake_contrast.png")

blurred_image = image.blur(5)
blurred_image.save("output/lake_blurred.png")

print("Image transformations completed.")