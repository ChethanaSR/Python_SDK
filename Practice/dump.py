import os
import xml.etree.ElementTree as et


xml_file = "C:\\Users\\rchethana\\Documents\\SDK_Automation\\XML-TestData\\Metadata\\359379947.xml"
tree = et.parse(xml_file)
root = tree.getroot()

#for child in root:
 #   print (child.tag, child.attrib)

#for child in root:
 #   for element in child:
  #      for items in element:
   #         if items.tag == 'metadata':
    #            for item in items:
     #               print (item.tag, item.text)

# data = et.Element('metadata')
# items = et.SubElement(data, 'items')
# item1 = et.SubElement(items, 'item')
# item2 = et.SubElement(items, 'item')
# item1.set('name','item1')
# item2.set('name','item2')
# print(item1.text)
# print(item2.text)

#for name in root.findall(".//item/metadata/status/"):
#    print(name.tag , name.text )

# from xml.etree.ElementTree import Element, SubElement, Comment, tostring
# import pprint
#
# top = Element('root')
#
# comment = Comment('Generated for PyMOTW')d
# top.append(comment)
#
# child = SubElement(top, 'child')
# child.text = 'This child contains text.'
#
# child_with_tail = SubElement(top, 'child_with_tail')
# child_with_tail.text = 'This child has regular text.'
# child_with_tail.tail = 'And "tail" text.'
#
# child_with_entity_ref = SubElement(top, 'child_with_entity_ref')
# child_with_entity_ref.text = 'This & that'
#
# f = open( "C:\\Users\\rchethana\\Desktop\\xml_writing.xml", 'w' )
# f.write(tostring(top) )
# f.close()
#
#
#print()


# import pandas
# df = pandas.read_csv('C:\\Users\\rchethana\\Desktop\\Insight 374.csv')
#
# print(df[' '][0])




import csv
import datetime


my_dict ={'entity_id': '359379947',
           'layout': [{u'database': {u'id': u'GLOBAL',
                                     u'name': u'Global Database'},
                       u'section': {u'id': u'SC2225117',
                                    u'name': u'\u6851\u5854\u523a\u72b6\u89e6\u53d1\u5668\u6d4b\u8bd5'},
                       u'seriesCode': u'SR85204367',
                       u'table': {u'id': u'TB2225127',
                                  u'name': u'\u751f\u4ea7\u6d4b\u8bd5\u53bb1\u91cd\u547d\u540d'},
                       u'topic': {u'id': u'TP70212',
                                  u'name': u'Z-Testing Topic(IT-use only)'}}],
           'metadata': {'classification': None,
                        'country': {'id': 'YY', 'name': 'Test'},
                        'end_date': datetime.date(2028, 12, 1),
                        'frequency': {'id': 'Y', 'name': 'Yearly'},
                        'id': 359379947,
                        'indicator': None,
                        'key_series': True,
                        'last_change': {'is_infinity': False,
                                        'is_opposite': False,
                                        'value': -90},
                        'last_update_time': datetime.datetime(2018, 1, 30, 8, 19, 36, ),
                        'last_value': 100,
                        'multiplier_code': 'NA',
                        'name': 'Testing1',
                        'new_series': False,
                        'number_of_observations': 14,
                        'period_end': 12,
                        'province': None,
                        'source': {'country_id': None,
                                   'id': '13962217',
                                   'name': 'CDM PROD TEST'},
                        'start_date': datetime.date(2010, 12, 1),
                        'status': {'id': 'T', 'name': 'Active'},
                        'unit': {'id': '99999', 'name': 'YYY'}},
           'subscribed': None,
           'time_points': None,
           'ui': None}


#with open('C:\\Users\\rchethana\\Desktop\\mycsvfile.csv', 'wb') as f:  # Just use 'w' mode in 3.x
 #   w = csv.DictWriter(f, my_dict.keys())
  #  w.writeheader()
   # w.writerow(my_dict)

my_dict = {'last_update_time': datetime.datetime(2018, 1, 30, 8, 19, 36), 'province': None, 'indicator': None, 'last_value': 100, 'end_date': datetime.date(2028, 12, 1), 'classification': None, 'country': {'id': 'YY', 'name': 'Test'}, 'number_of_observations': 14, 'name': 'Testing1', 'multiplier_code': 'NA', 'source': {'country_id': None, 'id': '13962217', 'name': 'CDM PROD TEST'}, 'frequency': {'id': 'Y', 'name': 'Yearly'}, 'status': {'id': 'T', 'name': 'Active'}, 'start_date': datetime.date(2010, 12, 1), 'period_end': 12, 'new_series': False, 'last_change': {'is_infinity': False, 'is_opposite': False, 'value': -90}, 'id': 359379947, 'unit': {'id': '99999', 'name': 'YYY'}, 'key_series': True}

with open( 'C:\\Users\\rchethana\\Desktop\\mycsvfile1.csv', 'wb' ) as f:
        w = csv.writer( f )
        w.writerow( my_dict.keys() )
        w.writerow( my_dict.values() )