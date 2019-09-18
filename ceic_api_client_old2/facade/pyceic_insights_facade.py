from ceic_api_client.apis.insights_api import InsightsApi
from ceic_api_client.facade.pyceic_decorators import CeicInsightsRequestDecorators as InsightDecorators
from ceic_api_client.facade.pyceic_facade_models import *
from ceic_api_client.facade.pyceic_adaptors import *


class CeicInsightsFacade(object):
    
    def __init__(self, ceic_configuration, ceic_requests_facade):
        self._ceic_configuration = ceic_configuration
        self._ceic_requests_facade = ceic_requests_facade
        
        self._insights_api = InsightsApi(self._ceic_configuration.api_client)
        max_ids_per_request = ceic_configuration.get_series_series_id_limit

        self._get_insights_adaptor = GetInsightsAdaptor(self._ceic_requests_facade, self._insights_api)
        self._search_insight_adaptor = SearchInsightsAdaptor(self._ceic_requests_facade, self._insights_api)
        self._get_insights_categories_adaptor = GetInsightsCategoriesAdaptor(
            self._ceic_requests_facade, self._insights_api
        )
        self._get_gallery_insights_categories_adaptor = GetGalleryInsightsCategoriesAdaptor(
            self._ceic_requests_facade, self._insights_api
        )
        self._get_insight_adaptor = GetInsightAdaptor(
            max_ids_per_request, self._ceic_requests_facade, self._insights_api
        )
        self._download_insight_adaptor = DownloadInsightAdaptor(
            max_ids_per_request, self._ceic_requests_facade, self._insights_api
        )
        self._get_insight_series_adaptor = GetInsightSeriesAdaptor(
            max_ids_per_request, self._ceic_requests_facade, self._insights_api
        )
        self._get_insight_series_data_adaptor = GetInsightSeriesDataAdaptor(
            max_ids_per_request, self._ceic_requests_facade, self._insights_api
        )
        self._get_insight_series_metadata_adaptor = GetInsightSeriesMetadataAdaptor(
            max_ids_per_request, self._ceic_requests_facade, self._insights_api
        )
        self._get_insight_series_list_adaptor = GetInsightSeriesListAdaptor(
            max_ids_per_request, self._ceic_requests_facade, self._insights_api
        )
        self._get_insight_series_data_list_adaptor = GetInsightSeriesDataListAdaptor(
            max_ids_per_request, self._ceic_requests_facade, self._insights_api
        )
        self._get_insight_series_metadata_list_adaptor = GetInsightSeriesMetadataListAdaptor(
            max_ids_per_request, self._ceic_requests_facade, self._insights_api
        )

    def get_insights(self, **kwargs):
        result = self._get_insights_adaptor.adapt_api_call(**kwargs)

        return result

    @InsightDecorators.insight_search
    def search_insights(self, search_method, **kwargs):
        result = CeicSearchInsightsResult(
            search_method,
            self._search_insight_adaptor.adapt_api_call(**kwargs),
            limit=kwargs["limit"] if "limit" in kwargs else None,
            offset=kwargs["offset"] if "offset" in kwargs else None
        )

        return result

    def get_insights_categories(self, **kwargs):
        result = self._get_insights_categories_adaptor.adapt_api_call(**kwargs)

        return result

    def get_gallery_insights_categories(self, **kwargs):
        result = self._get_gallery_insights_categories_adaptor.adapt_api_call(**kwargs)

        return result

    @InsightDecorators.insight_by_id
    def get_insight(self, **kwargs):
        result = self._get_insight_adaptor.adapt_api_call(**kwargs)

        return result

    @InsightDecorators.insight_by_id
    def download_insight(self, **kwargs):
        result = self._download_insight_adaptor.adapt_api_call(**kwargs)

        return result

    @InsightDecorators.insight_by_id
    def get_insight_series(self, **kwargs):
        result = CeicGetInsightSeriesResult(
            self._get_insight_series_adaptor.adapt_api_call,
            **kwargs
        )

        return result

    @InsightDecorators.insight_by_id
    def get_insight_series_data(self, **kwargs):
        result = CeicGetInsightSeriesResult(
            self._get_insight_series_data_adaptor.adapt_api_call,
            **kwargs
        )

        return result

    @InsightDecorators.insight_by_id
    def get_insight_series_metadata(self, **kwargs):
        result = CeicGetInsightSeriesResult(
            self._get_insight_series_metadata_adaptor.adapt_api_call,
            **kwargs
        )

        return result
    
    @InsightDecorators.insight_series_by_id
    def get_insight_series_list(self, **kwargs):
        result = CeicGetInsightSeriesListResult(
            self._get_insight_series_list_adaptor.adapt_api_call,
            **kwargs
        )

        return result

    @InsightDecorators.insight_series_by_id
    def get_insight_series_data_list(self, **kwargs):
        result = CeicGetInsightSeriesListResult(
            self._get_insight_series_data_list_adaptor.adapt_api_call,
            **kwargs
        )

        return result

    @InsightDecorators.insight_series_by_id
    def get_insight_series_metadata_list(self, **kwargs):
        result = CeicGetInsightSeriesListResult(
            self._get_insight_series_metadata_list_adaptor.adapt_api_call,
            **kwargs
        )

        return result
