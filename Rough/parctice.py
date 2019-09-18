# import dicttoxml
# import pprint
# import ast
# import os
# from Common.config import  *
#
# import datetime
# import time
# import re
# import json
#
# text = {'data': [{'entity_id': '310901801',
#            'layout': [{u'database': {u'id': u'GLOBAL',
#                                      u'name': u'Global Database'},
#                        u'section': {u'id': u'SC88033',
#                                     u'name': u'CDM Automation Test Data'},
#                        u'seriesCode': u'SR4825071',
#                        u'table': {u'id': u'TB88034',
#                                   u'name': u'Automation Static Test Data \u2013 not for update\u2019'},
#                        u'topic': {u'id': u'TP70212',
#                                   u'name': u'Z-Testing Topic(IT-use only)'}}],
#            'metadata': {'classification': None,
#                         'country': {'id': 'YY', 'name': 'Test'},
#                         'end_date': datetime.date(2012, 12, 1),
#                         'frequency': {'id': 'Y', 'name': 'Yearly'},
#                         'id': 310901801,
#                         'indicator': None,
#                         'key_series': False,
#                         'last_change': {'is_infinity': False,
#                                         'is_opposite': False,
#                                         'value': -91},
#                         'last_update_time': datetime.datetime(2014, 5, 22, 10, 8, 46),
#                         'last_value': 866666,
#                         'multiplier_code': 'MN',
#                         'name': 'Govt Revenue',
#                         'new_series': False,
#                         'number_of_observations': 63,
#                         'period_end': 12,
#                         'province': None,
#                         'source': {'country_id': None,
#                                    'id': 'YY-TEST',
#                                    'name': 'NRT SOURCE TEST'},
#                         'start_date': datetime.date(1950, 12, 1),
#                         'status': {'id': 'T', 'name': 'Active'},
#                         'unit': {'id': '20039', 'name': 'RMB mn'}},
#            'subscribed': None,
#            'time_points': None,
#            'ui': None},
#           {'entity_id': '310901701',
#            'layout': [{u'database': {u'id': u'GLOBAL',
#                                      u'name': u'Global Database'},
#                        u'section': {u'id': u'SC88033',
#                                     u'name': u'CDM Automation Test Data'},
#                        u'seriesCode': u'SR4825055',
#                        u'table': {u'id': u'TB88034',
#                                   u'name': u'Automation Static Test Data \u2013 not for update\u2019'},
#                        u'topic': {u'id': u'TP70212',
#                                   u'name': u'Z-Testing Topic(IT-use only)'}}],
#            'metadata': {'classification': None,
#                         'country': {'id': 'YY', 'name': 'Test'},
#                         'end_date': datetime.date(2011, 12, 1),
#                         'frequency': {'id': 'Y', 'name': 'Yearly'},
#                         'id': 310901701,
#                         'indicator': None,
#                         'key_series': False,
#                         'last_change': {'is_infinity': False,
#                                         'is_opposite': False,
#                                         'value': -17},
#                         'last_update_time': datetime.datetime(2014, 5, 22, 10, 8, 46),
#                         'last_value': 1667,
#                         'multiplier_code': 'MN',
#                         'name': 'Govt Revenue - Tax ; Individual Income',
#                         'new_series': False,
#                         'number_of_observations': 14,
#                         'period_end': 12,
#                         'province': None,
#                         'source': {'country_id': None,
#                                    'id': 'YY-TEST',
#                                    'name': 'NRT SOURCE TEST'},
#                         'start_date': datetime.date(1998, 12, 1),
#                         'status': {'id': 'T', 'name': 'Active'},
#                         'unit': {'id': '20039', 'name': 'RMB mn'}},
#            'subscribed': None,
#            'time_points': None,
#            'ui': None}],
#  'errors': None}
#
# #print type(text)
#
# #xml_data = dicttoxml.dicttoxml(text, attr_type=False, root=True )
#
# #print str(text)
#
# # f = open('C:\\Users\\rchethana\\Desktop\\replace.txt', 'r')
# # content = f.read()
# # #print content
# # string = ", ".join(x.strftime("%d/%m/%Y") for x in content)
# # print string
#
# #for word in f:
#
#    #print word
#     #if word.find('last_update_time') > 0:
#      #  print word
#
#
#
#
#
#
# #my_string = '2014-5-22 10:8:46'
# #print datetime.datetime.strptime(my_string, '%Y,%m,%d, %H,%M,%S')
#
#
#
# # from ast import literal_eval
# # python_dict = literal_eval(str(text))
# # print type(python_dict)
# #
# # #def done(self, request, form_list):
# #   #  model_form, field_form = form_list query = SortedDict() for field_name in field_form.fields: app, model, field = field_name.split('') name = '%s__%s' % (model, field) value = field_form.cleaned_data[field_name] #print value if value or value == 0: query[name] = value print value query['data_model_name'] = [model.split('')[1] for model in field_form.model_list] Model_name.objects.create(name=model_form.cleaned_data['report_name'],query=query)
# #
# #
# #
# # # #ast.literal_eval(text)
# # # #folder_name = "Metadata"
# # # def xml_write(folder_name, text):
# # #     # xml = dicttoxml.dicttoxml(text )
# # #     xml_data = dicttoxml.dicttoxml(text, attr_type=False, root=True )
# # #     path = os.environ['USERPROFILE'] + "\\Documents\\SDK_Automation\\XML-ActualData" +"\\" + folder_name + "\\" + datetime.datetime.now().strftime("%Y-%m-%d" + "," + "%I-%M-%S %p")+ ".xml"
# # #     print path
# # #     # "C:\Users\rchethana\Desktop\dictoxml.xml"
# # #     f = open(path, 'w' )
# #     f.write( xml_data )
# #     f.close()
# #
# # def my_function(text):
# #     print text
# #     xml_write("Metadata", text)
# #
# #
# # my_function(text)
# #import os
#
# #f = open (os.environ['USERPROFILE'] + "\\Documents\\SDK_Automation\\XML-ActualData\\practice.txt", "w+")
#
#
#
#
# #s = """{
# #     "motion_measure": {"INCAR": 69, "RANDOM": 63, "UNKNOWN": 62, "BIKING": 57, "WALKING": 48, "RUNNING": 41, "SEDENTARY": 0},
# #     "samples": [0, 1.1791444, 11.036073],
# #     "record_time": datetime.datetime(2018, 3, 26, 10, 3, 17, 441000),
# #     "another_time": datetime.datetime(2017, 3, 26, 10, 3)
# #     }"""
# # #My_String = str(s)
# # #print My_String
# #
# # # re.sub to replace datetime; json.loads to convert to dict
# # #d = re.sub(r'datetime\.datetime\(([^)]*)\)', r'[\1]', text)
# # #print (d)
#
# #import ast
#
# #result = ast.literal_eval(d)
# #assert type(result) is dict
#
# #xml = dicttoxml.dicttoxml(d)
# # xml = dicttoxml.dicttoxml(d,attr_type=False,root=True)
# # #"C:\Users\rchethana\Desktop\dictoxml.xml"
# # f = open('C:\\Users\\rchethana\\Desktop\\dictoxml1.xml','w')
# # f.write(xml)
# # f.close()
# # print d
#
# # datetime.datetime(...) to work with resulting datetime lists
# #date1 = datetime.datetime(*d['last_update_time'])
# #date2 = datetime.datetime(*d['another_time'])
# #print date1
# #print date2
#
# #Function to create a folder
# from datetime import datetime
# print xml_ad_path
# today = datetime.now()
# path = xml_ad_path +"\\" + "Metadata" + "\\"+ today.strftime("%Y-%m-%d" + "," + "%I-%M-%S %p")
# os.mkdir(path)
# print path
# actual_xml_path = path + "\\"+ today.strftime("%Y-%m-%d" + "," + "%I-%M-%S %p")+ ".xml"
#
# #os.mkdir(path)
#
# from datetime import datetime
# import
# #bvnb

abc = "dfd"








AccountXpath = "//div[@class='user-avatar -default -small']" \
               ""
SignoutXpath = "//a/span[contains(text(),'Sign out')]"


