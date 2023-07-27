import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from src.components.data_ingestion import DataIngestion

from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

class TraininingPipeline:

    
    def start_data_ingestion(self):
        try:
            data_ingestion = DataIngestion()
            train_data_path,test_data_path = data_ingestion.initiate_data_ingestion()
            return train_data_path,test_data_path
            
        except Exception as e:
            raise CustomException(e,sys)
        
    
    def start_data_transformation(self, train_data_path,test_data_path):
        try:
            data_transformation = DataTransformation()
            train_arr, test_arr,preprocessor_path = data_transformation.initiate_data_transformation(train_data_path,test_data_path)
            return train_arr, test_arr,preprocessor_path
            
        except Exception as e:
            raise CustomException(e,sys)


    def start_model_training(self, train_arr, test_arr):
        try:
            model_trainer = ModelTrainer()
            model_score = model_trainer.initiate_model_training(
                train_arr, test_arr
            )
            return model_score
            
        except Exception as e:
            raise CustomException(e,sys)
        

    def run_pipeline(self):
        try:
            train_data_path,test_data_path = self.start_data_ingestion()
            train_arr, test_arr,preprocessor_path = self.start_data_transformation(train_data_path,test_data_path)
            accuracy = self.start_model_training(train_arr, test_arr)
            
            
            print("training completed. Trained model score : ", accuracy)

        except Exception as e:
            raise CustomException(e, sys)
logging.info("training_pipeline is started")

# if __name__=='__main__':
#     try:
#         train_pipeline = TraininingPipeline()
#         train_pipeline.run_pipeline()

#         logging.info("Training Completed.")
        
#     except Exception as e:
#         raise CustomException(e,sys)
    # obj=DataIngestion()
    # train_data_path,test_data_path=obj.initiate_data_ingestion()
    # print(train_data_path,test_data_path)

    # data_transformation=DataTransformation()
    # train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)

    # model_trainer=ModelTrainer()
    # model_trainer.initate_model_training(train_arr,test_arr)