#!/usr/bin/env python
#############################################################################################################################################
__filename__ = "Metadata.py"
__description__ = """contains function related to MetaData"""
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
from  ceic_api_client.pyceic import Ceic
from Common import config
from Common.config import *
from Common.html_report import *
import os
#import datetime.tz
#from dataclasses import dataclass, asdict, field, InitVar
###################################################################################################################################


#def get_metadata(folder_name , test_input):
def get_metadata(func_data):
    # start_time = datetime.now().strftime( "%Y/%m/%d" + "  " + "%I:%M:%S %p")
    folder_name = func_data[0]
    config.testcase_id = func_data[2]
    test_input = func_data[3]
    config.test_description = func_data[4]
    config.exp_execution_time = str(func_data[5])

    test_input = test_input.replace(";", ",")

    #series_metadata_result = Ceic.series_metadata(test_input)

    # print(folder_name, test_input)

    access_token = config.access_token
    example_series_id = test_input
    # print example_series_id

    api_client = ApiClient(header_name="Authorization", header_value=access_token)
    series_api = SeriesApi(api_client=api_client)

    series_metadata_result = series_api.get_series_metadata(id=example_series_id)
    actual_xml_file = xml_write(folder_name, series_metadata_result.to_dict(), func_data[2])
    # time.sleep(10)
    cmp_result = xml_csv_comp_new(actual_xml_file, folder_name, test_input, func_data[2])

    # result = []
    # for value in range(len(cmp_result)):
    #     if cmp_result[value] == []:
    #         blnflag = True
    #     else:
    #         blnflag = False
    #         result.append(cmp_result[value])

    if cmp_result == "":
        config.tc_result = "PASS"
        config.tc_remark = "All Metadata is fetched for a provided series"
        config.bln_critical_error_found = False
        config.bln_sucess = True
    else:
        config.tc_result = "FAIL"
       # config.tc_remark = "API Results for provided Series Code is not fetched correctly"
        config.tc_remark = cmp_result
        config.bln_critical_error_found = False
        config.bln_sucess = True










    # #print series_metadata_result
    # #
    # #print actual_xml_file
    # result =xml_comp( actual_xml_file, folder_name, test_input)
    # if result ==[]:
    #     config.tc_result = "PASS"
    #     config.tc_remark = "All Metadata is featched for a provided series"
    # else:
    #     config.tc_result = "FAIL"
    #     config.tc_remark = result
    # #call_full_report()



###################################################################################################################################

#Function to search filter option by Series ID

def filter_option_by_seriesid(func_data):
    folder_name = func_data[0]
    config.testcase_id = func_data[2]
    config.test_description = func_data[4]
    config.exp_execution_time = str( func_data[5] )
    filteroption = func_data[6]
    test_input = func_data[3].replace( ";", "," )

    access_token = config.access_token
    example_series_id = test_input

    api_client = ApiClient( header_name="Authorization", header_value=access_token )
    series_api = SeriesApi( api_client=api_client )

    #series_metadata_result = series_api.get_series_metadata( id=example_series_id )
    series_result = series_api.get_series( id=example_series_id )
    #print series_result
    actual_xml_file = xml_write( folder_name, series_result.to_dict(), func_data[2] )
    if filteroption =="Timepoint":
        cmp_result = xml_csv_comp_filter_for_timepoint( actual_xml_file, folder_name, test_input ,func_data[2] )
    else:
        cmp_result = xml_csv_comp_filter( actual_xml_file, folder_name, test_input, filteroption )


    if cmp_result == True :
        config.tc_result = "PASS"
        #config.tc_remark = "API Results for provided SeriesCode/SRCode is fetched correctly"
        config.tc_remark = "API Results for provided '" +  filteroption +"' series is fetched correctly"
        config.bln_critical_error_found = False
        config.bln_sucess = True
    else:
        config.tc_result = "FAIL"
        config.tc_remark = "API Results for provided Series Code is not fetched correctly"
        config.bln_critical_error_found = False
        config.bln_sucess = True

#########################################################################################################################

# Function to Verify Metadata for more than 100 series

def get_metadata_pef(func_data):

    #Get All requied Inputs
    folder_name = func_data[0]
    config.testcase_id = func_data[2]
    test_input = func_data[3]
    config.test_description = func_data[4]
    config.exp_execution_time = str( func_data[5] )


    #Get Access detials from SDK
    access_token = config.access_token
    example_series_id = test_input
    # print example_series_id

    api_client = ApiClient( header_name="Authorization", header_value=access_token )
    series_api = SeriesApi( api_client=api_client )


    test_input = test_input.replace( ";", "," )
    id = test_input.split( "," )
    newseriesid = ""
    dict = []
    p = 0
    r = 0

    def update_without_overwriting(d, x):
        dict.update( {k: v for k, v in x.items() if k not in d} )

    # for i in range (len(id)): print id[i]

    for num in range( 1, len( id ) + 1 ):
        newseriesid = newseriesid + "," + id[r]
        p += 1
        r += 1
        if p % 100 == 0:
            newseriesid = newseriesid[1:]
            series_metadata_result = series_api.get_series_metadata( id=newseriesid ).to_dict()
            #series_metadata_result = Ceic.series_metadata("407293587").to_dict()
            dict.append( series_metadata_result )
            newseriesid = ""
            p = 0

    actual_xml_file = xml_write( folder_name,dict, func_data[2] )
    #time.sleep( )
    cmp_result = xml_csv_comp_new( actual_xml_file, folder_name, test_input, func_data[2] )

    if cmp_result == "":
        config.tc_result = "PASS"
        config.tc_remark = "All Metadata is fetched for a provided series"
        config.bln_critical_error_found = False
        config.bln_sucess = True
    else:
        config.tc_result = "FAIL"
        # config.tc_remark = "API Results for provided Series Code is not fetched correctly"
        config.tc_remark = cmp_result
        config.bln_critical_error_found = False
        config.bln_sucess = True


###################################################################################################################################

#Function to Find Subscribed and Unsubsribed Series Id:

def get_subscribed_series_id(func_data):
    # Get All requied Inputs
    folder_name = func_data[0]
    config.testcase_id = func_data[2]
    test_input = func_data[3]
    config.test_description = func_data[4]
    config.exp_execution_time = str( func_data[5] )

    # Get Access detials from SDK
    test_input = test_input.replace( ";", "," )
    access_token = "fdm90EDqQuKlowfkfZH9SwRIGhcE4UiVP8sdRcIbnwIEPyHe3GgoR4P0lNjxRen6sWLEsQFPpCyh0EBNh2nAWzuiJYFE2lsOT5MelyyIQNAsgL2xbETxriKeU1Z5CKkB"
    example_series_id = test_input
    # print example_series_id

    api_client = ApiClient( header_name="Authorization", header_value=access_token )
    series_api = SeriesApi( api_client=api_client )


    #featch Metadata details for the subscribed Series Id
    series_result = series_api.get_series( id=example_series_id )
   # series_metadata_result = series_api.get_series_metadata( id=example_series_id )
   # print series_result
    actual_xml_file = xml_write( folder_name, series_result.to_dict(), func_data[2] )

    import xml.etree.ElementTree as et

    tree = et.parse(actual_xml_file)
    root = tree.getroot()


    subscribed = []
    unsubscribed = []
    test_input =test_input.split(",")
    # for name in root.findall( ".//item/code"):
    #     unsubscribed.append(name.text)
    for name in root.findall( ".//entity_id"):
        subscribed.append( name.text)

    unsubscribed = list( set( test_input ) - set( subscribed ))
    #print unsubscribed




    result_string = ""
    result_string_unsubscribed =""
    if subscribed == [] :
        result_string = ""
        result_string_unsubscribed =""
        #unsubsription_string

    else:
        for x in subscribed: result_string += x +" ,"
        result_string = result_string[:-1] + "------ Are Subscribed Series"
        for x in unsubscribed : result_string_unsubscribed += x +" ,"
        result_string_unsubscribed = result_string_unsubscribed[:-1] + "------ Are UnSubscribed Series"


    config.tc_result = "PASS"
    config.tc_remark = result_string +"\n"+ result_string_unsubscribed
    print (tc_remark)
    config.bln_critical_error_found = False
    config.bln_sucess = True


