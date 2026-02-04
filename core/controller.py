from core.image_processor import ImageProcessor

class Controller:
    def __init__(self):
        self.processor = ImageProcessor()

    def load_image(self, path):
        return self.processor.load_image(path)

    def apply_grayscale(self):
        return self.processor.apply_grayscale()

    def get_current_image(self):
        return self.processor.get_image()
