# import lxml.etree
# import lxml.builder
# import xlrd
# from lxml import etree
#
# wb = xlrd.open_workbook("C:\\Users\\rchethana\\Desktop\\Test Series_excel_file.xlsx")
#
#
# root = etree.Element('network')
# root.set('name', 'Network')
# tree = etree.ElementTree(root)
# name = etree.Element('nodes')
# root.append(name)
# wb = xlrd.open_workbook("C:\\Users\\rchethana\\Desktop\\Test Series_excel_file.xlsx")
# sh = wb.sheet_by_index(0)
#
# for row in range(1, sh.nrows):
#     val = sh.row_values(row)
#     element = etree.SubElement(name, 'node')
#     element.set('id', str(val[0]))
#     element.set('x', str(val[1]))
#     #element.set('y', str(val[2]))
# print etree.tostring(root,pretty_print=False)


#import pandas
#df = pandas.read_excel("C:\\Users\\rchethana\\Desktop\\Test Series_excel_file.xlsx")
#print len(df)

import xml.etree.ElementTree as ET
#import arcpy

xmlfile = 'D:/Working/Test/Test.xml'
element_tree = ET.parse(xmlfile)
root = element_tree.getroot()
agreement = root.find(".//agreementid").text
arcpy.AddMessage(agreement)