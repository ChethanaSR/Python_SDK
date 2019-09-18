#!/usr/bin/python

#############################################################################################################################################
__filename__ = "main.py"
__description__ = "With the help of unittest call all function in main.py "
__author__ = "Chethana S R"
__copyright__ = "Copyright 2019"
__credits__ = ["Chethana S R"]
__version__ = "1.0"
__maintainer__ = "Chethana"
__email__ = "rchethana@shravas.com"
__status__ = "Developing Stage"
#############################################################################################################################################

#########################################################################################################################################
#Import Packages
import os
import openpyxl

from Tests.Metadata import *
from Common.config import *
import unittest
import datetime
from  datetime import datetime
from datetime import timedelta
import time
from Tests.KeyWord_Seach import *
import decimal


###################################################################################################################################

class Test_Functions(unittest.TestCase):
    config.first_tc_start_time = datetime.now()
    html_header()
    #print ("first_start_time ", config.total_tc_execution_time)
    data = excel_read()
    #print(data)
    for i in range(len(data)):
       start_time = round( time.clock())
       #print(start_time)
       func_data =data[i].split("$")
       #print("Start time "  , start_time)
       if func_data[0] =="Metadata" and func_data[1] == "get_metadata_pef":get_metadata_pef(func_data)
       elif func_data[0] =="Metadata" and func_data[1] == "get_metadata":get_metadata(func_data)
       elif func_data[0] =="Keyword" and func_data[1] == "search_by_keyword":search_by_keyword(func_data)
       elif func_data[0] == "Keyword_SeriesID" and func_data[1] == "keywordsearch_by_seriesid":filter_option_by_seriesid(func_data)
       elif func_data[0] == "Metadata" and  func_data[1] == "get_subscribed_series_id":get_subscribed_series_id(func_data)
       end_time = round(time.clock())
       #print("End Time ", end_time)
       config.tc_execution_time = round((end_time - start_time))
       #print ("Current TC Execution Time :" , config.tc_execution_time )
       #print("###############################################")
       html_body()
    config.total_tc_execution_time = round( config.total_tc_execution_time + end_time )
    #print ("Total TC Execution Time ", config.total_tc_execution_time)
    config.last_tc_end_time = datetime.now()
    html_footer()





def suit():
    #suit = unittest.TestSuite()
    # suite.addTest(Test_Functions('get_metadata'))
    # suite.addTest(Test_Functions('get_keyword_search'))
    unittest.TestSuite().addTest(Test_Functions('get_metadata'))
    unittest.TestSuite().addTest( Test_Functions( 'get_seriescode_search' ) )







if __name__== '__main()__':
    runner = unittest.TextTestRunner()
    unittest.main()
