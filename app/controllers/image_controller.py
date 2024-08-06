from flask import Blueprint, request, jsonify, Flask
from services import ImageService
from werkzeug.datastructures import FileStorage
from typing import List

class ImageController:
    """
    Controller for image-related endpoints.
    """
    
    image_service = ImageService()

    @staticmethod
    def register(app: Flask) -> None:
        """
        Register the image controller with the Flask application.

        Args:
            app (Flask): The Flask application instance.
        """
        image_controller = Blueprint('image_controller', __name__)
        image_controller.add_url_rule('/', 'health_check', ImageController.health_check, methods=['GET'])
        image_controller.add_url_rule('/classify', 'classify', ImageController.classify, methods=['POST'])
        image_controller.add_url_rule('/health', 'health_check', ImageController.health_check, methods=['GET'])
        image_controller.add_url_rule('/model-info', 'model_info', ImageController.model_info, methods=['GET'])
        app.register_blueprint(image_controller)

    @staticmethod
    def classify():
        """
        Endpoint to classify images.

        Returns:
            Response: JSON response containing the classification results.
        """
        images: List[FileStorage] = request.files.getlist('images')
        results = ImageController.image_service.classify_images(images)
        return jsonify(results)

    @staticmethod
    def health_check():
        """
        Endpoint to check the health status of the application.

        Returns:
            Response: JSON response indicating the health status.
        """
        return jsonify({"status": "healthy"})

    @staticmethod
    def model_info():
        """
        Endpoint to get information about the model.

        Returns:
            Response: JSON response containing the model information.
        """
        info = ImageController.image_service.get_model_info()
        return jsonify(info)
