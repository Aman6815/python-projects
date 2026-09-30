from pathlib import Path

import numpy as np
from PIL import Image as PILImage


class Image:
    """Represent an image as a NumPy array."""

    def __init__(self, filename=None, array=None):
        if filename is None and array is None:
            raise ValueError("Provide either a filename or an image array.")

        if filename is not None and array is not None:
            raise ValueError("Provide either a filename or an image array, not both.")

        if filename is not None:
            self.array = self._load_image(filename)
        else:
            self.array = self._validate_array(array)

    def _load_image(self, filename):
        path = Path(filename)

        if not path.exists():
            raise FileNotFoundError(f"Image not found: {path}")

        with PILImage.open(path) as image:
            image = image.convert("RGB")
            return np.asarray(image, dtype=np.float32) / 255.0

    def _validate_array(self, array):
        array = np.asarray(array, dtype=np.float32)

        if array.ndim != 3:
            raise ValueError("Image array must have three dimensions.")

        if array.shape[2] != 3:
            raise ValueError("Image must have exactly 3 color channels (RGB).")

        return array

    @property
    def height(self):
        return self.array.shape[0]

    @property
    def width(self):
        return self.array.shape[1]

    @property
    def channels(self):
        return self.array.shape[2]

    def brighten(self, factor):
        """Return a brighter or darker copy of the image."""

        if factor < 0:
            raise ValueError("Brightness factor cannot be negative.")

        return Image(array=self.array * factor)

    def adjust_contrast(self, factor):
        """Return a copy of the image with adjusted contrast."""

        middle = 0.5
        new_array = (self.array - middle) * factor + middle

        return Image(array=new_array)

    def apply_kernel(self, kernel):
        """Apply a 2D kernel to the image."""

        kernel = np.asarray(kernel, dtype=np.float32)

        if kernel.ndim != 2:
            raise ValueError("Kernel must be a 2D array.")

        kernel_height, kernel_width = kernel.shape

        if kernel_height % 2 == 0 or kernel_width % 2 == 0:
            raise ValueError("Kernel dimensions must be odd.")

        pad_y = kernel_height // 2
        pad_x = kernel_width // 2

        padded = np.pad(
            self.array,
            ((pad_y, pad_y), (pad_x, pad_x), (0, 0)),
            mode="edge",
        )

        result = np.zeros_like(self.array)

        for y in range(self.height):
            for x in range(self.width):
                region = padded[
                    y:y + kernel_height,
                    x:x + kernel_width,
                    :
                ]

                result[y, x] = np.sum(
                    region * kernel[:, :, np.newaxis],
                    axis=(0, 1),
                )

        return Image(array=result)

    def blur(self, size=3):
        """Blur the image using an averaging kernel."""

        if size < 1 or size % 2 == 0:
            raise ValueError("Blur size must be a positive odd number.")

        kernel = np.ones((size, size), dtype=np.float32) / (size * size)

        return self.apply_kernel(kernel)

    def combine(self, other):
        """Combine two images using their pixel values."""

        if self.array.shape != other.array.shape:
            raise ValueError("Images must have the same dimensions.")

        combined = np.sqrt(
            self.array ** 2 + other.array ** 2
        )

        return Image(array=combined)

    def grayscale(self):
        """Convert the image to grayscale."""

        gray = (
            0.299 * self.array[:, :, 0]
            + 0.587 * self.array[:, :, 1]
            + 0.114 * self.array[:, :, 2]
        )

        gray_array = np.stack([gray, gray, gray], axis=2)

        return Image(array=gray_array)

    def invert(self):
        """Invert the image colors."""

        return Image(array=1.0 - self.array)

    def flip_horizontal(self):
        """Flip the image from left to right."""

        return Image(array=np.fliplr(self.array).copy())

    def flip_vertical(self):
        """Flip the image from top to bottom."""

        return Image(array=np.flipud(self.array).copy())

    def rotate_90(self):
        """Rotate the image 90 degrees clockwise."""

        return Image(array=np.rot90(self.array, k=3).copy())

    def save(self, filename):
        """Save the image to a file."""

        output = np.clip(self.array, 0, 1)
        output = (output * 255).astype(np.uint8)

        image = PILImage.fromarray(output, "RGB")
        image.save(filename)