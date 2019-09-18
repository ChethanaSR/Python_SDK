from ceic_api_client.models.search_series_result import SearchSeriesResult
from ceic_api_client.models.series_result import SeriesResult
from ceic_api_client.models.insights_search_result import InsightsSearchResult
from ceic_api_client.models.insight_series_result import InsightSeriesResult


class CeicSeriesLayout(object):

    def __init__(self, id, layout):
        self._id = id
        self._layout = layout

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def layout(self):
        return self._layout

    @layout.setter
    def layout(self, value):
        self._layout = value


class CeicSearchResult(object):

    _DEFAULT_LIMIT = 100
    _DEFAULT_OFFSET = 0

    def __init__(self, search_method, search_series_result, limit, offset):
        self._search_method = search_method

        self._limit = limit if limit is not None else self._DEFAULT_LIMIT
        self._offset = offset if offset is not None else self._DEFAULT_OFFSET

        self._initial_offset = self._offset
        self._initial_result = search_series_result
        self._initial_iteration = True

    def __iter__(self):
        self._reset_iteration()
        return self

    def __next__(self):
        if self._initial_iteration:
            self._initial_iteration = False
            return self._initial_result

        self._offset += self._limit
        result = self._search_method(self._offset, self._limit)
        if len(result.data.items) == 0:
            self._reset_iteration()
            raise StopIteration()

        return result

    def next(self):
        return self.__next__()

    def _reset_iteration(self):
        self._offset = self._initial_offset
        self._initial_iteration = True


class CeicSearchSeriesResult(CeicSearchResult, SearchSeriesResult):

    def __init__(self, search_method, search_series_result, limit, offset):
        CeicSearchResult.__init__(self, search_method, search_series_result, limit, offset)
        SearchSeriesResult.__init__(self, search_series_result.data)


class CeicSearchInsightsResult(CeicSearchResult, InsightsSearchResult):

    def __init__(self, search_method, search_insights_result, limit, offset):
        CeicSearchResult.__init__(self, search_method, search_insights_result, limit, offset)
        InsightsSearchResult.__init__(self, search_insights_result.data)


class CeicSeriesResult(object):

    _SERIES_PER_REQUEST = 20

    def __init__(self, series_method, ids_key, **kwargs):
        self._series_method = series_method
        self._ids_key = ids_key
        self._kwargs = kwargs

        self._id_chunks = self._split_array_into_chunks(self._kwargs[ids_key])

        self._reset_iteration()
        self._initial_result = self._get_result_for(0)

    def __iter__(self):
        self._reset_iteration()
        return self

    def __next__(self):
        self._current_chunk_index += 1
        if self._current_chunk_index >= len(self._id_chunks):
            self._reset_iteration()
            raise StopIteration()

        if self._current_chunk_index == 0:
            return self._initial_result

        self._kwargs[self._ids_key] = self._id_chunks[self._current_chunk_index]
        result = self._series_method(**self._kwargs)

        return result

    def next(self):
        return self.__next__()

    def _split_array_into_chunks(self, ids):
        return [
            ids[index: index + self._SERIES_PER_REQUEST] for
            index in
            range(0, len(ids), self._SERIES_PER_REQUEST)
        ]

    def _reset_iteration(self):
        self._current_chunk_index = -1

    def _get_result_for(self, chunk_index):
        original_id = self._kwargs[self._ids_key]

        self._kwargs[self._ids_key] = self._id_chunks[chunk_index]
        result = self._series_method(**self._kwargs)

        self._kwargs[self._ids_key] = original_id

        return result


class CeicGetSeriesResult(CeicSeriesResult, SeriesResult):

    _IDS_KEY = "id"

    def __init__(self, get_series_method, **kwargs):
        CeicSeriesResult.__init__(self, get_series_method, self._IDS_KEY, **kwargs)
        SeriesResult.__init__(self, errors=self._initial_result.errors, data=self._initial_result.data)


class CeicSeriesLayoutsResult(CeicGetSeriesResult):

    def __next__(self):
        result = super(CeicSeriesLayoutsResult, self).__next__()
        result.data = self._get_layouts_for(result.data)

        return result

    @staticmethod
    def _get_layouts_for(series_list):
        series_layouts = [
            CeicSeriesLayout(series.metadata.id, series.layout) for series in series_list
        ]

        return series_layouts


class CeicGetInsightSeriesResult(CeicSeriesResult, InsightSeriesResult):

    _IDS_KEY = "id"

    def __init__(self, get_series_method, **kwargs):
        CeicSeriesResult.__init__(self, get_series_method, self._IDS_KEY, **kwargs)
        InsightSeriesResult.__init__(self, data=self._initial_result.data)


class CeicGetInsightSeriesListResult(CeicGetInsightSeriesResult):

    _IDS_KEY = "series_id"
