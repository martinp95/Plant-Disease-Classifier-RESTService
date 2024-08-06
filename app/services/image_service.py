from models import Classifier
from utils import ImagePreprocessor
import numpy as np
from config import Config
from werkzeug.datastructures import FileStorage
from typing import List, Dict, Any

class ImageService:
    """
    Service class for handling image classification operations.
    """

    def __init__(self) -> None:
        """
        Initializes the ImageService with a classifier.
        """
        self.classifier = Classifier(model_path=Config.MODEL_PATH, class_names_path=Config.CLASS_NAMES_PATH)

    def classify_images(self, images: List[FileStorage]) -> List[Dict[str, Any]]:
        """
        Classifies a list of images.

        Args:
            images (List[FileStorage]): List of images to be classified.

        Returns:
            List[Dict[str, Any]]: List of dictionaries containing classification results.
        """
        processed_images = []
        filenames = []

        for image in images:
            processed_image = ImagePreprocessor.preprocess_image(image)
            processed_images.append(processed_image)
            filenames.append(image.filename)

        # Convert to numpy array and make batch prediction
        processed_images = np.array(processed_images)
        predictions = self.classifier.predict(processed_images)

        results = []
        for i, prediction in enumerate(predictions):
            predicted_class, probability = prediction
            results.append({
                'image': filenames[i],
                'class': predicted_class,
                'probability': float(probability)  # Convert to float
            })

        return results

    def get_model_info(self) -> Dict[str, Any]:
        """
        Retrieves relevant information about the model.

        Returns:
            Dict[str, Any]: Dictionary containing the model information.
        """
        return self.classifier.model_info()
