import datetime

from ceic_api_client.api_client import ApiClient
from ceic_api_client.apis.dictionary_api import DictionaryApi
from ceic_api_client.apis.series_api import SeriesApi
from ceic_api_client.apis.insights_api import InsightsApi


import string
xmltext ={'data': [{'entity_id': '310901801',
           'layout': [{u'database': {u'id': u'GLOBAL',
                                     u'name': u'Global Database'},
                       u'section': {u'id': u'SC88033',
                                    u'name': u'CDM Automation Test Data'},
                       u'seriesCode': u'SR4825071',
                       u'table': {u'id': u'TB88034',
                                  u'name': u'Automation Static Test Data \u2013 not for update\u2019'},
                       u'topic': {u'id': u'TP70212',
                                  u'name': u'Z-Testing Topic(IT-use only)'}}],
           'metadata': {'classification': None,
                        'country': {'id': 'YY', 'name': 'Test'},
                        'end_date': datetime.date(2012, 12, 1),
                        'frequency': {'id': 'Y', 'name': 'Yearly'},
                        'id': 310901801,
                        'indicator': None,
                        'key_series': False,
                        'last_change': {'is_infinity': False,
                                        'is_opposite': False,
                                        'value': -91},
                        'last_update_time': datetime.datetime(2014, 5, 22, 10, 8, 46),
                        'last_value': 866666,
                        'multiplier_code': 'MN',
                        'name': 'Govt Revenue',
                        'new_series': False,
                        'number_of_observations': 63,
                        'period_end': 12,
                        'province': None,
                        'source': {'country_id': None,
                                   'id': 'YY-TEST',
                                   'name': 'NRT SOURCE TEST'},
                        'start_date': datetime.date(1950, 12, 1),
                        'status': {'id': 'T', 'name': 'Active'},
                        'unit': {'id': '20039', 'name': 'RMB mn'}},
           'subscribed': None,
           'time_points': None,
           'ui': None},
          {'entity_id': '310901701',
           'layout': [{u'database': {u'id': u'GLOBAL',
                                     u'name': u'Global Database'},
                       u'section': {u'id': u'SC88033',
                                    u'name': u'CDM Automation Test Data'},
                       u'seriesCode': u'SR4825055',
                       u'table': {u'id': u'TB88034',
                                  u'name': u'Automation Static Test Data \u2013 not for update\u2019'},
                       u'topic': {u'id': u'TP70212',
                                  u'name': u'Z-Testing Topic(IT-use only)'}}],
           'metadata': {'classification': None,
                        'country': {'id': 'YY', 'name': 'Test'},
                        'end_date': datetime.date(2011, 12, 1),
                        'frequency': {'id': 'Y', 'name': 'Yearly'},
                        'id': 310901701,
                        'indicator': None,
                        'key_series': False,
                        'last_change': {'is_infinity': False,
                                        'is_opposite': False,
                                        'value': -17},
                        'last_update_time': datetime.datetime(2014, 5, 22, 10, 8, 46),
                        'last_value': 1667,
                        'multiplier_code': 'MN',
                        'name': 'Govt Revenue - Tax ; Individual Income',
                        'new_series': False,
                        'number_of_observations': 14,
                        'period_end': 12,
                        'province': None,
                        'source': {'country_id': None,
                                   'id': 'YY-TEST',
                                   'name': 'NRT SOURCE TEST'},
                        'start_date': datetime.date(1998, 12, 1),
                        'status': {'id': 'T', 'name': 'Active'},
                        'unit': {'id': '20039', 'name': 'RMB mn'}},
           'subscribed': None,
           'time_points': None,
           'ui': None}],
 'errors': None}



#print dict(str(xmltext))
# import six
#
# def to_dict1(object ):
#     """Returns the model properties as a dict"""
#     result = {}
#
#     for attr, _ in six.iteritems( object.swagger_types ):
#         value = getattr( object, attr )
#         if isinstance( value, list ):
#             result[attr] = list( map( lambda x: x.to_dict() if hasattr( x, "to_dict" ) else x, value ) )
#         elif hasattr( value, "to_dict" ):
#             result[attr] = value.to_dict()
#         elif isinstance( value, dict ):
#             result[attr] = dict(
#                 map( lambda item: (item[0], item[1].to_dict()) if hasattr( item[1], "to_dict" ) else item,
#                     value.items() ) )
#         else:
#             result[attr] = value
#
#     return result
#
# result = to_dict1(str(xmltext))
# print(result)
#
#
# # #ceic_api_client.models.series_result.SeriesResult.to_dict(text)
# #
# # my_text = str(text)
# #
# # print type(dict(my_text))
# #
import ast
result = ast.literal_eval(str(xmltext))
print result



# #
# # import re
# #
# # d = re.sub(r'datetime\.datetime\(([^)]*)\)', r'[\1]', str(text))
# # print d
# # date1 = datetime.datetime(*d['last_update_time'])
# # print date1
# #
# #
# # f= open ("C:\\Users\\rchethana\\Desktop\\text_dic.txt", "w")
# # f.write(d )
# # f.close()
#
#
# f = open ("C:\\Users\\rchethana\\Desktop\\text_dic.txt", "r")
# content = f.read()
#
# #import ast
#
# #result = ast.literal_eval(content)
#
#
# #print content