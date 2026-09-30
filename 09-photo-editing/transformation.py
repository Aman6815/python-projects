    def brighten(self, factor):
        if factor < 0:
            raise ValueError("Brightness factor cannot be negative.")

        return Image(array=self.array * factor)

    def adjust_contrast(self, factor):
        middle = 0.5
        new_array = (self.array - middle) * factor + middle

        return Image(array=new_array)

    def apply_kernel(self, kernel):
        # existing code
        ...

    def blur(self, size=3):
        # existing code
        ...

    def combine(self, other):
        # existing code
        ...

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