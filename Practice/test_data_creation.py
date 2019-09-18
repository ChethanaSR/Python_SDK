import datetime
from dateutil.tz import tzutc
import dicttoxml
from datetime import datetime

from ceic_api_client.api_client import ApiClient
from ceic_api_client.apis.dictionary_api import DictionaryApi
from ceic_api_client.apis.series_api import SeriesApi
from ceic_api_client.apis.insights_api import InsightsApi

from ceic_api_client.api_client import ApiClient
from ceic_api_client.apis.dictionary_api import DictionaryApi
from ceic_api_client.apis.series_api import SeriesApi
from ceic_api_client.apis.insights_api import InsightsApi
from Common.config import *

access_token ="OrgKdLWRj2tHZcS3IoHih9SPLCqSoL9aP4vs6ZzFrzxTyQRZPRX7VCgwDVTP0Cnnn9V89NeQnRbu2IgWn8gHTd0YcnZxz93JoSSrqLWEBjftboESI81mAEiKwL8cuSFe"
example_series_id = "93881901,374588957,367538337,357527477,374586067"


api_client = ApiClient(header_name="Authorization", header_value=access_token)
series_api = SeriesApi(api_client=api_client)

#series_result = series_api.get_series(id=example_series_id)
#series_metadata_result = series_api.get_series_metadata(id=example_series_id)
series_metadata_result = series_api.get_series_metadata( id=example_series_id )

#print(series_metadata_result)

xml_data = dicttoxml.dicttoxml( series_metadata_result.to_dict(), attr_type=False, root=True )
path = xml_td_path + "\\" + "Metadata" + "\\" + datetime.now().strftime( "%Y-%m-%d" + "," + "%I-%M-%S %p" )
os.mkdir( path )
file_path = path + "\\" + datetime.now().strftime( "%Y-%m-%d" + "," + "%I-%M-%S %p" ) + ".xml"
f = open( file_path, 'w' )
f.write( xml_data )
f.close()

