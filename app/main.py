from flask import Flask
from controllers import ImageController

class AppFactory:
    """
    Factory class to create and configure the Flask application.
    """

    @staticmethod
    def create_app() -> Flask:
        """
        Create and configure the Flask application.

        Returns:
            Flask: The configured Flask application instance.
        """
        app = Flask(__name__)
        
        # Register the image controller with the Flask application
        ImageController.register(app)
        
        return app

if __name__ == '__main__':
    # Create the application instance
    app = AppFactory.create_app()
    
    # Run the application on the specified host and port
    app.run(host='0.0.0.0', port=5000)
