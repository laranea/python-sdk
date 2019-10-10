# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.8.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CryptoBookEntry(object):
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
        'price': 'float',
        'size': 'float'
    }

    attribute_map = {
        'price': 'price',
        'size': 'size'
    }

    def __init__(self, price=None, size=None):  # noqa: E501
        """CryptoBookEntry - a model defined in Swagger"""  # noqa: E501

        self._price = None
        self._size = None
        self.discriminator = None

        if price is not None:
            self.price = price
        if size is not None:
            self.size = size

    @property
    def price(self):
        """Gets the price of this CryptoBookEntry.  # noqa: E501

        The price of the book entry.  # noqa: E501

        :return: The price of this CryptoBookEntry.  # noqa: E501
        :rtype: float
        """
        return self._price
        
    @property
    def price_dict(self):
        """Gets the price of this CryptoBookEntry.  # noqa: E501

        The price of the book entry. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The price of this CryptoBookEntry.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.price
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'price': value }

        
        return result
        

    @price.setter
    def price(self, price):
        """Sets the price of this CryptoBookEntry.

        The price of the book entry.  # noqa: E501

        :param price: The price of this CryptoBookEntry.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def size(self):
        """Gets the size of this CryptoBookEntry.  # noqa: E501

        The size for the price of the book entry.  # noqa: E501

        :return: The size of this CryptoBookEntry.  # noqa: E501
        :rtype: float
        """
        return self._size
        
    @property
    def size_dict(self):
        """Gets the size of this CryptoBookEntry.  # noqa: E501

        The size for the price of the book entry. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The size of this CryptoBookEntry.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.size
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'size': value }

        
        return result
        

    @size.setter
    def size(self, size):
        """Sets the size of this CryptoBookEntry.

        The size for the price of the book entry.  # noqa: E501

        :param size: The size of this CryptoBookEntry.  # noqa: E501
        :type: float
        """

        self._size = size

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
        if not isinstance(other, CryptoBookEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
