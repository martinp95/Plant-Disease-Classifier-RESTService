class Config:
    """
    Configuration class containing paths to the model and class names file.
    """
    
    # Path to the pre-trained model file
    MODEL_PATH: str = '/workspaces/Plant-Disease-Classifier-RESTService/model/model.keras'

    # Path to the JSON file containing class names
    CLASS_NAMES_PATH: str = '/workspaces/Plant-Disease-Classifier-RESTService/model/model_class_names.json'
