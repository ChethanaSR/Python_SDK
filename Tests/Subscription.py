from ceic_api_client.api_client import ApiClient
from ceic_api_client.apis.dictionary_api import DictionaryApi
from ceic_api_client.apis.series_api import SeriesApi
from ceic_api_client.apis.insights_api import InsightsApi
from Common.config import *
import xml.etree.ElementTree as et

access_token = "fdm90EDqQuKlowfkfZH9SwRIGhcE4UiVP8sdRcIbnwIEPyHe3GgoR4P0lNjxRen6sWLEsQFPpCyh0EBNh2nAWzuiJYFE2lsOT5MelyyIQNAsgL2xbETxriKeU1Z5CKkB"
example_series_id = "104840208,366482857,178652402,178651402,104840708,338153901,338154101,338154301,338154901,338155101,338155301,338155501,338155701,338155901,387635397,338156101"

api_client = ApiClient( header_name="Authorization", header_value=access_token )
series_api = SeriesApi( api_client=api_client )

series_result = series_api.get_series( id=example_series_id)
#print (series_result)

actual_xml_file =  xml_write( "Metadata", series_result.to_dict(),example_series_id )

tree = et.parse("C:\\Users\\rchethana\\Documents\\SDK_Automation\\XML-ActualData\\Metadata\\2019-07-16\\"+example_series_id+".xml" )
root = tree.getroot()
#print


for name in root.findall( ".//item/code"):
    print name.text
for name in root.findall(".//entity_id"):
    print name.text