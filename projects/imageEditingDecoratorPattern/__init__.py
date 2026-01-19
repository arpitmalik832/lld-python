from abc import ABC


class ImageUtils:
    @staticmethod
    def apply_blur(image: bytes) -> bytes:
        return image

    @staticmethod
    def apply_sharpen(image: bytes) -> bytes:
        return image

    @staticmethod
    def apply_grayscale(image: bytes) -> bytes:
        return image


class ImageEditor(ABC):
    def __init__(self, image: bytes):
        self.image = image

    def render(self):
        return f"Rendering {self.image}"


# Task 1 - Modify the class definition to inherit from the editor class.
class BaseImageDecorator(ImageEditor, ABC):

    # Task 2 - Modify the __init__ method to store the image editor instance.
    def __init__(self, image_editor: ImageEditor, image: bytes = None):
        super().__init__(image)
        if image_editor is not None:
            self.image_editor = image_editor
        else:
            self.image_editor = None

    # Task 3 - Add a render method that calls the render method of the image editor instance.
    def render(self):
        if self.image_editor is not None:
            self.image_editor.render()
        return super().render()


class BlurImageDecorator(BaseImageDecorator):

    # Task 4 - Modify the __init__ method to pass the image editor instance to the parent class.
    def __init__(self, image_editor: ImageEditor, image: bytes):
        super().__init__(image_editor, image)

    # Task 5 - Implement the render method to apply the blur using apply_blur function and return the result.
    def render(self):
        ImageUtils.apply_blur(self.image_editor.image)
        return super().render()


class SharpenImageDecorator(BaseImageDecorator):

    # Task 4 - Modify the __init__ method to pass the image editor instance to the parent class.
    def __init__(self, image_editor: ImageEditor, image: bytes):
        super().__init__(image_editor, image)

    # Task 5 - Implement the render method to apply the sharpen using apply_sharpen function and return the result.
    def render(self):
        ImageUtils.apply_sharpen(self.image_editor.image)
        return super().render()


class GrayscaleImageDecorator(BaseImageDecorator):

    # Task 4 - Modify the __init__ method to pass the image editor instance to the parent class.
    def __init__(self, image_editor: ImageEditor, image: bytes):
        super().__init__(image_editor, image)

    # Task 5 - Implement the render method to apply the grayscale using apply_grayscale function and return the result.
    def render(self):
        ImageUtils.apply_grayscale(self.image_editor.image)
        return super().render()
