# import pandas
# import csv
# import xml.etree.ElementTree as et
# from dateutil.parser import parse
# from Common import config
#
# #xml_file = "C:\\Users\\rchethana\\Desktop\\359379947.xml"
# xml_file =  "C:\\Users\\rchethana\\Documents\\SDK_Automation\\XML-TestData\Metadata\\2019-02-25,04-50-38 PM\\2019-02-25,04-50-38 PM.xml"
# #xml_file =  config.xml_td_path + "\\" + "Metadata" + "\\"
# tree = et.parse(xml_file)
# root = tree.getroot()
#
#
# series_id =[]
# status = []
# series_code= []
# last_update_time =[]
# end_date = []
# start_date =[]
# country = []
# number_obs = []
# source = []
# frequency = []
# unit= []
#
#
#
#
# xml_list = ["entity_id", "item[1]/seriesCode","status/name","last_update_time", "end_date","country/name", "number_of_observations", "start_date", "source/name", "frequency/name", "unit/name" ]
#
#
# for i in range (len(xml_list)):
#     for name in root.findall(".//"+ str(xml_list[i])):
#         if xml_list[i] == "entity_id":series_id.append( name.text )
#         elif xml_list[i] == "item[1]/seriesCode" : series_code.append( name.text )
#         elif xml_list[i] == "status/name": status.append(name.text)
#         elif xml_list[i] == "last_update_time": last_update_time.append(name.text)
#         elif xml_list[i] == "end_date": end_date.append(name.text)
#         elif xml_list[i] == "country/name": country.append(name.text)
#         elif xml_list[i] == "number_of_observations":number_obs.append(name.text)
#         elif xml_list[i] == "start_date": start_date.append(name.text)
#         elif xml_list[i] == "source/name": source.append(name.text)
#         elif xml_list[i] == "frequency/name": frequency.append(name.text)
#         elif xml_list[i] == "unit/name": unit.append(name.text)
#
#
#
# csv_file = 'C:\\Users\\rchethana\\Desktop\\Chethana.csv'
# df = pandas.read_csv(csv_file)
# row_count = sum(1 for line in open(csv_file))
# country_cnt = frequency_cnt = unit_cnt = source_cnt = status_cnt = series_id_cnt = series_code_cnt = number_obs_cnt = last_update_time_cnt =  0
# start_date_cnt = end_date_cnt = 0
# for i in range (len(series_id)):
#     for j in range(row_count-1):
#         key = str(df['Series_Key'][j])
#         if key == "Region" and  df[series_id[i]][j]  ==  country[i]: country_cnt += 1
#         if key == "Frequency" and df[series_id[i]][j] == frequency[i]: frequency_cnt +=1
#         if key == "Unit" and df[series_id[i]][j] == unit[i]: unit_cnt +=1
#         if key == "Source" and df[series_id[i]][j] == source[i]: source_cnt +=1
#         if key == "Status" and df[series_id[i]][j] == status[i]:  status_cnt +=1
#         if key == "Series ID" and series_id[i] in df[series_id[i]][j]:series_id_cnt +=1
#         if key == "SR Code" and df[series_id[i]][j]  == series_code[i]: series_code_cnt += 1
#         if key == "No. of Obs" and df[series_id[i]][j]  == number_obs[i]:  number_obs_cnt += 1
#         if key == "Last Update Time":
#             num = last_update_time[i].find( "T" )
#             datestring = parse( last_update_time[i][:num] )
#             datestring = datestring.strftime( '%d/%m/%Y' )
#             if df[series_id[i]][j]  == datestring: last_update_time_cnt += 1
#         if key == "First Obs. Date":
#             datestring = parse( start_date[i] )
#             datestring = datestring.strftime( '%b-%y' )
#             if df[series_id[i]][j] == datestring : start_date_cnt += 1
#         if key == "Last Obs. Date":
#             datestring = parse( end_date[i] )
#             datestring = datestring.strftime( '%b-%y' )
#             if df[series_id[i]][j] == datestring: end_date_cnt += 1
#
#
#
#
# print (country_cnt, frequency_cnt, unit_cnt , source_cnt , status_cnt , series_id_cnt , series_code_cnt , number_obs_cnt, last_update_time_cnt, \
#        start_date_cnt, end_date_cnt)



















#megha_list = [series_id, status,series_code, last_update_time, end_date, start_date, country, number_obs , source, frequency, unit]

#for list in range(len(megha_list)):
 #    print megha_list[list]


# for i in range(len(last_update_time)):
#     #num = start_date[i].find("T")
#     #datestring = last_update_time[i][:num]
#     #)
#
#     dt = parse(start_date[i])
#     dt = dt.strftime( '%d-%b-%y' )
#     print dt



#megha_list = [series_id, status,series_code, last_update_time, end_date, start_date, country, number_obs , source, frequency]

# for list in range(len(megha_list)):
#      print megha_list[list]







#
# r
# for val in range(row_count-1):
#     key = str((df['Header'][val]))
#     key_element = ".//item/metadata/" + key + "/"
#     #print key_element
#     for name in root.findall(".//item/metadata/status/"):
#         print name.tag, name.text
#         print str(df['Values'][val])
#    print(name.tag , name.text )
   # print(str((df['Header'][val])) + ':' + (str(df['Values'][val])))

import csv

#Import Packages
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

def xml_csv_comp():
    path = "C:\\Users\\rchethana\\Desktop\\100_Series_Verification-001.csv"
    filename = "C:\\Users\\rchethana\\Desktop\\100_Series_Verification-001.xml"


    tree = et.parse( filename )
    root = tree.getroot()

    region_xml = []
    frequency_xml = []
    unit_xml = []
    source_xml = []
    status_xml = []
    series_id_xml = []
    sr_code_xml = []
    first_obs_date_xml = []
    last_obs_date_xml = []
    no_of_obs_xml =[]

    xml_list = ["entity_id", "layout/item[1]/series_code", "status/name", "last_update_time", "end_date", "country/name",
                "number_of_observations", "start_date", "source/name", "frequency/name", "unit/name"]

    for i in range( len( xml_list ) ):
        for name in root.findall( ".//" + str( xml_list[i] ) ):
            if xml_list[i] == "entity_id": series_id_xml.append( name.text )
            elif xml_list[i] == "layout/item[1]/series_code": sr_code_xml.append( name.text )
            elif xml_list[i] == "status/name":status_xml.append( name.text )
            elif xml_list[i] == "end_date": last_obs_date_xml.append( name.text )
            elif xml_list[i] == "country/name": region_xml.append( name.text )
            elif xml_list[i] == "number_of_observations":no_of_obs_xml.append( name.text )
            elif xml_list[i] == "start_date":first_obs_date_xml.append( name.text )
            elif xml_list[i] == "source/name":source_xml.append( name.text )
            elif xml_list[i] == "frequency/name":frequency_xml.append( name.text )
            elif xml_list[i] == "unit/name":unit_xml.append( name.text )



    #csv file reading
    f = open(path)
    csv_f = csv.reader(f)





    region_csv =[]
    frequency_csv =[]
    unit_csv =[]
    source_csv =[]
    status_csv =[]
    series_id_csv =[]
    sr_code_csv =[]
    first_obs_date_csv =[]
    last_obs_date_csv =[]
    no_of_obs_csv =[]

    blnregon = blnfrequency =  blnunit = blnsource= blnstatus = blnseries_id = blnsr_code= False
    blnfirst_obs_date = blnlast_obs_date = blnno_of_obs=  False

    region_cnt = frequency_cnt = unit_cnt = source_cnt = status_cnt = series_id_cnt = sr_code_cnt = 0
    first_obs_date_cnt = last_obs_date_cnt = no_of_obs_cnt = 0
    for row in csv_f:
        if row[0]== "Region":
            for col in  range(1, len(region_xml)+1):region_csv.append(row[col])
        if row[0]== "Frequency":
            for col in  range(1, len(region_xml)+1):frequency_csv.append(row[col])
        if row[0]== "Unit":
            for col in  range(1, len(region_xml)+1):unit_csv.append(row[col])
        if row[0]== "Source":
            for col in  range(1, len(region_xml)+1):source_csv.append(row[col])
        if row[0]== "Status":
            for col in  range(1, len(region_xml)+1):status_csv.append(row[col])
        if row[0]== "Series ID":
            for col in  range(1, len(region_xml)+1):series_id_csv.append(row[col])
        if row[0]== "SR Code":
            for col in  range(1, len(region_xml)+1):sr_code_csv.append(row[col])
        if row[0]== "First Obs. Date":
            for col in  range(1, len(region_xml)+1):first_obs_date_csv.append(str(row[col]))
        if row[0]== "Last Obs. Date":
            for col in  range(1, len(region_xml)+1):last_obs_date_csv.append(str(row[col]))
            break
        # if row[0]== "No. of Obs":
        #     for col in  range(1, len(region_xml)+1):no_of_obs_csv.append(str(row[col]))
        #     break



    # for i in range( len( region_xml)):
    #     for j in range( len(region_xml) ):
    #         if series_id_csv[i].find( series_id_xml[j] ) >= 0 and region_csv[i] == region_xml[j]:region_cnt += 1
    #
    #            # break




    error_result = []
    #for i in range( len( region_xml ) ):
    for i in range(len(region_xml)):
        for j in range( len(region_xml) ):
            if series_id_csv[i].find( series_id_xml[j] ) >= 0:
                if region_csv[i] != region_xml[j]: error_result.append("Region ("+ region_xml[j] +')is mismatched for series  Id' + series_id_xml[j])
                if unit_csv[i] != unit_xml[j]:     error_result.append("Unit ("+ unit_xml[j] +')is mismatched for series Id ' + series_id_xml[j])
                if source_csv[i] != source_xml[j]: error_result.append("Source ("+ source_xml[j] +')is mismatched for series Id ' + series_id_xml[j])
                if status_csv[i] != status_xml[j]: error_result.append("Status ("+ status_xml[j] +')is mismatched for series Id ' + series_id_xml[j])
                if series_id_csv[i].find( series_id_xml[j] ) < 0 : error_result.append("Series_ID ("+ series_id_xml[j] +')is mismatched for series Id ' + series_id_xml[j])
                if sr_code_csv[i] != sr_code_xml[j]: error_result.append("SR Code is ("+ sr_code_xml[j] +')is mismatched for series Id ' + series_id_xml[j])

                required_date = first_obs_date_xml[j]
                required_date = required_date.split("-")
                obtained_date = str( required_date[1] + "/" + required_date[0] )
                obtained_date1 = str( required_date[2] + "/" + required_date[1] + "/" + required_date[0] )
                obtained_date2 = str( required_date[0] )
                if (first_obs_date_csv[i] == obtained_date) \
                or (first_obs_date_csv[i] == obtained_date1) \
                or (first_obs_date_csv[i] == obtained_date2): first_obs_date_cnt += 1




                required_date = last_obs_date_xml[j]
                required_date = required_date.split( "-" )
                obtained_date = str( required_date[1] + "/" + required_date[0] )
                obtained_date1 = str( required_date[2] + "/" + required_date[1] + "/" + required_date[0] )
                obtained_date2 = str( required_date[0] )
                if (last_obs_date_csv[i] == obtained_date) \
                or (last_obs_date_csv[i] == obtained_date1) \
                or (last_obs_date_csv[i] == obtained_date2): last_obs_date_cnt += 1




                if frequency_csv[j].find( "Annual" ) > 0 and frequency_xml[i] == 'Yearly': frequency_cnt += 1
                elif frequency_csv[j].find("Monthly") > 0 and frequency_xml[i] == 'Monthly' : frequency_cnt += 1
                elif frequency_csv[j].find("Quarterly") >0  and frequency_xml[i] == 'Quarterly' : frequency_cnt += 1
                elif frequency_csv[j].find("Weekly") > 0  and frequency_xml[i] == 'Weekly' : frequency_cnt += 1
                elif frequency_csv[j].find("Daily") > 0  and frequency_xml[i] == 'Daily':frequency_cnt += 1


    if frequency_cnt  != len( series_id_xml ): error_result.append("Frequency ("+ frequency_xml[j] +')is mismatched for series Id ' + series_id_xml[j])
    if first_obs_date_cnt != len( series_id_xml ): \
            error_result.append("First Obs.Date (" + first_obs_date_xml[j] + ')is mismatched for series Id ' + series_id_xml[j] )
    if last_obs_date_cnt != len( series_id_xml ): \
            error_result.append("Lirst Obs.Date is =" + last_obs_date_xml[j] + ' mismatched for series Id ' + series_id_xml[j] )

    # print "region_cnt =" + str(region_cnt)
    # #print "frequency_cnt =" + str(frequency_cnt)
    # print "unit_cnt =" + str(unit_cnt)
    # print "source_cnt =" + str(source_cnt)
    # print "status_cnt =" + str(status_cnt)
    # print "series_id_cnt =" + str(series_id_cnt)
    # print "sr_code_cnt =" + str(sr_code_cnt)
    # print "first_obs_date_cnt =" + str(first_obs_date_cnt)
    # print "last_obs_date_cnt =" + str(last_obs_date_cnt)
    # print "no_of_obs_cnt =" + str(no_of_obs_cnt)



    # if region_cnt == len( series_id_xml ):blnregion = True
    # if frequency_cnt  == len( series_id_xml ): blnfrequency = True
    # if unit_cnt  == len( series_id_xml ): blnunit = True
    # if source_cnt  == len( series_id_xml ): blnsource = True
    # if status_cnt  == len( series_id_xml ): blnstatus  = True
    # if series_id_cnt  == len( series_id_xml ): blnseries_id = True
    # if sr_code_cnt  == len( series_id_xml ): blnsr_code = True
    # if first_obs_date_cnt  == len( series_id_xml): blnfirst_obs_date = True
    # if last_obs_date_cnt  == len( series_id_xml ): blnlast_obs_date= True
    # if no_of_obs_cnt  == len( series_id_xml ): blnno_of_obs = True

    # if blnregion==blnfrequency==blnunit==blnsource==blnstatus==blnseries_id==blnsr_code==blnfirst_obs_date==blnlast_obs_date==blnno_of_obs== True:
    if error_result == []: return True
    else: return error_result
    #return True if error_result == [] else return error_result




print  xml_csv_comp()









