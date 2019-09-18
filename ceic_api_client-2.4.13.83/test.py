from ceic_api_client.pyceic import Ceic
from ceic_api_client.apis.sessions_api import SessionsApi
from ceic_api_client.rest import ApiException
from ceic_api_client.apis.dictionary_api import DictionaryApi
from ceic_api_client.api_client import ApiClient
from ceic_api_client.configuration import Configuration

from ceic_api_client.facade.pyceic_exception import CeicException

from ceic_api_client.facade.pyceic_sessions_facade import CeicSessionsFacade
from ceic_api_client.facade.pyceic_configuration import CeicConfiguration

import sys
import cmd
import six
import getpass


username = "sdk-integration-tests@apiqatest1.com"
password = "4P11nTegr4t10nTests"

invalid_username = "asd"
invalid_password = "asd"

series_id = "310917301"
series_list = ["310917301", "371376337"]

search_indicator = ["301504"]

Ceic.login(username, password)
Ceic.series(series_id)

ceic = Ceic()
ceic.series(series_id)

Ceic.get_classifications()


# ceic = Ceic()
# ceic.login(username, password)
# ceic.logout()
#series = ceic.series(series_id)

# # Use-Case 1
# for result in ceic.search(indicator=search_indicator):
#     print(len(result.data.items))
#
# # Use-Case 2
# result = Ceic.search(indicator=search_indicator)
#
# for res in result:
#     print(len(res.data.items))
#
# for res in result:
#     print(len(res.data.items))
#
# # Use-Case 3
# for result in ceic.search(indicator=search_indicator, limit=50):
#     print(len(result.data.items))
#
# # Use-Case 4
# result = Ceic.search(indicator=search_indicator)
# print(len(result.data.items))
# result = result.next()
# print(len(result.data.items))
# result = result.next()
# print(len(result.data.items))
# result = result.next()
# print(len(result.data.items))
# result = result.next()
# print(len(result.data.items))
# result = result.next()
# print(len(result.data.items))
# result = result.next()
# print(len(result.data.items))
# result = result.next()
# print(len(result.data.items))
