# coding: utf-8

# flake8: noqa

"""
    CEIC API

    CEIC API v2 is a new generation RESTful API that provides an easy access to CEIC's analytical and time series information, including all metadata items and time point values. It includes powerful keyword and criteria search, as well as a data feed option – retrieving only the newest time points data, in order to feed user’s own database and compare the actual changes introduced. Supported output formats include XML, JSON and CSV.  API access is secured utilizing API keys and all data transfer encrypted via HTTPS. In order to use any of the API functions, users shall generate such a key. This can be done through user's profile menu under CDMNext. Users can have only one active API key. Generating a new key will invalidate the existing one. API keys have to be included with each HTTP request, either as an `Authorization` header or as `token` query parameter.  All dates for both input parameters and output attributes are in ISO 8601 format (YYYYMMDD or YYYY-MM-DD) in order to avoid misinterpretation of numeric representations of dates and times, particularly when data are transferred between countries with different conventions for writing numeric dates and times.  <p style=\"color: red\">Security Notice: As of June 30, 2018 the CEIC API v2 will not be accessible by clients using SSL or TLS 1.0 security protocol</p>  <ul>         <li>             <a href='https://downloads.ceicdata.com/python/documentation/CEIC+Python+SDK+-+Development%20Guide.html'>CEIC Python SDK - Development Guide</a>         </li>         <li>             <a href='https://downloads.ceicdata.com/php/documentation/CEIC+PHP+SDK+-+Development+Guide.html'>CEIC PHP SDK - Development Guide</a>         </li>         <li>             <a href='https://downloads.ceicdata.com/javascript/documentation/CEIC+JavaScript+SDK+-+Development+Guide.html'>CEIC JavaScript SDK - Development Guide</a>         </li>     <li>   <a href='https://downloads.ceicdata.com/api/documentation/api-release-notes.html'>Release Notes</a>   <span>             <a href=\"https://downloads.ceicdata.com/api/documentation/api-release-notes-rss.xml\">                 <img src=\"https://downloads.ceicdata.com/api/documentation/release-notes-files/rss-logo-rectangle-35x75.png\">             </a>         </span>     </li>  </ul>  <div>     <a href='https://api-status.ceicdata.com/'>Monitor CEIC API Status</a> </div>  # noqa: E501

    OpenAPI spec version: 2.4.12
    Contact: helpdesk@ceicdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from ceic_api_client.apis.dictionary_api import DictionaryApi
from ceic_api_client.apis.dumps_api import DumpsApi
from ceic_api_client.apis.feeds_api import FeedsApi
from ceic_api_client.apis.filters_api import FiltersApi
from ceic_api_client.apis.insights_api import InsightsApi
from ceic_api_client.apis.layout_api import LayoutApi
from ceic_api_client.apis.series_api import SeriesApi
from ceic_api_client.apis.sessions_api import SessionsApi
from ceic_api_client.apis.default_api import DefaultApi

# import ApiClient
from ceic_api_client.api_client import ApiClient
from ceic_api_client.configuration import Configuration
# import models into sdk package
from ceic_api_client.models.base_series_information import BaseSeriesInformation
from ceic_api_client.models.classification import Classification
from ceic_api_client.models.classifications_result import ClassificationsResult
from ceic_api_client.models.countries_result import CountriesResult
from ceic_api_client.models.country import Country
from ceic_api_client.models.dictionary_data import DictionaryData
from ceic_api_client.models.dictionary_result import DictionaryResult
from ceic_api_client.models.dump_information import DumpInformation
from ceic_api_client.models.dump_result import DumpResult
from ceic_api_client.models.empty_object import EmptyObject
from ceic_api_client.models.facet import Facet
from ceic_api_client.models.facet_entry import FacetEntry
from ceic_api_client.models.feed_information import FeedInformation
from ceic_api_client.models.feed_result import FeedResult
from ceic_api_client.models.feeds_result import FeedsResult
from ceic_api_client.models.filter_details import FilterDetails
from ceic_api_client.models.filter_details_search import FilterDetailsSearch
from ceic_api_client.models.filters_result import FiltersResult
from ceic_api_client.models.frequencies_result import FrequenciesResult
from ceic_api_client.models.frequency import Frequency
from ceic_api_client.models.impersonate_api_key import ImpersonateAPIKey
from ceic_api_client.models.impersonate_api_key_result import ImpersonateAPIKeyResult
from ceic_api_client.models.indicator import Indicator
from ceic_api_client.models.indicators_result import IndicatorsResult
from ceic_api_client.models.insight_download import InsightDownload
from ceic_api_client.models.insight_download_result import InsightDownloadResult
from ceic_api_client.models.insight_series import InsightSeries
from ceic_api_client.models.insight_series_information import InsightSeriesInformation
from ceic_api_client.models.insight_series_result import InsightSeriesResult
from ceic_api_client.models.insights import Insights
from ceic_api_client.models.insights_categories_result import InsightsCategoriesResult
from ceic_api_client.models.insights_category import InsightsCategory
from ceic_api_client.models.insights_result import InsightsResult
from ceic_api_client.models.insights_search import InsightsSearch
from ceic_api_client.models.insights_search_result import InsightsSearchResult
from ceic_api_client.models.layout import Layout
from ceic_api_client.models.layout_information import LayoutInformation
from ceic_api_client.models.layout_item import LayoutItem
from ceic_api_client.models.layout_item_metadata import LayoutItemMetadata
from ceic_api_client.models.layout_items_result import LayoutItemsResult
from ceic_api_client.models.layouts_result import LayoutsResult
from ceic_api_client.models.province import Province
from ceic_api_client.models.region import Region
from ceic_api_client.models.regions_result import RegionsResult
from ceic_api_client.models.response_error import ResponseError
from ceic_api_client.models.search_series import SearchSeries
from ceic_api_client.models.search_series_result import SearchSeriesResult
from ceic_api_client.models.series import Series
from ceic_api_client.models.series_data import SeriesData
from ceic_api_client.models.series_filter import SeriesFilter
from ceic_api_client.models.series_information import SeriesInformation
from ceic_api_client.models.series_metadata import SeriesMetadata
from ceic_api_client.models.series_metadata_last_change import SeriesMetadataLastChange
from ceic_api_client.models.series_replacements import SeriesReplacements
from ceic_api_client.models.series_result import SeriesResult
from ceic_api_client.models.series_ui_settings import SeriesUISettings
from ceic_api_client.models.session_status import SessionStatus
from ceic_api_client.models.session_status_result import SessionStatusResult
from ceic_api_client.models.source import Source
from ceic_api_client.models.sources_result import SourcesResult
from ceic_api_client.models.status import Status
from ceic_api_client.models.statuses_result import StatusesResult
from ceic_api_client.models.time_point import TimePoint
from ceic_api_client.models.unit import Unit
from ceic_api_client.models.units_result import UnitsResult
from ceic_api_client.models.user_information import UserInformation
from ceic_api_client.models.user_session import UserSession
from ceic_api_client.models.user_session_result import UserSessionResult