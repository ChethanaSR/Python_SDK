#!/usr/bin/env python
#############################################################################################################################################
__filename__ = "KeyWord_Search.py"
__description__ = """contains all functions related to KeyWord_Search"""
__author__ = "Chethana S R"
__copyright__ = "Copyright 2019"
__credits__ = ["Chethana S R"]
__version__ = "1.0"
__maintainer__ = "Chethana"
__email__ = "rchethana@shravas.com"
__status__ = "Testing"  # Upgrade to Production once tested to function.
#############################################################################################################################################

#Import Packages
#########################################################################################################################################
from ceic_api_client.api_client import ApiClient
from ceic_api_client.apis.dictionary_api import DictionaryApi
from ceic_api_client.apis.series_api import SeriesApi
from ceic_api_client.apis.insights_api import InsightsApi
from  datetime import datetime
from Common import config
from Common.config import *
from Common.html_report import *

import os
#import datetime.tz
#from dataclasses import dataclass, asdict, field, InitVar
###################################################################################################################################
def search_by_keyword(func_data):
    folder_name = func_data[0]
    config.testcase_id = func_data[2]
    config.test_description = func_data[4]
    config.exp_execution_time = str( func_data[5] )
    filteroption = func_data[6]
    test_input = func_data[3].replace( ";", "," )
    access_token = config.access_token


    api_client = ApiClient(header_name="Authorization", header_value=access_token)
    series_api = SeriesApi(api_client=api_client)
    keywords = []
    keywords.append(test_input)

    #print keywords
    series_search_result = series_api.search_series(keyword=", ".join(keywords), status="T,C,B")
    #series_search_result = series_api.search_series( keyword=", ".join( keywords ))
    #print series_search_result.to_dict()["data"]["items"]
    #print series_search_result
    actual_xml_file = xml_write( folder_name, series_search_result.to_dict())
    cmp_result = xml_csv_comp_filter( actual_xml_file, folder_name, test_input, filteroption )
    if cmp_result == True :
        config.tc_result = "PASS"
        #config.tc_remark = "API Results for provided SeriesCode/SRCode is fetched correctly"
        config.tc_remark = "API Results for provided '" +  filteroption +"' is fetched correctly"
        config.bln_critical_error_found = False
        config.bln_sucess = True
    else:
        config.tc_result = "FAIL"
        config.tc_remark = "API Results for provided Series Code is not fetched correctly"
        config.bln_critical_error_found = False
        config.bln_sucess = True






