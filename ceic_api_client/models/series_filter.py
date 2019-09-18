# coding: utf-8

"""
    CEIC API

    CEIC API v2 is a new generation RESTful API that provides an easy access to CEIC's analytical and time series information, including all metadata items and time point values. It includes powerful keyword and criteria search, as well as a data feed option – retrieving only the newest time points data, in order to feed user’s own database and compare the actual changes introduced. Supported output formats include XML, JSON and CSV.  API access is secured utilizing API keys and all data transfer encrypted via HTTPS. In order to use any of the API functions, users shall generate such a key. This can be done through user's profile menu under CDMNext. Users can have only one active API key. Generating a new key will invalidate the existing one. API keys have to be included with each HTTP request, either as an `Authorization` header or as `token` query parameter.  All dates for both input parameters and output attributes are in ISO 8601 format (YYYYMMDD or YYYY-MM-DD) in order to avoid misinterpretation of numeric representations of dates and times, particularly when data are transferred between countries with different conventions for writing numeric dates and times.  <p style=\"color: red\">Security Notice: As of June 30, 2018 the CEIC API v2 will not be accessible by clients using SSL or TLS 1.0 security protocol</p>  <ul>         <li>             <a href='https://downloads.ceicdata.com/python/documentation/CEIC+Python+SDK+-+Development%20Guide.html'>CEIC Python SDK - Development Guide</a>         </li>         <li>             <a href='https://downloads.ceicdata.com/php/documentation/CEIC+PHP+SDK+-+Development+Guide.html'>CEIC PHP SDK - Development Guide</a>         </li>         <li>             <a href='https://downloads.ceicdata.com/javascript/documentation/CEIC+JavaScript+SDK+-+Development+Guide.html'>CEIC JavaScript SDK - Development Guide</a>         </li>     <li>   <a href='https://downloads.ceicdata.com/api/documentation/api-release-notes.html'>Release Notes</a>   <span>             <a href=\"https://downloads.ceicdata.com/api/documentation/api-release-notes-rss.xml\">                 <img src=\"https://downloads.ceicdata.com/api/documentation/release-notes-files/rss-logo-rectangle-35x75.png\">             </a>         </span>     </li>  </ul>  <div>     <a href='https://api-status.ceicdata.com/'>Monitor CEIC API Status</a> </div>  # noqa: E501

    OpenAPI spec version: 2.4.12
    Contact: helpdesk@ceicdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ceic_api_client.models.filter_details import FilterDetails  # noqa: F401,E501


class SeriesFilter(object):
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
        'creator_id': 'str',
        'filter_details': 'FilterDetails',
        'created_at': 'date',
        'id': 'str'
    }

    attribute_map = {
        'creator_id': 'creator_id',
        'filter_details': 'filter_details',
        'created_at': 'created_at',
        'id': 'id'
    }

    def __init__(self, creator_id=None, filter_details=None, created_at=None, id=None):  # noqa: E501
        """SeriesFilter - a model defined in Swagger"""  # noqa: E501

        self._creator_id = None
        self._filter_details = None
        self._created_at = None
        self._id = None
        self.discriminator = None

        if creator_id is not None:
            self.creator_id = creator_id
        if filter_details is not None:
            self.filter_details = filter_details
        if created_at is not None:
            self.created_at = created_at
        if id is not None:
            self.id = id

    @property
    def creator_id(self):
        """Gets the creator_id of this SeriesFilter.  # noqa: E501

        User ID  # noqa: E501

        :return: The creator_id of this SeriesFilter.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this SeriesFilter.

        User ID  # noqa: E501

        :param creator_id: The creator_id of this SeriesFilter.  # noqa: E501
        :type: str
        """

        self._creator_id = creator_id

    @property
    def filter_details(self):
        """Gets the filter_details of this SeriesFilter.  # noqa: E501


        :return: The filter_details of this SeriesFilter.  # noqa: E501
        :rtype: FilterDetails
        """
        return self._filter_details

    @filter_details.setter
    def filter_details(self, filter_details):
        """Sets the filter_details of this SeriesFilter.


        :param filter_details: The filter_details of this SeriesFilter.  # noqa: E501
        :type: FilterDetails
        """

        self._filter_details = filter_details

    @property
    def created_at(self):
        """Gets the created_at of this SeriesFilter.  # noqa: E501

        Filter creation time  # noqa: E501

        :return: The created_at of this SeriesFilter.  # noqa: E501
        :rtype: date
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SeriesFilter.

        Filter creation time  # noqa: E501

        :param created_at: The created_at of this SeriesFilter.  # noqa: E501
        :type: date
        """

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this SeriesFilter.  # noqa: E501

        Filter ID  # noqa: E501

        :return: The id of this SeriesFilter.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SeriesFilter.

        Filter ID  # noqa: E501

        :param id: The id of this SeriesFilter.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, SeriesFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
