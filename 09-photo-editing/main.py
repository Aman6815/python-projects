from image import Image


image = Image("input/lake.png")

# Brightness
bright_image = image.brighten(1.5)
bright_image.save("output/lake_bright.png")

# Contrast
contrast_image = image.adjust_contrast(1.5)
contrast_image.save("output/lake_contrast.png")

# Blur
blurred_image = image.blur(5)
blurred_image.save("output/lake_blurred.png")

# Edge detection
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

# Grayscale
gray_image = image.grayscale()
gray_image.save("output/lake_grayscale.png")

# Invert
inverted_image = image.invert()
inverted_image.save("output/lake_inverted.png")

# Flip
flipped_horizontal = image.flip_horizontal()
flipped_horizontal.save("output/lake_flip_horizontal.png")

flipped_vertical = image.flip_vertical()
flipped_vertical.save("output/lake_flip_vertical.png")

# Rotate
rotated_image = image.rotate_90()
rotated_image.save("output/lake_rotated.png")

print("All image transformations completed.")