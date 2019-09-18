

class CeicRequestDecorator(object):

    _DEFAULT_ID_KEY = "id"

    @staticmethod
    def _get_by_id(self, func, id_key=None, **kwargs):
        if id_key is None:
            id_key = CeicRequestDecorator._DEFAULT_ID_KEY

        def wrapper():
            ids = kwargs[id_key]
            ids = CeicRequestDecorator._normalize_ids(ids)
            kwargs[id_key] = ids

            return func(self, **kwargs)

        return wrapper()

    @staticmethod
    def _search(self, func, search_adaptor, **kwargs):
        def wrapper():
            def search_method(offset, limit):
                kwargs["offset"] = offset
                kwargs["limit"] = limit

                return search_adaptor.adapt_api_call(**kwargs)

            return func(self, search_method, **kwargs)

        return wrapper()

    @staticmethod
    def _normalize_ids(ids):
        ids = CeicRequestDecorator._normalize_ids_param_format(ids)
        ids = CeicRequestDecorator._remove_duplicate_ids(ids)

        return ids

    @staticmethod
    def _normalize_ids_param_format(ids):
        if isinstance(ids, int):
            ids = str(ids)

        if isinstance(ids, str):
            ids = CeicRequestDecorator._convert_ids_str_to_list(ids)

        if not isinstance(ids, list):
            raise ValueError("Unsupported id format: {0}".format(type(ids)))

        ids = CeicRequestDecorator._normalize_ids_list_elements(ids)

        for single_id in ids:
            CeicRequestDecorator._check_id_str_limit(single_id)

        return ids

    @staticmethod
    def _remove_duplicate_ids(ids):
        ids_set = set(ids)
        ids = list(ids_set)

        return ids

    @staticmethod
    def _convert_ids_str_to_list(ids):
        CeicRequestDecorator._check_id_str_limit(ids)

        return [ids]

    @staticmethod
    def _normalize_ids_list_elements(ids):
        for index in range(0, len(ids)):
            single_id = ids[index]
            if not isinstance(single_id, str):
                ids[index] = str(single_id)

        return ids

    @staticmethod
    def _check_id_str_limit(single_id):
        if "," in single_id:
            raise ValueError("Only single ids can be passed as strings.\n"
                             "Multiple id values must be passed as list.")


class CeicSeriesRequestDecorators(CeicRequestDecorator):

    @staticmethod
    def get_by_id(func):
        def wrapper(self, **kwargs):
            return CeicRequestDecorator._get_by_id(self, func, **kwargs)

        return wrapper

    @staticmethod
    def search(func):
        def wrapper(self, **kwargs):
            search_adaptor = self._search_series_adaptor
            return CeicRequestDecorator._search(self, func, search_adaptor, **kwargs)

        return wrapper


class CeicInsightsRequestDecorators(CeicRequestDecorator):

    _INSIGHT_SERIES_KEY = "series_id"

    @staticmethod
    def insight_search(func):
        def wrapper(self, **kwargs):
            search_adaptor = self._search_insight_adaptor
            return CeicRequestDecorator._search(self, func, search_adaptor, **kwargs)

        return wrapper

    @staticmethod
    def insight_by_id(func):
        def wrapper(self, **kwargs):
            return CeicRequestDecorator._get_by_id(self, func, **kwargs)

        return wrapper

    @staticmethod
    def insight_series_by_id(func):
        def wrapper(self, **kwargs):
            return CeicRequestDecorator._get_by_id(
                self, func, CeicInsightsRequestDecorators._INSIGHT_SERIES_KEY, **kwargs
            )

        return wrapper
