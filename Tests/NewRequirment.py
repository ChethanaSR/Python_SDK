from ceic_api_client.api_client import ApiClient
from ceic_api_client.apis.dictionary_api import DictionaryApi
from ceic_api_client.apis.series_api import SeriesApi
from ceic_api_client.apis.insights_api import InsightsApi

access_token ="OrgKdLWRj2tHZcS3IoHih9SPLCqSoL9aP4vs6ZzFrzxTyQRZPRX7VCgwDVTP0Cnnn9V89NeQnRbu2IgWn8gHTd0YcnZxz93JoSSrqLWEBjftboESI81mAEiKwL8cuSFe"
#example_series_id = "366946997,383129097,352636197,114157808,379564047"
example_series_id = "369765247,369765617,369765877,380485087"

api_client = ApiClient( header_name="Authorization", header_value=access_token )
series_api = SeriesApi( api_client=api_client )

series_result = series_api.get_series( id=example_series_id )
series_metadata_result = series_api.get_series_metadata( id=example_series_id )
series_time_points_result = series_api.get_series_time_points( id=example_series_id )
series = series_result.data[0]
series_metadata = series.metadata
series_frequency1 = series_metadata.frequency
print series_frequency1
series = series_result.data[1]
series_metadata = series.metadata
series_frequency2 = series_metadata.frequency
print series_frequency2
series = series_result.data[2]
series_metadata = series.metadata
series_frequency3 = series_metadata.frequency
print series_frequency3
series = series_result.data[3]
series_metadata = series.metadata
series_frequency4 = series_metadata.frequency
print series_frequency4
# series = series_result.data[4]
# series_metadata = series.metadata
# series_frequency5 = series_metadata.frequency
# print series_frequency5

