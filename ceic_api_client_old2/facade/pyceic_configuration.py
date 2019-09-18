from ceic_api_client.api_client import ApiClient


class CeicConfiguration(object):

    _DEFAULT_RETURN_TYPE = "application/json"
    _GET_SERIES_SERIES_ID_LIMIT = 3000

    def __init__(self):
        self._api_client = ApiClient()
        self._set_default_return_type()

    @property
    def api_client(self):
        return self._api_client

    @property
    def downloads_file_url(self):
        return "https://downloads-stage.ceicdata.com/downloads.json" if \
            "api-stage" in self._api_client.configuration.host else \
            "https://downloads.ceicdata.com/downloads.json"

    @property
    def python_package_url(self):
        return "https://downloads-stage.ceicdata.com/python" if \
            "api-stage" in self._api_client.configuration.host else \
            "https://downloads.ceicdata.com/python"

    @property
    def get_series_series_id_limit(self):
        return self._GET_SERIES_SERIES_ID_LIMIT

    @property
    def server(self):
        return self._api_client.configuration.host

    @server.setter
    def server(self, value):
        self._api_client.configuration.host = value

    def set_token(self, access_token):
        self._api_client.set_default_header("Authorization", access_token)

    def unset_token(self):
        self._api_client.default_headers.pop("Authorization")

    def set_proxy(self, proxy_url=None, proxy_username=None, proxy_password=None):
        self._api_client.configuration.set_proxy(proxy_url, proxy_username, proxy_password)

    def _set_default_return_type(self):
        self._api_client.set_default_header("Accept", self._DEFAULT_RETURN_TYPE)
