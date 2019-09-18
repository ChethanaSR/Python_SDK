

class CeicAdaptor(object):

    def __init__(self, max_ids_per_request, ceic_requests_facade, api):
        self._max_ids_per_request = max_ids_per_request
        self._ceic_requests_facade = ceic_requests_facade

        self._api = api

    def adapt_api_call(self, **kwargs):
        raise NotImplementedError()

    def _adapt_api_call(self, api_method, **kwargs):
        result = self._ceic_requests_facade.make_request(
            api_method,
            **kwargs
        )

        return result

    def _check_id_param_limit(self, series_id):
        if len(series_id) > self._max_ids_per_request:
            raise AssertionError(
                "Too many requested ids. "
                "Cannot request more than {0} ids with a single request".format(
                    self._max_ids_per_request
                )
            )

    def _get_normalized_id_parameter(self, **kwargs):
        self._check_id_param_limit(kwargs["id"])
        ids = ",".join(kwargs["id"])

        return ids


class GetSeriesAdaptor(CeicAdaptor):

    def adapt_api_call(self, **kwargs):
        kwargs["id"] = self._get_normalized_id_parameter(**kwargs)
        api_method = self._api.get_series

        result = super(GetSeriesAdaptor, self)._adapt_api_call(api_method, **kwargs)

        return result


class GetSeriesMetadataAdaptor(CeicAdaptor):

    def adapt_api_call(self, **kwargs):
        kwargs["id"] = self._get_normalized_id_parameter(**kwargs)
        api_method = self._api.get_series_metadata

        result = super(GetSeriesMetadataAdaptor, self)._adapt_api_call(api_method, **kwargs)

        return result


class GetSeriesDataAdaptor(CeicAdaptor):

    def adapt_api_call(self, **kwargs):
        kwargs["id"] = self._get_normalized_id_parameter(**kwargs)
        api_method = self._api.get_series_time_points

        result = super(GetSeriesDataAdaptor, self)._adapt_api_call(api_method, **kwargs)

        return result


class SearchSeriesAdaptor(CeicAdaptor):

    def adapt_api_call(self, **kwargs):
        api_method = self._api.search_series

        result = super(SearchSeriesAdaptor, self)._adapt_api_call(api_method, **kwargs)

        return result


class GetInsightsAdaptor(CeicAdaptor):

    def __init__(self, ceic_requests_facade, api):
        super(GetInsightsAdaptor, self).__init__(0, ceic_requests_facade, api)

    def adapt_api_call(self, **kwargs):
        api_method = self._api.get_insights

        result = super(GetInsightsAdaptor, self)._adapt_api_call(api_method, **kwargs)

        return result


class GetInsightsCategoriesAdaptor(GetInsightsAdaptor):
    def adapt_api_call(self, **kwargs):
        api_method = self._api.get_insights_categories

        result = super(GetInsightsCategoriesAdaptor, self)._adapt_api_call(api_method, **kwargs)

        return result


class GetGalleryInsightsCategoriesAdaptor(GetInsightsAdaptor):
    def adapt_api_call(self, **kwargs):
        api_method = self._api.get_gallery_insights_categories

        result = super(GetGalleryInsightsCategoriesAdaptor, self)._adapt_api_call(api_method, **kwargs)

        return result


class SearchInsightsAdaptor(GetInsightsAdaptor):
    
    def adapt_api_call(self, **kwargs):
        api_method = self._api.search_insights

        result = super(SearchInsightsAdaptor, self)._adapt_api_call(api_method, **kwargs)

        return result


class GetInsightAdaptor(CeicAdaptor):

    def adapt_api_call(self, **kwargs):
        kwargs["id"] = self._get_normalized_id_parameter(**kwargs)
        api_method = self._api.get_insight

        result = super(GetInsightAdaptor, self)._adapt_api_call(api_method, **kwargs)

        return result


class DownloadInsightAdaptor(CeicAdaptor):

    def adapt_api_call(self, **kwargs):
        kwargs["id"] = self._get_normalized_id_parameter(**kwargs)
        api_method = self._api.download_insight

        result = super(DownloadInsightAdaptor, self)._adapt_api_call(api_method, **kwargs)

        return result


class GetInsightSeriesAdaptor(CeicAdaptor):

    def adapt_api_call(self, **kwargs):
        kwargs["id"] = self._get_normalized_id_parameter(**kwargs)
        api_method = self._api.get_insight_series

        result = super(GetInsightSeriesAdaptor, self)._adapt_api_call(api_method, **kwargs)

        return result


class GetInsightSeriesDataAdaptor(CeicAdaptor):

    def adapt_api_call(self, **kwargs):
        kwargs["id"] = self._get_normalized_id_parameter(**kwargs)
        api_method = self._api.get_insight_series_data

        result = super(GetInsightSeriesDataAdaptor, self)._adapt_api_call(api_method, **kwargs)

        return result


class GetInsightSeriesMetadataAdaptor(CeicAdaptor):

    def adapt_api_call(self, **kwargs):
        kwargs["id"] = self._get_normalized_id_parameter(**kwargs)
        api_method = self._api.get_insight_series_metadata

        result = super(GetInsightSeriesMetadataAdaptor, self)._adapt_api_call(api_method, **kwargs)

        return result


class GetInsightSeriesListAdaptor(CeicAdaptor):

    def adapt_api_call(self, **kwargs):
        kwargs["series_id"] = self._get_normalized_id_parameter(**kwargs)
        api_method = self._api.get_insight_series_list

        result = super(GetInsightSeriesListAdaptor, self)._adapt_api_call(api_method, **kwargs)

        return result


class GetInsightSeriesDataListAdaptor(CeicAdaptor):

    def adapt_api_call(self, **kwargs):
        kwargs["series_id"] = self._get_normalized_id_parameter(**kwargs)
        api_method = self._api.get_insight_series_list_data

        result = super(GetInsightSeriesDataListAdaptor, self)._adapt_api_call(api_method, **kwargs)

        return result


class GetInsightSeriesMetadataListAdaptor(CeicAdaptor):

    def adapt_api_call(self, **kwargs):
        kwargs["series_id"] = self._get_normalized_id_parameter(**kwargs)
        api_method = self._api.get_insight_series_list_metadata

        result = super(GetInsightSeriesMetadataListAdaptor, self)._adapt_api_call(api_method, **kwargs)

        return result
