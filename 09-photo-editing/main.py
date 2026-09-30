from image import Image


def edit_image(input_path, output_dir):
    """Apply several edits to an image."""

    image = Image(input_path)

    image.brighten(1.5).save(output_dir / "bright.png")
    image.adjust_contrast(1.5).save(output_dir / "contrast.png")
    image.blur(5).save(output_dir / "blurred.png")

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

    horizontal_edges.save(output_dir / "edges_horizontal.png")
    vertical_edges.save(output_dir / "edges_vertical.png")

    horizontal_edges.combine(vertical_edges).save(
        output_dir / "edges.png"
    )

    image.grayscale().save(output_dir / "grayscale.png")
    image.invert().save(output_dir / "inverted.png")
    image.flip_horizontal().save(output_dir / "flip_horizontal.png")
    image.flip_vertical().save(output_dir / "flip_vertical.png")
    image.rotate_90().save(output_dir / "rotated.png")


if __name__ == "__main__":
    from pathlib import Path

    input_path = Path("input/lake.png")
    output_dir = Path("output")

    edit_image(input_path, output_dir)

    print("Photo editing completed successfully.")