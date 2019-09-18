# file1 = open("C:\\Users\\rchethana\\Desktop\\notepad_python.txt","w")
# file1.writelines("Chethana")
# file1.close()

from ceic_api_client.api_client import ApiClient
from ceic_api_client.apis.dictionary_api import DictionaryApi
from ceic_api_client.apis.series_api import SeriesApi
from ceic_api_client.apis.insights_api import InsightsApi

access_token = "oC6OX7cRKs386i8KhqkHVi5BOgRCVMAkUVmL1EQlrKz8qNztEkUoLhior6c2RYBmhkTUenYrLBM8Kzl4R7cu2c4ywikS1F4cevkHegEKEdIEhoyYMzkgKXAWXqwzHyC8"
example_series_id = "266502802"

api_client = ApiClient( header_name="Authorization", header_value=access_token )
series_api = SeriesApi( api_client=api_client )

series_result = series_api.get_series( id=example_series_id )
series_metadata_result = series_api.get_series_metadata( id=example_series_id )
print series_metadata_result