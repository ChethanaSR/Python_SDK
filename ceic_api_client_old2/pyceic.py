from ceic_api_client.facade.pyceic_configuration import CeicConfiguration
from ceic_api_client.facade.pyceic_requests_facade import CeicRequestsFacade
from ceic_api_client.facade.pyceic_sessions_facade import CeicSessionsFacade
from ceic_api_client.facade.pyceic_series_facade import CeicSeriesFacade
from ceic_api_client.facade.pyceic_dictionary_facade import CeicDictionaryFacade
from ceic_api_client.facade.pyceic_layout_facade import CeicLayoutFacade
from ceic_api_client.facade.pyceic_insights_facade import CeicInsightsFacade
from ceic_api_client.facade.pyceic_exception import *


class Ceic(object):

    _INSTANCE = None
    _INSTANCE_INIT = False

    def __new__(cls, username=None, password=None, *args, **kwargs):
        if not cls._INSTANCE:
            cls._INSTANCE = super(Ceic, cls).__new__(cls, *args, **kwargs)

        return cls._INSTANCE

    def __init__(self, username=None, password=None, proxy_url=None, proxy_username=None, proxy_password=None):
        """
        Constructor for the CEIC SDK Facade.

        :param username: Login username
        :type username: str
        :param password: Login password
        :type password: str
        :param proxy_url: Proxy URL
        :type proxy_url: str
        :param str proxy_username: Proxy username
        :type proxy_username: str
        :param proxy_password: Proxy password
        :type proxy_password: str
        """

        if not self._INSTANCE_INIT:
            self._init_object(username, password, proxy_url, proxy_username, proxy_password)
            self._INSTANCE_INIT = True

        self._try_set_proxy(proxy_url, proxy_username, proxy_password)
        self._try_login(username, password)

    @staticmethod
    def set_server(server):
        """
        Changes the API server address.

        :param server: Server URL
        :type server: str

        :return: self
        :rtype: ceic_api_client.pyceic.Ceic
        """

        instance = Ceic._get_instance()
        
        instance._ceic_configuration.server = server

        return instance

    @staticmethod
    def get_server():
        """
        Gets the address of the currently set API server.

        :return: The currently set API server
        :rtype: str
        """

        instance = Ceic._get_instance()

        return instance._ceic_configuration.server

    @staticmethod
    def set_proxy(proxy_url=None, proxy_username=None, proxy_password=None):
        """
        Sets a proxy connection.

        :param proxy_url: Proxy URL
        :type proxy_url: str
        :param proxy_username: Proxy username
        :type proxy_username: str
        :param proxy_password: Proxy password
        :type proxy_password: str

        :return: self
        :rtype: ceic_api_client.pyceic.Ceic
        """

        instance = Ceic._get_instance()

        instance._ceic_configuration.set_proxy(proxy_url, proxy_username, proxy_password)

        return instance

    @staticmethod
    def login(username=None, password=None):
        """
        Attempts to login and create a login session.

        :param username: Login username
        :type username: str
        :param password: Login password
        :type password: str

        :return self
        :rtype ceic_api_client.pyceic.Ceic

        :raises ceic_api_client.facade.pyceic_exception.CeicInvalidLoginDetailsException : Invalid login details
        :raises ceic_api_client.facade.pyceic_exception.CeicActiveSessionException : User already has an active session
        """

        instance = Ceic._get_instance()

        instance._sessions_facade.login(username, password)
        instance._try_set_session()

        return instance

    @staticmethod
    def logout():
        """
        Attempts to logout and delete the saved session.

        :return: self - Same Ceic instance
        :rtype: ceic_api_client.pyceic.Ceic

        :raises ceic_api_client.facade.pyceic_exception.CeicSessionExpiredException : Saved session is already expired
        :raises ceic_api_client.facade.pyceic_exception.CeicNoActiveSessionsException : There is no saved session
        """

        instance = Ceic._get_instance()

        instance._sessions_facade.logout()
        instance._try_unset_session()

        return instance

    @staticmethod
    def series(series_id, **kwargs):
        """
        Gets full series data. Result contains both metadata and time-points data.

        :param series_id: A single series id can be passed as a string, an integer, or a list.
            Multiple series ids can be passed as a list only.
        :type series_id: str, int, list

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.
        :keyword int count: Limit the amount of latest time-points returned, by the number specified.
        :keyword date start_date: Limits the start date after which the time-points will be returned.
        :keyword date end_date: Limits the end date before which the time-points will be returned.
        :keyword datetime updated_after: Returns only the updated time-points after the date specified.
        :keyword bool blank_observations: If it's set to true, empty time-points will be returned
        :keyword str time_points_status: Time points filter. One or more comma separated status code values.
            When not explicitly set, defaults to `active`. Possible values:
                            * active
                            * deleted
        :keyword bool with_replacements_metadata: If it is `true` result will contain
            replacements metadata not only list of id`s.

        :return: An iterable object which contains result data. Each object can contain up to 20 result objects.
        :rtype: ceic_api_client.facade.pyceic_facade_models.CeicGetSeriesResult
        """

        instance = Ceic._get_instance()

        kwargs["id"] = series_id
        get_series_method = instance._series_facade.get_series
        result = instance._make_request(get_series_method, **kwargs)

        return result

    @staticmethod
    def series_metadata(series_id, **kwargs):
        """
        Gets series metadata only.

        :param series_id: A single series id can be passed as a string, an integer, or a list.
                            Multiple series ids can be passed as a list only.
        :type series_id: str, int, list

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.
        :keyword bool with_replacements_metadata: If it is `true` result will contain
            replacements metadata not only list of id`s.

        :return: An iterable object which contains result data. Each object can contain up to 20 result objects.
        :rtype: ceic_api_client.facade.pyceic_facade_models.CeicGetSeriesResult
        """

        instance = Ceic._get_instance()

        kwargs["id"] = series_id
        get_series_method = instance._series_facade.get_series_metadata
        result = instance._make_request(get_series_method, **kwargs)

        return result

    @staticmethod
    def series_data(series_id, **kwargs):
        """
        Gets series time-points only.

        :param series_id: A single series id can be passed as a string, an integer, or a list.
                            Multiple series ids can be passed as a list only.
        :type series_id: str, int, list

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.
        :keyword int count: Limit the amount of latest time-points returned, by the number specified.
        :keyword date start_date: Limits the start date after which the time-points will be returned.
        :keyword date end_date: Limits the end date before which the time-points will be returned.
        :keyword datetime updated_after: Returns only the updated time-points after the date specified.
        :keyword bool blank_observations: If it's set to true, empty time-points will be returned
        :keyword str time_points_status: Time points filter. One or more comma separated status code values.
            When not explicitly set, defaults to `active`. Possible values:
                            * active
                            * deleted

        :return: An iterable object which contains result data. Each object can contain up to 20 result objects.
        :rtype: ceic_api_client.facade.pyceic_facade_models.CeicGetSeriesResult
        """

        instance = Ceic._get_instance()

        kwargs["id"] = series_id
        get_series_method = instance._series_facade.get_series_data
        result = instance._make_request(get_series_method, **kwargs)

        return result

    @staticmethod
    def series_layouts(series_id, **kwargs):
        """
        Gets series layout information only.
        
        :param series_id: A single series id can be passed as a string, an integer, or a list.
                            Multiple series ids can be passed as a list only.
        :type series_id: str, int, list

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.
        :keyword int count: Limit the amount of latest time-points returned, by the number specified.
        :keyword date start_date: Limits the start date after which the time-points will be returned.
        :keyword date end_date: Limits the end date before which the time-points will be returned.
        :keyword datetime updated_after: Returns only the updated time-points after the date specified.
        :keyword bool blank_observations: If it's set to true, empty time-points will be returned
        :keyword str time_points_status: Time points filter. One or more comma separated status code values.
            When not explicitly set, defaults to `active`. Possible values:
                            * active
                            * deleted
        :keyword bool with_replacements_metadata: If it is `true` result will contain
            replacements metadata not only list of id`s.

        :return: An iterable object which contains result data. Each object can contain up to 20 result objects.
        :rtype: ceic_api_client.facade.pyceic_facade_models.CeicGetSeriesResult
        """

        instance = Ceic._get_instance()

        kwargs["id"] = series_id
        get_series_method = instance._series_facade.get_series_layouts
        result = instance._make_request(get_series_method, **kwargs)

        return result

    @staticmethod
    def search(keyword=None, **kwargs):
        """
        Allows searching for series by a keyword and additional filtering criteria.
        Each filtering criteria accepts one or more, comma separated code values.
        See Dictionary functions for details on how to retrieve a specific filter code.
        The multi-dimensional filters include the economic classification and
        indicators (defined by CEIC database structure), region/country, frequency,
        unit, source, status and observation date.
        
        :param keyword: Search term. One or more keywords.
                        May contain special words further controlling the search results. Keyword search tips:
                            * Retail Sales - Show series with both keywords while
                                the sequence of keywords is irrelevant.
                                Equivalent to search Sales Retail
                            * Retail AND Sales - Show results: series with terms of Retail AND Sales,
                                regardless of the sequence. E. g. Retail Sales, Automobile Sales Retail.
                            * Retail;Sales - Show series with either keyword and series with both keywords while
                                the sequence of keywords is irrelevant, equivalent to search: Sales;Retail
                            * Retail OR Sales - Show results: series with terms of Retail OR Sales,
                                regardless of the sequence. E. g. Retail Sales, Retail Trade,
                                Sales Price, Motor Vehicle Sales
                            * Retail NOT Sales - Narrow a search by excluding specific terms while
                                the sequence of keywords is relevant. Show results: series with terms that
                                include Retail, but NOT Sales. E. g. Retail Trade, Retail Price, Retail Bank
                            * Retail Sales NOT (Hong Kong) - Narrow a search by excluding a set of words in parentheses
                                while the sequence of keywords in parentheses is irrelevant, equivalent to search:
                                Retail Sales NOT (Hong Kong). Show results: series with terms that
                                include Retail Sales, but NOT Hong Kong, such as
                                Retail Sales YoY: China, Retail Sales YoY: United States
        :type keyword: str

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.
        :keyword float limit: Number of records to return in the range 1 - 100. Default is 100.
        :keyword float offset: The offset from which the records will be returned.
            Used to get the next set of records when the limit is reached.
        :keyword list[str] database:  Database filter. One or more comma separated database code values.
            Use `/dictionary/databases` to get an up to date list of available databases. WORLD - *World Trend Plus*
            GLOBAL - *Global Database*  CEICGLBKS - *Global Key Series Database*
            PMI - *Markit Purchasing Managers' Index*  DAILY - *Daily Database*
            BRAZIL - *Brazil Premium Database*  RUSSIA - *Russia Premium Database*
            INDIA - *India Premium Database*  INDONESIA - *Indonesia Premium Database*
            CN - *China Premium Database*  OECD-MEI - *OECD - Main Economic Indicators*
            OECD-EO - *OECD - Economic Outlook*  OECD-PROD - *OECD - Productivity*
        :keyword list[str] frequency: Frequency filter. One or more comma separated frequency code values.
            D - Daily W - Weekly M - Monthly Q - Quarterly S - Semi-annual Y - Annual
        :keyword list[str] country: Country filter. One or more comma separated country code values.
            See related Dictionary function to get the full list of accepted countries.
        :keyword list[str] source: Source filter. One or more comma separated source code values.
            See related Dictionary function to get the full list of accepted sources.
        :keyword list[str] unit: Unit filter. One or more comma separated unit code values.
            See related Dictionary function to get the full list of accepted units.
        :keyword list[str] indicator: Indicator filter. One or more comma separated indicator code values.
            See related Dictionary function to get full list of accepted indicators.
        :keyword list[str] region: Region filter. One or more comma separated region code values.
            See related Dictionary function to get the full list of accepted regions.
        :keyword bool subscribed_only: Show only results for subscribed series when set to `true`.
            By default show results for all the series found.
        :keyword bool key_only: Show only 'key' series when set to `true`.
        :keyword bool new_only: Show only series created less than 1 month ago when set to `true`.
        :keyword bool name_only: This filter related with the `keyword` filter.
            If it's `true` keyword search will be searched only in series name instead of all series attributes.
        :keyword date start_date_before: Will return series with first observation before `start_date_before`
        :keyword date end_date_after: Will return series with last observation after `end_date_after`
        :keyword date created_after: Will return series created after `created_after` date
        :keyword date updated_after: Will return series last time updated after `updated_after` date
        :keyword list[str] status: Status filter. One or more comma separated status code values.
            When not explicitly set, defaults to T.  T - Active C - Discontinued B - Rebased
        :keyword list[str] topic: Topic filter. One or more comma separated topic code values.
        :keyword list[str] section: Section filter. One or more comma separated section code values.
        :keyword list[str] table: Table filter. One or more comma separated table code values.
        :keyword list[str] order: Sort order. Default is `relevance`.
        :keyword list[str] direction: Sort order direction. Default is `asc`.
            Accepted values: `asc` - ascending `desc` - descending
        :keyword list[str] filter_id: Filter ID used to define a subset of data over which the search will be executed.
            When combined with additional search criterion, the result will be an intesection of both.
        :keyword bool with_replacements_metadata: If it is `true` result will contain
            replacements metadata not only list of id`s
        :keyword list[str] facet: List of facets to return

        :return: An iterable object which contains result data. Each object can contain up to 20 result objects.
        :rtype: ceic_api_client.facade.pyceic_facade_models.CeicSearchSeriesResult
        """

        instance = Ceic._get_instance()

        if keyword is not None and keyword.strip() != "":
            kwargs["keyword"] = keyword

        search_series_method = instance._series_facade.search_series
        result = instance._make_request(search_series_method, **kwargs)

        return result

    @staticmethod
    def get_dictionaries(**kwargs):
        """
        Full dictionary list . Returns all the available dictionaries.

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.

        :return: Full dictionary list
        :rtype: ceic_api_client.models.dictionary_result.DictionaryResult
        """

        instance = Ceic._get_instance()

        get_dictionaries_method = instance._dictionary_facade.get_dictionaries
        result = instance._make_request(get_dictionaries_method, **kwargs)

        return result

    @staticmethod
    def get_indicators(**kwargs):
        """
        Returns full list of supported indicators, their codes and the related top level classifications.

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.

        :return: Object containing indicators list.
        :rtype: ceic_api_client.models.indicators_result.IndicatorsResult
        """

        instance = Ceic._get_instance()

        get_dictionaries_method = instance._dictionary_facade.get_indicators
        result = instance._make_request(get_dictionaries_method, **kwargs)

        return result

    @staticmethod
    def get_classifications(**kwargs):
        """
        Returns full list of supported top level classifications and their codes.

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.

        :return: Object containing classifications list.
        :rtype: ceic_api_client.models.classifications_result.ClassificationsResult
        """

        instance = Ceic._get_instance()

        get_dictionaries_method = instance._dictionary_facade.get_classifications
        result = instance._make_request(get_dictionaries_method, **kwargs)

        return result

    @staticmethod
    def get_classification_indicators(classification_id, **kwargs):
        """
        Returns full list of indicators for specific classification.

        :param classification_id: The ID of the specific classification
        :type classification_id: str

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.

        :return: Object containing indicators list.
        :rtype: ceic_api_client.models.indicators_result.IndicatorsResult
        """

        instance = Ceic._get_instance()

        kwargs["id"] = classification_id
        get_dictionaries_method = instance._dictionary_facade.get_classification_indicators
        result = instance._make_request(get_dictionaries_method, **kwargs)

        return result

    @staticmethod
    def get_countries(**kwargs):
        """
        Returns full list of supported countries and their codes.

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.

        :return: Object containing countries list.
        :rtype: ceic_api_client.models.countries_result.CountriesResult
        """

        instance = Ceic._get_instance()

        get_dictionaries_method = instance._dictionary_facade.get_countries
        result = instance._make_request(get_dictionaries_method, **kwargs)

        return result

    @staticmethod
    def get_country_sources(country_id, **kwargs):
        """
        Returns full list of sources for a specific country.

        :param country_id: The ID of the specific country
        :type country_id: str

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.

        :return: Object containing sources list for the specific country.
        :rtype: ceic_api_client.models.sources_result.SourcesResult
        """

        instance = Ceic._get_instance()

        kwargs["id"] = country_id
        get_dictionaries_method = instance._dictionary_facade.get_country_sources
        result = instance._make_request(get_dictionaries_method, **kwargs)

        return result

    @staticmethod
    def get_regions(**kwargs):
        """
        Returns full list of supported regions and their codes.

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.

        :return: Object containing regions list.
        :rtype: ceic_api_client.models.regions_result.RegionsResult
        """

        instance = Ceic._get_instance()

        get_dictionaries_method = instance._dictionary_facade.get_regions
        result = instance._make_request(get_dictionaries_method, **kwargs)

        return result

    @staticmethod
    def get_sources(**kwargs):
        """
        Returns full list of supported sources and their codes.

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.

        :return: Object containing sources list.
        :rtype: ceic_api_client.models.sources_result.SourcesResult
        """

        instance = Ceic._get_instance()

        get_dictionaries_method = instance._dictionary_facade.get_sources
        result = instance._make_request(get_dictionaries_method, **kwargs)

        return result

    @staticmethod
    def get_units(**kwargs):
        """
        Returns full list of supported units and their codes.

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.

        :return: Object containing units list.
        :rtype: ceic_api_client.models.units_result.UnitsResult
        """

        instance = Ceic._get_instance()

        get_dictionaries_method = instance._dictionary_facade.get_units
        result = instance._make_request(get_dictionaries_method, **kwargs)

        return result

    @staticmethod
    def get_frequencies(**kwargs):
        """
        Returns full list of supported frequencies and their codes.

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.

        :return: Object containing units list.
        :rtype: ceic_api_client.models.frequencies_result.FrequenciesResult
        """

        instance = Ceic._get_instance()

        get_dictionaries_method = instance._dictionary_facade.get_frequencies
        result = instance._make_request(get_dictionaries_method, **kwargs)

        return result

    @staticmethod
    def get_statuses(**kwargs):
        """
        Returns full list of supported statuses and their codes.

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.

        :return: Object containing statuses list.
        :rtype: ceic_api_client.models.statuses_result.StatusesResult
        """

        instance = Ceic._get_instance()

        get_dictionaries_method = instance._dictionary_facade.get_statuses
        result = instance._make_request(get_dictionaries_method, **kwargs)

        return result

    @staticmethod
    def get_layout_databases(keyword=None, **kwargs):
        """
        Returns list of layout databases. This is the top level from the layout hierarchy.

        :param keyword: Search term. One or more keywords.
                        May contain special words further controlling the search results. Keyword search tips:
                            * Retail Sales - Show series with both keywords while
                                the sequence of keywords is irrelevant.
                                Equivalent to search Sales Retail
                            * Retail AND Sales - Show results: series with terms of Retail AND Sales,
                                regardless of the sequence. E. g. Retail Sales, Automobile Sales Retail.
                            * Retail;Sales - Show series with either keyword and series with both keywords while
                                the sequence of keywords is irrelevant, equivalent to search: Sales;Retail
                            * Retail OR Sales - Show results: series with terms of Retail OR Sales,
                                regardless of the sequence. E. g. Retail Sales, Retail Trade,
                                Sales Price, Motor Vehicle Sales
                            * Retail NOT Sales - Narrow a search by excluding specific terms while
                                the sequence of keywords is relevant. Show results: series with terms that
                                include Retail, but NOT Sales. E. g. Retail Trade, Retail Price, Retail Bank
                            * Retail Sales NOT (Hong Kong) - Narrow a search by excluding a set of words in parentheses
                                while the sequence of keywords in parentheses is irrelevant, equivalent to search:
                                Retail Sales NOT (Hong Kong). Show results: series with terms that
                                include Retail Sales, but NOT Hong Kong, such as
                                Retail Sales YoY: China, Retail Sales YoY: United States
        :type keyword: str

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.
        :keyword list[str] frequency: Frequency filter. One or more comma separated frequency code values.
            D - Daily W - Weekly M - Monthly Q - Quarterly S - Semi-annual Y - Annual
        :keyword list[str] country: Country filter. One or more comma separated country code values.
            See related Dictionary function to get the full list of accepted countries.
        :keyword list[str] source: Source filter. One or more comma separated source code values.
            See related Dictionary function to get the full list of accepted sources.
        :keyword list[str] unit: Unit filter. One or more comma separated unit code values.
            See related Dictionary function to get the full list of accepted units.
        :keyword list[str] indicator: Indicator filter. One or more comma separated indicator code values.
            See related Dictionary function to get full list of accepted indicators.
        :keyword list[str] region: Region filter. One or more comma separated region code values.
            See related Dictionary function to get the full list of accepted regions.
        :keyword bool subscribed_only: Show only results for subscribed series when set to `true`.
            By default show results for all the series found.
        :keyword bool key_only: Show only 'key' series when set to `true`.
        :keyword bool new_only: Show only series created less than 1 month ago when set to `true`.
        :keyword bool name_only: This filter related with the `keyword` filter.
            If it's `true` keyword search will be searched only in series name instead of all series attributes.
        :keyword date start_date_before: Will return series with first observation before `start_date_before`
        :keyword date end_date_after: Will return series with last observation after `end_date_after`
        :keyword date created_after: Will return series created after `created_after` date
        :keyword date updated_after: Will return series last time updated after `updated_after` date
        :keyword list[str] status: Status filter. One or more comma separated status code values.
            When not explicitly set, defaults to T.  T - Active C - Discontinued B - Rebased
        :keyword list[str] filter_id: Filter ID used to define a subset of data over which the search will be executed.
            When combined with additional search criterion, the result will be an intesection of both.

        :return: Object containing layout databases list.
        :rtype: ceic_api_client.models.layout_items_result.LayoutItemsResult
        """

        instance = Ceic._get_instance()

        if keyword is not None and keyword.strip() != "":
            kwargs["keyword"] = keyword

        get_layouts_method = instance._layouts_facade.get_layout_databases
        result = instance._make_request(get_layouts_method, **kwargs)

        return result

    @staticmethod
    def get_layout_database_topics(database_id, keyword=None, **kwargs):
        """
        Returns list of topics for a specific database.

        :param database_id: The database ID
        :type database_id: str
        :param keyword: Search term. One or more keywords.
                        May contain special words further controlling the search results. Keyword search tips:
                            * Retail Sales - Show series with both keywords while
                                the sequence of keywords is irrelevant.
                                Equivalent to search Sales Retail
                            * Retail AND Sales - Show results: series with terms of Retail AND Sales,
                                regardless of the sequence. E. g. Retail Sales, Automobile Sales Retail.
                            * Retail;Sales - Show series with either keyword and series with both keywords while
                                the sequence of keywords is irrelevant, equivalent to search: Sales;Retail
                            * Retail OR Sales - Show results: series with terms of Retail OR Sales,
                                regardless of the sequence. E. g. Retail Sales, Retail Trade,
                                Sales Price, Motor Vehicle Sales
                            * Retail NOT Sales - Narrow a search by excluding specific terms while
                                the sequence of keywords is relevant. Show results: series with terms that
                                include Retail, but NOT Sales. E. g. Retail Trade, Retail Price, Retail Bank
                            * Retail Sales NOT (Hong Kong) - Narrow a search by excluding a set of words in parentheses
                                while the sequence of keywords in parentheses is irrelevant, equivalent to search:
                                Retail Sales NOT (Hong Kong). Show results: series with terms that
                                include Retail Sales, but NOT Hong Kong, such as
                                Retail Sales YoY: China, Retail Sales YoY: United States
        :type keyword: str

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.
        :keyword list[str] frequency: Frequency filter. One or more comma separated frequency code values.
            D - Daily W - Weekly M - Monthly Q - Quarterly S - Semi-annual Y - Annual
        :keyword list[str] country: Country filter. One or more comma separated country code values.
            See related Dictionary function to get the full list of accepted countries.
        :keyword list[str] source: Source filter. One or more comma separated source code values.
            See related Dictionary function to get the full list of accepted sources.
        :keyword list[str] unit: Unit filter. One or more comma separated unit code values.
            See related Dictionary function to get the full list of accepted units.
        :keyword list[str] indicator: Indicator filter. One or more comma separated indicator code values.
            See related Dictionary function to get full list of accepted indicators.
        :keyword list[str] region: Region filter. One or more comma separated region code values.
            See related Dictionary function to get the full list of accepted regions.
        :keyword bool subscribed_only: Show only results for subscribed series when set to `true`.
            By default show results for all the series found.
        :keyword bool key_only: Show only 'key' series when set to `true`.
        :keyword bool new_only: Show only series created less than 1 month ago when set to `true`.
        :keyword bool name_only: This filter related with the `keyword` filter.
            If it's `true` keyword search will be searched only in series name instead of all series attributes.
        :keyword date start_date_before: Will return series with first observation before `start_date_before`
        :keyword date end_date_after: Will return series with last observation after `end_date_after`
        :keyword date created_after: Will return series created after `created_after` date
        :keyword date updated_after: Will return series last time updated after `updated_after` date
        :keyword list[str] status: Status filter. One or more comma separated status code values.
            When not explicitly set, defaults to T.  T - Active C - Discontinued B - Rebased
        :keyword list[str] filter_id: Filter ID used to define a subset of data over which the search will be executed.
            When combined with additional search criterion, the result will be an intesection of both.

        :return: Object containing layout databases list.
        :rtype: ceic_api_client.models.layout_items_result.LayoutItemsResult
        """

        instance = Ceic._get_instance()

        kwargs["id"] = database_id
        if keyword is not None and keyword.strip() != "":
            kwargs["keyword"] = keyword

        get_layouts_method = instance._layouts_facade.get_layout_database_topics
        result = instance._make_request(get_layouts_method, **kwargs)

        return result

    @staticmethod
    def get_layout_topic_sections(topic_id, keyword=None, **kwargs):
        """
        Returns list of sections for a specific topic.

        :param topic_id: The topic ID
        :type topic_id: str
        :param keyword: Search term. One or more keywords.
                        May contain special words further controlling the search results. Keyword search tips:
                            * Retail Sales - Show series with both keywords while
                                the sequence of keywords is irrelevant.
                                Equivalent to search Sales Retail
                            * Retail AND Sales - Show results: series with terms of Retail AND Sales,
                                regardless of the sequence. E. g. Retail Sales, Automobile Sales Retail.
                            * Retail;Sales - Show series with either keyword and series with both keywords while
                                the sequence of keywords is irrelevant, equivalent to search: Sales;Retail
                            * Retail OR Sales - Show results: series with terms of Retail OR Sales,
                                regardless of the sequence. E. g. Retail Sales, Retail Trade,
                                Sales Price, Motor Vehicle Sales
                            * Retail NOT Sales - Narrow a search by excluding specific terms while
                                the sequence of keywords is relevant. Show results: series with terms that
                                include Retail, but NOT Sales. E. g. Retail Trade, Retail Price, Retail Bank
                            * Retail Sales NOT (Hong Kong) - Narrow a search by excluding a set of words in parentheses
                                while the sequence of keywords in parentheses is irrelevant, equivalent to search:
                                Retail Sales NOT (Hong Kong). Show results: series with terms that
                                include Retail Sales, but NOT Hong Kong, such as
                                Retail Sales YoY: China, Retail Sales YoY: United States
        :type keyword: str

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.
        :keyword list[str] frequency: Frequency filter. One or more comma separated frequency code values.
            D - Daily W - Weekly M - Monthly Q - Quarterly S - Semi-annual Y - Annual
        :keyword list[str] country: Country filter. One or more comma separated country code values.
            See related Dictionary function to get the full list of accepted countries.
        :keyword list[str] source: Source filter. One or more comma separated source code values.
            See related Dictionary function to get the full list of accepted sources.
        :keyword list[str] unit: Unit filter. One or more comma separated unit code values.
            See related Dictionary function to get the full list of accepted units.
        :keyword list[str] indicator: Indicator filter. One or more comma separated indicator code values.
            See related Dictionary function to get full list of accepted indicators.
        :keyword list[str] region: Region filter. One or more comma separated region code values.
            See related Dictionary function to get the full list of accepted regions.
        :keyword bool subscribed_only: Show only results for subscribed series when set to `true`.
            By default show results for all the series found.
        :keyword bool key_only: Show only 'key' series when set to `true`.
        :keyword bool new_only: Show only series created less than 1 month ago when set to `true`.
        :keyword bool name_only: This filter related with the `keyword` filter.
            If it's `true` keyword search will be searched only in series name instead of all series attributes.
        :keyword date start_date_before: Will return series with first observation before `start_date_before`
        :keyword date end_date_after: Will return series with last observation after `end_date_after`
        :keyword date created_after: Will return series created after `created_after` date
        :keyword date updated_after: Will return series last time updated after `updated_after` date
        :keyword list[str] status: Status filter. One or more comma separated status code values.
            When not explicitly set, defaults to T.  T - Active C - Discontinued B - Rebased
        :keyword list[str] filter_id: Filter ID used to define a subset of data over which the search will be executed.
            When combined with additional search criterion, the result will be an intesection of both.

        :return: Object containing layout databases list.
        :rtype: ceic_api_client.models.layout_items_result.LayoutItemsResult
        """

        instance = Ceic._get_instance()

        kwargs["id"] = topic_id
        if keyword is not None and keyword.strip() != "":
            kwargs["keyword"] = keyword

        get_layouts_method = instance._layouts_facade.get_layout_topic_sections
        result = instance._make_request(get_layouts_method, **kwargs)

        return result

    @staticmethod
    def get_layout_section_tables(section_id, keyword=None, **kwargs):
        """
        Returns list of tables for a specific section.

        :param section_id: The section ID
        :type section_id: str
        :param keyword: Search term. One or more keywords.
                        May contain special words further controlling the search results. Keyword search tips:
                            * Retail Sales - Show series with both keywords while
                                the sequence of keywords is irrelevant.
                                Equivalent to search Sales Retail
                            * Retail AND Sales - Show results: series with terms of Retail AND Sales,
                                regardless of the sequence. E. g. Retail Sales, Automobile Sales Retail.
                            * Retail;Sales - Show series with either keyword and series with both keywords while
                                the sequence of keywords is irrelevant, equivalent to search: Sales;Retail
                            * Retail OR Sales - Show results: series with terms of Retail OR Sales,
                                regardless of the sequence. E. g. Retail Sales, Retail Trade,
                                Sales Price, Motor Vehicle Sales
                            * Retail NOT Sales - Narrow a search by excluding specific terms while
                                the sequence of keywords is relevant. Show results: series with terms that
                                include Retail, but NOT Sales. E. g. Retail Trade, Retail Price, Retail Bank
                            * Retail Sales NOT (Hong Kong) - Narrow a search by excluding a set of words in parentheses
                                while the sequence of keywords in parentheses is irrelevant, equivalent to search:
                                Retail Sales NOT (Hong Kong). Show results: series with terms that
                                include Retail Sales, but NOT Hong Kong, such as
                                Retail Sales YoY: China, Retail Sales YoY: United States
        :type keyword: str

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.
        :keyword list[str] frequency: Frequency filter. One or more comma separated frequency code values.
            D - Daily W - Weekly M - Monthly Q - Quarterly S - Semi-annual Y - Annual
        :keyword list[str] country: Country filter. One or more comma separated country code values.
            See related Dictionary function to get the full list of accepted countries.
        :keyword list[str] source: Source filter. One or more comma separated source code values.
            See related Dictionary function to get the full list of accepted sources.
        :keyword list[str] unit: Unit filter. One or more comma separated unit code values.
            See related Dictionary function to get the full list of accepted units.
        :keyword list[str] indicator: Indicator filter. One or more comma separated indicator code values.
            See related Dictionary function to get full list of accepted indicators.
        :keyword list[str] region: Region filter. One or more comma separated region code values.
            See related Dictionary function to get the full list of accepted regions.
        :keyword bool subscribed_only: Show only results for subscribed series when set to `true`.
            By default show results for all the series found.
        :keyword bool key_only: Show only 'key' series when set to `true`.
        :keyword bool new_only: Show only series created less than 1 month ago when set to `true`.
        :keyword bool name_only: This filter related with the `keyword` filter.
            If it's `true` keyword search will be searched only in series name instead of all series attributes.
        :keyword date start_date_before: Will return series with first observation before `start_date_before`
        :keyword date end_date_after: Will return series with last observation after `end_date_after`
        :keyword date created_after: Will return series created after `created_after` date
        :keyword date updated_after: Will return series last time updated after `updated_after` date
        :keyword list[str] status: Status filter. One or more comma separated status code values.
            When not explicitly set, defaults to T.  T - Active C - Discontinued B - Rebased
        :keyword list[str] filter_id: Filter ID used to define a subset of data over which the search will be executed.
            When combined with additional search criterion, the result will be an intesection of both.

        :return: Object containing layout databases list.
        :rtype: ceic_api_client.models.layout_items_result.LayoutItemsResult
        """

        instance = Ceic._get_instance()

        kwargs["id"] = section_id
        if keyword is not None and keyword.strip() != "":
            kwargs["keyword"] = keyword

        get_layouts_method = instance._layouts_facade.get_layout_section_tables
        result = instance._make_request(get_layouts_method, **kwargs)

        return result

    @staticmethod
    def get_layout_table_series(table_id, keyword=None, **kwargs):
        """
        Returns list of series inside of a specific table

        :param table_id: The section ID
        :type table_id: str
        :param keyword: Search term. One or more keywords.
                        May contain special words further controlling the search results. Keyword search tips:
                            * Retail Sales - Show series with both keywords while
                                the sequence of keywords is irrelevant.
                                Equivalent to search Sales Retail
                            * Retail AND Sales - Show results: series with terms of Retail AND Sales,
                                regardless of the sequence. E. g. Retail Sales, Automobile Sales Retail.
                            * Retail;Sales - Show series with either keyword and series with both keywords while
                                the sequence of keywords is irrelevant, equivalent to search: Sales;Retail
                            * Retail OR Sales - Show results: series with terms of Retail OR Sales,
                                regardless of the sequence. E. g. Retail Sales, Retail Trade,
                                Sales Price, Motor Vehicle Sales
                            * Retail NOT Sales - Narrow a search by excluding specific terms while
                                the sequence of keywords is relevant. Show results: series with terms that
                                include Retail, but NOT Sales. E. g. Retail Trade, Retail Price, Retail Bank
                            * Retail Sales NOT (Hong Kong) - Narrow a search by excluding a set of words in parentheses
                                while the sequence of keywords in parentheses is irrelevant, equivalent to search:
                                Retail Sales NOT (Hong Kong). Show results: series with terms that
                                include Retail Sales, but NOT Hong Kong, such as
                                Retail Sales YoY: China, Retail Sales YoY: United States
        :type keyword: str

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.
        :keyword list[str] frequency: Frequency filter. One or more comma separated frequency code values.
            D - Daily W - Weekly M - Monthly Q - Quarterly S - Semi-annual Y - Annual
        :keyword list[str] country: Country filter. One or more comma separated country code values.
            See related Dictionary function to get the full list of accepted countries.
        :keyword list[str] source: Source filter. One or more comma separated source code values.
            See related Dictionary function to get the full list of accepted sources.
        :keyword list[str] unit: Unit filter. One or more comma separated unit code values.
            See related Dictionary function to get the full list of accepted units.
        :keyword list[str] indicator: Indicator filter. One or more comma separated indicator code values.
            See related Dictionary function to get full list of accepted indicators.
        :keyword list[str] region: Region filter. One or more comma separated region code values.
            See related Dictionary function to get the full list of accepted regions.
        :keyword bool subscribed_only: Show only results for subscribed series when set to `true`.
            By default show results for all the series found.
        :keyword bool key_only: Show only 'key' series when set to `true`.
        :keyword bool new_only: Show only series created less than 1 month ago when set to `true`.
        :keyword bool name_only: This filter related with the `keyword` filter.
            If it's `true` keyword search will be searched only in series name instead of all series attributes.
        :keyword date start_date_before: Will return series with first observation before `start_date_before`
        :keyword date end_date_after: Will return series with last observation after `end_date_after`
        :keyword date created_after: Will return series created after `created_after` date
        :keyword date updated_after: Will return series last time updated after `updated_after` date
        :keyword list[str] status: Status filter. One or more comma separated status code values.
            When not explicitly set, defaults to T.  T - Active C - Discontinued B - Rebased
        :keyword list[str] filter_id: Filter ID used to define a subset of data over which the search will be executed.
            When combined with additional search criterion, the result will be an intesection of both.

        :return: Object containing layout databases list.
        :rtype: ceic_api_client.models.layout_items_result.LayoutItemsResult
        """

        instance = Ceic._get_instance()

        kwargs["id"] = table_id
        if keyword is not None and keyword.strip() != "":
            kwargs["keyword"] = keyword

        get_layouts_method = instance._layouts_facade.get_layout_table_series
        result = instance._make_request(get_layouts_method, **kwargs)

        return result

    @staticmethod
    def get_insights(**kwargs):
        """
        Returns full list of CDMNext user created insights.

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.

        :return: Object containing insights list.
        :rtype: ceic_api_client.models.insights_result.InsightsResult
        """

        instance = Ceic._get_instance()

        get_insights_method = instance._insights_facade.get_insights
        result = instance._make_request(get_insights_method, **kwargs)

        return result

    @staticmethod
    def search_insights(keyword=None, **kwargs):
        """
        Search for insights. Those could be user created, shared, or CEIC created ones.
        
        :param keyword: Search term. One or more keywords.
                        May contain special words further controlling the search results. Keyword search tips:
                            * Retail Sales - Show series with both keywords while
                                the sequence of keywords is irrelevant.
                                Equivalent to search Sales Retail
                            * Retail AND Sales - Show results: series with terms of Retail AND Sales,
                                regardless of the sequence. E. g. Retail Sales, Automobile Sales Retail.
                            * Retail;Sales - Show series with either keyword and series with both keywords while
                                the sequence of keywords is irrelevant, equivalent to search: Sales;Retail
                            * Retail OR Sales - Show results: series with terms of Retail OR Sales,
                                regardless of the sequence. E. g. Retail Sales, Retail Trade,
                                Sales Price, Motor Vehicle Sales
                            * Retail NOT Sales - Narrow a search by excluding specific terms while
                                the sequence of keywords is relevant. Show results: series with terms that
                                include Retail, but NOT Sales. E. g. Retail Trade, Retail Price, Retail Bank
                            * Retail Sales NOT (Hong Kong) - Narrow a search by excluding a set of words in parentheses
                                while the sequence of keywords in parentheses is irrelevant, equivalent to search:
                                Retail Sales NOT (Hong Kong). Show results: series with terms that
                                include Retail Sales, but NOT Hong Kong, such as
                                Retail Sales YoY: China, Retail Sales YoY: United States
        :type keyword: str

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.
        :keyword str group: Insights group. Default is `my`. Possible values:
                            * favorite
                            * my
                            * analytics
                            * shared
                            * recent
                            * all
                            * gallery
                            * data_talk
                            * wpic_platinum
        :keyword float limit: Number of records to return
        :keyword float offset: The offset from which the records will be returned
        :keyword str order: Sort order. Possible values:
                            * name
                            * edit_date
                            * open_date
        :keyword str direction: Sort order direction. Possible values:
                            * asc
                            * desc
        :keyword list[str] tags: List of insight tags to search by tag
        :keyword list[str] categories: List of insights categories to search by category

        :return: An iterable object which contains result data. Each object can contain up to 20 result objects.
        :rtype: ceic_api_client.facade.pyceic_facade_models.CeicSearchInsightsResult
        """
        
        instance = Ceic._get_instance()

        if keyword is not None and keyword.strip() != "":
            kwargs["keyword"] = keyword

        search_insights_method = instance._insights_facade.search_insights
        result = instance._make_request(search_insights_method, **kwargs)

        return result

    @staticmethod
    def get_insights_categories(**kwargs):
        """
        Returns list of insight categories.
        To be used wtih group filters \"favorite\", \"my\", \"shared\", \"recent\", all\".

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.

        :return: Object containing insight categories list.
        :rtype: ceic_api_client.models.insights_categories_result.InsightsCategoriesResult
        """

        instance = Ceic._get_instance()

        get_insight_categories_method = instance._insights_facade.get_insights_categories
        result = instance._make_request(get_insight_categories_method, **kwargs)

        return result
    
    @staticmethod
    def get_gallery_insights_categories(**kwargs):
        """
        Returns list of gallery categories. To be used with group filters \"analytics\" and \"gallery\".

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.

        :return: Object containing gallery insight categories list.
        :rtype: ceic_api_client.models.insights_categories_result.InsightsCategoriesResult
        """

        instance = Ceic._get_instance()
        
        get_gallery_insights_categories_method = instance._insights_facade.get_gallery_insights_categories
        result = instance._make_request(get_gallery_insights_categories_method, **kwargs)

        return result

    @staticmethod
    def get_insight(insight_id, **kwargs):
        """
        Returns information about a specified insight.

        :param insight_id: The insight ID
        :type insight_id: str

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.

        :return: Object containing insight result data.
        :rtype: ceic_api_client.models.insights_result.InsightsResult
        """

        instance = Ceic._get_instance()

        kwargs["id"] = insight_id
        get_insight_method = instance._insights_facade.get_insight
        result = instance._make_request(get_insight_method, **kwargs)

        return result

    @staticmethod
    def download_insight(insight_id, file_format, **kwargs):
        """
        Returns one or more links to the insight report.
        When the report generation takes too much time to complete in a timely manner, returns HTTP 408.
        In this case the request have to be repeated after a minute.
        Once the report is generated, consecutive requests are returned immediately.
        Each successful response returns one or more download links that expires in 5 minutes.
        The client application consuming the API shall download the file within this period or
        send additional request to the API.

        :param insight_id: The insight ID
        :type insight_id: str
        :param file_format: Insight report file format. Possible values:
                            * xlsx
                            * pdf
        :type file_format: str

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.

        :return: Object containing links to the insight report.
        :rtype: ceic_api_client.models.insight_download_result.InsightDownloadResult
        """

        instance = Ceic._get_instance()

        kwargs["id"] = insight_id
        kwargs["file_format"] = file_format
        download_insight_method = instance._insights_facade.download_insight
        result = instance._make_request(download_insight_method, **kwargs)

        return result

    @staticmethod
    def get_insight_series(insight_id, **kwargs):
        """
        Returns all series from the specified insight(s), including all time-points and metadata,
        as well as their layout in the insight context in terms of grouping and separators.

        :param insight_id: The insight ID
        :type insight_id: str

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.
        :keyword int count: Limit the amount of latest time-points returned, by the number specified.
        :keyword date start_date: Limits the start date after which the time-points will be returned.
        :keyword date end_date: Limits the end date before which the time-points will be returned.
        :keyword datetime updated_after: Returns only the updated time-points after the date specified.
        :keyword bool blank_observations: If it's set to true, empty time-points will be returned.
        :keyword bool with_replacements_metadata: If it is `true` result will contain
            replacements metadata not only list of id`s.
        :keyword str time_points_status: Time points filter. One or more comma separated status code values.
            When not explicitly set, defaults to `active`. Possible values:
                            * active
                            * deleted
        :keyword float limit: Number of records to return in the range 1 - 100. Default is 100.
        :keyword float offset: The offset from which the records will be returned.

        :return: An iterable object containing insight series result data.
            Each object can contain up to 20 result objects.
        :rtype: ceic_api_client.facade.pyceic_facade_models.CeicGetInsightSeriesResult
        """
        
        instance = Ceic._get_instance()

        kwargs["id"] = insight_id
        get_insight_series_method = instance._insights_facade.get_insight_series
        result = instance._make_request(get_insight_series_method, **kwargs)

        return result

    @staticmethod
    def get_insight_series_data(insight_id, **kwargs):
        """
        Returns all series time-points from the specified insight series.

        :param insight_id: The insight ID
        :type insight_id: str

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.
        :keyword int count: Limit the amount of latest time-points returned, by the number specified.
        :keyword date start_date: Limits the start date after which the time-points will be returned.
        :keyword date end_date: Limits the end date before which the time-points will be returned.
        :keyword datetime updated_after: Returns only the updated time-points after the date specified.
        :keyword bool blank_observations: If it's set to true, empty time-points will be returned.
        :keyword str time_points_status: Time points filter. One or more comma separated status code values.
            When not explicitly set, defaults to `active`. Possible values:
                            * active
                            * deleted
        :keyword float limit: Number of records to return in the range 1 - 100. Default is 100.
        :keyword float offset: The offset from which the records will be returned.

        :return: An iterable object containing insight series time-points result data.
            Each object can contain up to 20 result objects.
        :rtype: ceic_api_client.facade.pyceic_facade_models.CeicGetInsightSeriesResult
        """

        instance = Ceic._get_instance()

        kwargs["id"] = insight_id
        get_insight_series_data_method = instance._insights_facade.get_insight_series_data
        result = instance._make_request(get_insight_series_data_method, **kwargs)

        return result

    @staticmethod
    def get_insight_series_metadata(insight_id, **kwargs):
        """
        Returns all series metadata from the specified insight(s),
        as well as their layout in the insight context in terms of grouping and separators.

        :param insight_id: The insight ID
        :type insight_id: str

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.
        :keyword bool with_replacements_metadata: If it is `true` result will contain
            replacements metadata not only list of id`s.
        :keyword float limit: Number of records to return in the range 1 - 100. Default is 100.
        :keyword float offset: The offset from which the records will be returned.

        :return: An iterable object containing insight series metadata result.
            Each object can contain up to 20 result objects.
        :rtype: ceic_api_client.facade.pyceic_facade_models.CeicGetInsightSeriesResult
        """

        instance = Ceic._get_instance()

        kwargs["id"] = insight_id
        get_insight_series_metadata_method = instance._insights_facade.get_insight_series_metadata
        result = instance._make_request(get_insight_series_metadata_method, **kwargs)

        return result

    @staticmethod
    def get_insight_series_for(insight_series_id, **kwargs):
        """
        Returns full series data, based on their insight ID.
        It can include any formulas or transformations applied to the data,
        or changes to the metadata (ex. title) as part of the insight context.

        :param insight_series_id: The insight series ID.
        :type insight_series_id: str

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.
        :keyword int count: Limit the amount of latest time-points returned, by the number specified.
        :keyword date start_date: Limits the start date after which the time-points will be returned.
        :keyword date end_date: Limits the end date before which the time-points will be returned.
        :keyword datetime updated_after: Returns only the updated time-points after the date specified.
        :keyword bool blank_observations: If it's set to true, empty time-points will be returned.
        :keyword bool with_replacements_metadata: If it is `true` result will contain
            replacements metadata not only list of id`s.
        :keyword str time_points_status: Time points filter. One or more comma separated status code values.
            When not explicitly set, defaults to `active`. Possible values:
                            * active
                            * deleted

        :return: An iterable object containing insight series result data for specific insight.
            Each object can contain up to 20 result objects.
        :rtype: ceic_api_client.facade.pyceic_facade_models.CeicGetInsightSeriesListResult
        """
        instance = Ceic._get_instance()

        kwargs["series_id"] = insight_series_id
        get_insight_series_list_method = instance._insights_facade.get_insight_series_list
        result = instance._make_request(get_insight_series_list_method, **kwargs)

        return result

    @staticmethod
    def get_insight_series_data_for(insight_series_id, **kwargs):
        """
        Returns series time-points data, based on their insight ID.
        It can include any formulas or
        transformations applied to the data as part of the insight context.

        :param insight_series_id: The insight series ID.
        :type insight_series_id: str

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.
        :keyword int count: Limit the amount of latest time-points returned, by the number specified.
        :keyword date start_date: Limits the start date after which the time-points will be returned.
        :keyword date end_date: Limits the end date before which the time-points will be returned.
        :keyword datetime updated_after: Returns only the updated time-points after the date specified.
        :keyword bool blank_observations: If it's set to true, empty time-points will be returned.
        :keyword str time_points_status: Time points filter. One or more comma separated status code values.
            When not explicitly set, defaults to `active`. Possible values:
                            * active
                            * deleted

        :return: An iterable object containing insight series time-points result data for specific insight.
            Each object can contain up to 20 result objects.
        :rtype: ceic_api_client.facade.pyceic_facade_models.CeicGetInsightSeriesListResult
        """
        instance = Ceic._get_instance()

        kwargs["series_id"] = insight_series_id
        get_insight_series_data_list_method = instance._insights_facade.get_insight_series_data_list
        result = instance._make_request(get_insight_series_data_list_method, **kwargs)

        return result

    @staticmethod
    def get_insight_series_metadata_for(insight_series_id, **kwargs):
        """
        Returns series metadata, based on their insight ID.
        It can include changes to the metadata (ex. title) as part of the insight context.

        :param insight_series_id: The insight series ID.
        :type insight_series_id: str

        :keyword str lang: Preferred language code in which data will be returned.
            Defaults to `English` if no translation in the language specified is available. Possible Values:
                            * en - English
                            * zh - Chinese
                            * ru - Russian
                            * id - Indonesian
                            * jp - Japanese
        :keyword str format: Response data format. Default is `json`. Possible values:
                            * json
                            * xml
                            * csv
        :keyword bool with_model_information: If set to `true` returns the model names as part of the response.
        :keyword bool with_replacements_metadata: If it is `true` result will contain
            replacements metadata not only list of id`s.

        :return: An iterable object containing insight series metadata result for specific insight.
            Each object can contain up to 20 result objects.
        :rtype: ceic_api_client.facade.pyceic_facade_models.CeicGetInsightSeriesListResult
        """

        instance = Ceic._get_instance()

        kwargs["series_id"] = insight_series_id
        get_insight_series_metadata_list_method = instance._insights_facade.get_insight_series_metadata_list
        result = instance._make_request(get_insight_series_metadata_list_method, **kwargs)

        return result

    @staticmethod
    def _set_token(token):
        instance = Ceic._get_instance()

        instance._ceic_configuration.set_token(token)

        return instance

    @staticmethod
    def _unset_token():
        instance = Ceic._get_instance()

        instance._ceic_configuration.unset_token()

        return instance

    @staticmethod
    def _get_instance():
        if not Ceic._INSTANCE:
            Ceic._INSTANCE = Ceic()

        return Ceic._INSTANCE

    def _init_object(self, username=None, password=None, proxy_url=None, proxy_username=None, proxy_password=None):
        self._ceic_configuration = CeicConfiguration()
        self._ceic_requests_facade = CeicRequestsFacade()

        self._sessions_facade = CeicSessionsFacade(self._ceic_configuration, self._ceic_requests_facade)
        self._series_facade = CeicSeriesFacade(
            self._ceic_configuration,
            self._ceic_requests_facade
        )
        self._dictionary_facade = CeicDictionaryFacade(self._ceic_configuration, self._ceic_requests_facade)
        self._layouts_facade = CeicLayoutFacade(self._ceic_configuration, self._ceic_requests_facade)
        self._insights_facade = CeicInsightsFacade(self._ceic_configuration, self._ceic_requests_facade)

        self._try_set_proxy(proxy_url, proxy_username, proxy_password)
        self._try_login(username, password)

        self._try_set_session()

    def _try_set_proxy(self, proxy_url=None, proxy_username=None, proxy_password=None):
        if proxy_url is not None or proxy_username is not None or proxy_password is not None:
            self.set_proxy(proxy_url, proxy_username, proxy_password)

    def _try_login(self, username=None, password=None):
        if username is not None or password is not None:
            self.login(username, password)

    def _make_request(self, method, **kwargs):
        try:
            result = method(**kwargs)
        except (CeicNotLoggedIn, CeicSessionExpiredException, CeicSessionTerminatedException):
            self.login()
            result = self._make_request(method, **kwargs)

        return result

    def _try_set_session(self):
        if self._sessions_facade.session_id is not None:
            self._ceic_configuration.set_token(self._sessions_facade.session_id)

    def _try_unset_session(self):
        if self._sessions_facade.session_id is None:
            self._ceic_configuration.unset_token()
