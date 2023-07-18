import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            data_scaled=preprocessor.transform(features)

            pred=model.predict(data_scaled)
            return pred
            

        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)
        
# class CustomData:
#     def __init__(self,
#                  qty_questionmark_url,
                # 'qty_equal_url',
                # 'qty_at_url',
                # 'qty_and_url',
                # 'qty_exclamation_url',
                # 'qty_space_url',
                # 'qty_tilde_url',
                # 'qty_comma_url',
                # 'qty_plus_url',
                # 'qty_asterisk_url',
                # 'qty_hashtag_url',
                # 'qty_dollar_url',
                # 'qty_underline_domain',
                # 'qty_slash_domain',
                # 'qty_questionmark_domain',
                # 'qty_equal_domain',
                # 'qty_at_domain',
                # 'qty_and_domain',
                # 'qty_exclamation_domain',
                # 'qty_space_domain',
                # 'qty_tilde_domain',
                # 'qty_comma_domain',
                # 'qty_plus_domain',
                # 'qty_asterisk_domain',
                # 'qty_hashtag_domain',
                # 'qty_dollar_domain',
                # 'qty_percent_domain',
                # 'domain_in_ip',
                # 'server_client_domain',
                # 'qty_dot_directory',
                # 'qty_slash_directory',
                # 'qty_questionmark_directory',
                # 'qty_equal_directory',
                # 'qty_at_directory',
                # 'qty_and_directory',
                # 'qty_exclamation_directory',
                # 'qty_space_directory',
                # 'qty_tilde_directory',
                # 'qty_comma_directory',
                # 'qty_hashtag_directory',
                # 'qty_dollar_directory',
                # 'qty_dot_file',
                # 'qty_underline_file',
                # 'qty_slash_file',
                # 'qty_questionmark_file',
                # 'qty_equal_file',
                # 'qty_at_file',
                # 'qty_and_file',
                # 'qty_exclamation_file',
                # 'qty_space_file',
                # 'qty_tilde_file',
                # 'qty_comma_file',
                # 'qty_plus_file',
                # 'qty_asterisk_file',
                # 'qty_hashtag_file',
                # 'qty_dollar_file',
                # 'qty_percent_file',
                # 'qty_hyphen_params',
                # 'qty_slash_params',
                # 'qty_questionmark_params',
                # 'qty_at_params',
                # 'qty_and_params',
                # 'qty_exclamation_params',
                # 'qty_space_params',
                # 'qty_tilde_params',
                # 'qty_comma_params',
                # 'qty_asterisk_params',
                # 'qty_hashtag_params',
                # 'qty_dollar_params',
                # 'params_length',
                # 'tld_present_params',
                # 'qty_params',
                # 'email_in_url',
                # 'time_response',
                # 'domain_spf',
                # 'asn_ip',
                # 'time_domain_expiration',
                # 'qty_ip_resolved',
                # qty_nameservers,
                # qty_mx_servers,
                # ttl_hostname,
                # tls_ssl_certificate,
                # qty_redirects,
                # url_google_index,
                # domain_google_index:int,
                # url_shortened:int):
        
#         self.qty_questionmark_url=qty_questionmark_url
#         self.qty_equal_url=qty_equal_url
#         self.

#     def get_data_as_dataframe(self):
#         try:
#             custom_data_input_dict = {
#                 'qty_questionmark_url':[self.qty_questionmark_url],
#                 'qty_equal_url':[self.qty_equal_url],

#             }
#             df = pd.DataFrame(custom_data_input_dict)
#             logging.info('Dataframe Gathered')
#             return df
#         except Exception as e:
#             logging.info('Exception Occured in prediction pipeline')
#             raise CustomException(e,sys)

