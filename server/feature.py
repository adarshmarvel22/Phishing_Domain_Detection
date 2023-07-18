import pandas as pd
import numpy as np
# import ipaddress
# import re
import urllib.request
from bs4 import BeautifulSoup
# import socket
import requests
from googlesearch import search
import whois
from datetime import date, datetime
from dateutil.parser import parse as date_parse
from urllib.parse import urlparse


class FeatureExtraction:
    extracted_features=[]
    def __init__(self):
       self.extracted_features=[]
    
    @staticmethod
    def __extract_domain(url):
        try:
            return url.split("//")[1].split("/")[0]
        except Exception as e:
            return ""
    
    @staticmethod
    def __extract_directory(url):
        try:
            return url.split("//")[1].split("/")[1]
        except Exception as e:
            return ""
        
    @staticmethod
    def __extract_file(url):
        try:
            return url.split("//")[1].split("/")[2]
        except Exception as e:
            return ""
    
    @staticmethod
    def __extract_parameters(url):
        try:
            return url.split("//")[1].split("/")[3]
        except Exception as e:
            return ""
    
    @staticmethod
    def __extract_directory_length(directory):
        if directory == "":
            return -1
        return len(directory)
    
    @staticmethod
    def __extract_time_domain_activation(url):
        try:
            res = whois.whois(url)
            day_created = res['creation_date'][0]
            days= (datetime.datetime.now()-day_created).days
            return days
        except:
            return -1
    
    
    @staticmethod
    def __extract_length_url(url):
        return len(url)
    
    @staticmethod
    def __extract_file_length(file):
        
        if file == "":
            return -1
        
        return len(file)
    
    @staticmethod
    def __extract_qty_slash_url(url):
        return url.count("/")
    
    @staticmethod
    def __extract_qty_plus_directory(directory):
        return directory.count("+")
    
    @staticmethod
    def __extract_qty_vowels_domain(domain):
        qty_vowels_domain = 0
        for i in domain:
            if i in {"a","e","i","o","u"}:
                qty_vowels_domain+=1
        
        return qty_vowels_domain
    
    @staticmethod
    def __extract_qty_asterik_directory(directory):
        if directory == "":
            return -1
        
        return directory.count("*")
    
    @staticmethod
    def __extract_qty_hyphen_directory(directory):
        if directory == "":
            return  -1
        return directory.count("-")
    
    @staticmethod
    def __extract_qty_underline_directory(directory):
        if directory == "":
            return -1
        
        return directory.count("_")
    
    
    @staticmethod
    def __extract_qty_percent_directory(directory):
        if directory == "":
            return -1
        return directory.count("%")
    
    
    @staticmethod
    def __extract_qty_hyphen_file(file):
        if file == "":  
            return -1
        return file.count("-")
    
    @staticmethod
    def __extract_params_length(parameters):
        if parameters == "":
            return -1
        return len(parameters)
    
    @staticmethod
    def __extract_qty_tld_url(domain):
        try:
            
            top_level_domain = domain.split(".")[-1]
            
            return len(top_level_domain)

        except Exception as e:
            return 1
    
    @staticmethod
    def __extract_qty_plus_params(parameters):
        if parameters == "":
            return -1
        
        return parameters.count("+")
    
    @staticmethod
    def __extract_qty_equal_params(parameters):
        if parameters == "":
            return -1
        
        return parameters.count("=")
    
    @staticmethod
    def __extract_qty_dot_params(parameters):
        if parameters == "":    
            return -1
        
        return parameters.count(".")
    
    
    @staticmethod
    def __extract_qty_percent_params(parameters):
        if parameters == "":
            return -1
        return parameters.count("%")
    
    @staticmethod
    def __extract_qty_underline_params(parameters):
        if parameters == "":
            return -1
        return parameters.count("_")
    
    def generate_dataframe_from_url(self, url:str):

        domain = FeatureExtraction.__extract_domain(url)
        directory = FeatureExtraction.__extract_directory(url)
        file = FeatureExtraction.__extract_file(url)
        parameters = FeatureExtraction.__extract_parameters(url)
        directory_length = FeatureExtraction.__extract_directory_length(directory)
        time_domain_activation = FeatureExtraction.__extract_time_domain_activation(url)
        length_url = FeatureExtraction.__extract_length_url(url)
        file_length = FeatureExtraction.__extract_file_length(file)
        qty_slash_url = FeatureExtraction.__extract_qty_slash_url(url)
        qty_plus_directory = FeatureExtraction.__extract_qty_plus_directory(directory)
        domain_length = len(domain)
        qty_vowels_domain = FeatureExtraction.__extract_qty_vowels_domain(domain)
        qty_asterisk_directory = FeatureExtraction.__extract_qty_asterik_directory(directory)
        qty_hyphen_directory = FeatureExtraction.__extract_qty_hyphen_directory(directory)
        qty_dot_domain = domain.count(".")
        qty_underline_directory = FeatureExtraction.__extract_qty_underline_directory(directory)
        qty_percent_directory = FeatureExtraction.__extract_qty_percent_directory(directory)
        qty_dot_url = url.count(".")
        qty_hyphen_url = url.count("-")
        qty_hyphen_file = FeatureExtraction.__extract_qty_hyphen_file(file)
        qty_hyphen_domain = domain.count("-")
        qty_params_length = FeatureExtraction.__extract_params_length(parameters)
        qty_underline_url = url.count("_")
        qty_tld_url = FeatureExtraction.__extract_qty_tld_url(domain)
        qty_plus_params = FeatureExtraction.__extract_qty_plus_params(parameters)
        qty_percent_url = url.count("%")
        qty_equal_params = FeatureExtraction.__extract_qty_equal_params(parameters)
        qty_dot_params = FeatureExtraction.__extract_qty_dot_params(parameters)
        qty_percent_params = FeatureExtraction.__extract_qty_percent_params(parameters)
        qty_underline_params = FeatureExtraction.__extract_qty_underline_params(parameters)

        self.extracted_features=[qty_dot_url,
                               qty_hyphen_url, 
                               qty_underline_url,
                                qty_slash_url, qty_percent_url,
                                qty_tld_url, length_url, 
                                qty_dot_domain, qty_hyphen_domain, 
                                qty_vowels_domain, domain_length, 
                                qty_hyphen_directory, qty_underline_directory, 
                                qty_plus_directory, qty_asterisk_directory, 
                                qty_percent_directory, directory_length, 
                                qty_hyphen_file, file_length, qty_dot_params, 
                                qty_underline_params, qty_equal_params, 
                                qty_plus_params, qty_percent_params, 
                                time_domain_activation]
     
    def getFeaturesList(self):
        return self.extracted_features