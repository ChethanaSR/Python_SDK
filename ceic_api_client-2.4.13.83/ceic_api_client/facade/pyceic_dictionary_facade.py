from ceic_api_client.apis.dictionary_api import DictionaryApi


class CeicDictionaryFacade(object):

    def __init__(self, ceic_configuration, ceic_requests_facade):
        self._ceic_configuration = ceic_configuration
        self._ceic_requests_facade = ceic_requests_facade

        self._dictionary_api = DictionaryApi(self._ceic_configuration.api_client)

    def get_dictionaries(self, **kwargs):
        result = self._ceic_requests_facade.make_request(
            self._dictionary_api.get_dictionaries,
            **kwargs
        )

        return result

    def get_indicators(self, **kwargs):
        result = self._ceic_requests_facade.make_request(
            self._dictionary_api.get_indicators,
            **kwargs
        )

        return result

    def get_classifications(self, **kwargs):
        result = self._ceic_requests_facade.make_request(
            self._dictionary_api.get_classifications,
            **kwargs
        )

        return result

    def get_classification_indicators(self, **kwargs):
        result = self._ceic_requests_facade.make_request(
            self._dictionary_api.get_classification_indicators,
            **kwargs
        )

        return result

    def get_countries(self, **kwargs):
        result = self._ceic_requests_facade.make_request(
            self._dictionary_api.get_countries,
            **kwargs
        )

        return result

    def get_country_sources(self, **kwargs):
        result = self._ceic_requests_facade.make_request(
            self._dictionary_api.get_country_sources,
            **kwargs
        )

        return result

    def get_regions(self, **kwargs):
        result = self._ceic_requests_facade.make_request(
            self._dictionary_api.get_regions,
            **kwargs
        )

        return result

    def get_sources(self, **kwargs):
        result = self._ceic_requests_facade.make_request(
            self._dictionary_api.get_sources,
            **kwargs
        )

        return result

    def get_units(self, **kwargs):
        result = self._ceic_requests_facade.make_request(
            self._dictionary_api.get_units,
            **kwargs
        )

        return result

    def get_frequencies(self, **kwargs):
        result = self._ceic_requests_facade.make_request(
            self._dictionary_api.get_frequencies,
            **kwargs
        )

        return result

    def get_statuses(self, **kwargs):
        result = self._ceic_requests_facade.make_request(
            self._dictionary_api.get_statuses,
            **kwargs
        )

        return result
