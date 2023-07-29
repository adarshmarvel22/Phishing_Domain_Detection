from sklearn.impute import SimpleImputer ## HAndling Missing Values
from sklearn.preprocessing import StandardScaler # HAndling Feature Scaling
# from sklearn.preprocessing import OrdinalEncoder # Ordinal Encoding
## pipelines
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

import sys,os
from dataclasses import dataclass
import pandas as pd
import numpy as np

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object


## Data Transformation config

@dataclass
class DataTransformationconfig:
    logging.info("data_transformation_config class started")
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')



## Data Ingestionconfig class

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationconfig()

    def get_data_transformation_object(self):
         
         try:
            logging.info('Data Transformation initiated')
            # Define which columns which should be scaled
            numerical_cols = ['qty_dot_url',
                               'qty_hyphen_url', 
                               'qty_underline_url',
                                'qty_slash_url', 'qty_percent_url',
                                'qty_tld_url', 'length_url', 
                                'qty_dot_domain', 'qty_hyphen_domain', 
                                'qty_vowels_domain', 'domain_length', 
                                'qty_hyphen_directory', 'qty_underline_directory', 
                                'qty_plus_directory', 'qty_asterisk_directory', 
                                'qty_percent_directory', 'directory_length', 
                                'qty_hyphen_file', 'file_length', 'qty_dot_params', 
                                'qty_underline_params', 'qty_equal_params', 
                                'qty_plus_params', 'qty_percent_params', 
                                'time_domain_activation'
                                ]
            # print(len(numerical_cols))
            logging.info('Pipeline Initiated')

            ## Numerical Pipeline
            num_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('scaler',StandardScaler())
                ]
            )

            preprocessor=ColumnTransformer([
            ('num_pipeline',num_pipeline,numerical_cols),
            ])
            
            return preprocessor
            
            logging.info('Pipeline Completed')

         except Exception as e:
            
            logging.info("Error in Data Trnasformation")
            raise CustomException(e,sys)



    def initiate_data_transformation(self,train_path,test_path):
        try:
            # Reading train and test data
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info('Read train and test data completed')
            logging.info(f'Train Dataframe Head : \n{train_df.head().to_string()}')
            logging.info(f'Test Dataframe Head  : \n{test_df.head().to_string()}')

            logging.info('Obtaining preprocessing object')

            preprocessing_obj = self.get_data_transformation_object()

            target_column_name = 'phishing'
            drop_columns = [target_column_name,'qty_questionmark_url',
                                                'qty_equal_url',
                                                'qty_at_url',
                                                'qty_and_url',
                                                'qty_exclamation_url',
                                                'qty_space_url',
                                                'qty_tilde_url',
                                                'qty_comma_url',
                                                'qty_plus_url',
                                                'qty_asterisk_url',
                                                'qty_hashtag_url',
                                                'qty_dollar_url',
                                                'qty_underline_domain',
                                                'qty_slash_domain',
                                                'qty_questionmark_domain',
                                                'qty_equal_domain',
                                                'qty_at_domain',
                                                'qty_and_domain',
                                                'qty_exclamation_domain',
                                                'qty_space_domain',
                                                'qty_tilde_domain',
                                                'qty_comma_domain',
                                                'qty_plus_domain',
                                                'qty_asterisk_domain',
                                                'qty_hashtag_domain',
                                                'qty_dollar_domain',
                                                'qty_percent_domain',
                                                'domain_in_ip',
                                                'server_client_domain',
                                                'qty_dot_directory',
                                                'qty_slash_directory',
                                                'qty_questionmark_directory',
                                                'qty_equal_directory',
                                                'qty_at_directory',
                                                'qty_and_directory',
                                                'qty_exclamation_directory',
                                                'qty_space_directory',
                                                'qty_tilde_directory',
                                                'qty_comma_directory',
                                                'qty_hashtag_directory',
                                                'qty_dollar_directory',
                                                'qty_dot_file',
                                                'qty_underline_file',
                                                'qty_slash_file',
                                                'qty_questionmark_file',
                                                'qty_equal_file',
                                                'qty_at_file',
                                                'qty_and_file',
                                                'qty_exclamation_file',
                                                'qty_space_file',
                                                'qty_tilde_file',
                                                'qty_comma_file',
                                                'qty_plus_file',
                                                'qty_asterisk_file',
                                                'qty_hashtag_file',
                                                'qty_dollar_file',
                                                'qty_percent_file',
                                                'qty_hyphen_params',
                                                'qty_slash_params',
                                                'qty_questionmark_params',
                                                'qty_at_params',
                                                'qty_and_params',
                                                'qty_exclamation_params',
                                                'qty_space_params',
                                                'qty_tilde_params',
                                                'qty_comma_params',
                                                'qty_asterisk_params',
                                                'qty_hashtag_params',
                                                'qty_dollar_params',
                                                'params_length',
                                                'tld_present_params',
                                                'qty_params',
                                                'email_in_url',
                                                'time_response',
                                                'domain_spf',
                                                'asn_ip',
                                                'time_domain_expiration',
                                                'qty_ip_resolved',
                                                'qty_nameservers',
                                                'qty_mx_servers',
                                                'ttl_hostname',
                                                'tls_ssl_certificate',
                                                'qty_redirects',
                                                'url_google_index',
                                                'domain_google_index',
                                                'url_shortened',]

            ## features into independent and dependent features

            input_feature_train_df = train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df=train_df[target_column_name]


            input_feature_test_df=test_df.drop(columns=drop_columns,axis=1)
            target_feature_test_df=test_df[target_column_name]

            ## apply the transformation

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            logging.info("Applying preprocessing object on training and testing datasets.")

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            logging.info('Processsor pickle in created and saved')

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")

            raise CustomException(e,sys)
        