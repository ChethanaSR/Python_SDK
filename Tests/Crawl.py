import os
import openpyxl
import time
import dicttoxml
from datetime import datetime
from xmldiff import main
import pandas
import csv
import xml.etree.ElementTree as et
from dateutil.parser import parse


def xml_csv_comp_filter_for_timepoint():

    #csv_file = "C:\\Users\\rchethana\\Documents\\SDK_Automation\\XML-TestData\\Keyword_SeriesID\\386599657,210461702,117868108,384678537,118117308.csv"
    xml_file = ":\\Users\\rchethana\\Documents\\SDK_Automation\\XML-ActualData\\Keyword_SeriesID\\2019-05-28,12-23-09 PM\\2019-05-28,12-23-09 PM.xml"
    series_id = []

    tree = et.parse( xml_file )
    root = tree.getroot()
    series = root.findall( ".//entity_id" )
    for id in range (len(series)):
        series_id.append(series[id].text)
    print series_id

xml_csv_comp_filter_for_timepoint()

    # verifyoption = "No. of Obs"
    # series = root.findall( ".//entity_id" )
    #
    #
    #
    #
    # series_date =[]
    # series_value = []
    # series_id_cvs = []
    # I = 1
    # for id in range (len(series)):
    #     filterdate = []
    #     filetrvalue = []
    #     date = root.findall( ".//item[" +str(I)+ "]/time_points/item/date" )
    #     value = root.findall( ".//item["+str(I)+"]/time_points/item/value" )
    #     year_in_date = datetime.strptime( date[id].text, '%Y-%m-%d' ).year
    #     series_id.append( series[id].text )
    #     with open(csv_file ) as csvfile:
    #         readCSV = csv.reader( csvfile, delimiter=',' )
    #         for row in readCSV:
    #             if row[0] == "Series ID":
    #                 for num in range( 1, len( series ) + 1 ): series_id_cvs.append( row[num] )
    #
    #             if row[0]== str(year_in_date) and series_id_cvs[id]== series[id].text:
    #                 print value[id].text