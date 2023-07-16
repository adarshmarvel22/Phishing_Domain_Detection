import sys

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.exception import CustomException


class TrainPipeline:
    def __init__(self) -> None:
        # Create instances of the required classes
        self.data_ingestion = DataIngestion()

        self.data_transformation = DataTransformation()
        
        self.model_trainer = ModelTrainer()

    def run_pipeline(self):
        try:
            # Initiate data ingestion and retrieve file paths for train and test data
            train_path, test_path = self.data_ingestion.initiate_data_ingestion()

            # Initiate data transformation and retrieve transformed data and preprocessor file path
            (
                train_arr,
                test_arr,
                preprocessor_file_path,
            ) = self.data_transformation.initiate_data_transformation(
                train_path=train_path, test_path=test_path
            )

            # Initiate model training and retrieve the R-squared score
            r2_square = self.model_trainer.initiate_model_trainer(
                train_array=train_arr,
                test_array=test_arr,
                preprocessor_path=preprocessor_file_path,
            )

            # Print the trained model's R-squared score
            print("training completed. Trained model score : ", r2_square)

        except Exception as e:
            raise CustomException(e, sys)
