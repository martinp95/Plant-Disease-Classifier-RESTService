
# Image Classification Service

This project provides a web service for classifying images using a TensorFlow model. It includes a Flask-based web server that handles HTTP requests for image classification, model information, and health checks.

## Project Structure

```
- app/
  - controllers/
    - __init__.py
    - image_controller.py
  - models/
    - __init__.py
    - classifier.py
  - services/
    - __init__.py
    - image_service.py
  - utils/
    - __init__.py
    - image_preprocessing.py
  - config.py
  - main.py
  - __init__.py
- model/
  - model_class_names.json
  - model.keras
- notebooks/
  - pruebas_ws.ipynb
```

## Configuration

Update the `app/config.py` file to specify the paths to the TensorFlow model and class names JSON file:
```python
class Config:
    """
    Configuration class containing paths to the model and class names file.
    """
    
    # Path to the pre-trained model file
    MODEL_PATH: str = '/workspaces/Plant-Disease-Classifier-RESTService/model/model.keras'

    # Path to the JSON file containing class names
    CLASS_NAMES_PATH: str = '/workspaces/Plant-Disease-Classifier-RESTService/model/model_class_names.json'
```

## Running the Application

To run the Flask application, use the following command:
```
python -m app.main
```

The application will be available at `http://0.0.0.0:5000`.

## API Endpoints

### Classify Images

- **URL**: `/classify`
- **Method**: `POST`
- **Description**: Classifies the uploaded images.
- **Request**: `multipart/form-data`
  - `images`: List of image files to be classified.
- **Response**: `application/json`
  ```json
  [
    {
      "image": "image_filename.jpg",
      "class": "predicted_class",
      "probability": 0.95
    },
    ...
  ]
  ```

### Health Check

- **URL**: `/health`
- **Method**: `GET`
- **Description**: Checks the health status of the application.
- **Response**: `application/json`
  ```json
  {
    "status": "healthy"
  }
  ```

### Model Information

- **URL**: `/model-info`
- **Method**: `GET`
- **Description**: Retrieves information about the model.
- **Response**: `application/json`
  ```json
  {
    "model_summary": "model_json_summary"
  }
  ```