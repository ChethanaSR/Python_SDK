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

from ceic_api_client.models.insights_category import InsightsCategory  # noqa: F401,E501
from ceic_api_client.models.user_information import UserInformation  # noqa: F401,E501


class Insights(object):
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
        'category': 'InsightsCategory',
        'subscribed': 'str',
        'description': 'str',
        'last_update_time': 'datetime',
        'creator': 'UserInformation',
        'creation_time': 'datetime',
        'keywords': 'list[str]',
        'last_editor': 'UserInformation',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'category': 'category',
        'subscribed': 'subscribed',
        'description': 'description',
        'last_update_time': 'lastUpdateTime',
        'creator': 'creator',
        'creation_time': 'creationTime',
        'keywords': 'keywords',
        'last_editor': 'lastEditor',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, category=None, subscribed=None, description=None, last_update_time=None, creator=None, creation_time=None, keywords=None, last_editor=None, id=None, name=None):  # noqa: E501
        """Insights - a model defined in Swagger"""  # noqa: E501

        self._category = None
        self._subscribed = None
        self._description = None
        self._last_update_time = None
        self._creator = None
        self._creation_time = None
        self._keywords = None
        self._last_editor = None
        self._id = None
        self._name = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if subscribed is not None:
            self.subscribed = subscribed
        if description is not None:
            self.description = description
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if creator is not None:
            self.creator = creator
        if creation_time is not None:
            self.creation_time = creation_time
        if keywords is not None:
            self.keywords = keywords
        if last_editor is not None:
            self.last_editor = last_editor
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def category(self):
        """Gets the category of this Insights.  # noqa: E501


        :return: The category of this Insights.  # noqa: E501
        :rtype: InsightsCategory
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Insights.


        :param category: The category of this Insights.  # noqa: E501
        :type: InsightsCategory
        """

        self._category = category

    @property
    def subscribed(self):
        """Gets the subscribed of this Insights.  # noqa: E501

        Indicates whether the user is subscribed or not for the insight  # noqa: E501

        :return: The subscribed of this Insights.  # noqa: E501
        :rtype: str
        """
        return self._subscribed

    @subscribed.setter
    def subscribed(self, subscribed):
        """Sets the subscribed of this Insights.

        Indicates whether the user is subscribed or not for the insight  # noqa: E501

        :param subscribed: The subscribed of this Insights.  # noqa: E501
        :type: str
        """

        self._subscribed = subscribed

    @property
    def description(self):
        """Gets the description of this Insights.  # noqa: E501

        Insight description  # noqa: E501

        :return: The description of this Insights.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Insights.

        Insight description  # noqa: E501

        :param description: The description of this Insights.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def last_update_time(self):
        """Gets the last_update_time of this Insights.  # noqa: E501

        The last update date/time  # noqa: E501

        :return: The last_update_time of this Insights.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this Insights.

        The last update date/time  # noqa: E501

        :param last_update_time: The last_update_time of this Insights.  # noqa: E501
        :type: datetime
        """

        self._last_update_time = last_update_time

    @property
    def creator(self):
        """Gets the creator of this Insights.  # noqa: E501


        :return: The creator of this Insights.  # noqa: E501
        :rtype: UserInformation
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this Insights.


        :param creator: The creator of this Insights.  # noqa: E501
        :type: UserInformation
        """

        self._creator = creator

    @property
    def creation_time(self):
        """Gets the creation_time of this Insights.  # noqa: E501

        Creation date/time  # noqa: E501

        :return: The creation_time of this Insights.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this Insights.

        Creation date/time  # noqa: E501

        :param creation_time: The creation_time of this Insights.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def keywords(self):
        """Gets the keywords of this Insights.  # noqa: E501

        List of keywords  # noqa: E501

        :return: The keywords of this Insights.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this Insights.

        List of keywords  # noqa: E501

        :param keywords: The keywords of this Insights.  # noqa: E501
        :type: list[str]
        """

        self._keywords = keywords

    @property
    def last_editor(self):
        """Gets the last_editor of this Insights.  # noqa: E501


        :return: The last_editor of this Insights.  # noqa: E501
        :rtype: UserInformation
        """
        return self._last_editor

    @last_editor.setter
    def last_editor(self, last_editor):
        """Sets the last_editor of this Insights.


        :param last_editor: The last_editor of this Insights.  # noqa: E501
        :type: UserInformation
        """

        self._last_editor = last_editor

    @property
    def id(self):
        """Gets the id of this Insights.  # noqa: E501

        Insight ID  # noqa: E501

        :return: The id of this Insights.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Insights.

        Insight ID  # noqa: E501

        :param id: The id of this Insights.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Insights.  # noqa: E501

        Insight name  # noqa: E501

        :return: The name of this Insights.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Insights.

        Insight name  # noqa: E501

        :param name: The name of this Insights.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, Insights):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other