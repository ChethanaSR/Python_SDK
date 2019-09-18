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


class DumpInformation(object):
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
        'status': 'str',
        'total_series_number': 'float',
        'download_link': 'str',
        'collected_series_number': 'float',
        'progress': 'str',
        'id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'total_series_number': 'totalSeriesNumber',
        'download_link': 'downloadLink',
        'collected_series_number': 'collectedSeriesNumber',
        'progress': 'progress',
        'id': 'id'
    }

    def __init__(self, status=None, total_series_number=None, download_link=None, collected_series_number=None, progress=None, id=None):  # noqa: E501
        """DumpInformation - a model defined in Swagger"""  # noqa: E501

        self._status = None
        self._total_series_number = None
        self._download_link = None
        self._collected_series_number = None
        self._progress = None
        self._id = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if total_series_number is not None:
            self.total_series_number = total_series_number
        if download_link is not None:
            self.download_link = download_link
        if collected_series_number is not None:
            self.collected_series_number = collected_series_number
        if progress is not None:
            self.progress = progress
        if id is not None:
            self.id = id

    @property
    def status(self):
        """Gets the status of this DumpInformation.  # noqa: E501

        Status of generation process  # noqa: E501

        :return: The status of this DumpInformation.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DumpInformation.

        Status of generation process  # noqa: E501

        :param status: The status of this DumpInformation.  # noqa: E501
        :type: str
        """
        allowed_values = ["INITIALIZED", "RETRIEVING_DATA", "CONSOLIDATING_RESULTS", "DONE", "ERROR"]  # noqa: E501

        status = self._parse_enum_value(status, allowed_values)
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def total_series_number(self):
        """Gets the total_series_number of this DumpInformation.  # noqa: E501

        Number of series to generate  # noqa: E501

        :return: The total_series_number of this DumpInformation.  # noqa: E501
        :rtype: float
        """
        return self._total_series_number

    @total_series_number.setter
    def total_series_number(self, total_series_number):
        """Sets the total_series_number of this DumpInformation.

        Number of series to generate  # noqa: E501

        :param total_series_number: The total_series_number of this DumpInformation.  # noqa: E501
        :type: float
        """

        self._total_series_number = total_series_number

    @property
    def download_link(self):
        """Gets the download_link of this DumpInformation.  # noqa: E501

        Link to download generated file  # noqa: E501

        :return: The download_link of this DumpInformation.  # noqa: E501
        :rtype: str
        """
        return self._download_link

    @download_link.setter
    def download_link(self, download_link):
        """Sets the download_link of this DumpInformation.

        Link to download generated file  # noqa: E501

        :param download_link: The download_link of this DumpInformation.  # noqa: E501
        :type: str
        """

        self._download_link = download_link

    @property
    def collected_series_number(self):
        """Gets the collected_series_number of this DumpInformation.  # noqa: E501

        Number of processed series  # noqa: E501

        :return: The collected_series_number of this DumpInformation.  # noqa: E501
        :rtype: float
        """
        return self._collected_series_number

    @collected_series_number.setter
    def collected_series_number(self, collected_series_number):
        """Sets the collected_series_number of this DumpInformation.

        Number of processed series  # noqa: E501

        :param collected_series_number: The collected_series_number of this DumpInformation.  # noqa: E501
        :type: float
        """

        self._collected_series_number = collected_series_number

    @property
    def progress(self):
        """Gets the progress of this DumpInformation.  # noqa: E501

        % of completed  # noqa: E501

        :return: The progress of this DumpInformation.  # noqa: E501
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this DumpInformation.

        % of completed  # noqa: E501

        :param progress: The progress of this DumpInformation.  # noqa: E501
        :type: str
        """

        self._progress = progress

    @property
    def id(self):
        """Gets the id of this DumpInformation.  # noqa: E501

        Dump ID  # noqa: E501

        :return: The id of this DumpInformation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DumpInformation.

        Dump ID  # noqa: E501

        :param id: The id of this DumpInformation.  # noqa: E501
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
        if not isinstance(other, DumpInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
