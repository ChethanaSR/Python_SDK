from ceic_api_client.apis.series_api import SeriesApi
from ceic_api_client.facade.pyceic_decorators import CeicSeriesRequestDecorators as SeriesDecorator
from ceic_api_client.facade.pyceic_adaptors import *
from ceic_api_client.facade.pyceic_facade_models import *


class CeicSeriesFacade(object):

    def __init__(self, ceic_configuration, ceic_requests_facade):
        self._ceic_configuration = ceic_configuration
        self._ceic_requests_facade = ceic_requests_facade

        series_api = SeriesApi(ceic_configuration.api_client)
        max_series_ids_per_request = ceic_configuration.get_series_series_id_limit

        self._get_series_adaptor = GetSeriesAdaptor(max_series_ids_per_request, ceic_requests_facade, series_api)
        self._get_series_metadata_adaptor = GetSeriesMetadataAdaptor(
            max_series_ids_per_request, ceic_requests_facade, series_api
        )
        self._get_series_data_adaptor = GetSeriesDataAdaptor(
            max_series_ids_per_request, ceic_requests_facade, series_api
        )

        self._search_series_adaptor = SearchSeriesAdaptor(
            max_series_ids_per_request, ceic_requests_facade, series_api
        )

    @SeriesDecorator.get_by_id
    def get_series(self, **kwargs):
        result = CeicGetSeriesResult(
            self._get_series_adaptor.adapt_api_call,
            **kwargs
        )
        return result

    @SeriesDecorator.get_by_id
    def get_series_metadata(self, **kwargs):
        result = CeicGetSeriesResult(
            self._get_series_metadata_adaptor.adapt_api_call,
            **kwargs
        )
        return result

    @SeriesDecorator.get_by_id
    def get_series_data(self, **kwargs):
        result = CeicGetSeriesResult(
            self._get_series_data_adaptor.adapt_api_call,
            **kwargs
        )
        return result

    @SeriesDecorator.get_by_id
    def get_series_layouts(self, **kwargs):
        result = CeicSeriesLayoutsResult(
            self._get_series_adaptor.adapt_api_call,
            **kwargs
        )
        return result

    @SeriesDecorator.search
    def search_series(self, search_method, **kwargs):
        result = CeicSearchSeriesResult(
            search_method,
            self._search_series_adaptor.adapt_api_call(**kwargs),
            limit=kwargs["limit"] if "limit" in kwargs else None,
            offset=kwargs["offset"] if "offset" in kwargs else None
        )

        return result
