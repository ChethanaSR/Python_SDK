from ceic_api_client.api_client import ApiClient
from ceic_api_client.apis.dictionary_api import DictionaryApi
from ceic_api_client.apis.series_api import SeriesApi
from ceic_api_client.apis.insights_api import InsightsApi

access_token ="OrgKdLWRj2tHZcS3IoHih9SPLCqSoL9aP4vs6ZzFrzxTyQRZPRX7VCgwDVTP0Cnnn9V89NeQnRbu2IgWn8gHTd0YcnZxz93JoSSrqLWEBjftboESI81mAEiKwL8cuSFe"


api_client = ApiClient( header_name="Authorization", header_value=access_token )
series_api = SeriesApi( api_client=api_client )

key_words = ["GDP"]
series_search_result = series_api.search_series( keyword=", ".join( key_words ) )
print series_search_result
