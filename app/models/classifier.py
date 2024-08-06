import tensorflow as tf
import json
from typing import Tuple, Dict, Any, List

class Classifier:
    """
    A class to handle image classification using a TensorFlow model.
    """

    def __init__(self, model_path: str, class_names_path: str) -> None:
        """
        Initializes the Classifier with a model and class names.

        Args:
            model_path (str): Path to the TensorFlow model.
            class_names_path (str): Path to the JSON file containing class names.
        """
        self.model = tf.keras.models.load_model(model_path)
        with open(class_names_path, 'r') as f:
            self.class_names = json.load(f)

    def predict(self, images: Any) -> List[Tuple[str, float]]:
        """
        Predicts the class of the given images.

        Args:
            images (Any): The images to be classified.

        Returns:
            List[Tuple[str, float]]: A list of tuples containing the predicted class and its probability for each image.
        """
        predictions = self.model.predict(images)
        results = []

        for prediction in predictions:
            predicted_class = self.class_names[prediction.argmax()]
            probability = float(prediction.max())  # Convert to float
            results.append((predicted_class, probability))

        return results

    def model_info(self) -> Dict[str, Any]:
        """
        Returns relevant information about the model.

        Returns:
            Dict[str, Any]: A dictionary containing the model name, input shape, output shape, and total parameters.
        """
        model_summary = {
            "model_name": self.model.name,
            "input_shape": self.model.input_shape,
            "output_shape": self.model.output_shape,
            "total_parameters": self.model.count_params()
        }
        return model_summary
