from PIL import Image
import numpy as np
from typing import Tuple, Any

class ImagePreprocessor:
    """
    A class for preprocessing images.
    """
    
    @staticmethod
    def preprocess_image(image: Any, target_size: Tuple[int, int] = (512, 512)) -> np.ndarray:
        """
        Preprocesses the input image by resizing it and converting it to a numpy array.

        Args:
            image (Any): The input image to preprocess.
            target_size (Tuple[int, int]): The target size to resize the image to.

        Returns:
            np.ndarray: The preprocessed image as a numpy array.
        """
        img = Image.open(image)
        img = img.resize(target_size)
        image_array = np.array(img)
        return image_array
