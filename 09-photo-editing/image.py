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

    def save(self, filename):
        """Save the image to a file."""

        output = np.clip(self.array, 0, 1)
        output = (output * 255).astype(np.uint8)

        image = PILImage.fromarray(output, "RGB")
        image.save(filename)