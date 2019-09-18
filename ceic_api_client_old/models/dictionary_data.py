# coding: utf-8

"""
    CEIC API

    CEIC API v2 is a new generation RESTful API that provides an easy access to CEIC's analytical and time series information, including all metadata items and time point values. It includes powerful keyword and criteria search, as well as a data feed option – retrieving only the newest time points data, in order to feed user’s own database and compare the actual changes introduced. Supported output formats include XML, JSON and CSV.  API access is secured utilizing API keys and all data transfer encrypted via HTTPS. In order to use any of the API functions, users shall generate such a key. This can be done through user's profile menu under CDMNext. Users can have only one active API key. Generating a new key will invalidate the existing one. API keys have to be included with each HTTP request, either as an `Authorization` header or as `token` query parameter.  All dates for both input parameters and output attributes are in ISO 8601 format (YYYYMMDD or YYYY-MM-DD) in order to avoid misinterpretation of numeric representations of dates and times, particularly when data are transferred between countries with different conventions for writing numeric dates and times.  <p style=\"color: red\">Security Notice: As of June 30, 2018 the CEIC API v2 will not be accessible by clients using SSL or TLS 1.0 security protocol</p>  <ul>         <li>             <a href='https://downloads.ceicdata.com/python/documentation/CEIC+Python+SDK+-+Development%20Guide.html'>CEIC Python SDK - Development Guide</a>         </li>         <li>             <a href='https://downloads.ceicdata.com/php/documentation/CEIC+PHP+SDK+-+Development+Guide.html'>CEIC PHP SDK - Development Guide</a>         </li>         <li>             <a href='https://downloads.ceicdata.com/javascript/documentation/CEIC+JavaScript+SDK+-+Development+Guide.html'>CEIC JavaScript SDK - Development Guide</a>         </li>     <li>   <a href='https://downloads.ceicdata.com/api/documentation/api-release-notes.html'>Release Notes</a>   <span>             <a href=\"https://downloads.ceicdata.com/api/documentation/api-release-notes-rss.xml\">                 <img src=\"https://downloads.ceicdata.com/api/documentation/release-notes-files/rss-logo-rectangle-35x75.png\">             </a>         </span>     </li>  </ul>  <div>     <a href='https://api-status.ceicdata.com/'>Monitor CEIC API Status</a> </div>  # noqa: E501

    OpenAPI spec version: 2.4.13
    Contact: helpdesk@ceicdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ceic_api_client.models.classification import Classification  # noqa: F401,E501
from ceic_api_client.models.country import Country  # noqa: F401,E501
from ceic_api_client.models.indicator import Indicator  # noqa: F401,E501
from ceic_api_client.models.layout import Layout  # noqa: F401,E501
from ceic_api_client.models.region import Region  # noqa: F401,E501
from ceic_api_client.models.source import Source  # noqa: F401,E501
from ceic_api_client.models.unit import Unit  # noqa: F401,E501


class DictionaryData(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'classifications': 'list[Classification]',
        'countries': 'list[Country]',
        'regions': 'list[Region]',
        'sources': 'list[Source]',
        'layouts': 'list[Layout]',
        'units': 'list[Unit]',
        'indicators': 'list[Indicator]'
    }

    attribute_map = {
        'classifications': 'classifications',
        'countries': 'countries',
        'regions': 'regions',
        'sources': 'sources',
        'layouts': 'layouts',
        'units': 'units',
        'indicators': 'indicators'
    }

    def __init__(self, classifications=None, countries=None, regions=None, sources=None, layouts=None, units=None, indicators=None):  # noqa: E501
        """DictionaryData - a model defined in Swagger"""  # noqa: E501

        self._classifications = None
        self._countries = None
        self._regions = None
        self._sources = None
        self._layouts = None
        self._units = None
        self._indicators = None
        self.discriminator = None

        if classifications is not None:
            self.classifications = classifications
        if countries is not None:
            self.countries = countries
        if regions is not None:
            self.regions = regions
        if sources is not None:
            self.sources = sources
        if layouts is not None:
            self.layouts = layouts
        if units is not None:
            self.units = units
        if indicators is not None:
            self.indicators = indicators

    @property
    def classifications(self):
        """Gets the classifications of this DictionaryData.  # noqa: E501

        List of all classifications and their codes  # noqa: E501

        :return: The classifications of this DictionaryData.  # noqa: E501
        :rtype: list[Classification]
        """
        return self._classifications

    @classifications.setter
    def classifications(self, classifications):
        """Sets the classifications of this DictionaryData.

        List of all classifications and their codes  # noqa: E501

        :param classifications: The classifications of this DictionaryData.  # noqa: E501
        :type: list[Classification]
        """

        self._classifications = classifications

    @property
    def countries(self):
        """Gets the countries of this DictionaryData.  # noqa: E501

        List of all countries and their codes  # noqa: E501

        :return: The countries of this DictionaryData.  # noqa: E501
        :rtype: list[Country]
        """
        return self._countries

    @countries.setter
    def countries(self, countries):
        """Sets the countries of this DictionaryData.

        List of all countries and their codes  # noqa: E501

        :param countries: The countries of this DictionaryData.  # noqa: E501
        :type: list[Country]
        """

        self._countries = countries

    @property
    def regions(self):
        """Gets the regions of this DictionaryData.  # noqa: E501

        List of all regions and their codes  # noqa: E501

        :return: The regions of this DictionaryData.  # noqa: E501
        :rtype: list[Region]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """Sets the regions of this DictionaryData.

        List of all regions and their codes  # noqa: E501

        :param regions: The regions of this DictionaryData.  # noqa: E501
        :type: list[Region]
        """

        self._regions = regions

    @property
    def sources(self):
        """Gets the sources of this DictionaryData.  # noqa: E501

        List of all sources and their codes  # noqa: E501

        :return: The sources of this DictionaryData.  # noqa: E501
        :rtype: list[Source]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this DictionaryData.

        List of all sources and their codes  # noqa: E501

        :param sources: The sources of this DictionaryData.  # noqa: E501
        :type: list[Source]
        """

        self._sources = sources

    @property
    def layouts(self):
        """Gets the layouts of this DictionaryData.  # noqa: E501

        DEPRECATED. Use `/layout/databases` instead. List of all database layouts and their codes.  # noqa: E501

        :return: The layouts of this DictionaryData.  # noqa: E501
        :rtype: list[Layout]
        """
        return self._layouts

    @layouts.setter
    def layouts(self, layouts):
        """Sets the layouts of this DictionaryData.

        DEPRECATED. Use `/layout/databases` instead. List of all database layouts and their codes.  # noqa: E501

        :param layouts: The layouts of this DictionaryData.  # noqa: E501
        :type: list[Layout]
        """

        self._layouts = layouts

    @property
    def units(self):
        """Gets the units of this DictionaryData.  # noqa: E501

        List of all units and their codes  # noqa: E501

        :return: The units of this DictionaryData.  # noqa: E501
        :rtype: list[Unit]
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this DictionaryData.

        List of all units and their codes  # noqa: E501

        :param units: The units of this DictionaryData.  # noqa: E501
        :type: list[Unit]
        """

        self._units = units

    @property
    def indicators(self):
        """Gets the indicators of this DictionaryData.  # noqa: E501

        List of all indicators and their codes  # noqa: E501

        :return: The indicators of this DictionaryData.  # noqa: E501
        :rtype: list[Indicator]
        """
        return self._indicators

    @indicators.setter
    def indicators(self, indicators):
        """Sets the indicators of this DictionaryData.

        List of all indicators and their codes  # noqa: E501

        :param indicators: The indicators of this DictionaryData.  # noqa: E501
        :type: list[Indicator]
        """

        self._indicators = indicators

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    @staticmethod
    def _parse_enum_value(value, enum_values):
        for enum_value in enum_values:
            if str(value).lower() == str(enum_value).lower():
                value = enum_value

        return value

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DictionaryData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other