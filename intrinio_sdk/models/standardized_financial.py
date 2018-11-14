# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Marketplace, we offer a wide selection of financial data feeds sourced by our own proprietary processes as well as from many data vendors. The primary application of the Intrinio API is for use in third-party applications and integrations or for end-users utilizing the Excel add-in and Google Sheets add-on. The Intrinio API uses HTTPS verbs and a RESTful endpoint structure, which makes it easy to request data from Intrinio. Responses are delivered in JSON format. If you need additional help in using the API, go to our home page (https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from intrinio_sdk.models.standardized_tag import StandardizedTag  # noqa: F401,E501


class StandardizedFinancial(object):
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
        'data_tag': 'StandardizedTag',
        'value': 'float'
    }

    attribute_map = {
        'data_tag': 'data_tag',
        'value': 'value'
    }

    def __init__(self, data_tag=None, value=None):  # noqa: E501
        """StandardizedFinancial - a model defined in Swagger"""  # noqa: E501

        self._data_tag = None
        self._value = None
        self.discriminator = None

        if data_tag is not None:
            self.data_tag = data_tag
        if value is not None:
            self.value = value

    @property
    def data_tag(self):
        """Gets the data_tag of this StandardizedFinancial.  # noqa: E501


        :return: The data_tag of this StandardizedFinancial.  # noqa: E501
        :rtype: StandardizedTag
        """
        return self._data_tag

    @data_tag.setter
    def data_tag(self, data_tag):
        """Sets the data_tag of this StandardizedFinancial.


        :param data_tag: The data_tag of this StandardizedFinancial.  # noqa: E501
        :type: StandardizedTag
        """

        self._data_tag = data_tag

    @property
    def value(self):
        """Gets the value of this StandardizedFinancial.  # noqa: E501

        The value for the Standardized Tag within the scope of the Fundamental  # noqa: E501

        :return: The value of this StandardizedFinancial.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this StandardizedFinancial.

        The value for the Standardized Tag within the scope of the Fundamental  # noqa: E501

        :param value: The value of this StandardizedFinancial.  # noqa: E501
        :type: float
        """

        self._value = value

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

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StandardizedFinancial):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
