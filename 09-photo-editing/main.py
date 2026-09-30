from image import Image


image = Image("input/lake.png")

bright_image = image.brighten(1.5)
bright_image.save("output/lake_bright.png")

contrast_image = image.adjust_contrast(1.5)
contrast_image.save("output/lake_contrast.png")

blurred_image = image.blur(5)
blurred_image.save("output/lake_blurred.png")

horizontal_kernel = [
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1],
]

vertical_kernel = [
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1],
]

horizontal_edges = image.apply_kernel(horizontal_kernel)
vertical_edges = image.apply_kernel(vertical_kernel)

edges = horizontal_edges.combine(vertical_edges)
edges.save("output/lake_edges.png")

print("All image transformations completed.")

gray_image = image.grayscale()
gray_image.save("output/lake_grayscale.png")

inverted_image = image.invert()
inverted_image.save("output/lake_inverted.png")