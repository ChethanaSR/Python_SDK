
xml_path = "C:\\Users\\rchethana\\Documents\\SDK_Automation\\XML-ActualData\\Metadata\\2019-07-10\\500_Stage_Perf_Series_verification_001.xml"
csv_path = "C:\\Users\\rchethana\\Documents\\SDK_Automation\\XML-TestData\Metadata\\500_Stage_Perf_Series_verification_001.csv"

import xml.etree.ElementTree as ET
import csv

tree = ET.parse(xml_path)
root = tree.getroot()

sr_code_csv =[]
sr_code_xml =[]
series_id = []

[series_id.append(name.text)for name in root.findall( ".//entity_id" )]
print len(series_id)


f = open( csv_path )
csv_f = csv.reader( f )

for name in root.findall(".//layout/item/series_code"):
    sr_code_xml.append(name.text)
print len(sr_code_xml)
print sr_code_xml

for row in csv_f:
    if row[0] == "SR Code":
        for col in range( 1, len( series_id ) + 1 ): sr_code_csv.append( row[col] )
print sr_code_csv
print len(sr_code_csv)

sr_code_xml_cnt =0
for i in range(len(sr_code_csv)):
    for j in range(len(sr_code_xml)):
        if sr_code_csv[i] == sr_code_xml[j]: sr_code_xml_cnt +=1
print sr_code_xml_cnt

if len(sr_code_csv) == sr_code_xml_cnt:
    print "Pass"








# f = open( csv_path )
# csv_f = csv.reader( f )
# sr_code_csv =[]
#
#
#
# sr_code =[]
# series_id = []
# SR_Code =[]
# series_id_csv =[]
# [series_id.append(name.text)for name in root.findall( ".//entity_id" )]
# print len(series_id)
#
#
# for row in csv_f:
#     if row[0] == "Series ID":
#         for col in range( 1, len( series_id )+1 ):
#             series_id_csv.append( row[col] )
#
#     if row[0] == "SR Code":
#         for col in range( 1, len( series_id )+1 ): sr_code_csv.append( row[col] )
#         break
#
#
#
#
#
# #for i in range(len(sr_code_csv)):print(sr_code_csv[i])
# #
# # xml_list = ["entity_id", "layout/item/series_code"]
# #
# #
# #
# # for i in range (len(series_id)):
# #     if
# i =0
# sr_code = []
# series_code =[]
#
# cnt =0
# for child in root:
#     cnt +=1
#
# print cnt
#     #print(child.tag, child.attrib)
#
# l=1
# j = 0
#
#
#
# for name in root.findall(".//entity_id"):
#     series_id.append(name.text)
# print series_id
#
#
#
# for name in root.findall(".//layout/item/series_code"):
#     sr_code.append(name.text)
# print len(sr_code)
#
#
# i = 0
# srCnt = 0
# for id in range(len(sr_code_csv)):
#     if sr_code[id] == sr_code_csv[i]: srCnt += 1
#     else: i+=1
# print srCnt
# print len(sr_code_csv)
#
# # for name in root.findall( ".//entity_id" ):
# #     if series_id[i] == name.text:
# #         j += 1
# #         i +=1
# #         #print (".//item["+str(l)+"]/item["+str(i)+"]/layout/item/series_code")
# #         for series_code_xml in root.findall(".//item["+str(l)+"]/data/item["+str(j)+"]/layout/item/series_code"):
# #             sr_code.append(series_code_xml.text)
# #             #print(sr_code)
# #             if i%100 == 0 :
# #                 l += 1
# #                 j =1
# #                 print(l)
# #                 print (".//item[" + str( l ) + "]/item[" + str( i ) + "]/layout/item/series_code")
# #                 #print(series_code)
# #
# #         print sr_code
# #
# #         series_code.append( sr_code )
# #         sr_code =[]
# #         #print series_code
# #
# # for i in range(len(series_code)):
# #     print( series_code[i])
# #
# # # print (len(series_code), len(series_id))
# # # for i in range (len(series_id)):
# # #     print series_code[i]
# #
# #
# # print sr_code_csv[0]
# #
# #
# # error_result = []
# # for i in range( len( series_id ) ):
# #     for j in range( len( series_id ) ):
# #         if series_id_csv[i].find( series_id[j] ) >= 0:
# #             sr_cnt = 0
# #             for k in range(len(series_code[j])):
# #                 if sr_code_csv[i] == series_code[j][k]:
# #                     sr_cnt +=1
# #             if sr_cnt != 1:
# #                 error_result.append("SR Code is (" + sr_code_csv[i] + ')is not exists for series id' + series_id[j] + " " )
# # #
# # #
# # #
# # print (error_result)
# # #
#
