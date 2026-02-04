import cv2
from effects import grayscale

class ImageProcessor:
    def __init__(self):
        self.original_image = None
        self.current_image = None

    def load_image(self, path):
        self.original_image = cv2.imread(path)
        self.current_image = self.original_image.copy()
        return self.current_image

    def get_image(self):
        return self.current_image

    def apply_grayscale(self):
        if self.current_image is None:
            return None

        self.current_image = grayscale.apply(self.current_image)
        return self.current_image
