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

horizontal_edges.save("output/edges_horizontal.png")
vertical_edges.save("output/edges_vertical.png")

print("Image transformations completed.")