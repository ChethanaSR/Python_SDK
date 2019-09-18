import csv
import xml.etree.ElementTree as et
from datetime import datetime

csv_file ="C:\\Users\\rchethana\\Documents\\SDK_Automation\\XML-TestData\\Keyword_SeriesID\\TimePoint_Search_001 - Copy.csv"
xml_file ="C:\\Users\\rchethana\\Documents\\SDK_Automation\\XML-ActualData\\Keyword_SeriesID\\2019-07-17\\TimePoint_Search_001.xml"

series_id_xml =[]
time_point_date_xml =[]
time_point_value_xml =[]

tree = et.parse( xml_file )
root = tree.getroot()
for name in root.findall( ".//entity_id" ): series_id_xml.append(name.text)

i=0
time_point_date =[]
time_point_value =[]
for id in root.findall( ".//entity_id" ):
    if series_id_xml[i] == id.text:
        #print ".//item[" +str(i+1)+"/time_points/item/date"
        for name in root.findall (".//item[" +str(i+1)+"]/time_points/item/date"): time_point_date.append(name.text)
        for name in root.findall( ".//item[" + str( i+1 ) + "]/time_points/item/value" ): time_point_value.append(name.text )
        time_point_value_xml.append(time_point_value)
        time_point_date_xml.append(time_point_date)
        time_point_date = []
        time_point_value =[]
        i +=1





series_id_csv =[]
timepoint_date_csv =[]
time_point_vlaue_csv =[]
with open( csv_file ) as f:
    reader = csv.reader( f, delimiter="," )
    for row in reader:
       if row[0]== "Series ID":
           for col in range( 1, len( series_id_xml ) + 1 ): series_id_csv.append( row[col] )



#


# datecnt = 0
#for id in range( len( series_id_xml ) ): series_id_xml.append( series_id_xml[id].text )
for I in range( 1, (len( series_id_xml )+1) ):
    date = root.findall( ".//item[" + str(I) + "]/time_points/item/date" )
    value = root.findall( ".//item["+str(I)+"]/time_points/item/value" )
    print I
    J= K= 0
    for J in range (len(date)):
        year_in_date = datetime.strptime( date[J].text, '%Y-%m-%d' ).year
        with open( csv_file ) as f:
            reader = csv.reader( f, delimiter="," )
            for row in reader:
                if series_id_csv[K] == series_id_xml[I-1]:
                    col = K+1
                    break



            for row in reader:
                if row[0] == str( year_in_date ):
                    if round(float(value[J].text))== round(float(row[col])):
                        blnFalg = True
                        break



#return blnFalg
