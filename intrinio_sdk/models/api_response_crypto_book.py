# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from intrinio_sdk.models.crypto_book_entry import CryptoBookEntry  # noqa: F401,E501
from intrinio_sdk.models.crypto_exchange_summary import CryptoExchangeSummary  # noqa: F401,E501
from intrinio_sdk.models.crypto_pair_summary import CryptoPairSummary  # noqa: F401,E501


class ApiResponseCryptoBook(object):
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
        'bids': 'list[CryptoBookEntry]',
        'asks': 'list[CryptoBookEntry]',
        'pair': 'CryptoPairSummary',
        'exchange': 'CryptoExchangeSummary',
        'last_updated': 'str'
    }

    attribute_map = {
        'bids': 'bids',
        'asks': 'asks',
        'pair': 'pair',
        'exchange': 'exchange',
        'last_updated': 'last_updated'
    }

    def __init__(self, bids=None, asks=None, pair=None, exchange=None, last_updated=None):  # noqa: E501
        """ApiResponseCryptoBook - a model defined in Swagger"""  # noqa: E501

        self._bids = None
        self._asks = None
        self._pair = None
        self._exchange = None
        self._last_updated = None
        self.discriminator = None

        if bids is not None:
            self.bids = bids
        if asks is not None:
            self.asks = asks
        if pair is not None:
            self.pair = pair
        if exchange is not None:
            self.exchange = exchange
        if last_updated is not None:
            self.last_updated = last_updated

    @property
    def bids(self):
        """Gets the bids of this ApiResponseCryptoBook.  # noqa: E501

        The bid prices and their respective sizes, in descending order of price.  # noqa: E501

        :return: The bids of this ApiResponseCryptoBook.  # noqa: E501
        :rtype: list[CryptoBookEntry]
        """
        return self._bids
        
    @property
    def bids_dict(self):
        """Gets the bids of this ApiResponseCryptoBook.  # noqa: E501

        The bid prices and their respective sizes, in descending order of price. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The bids of this ApiResponseCryptoBook.  # noqa: E501
        :rtype: list[CryptoBookEntry]
        """

        result = None

        value = self.bids
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
            result = { 'bids': value }

        
        return result
        

    @bids.setter
    def bids(self, bids):
        """Sets the bids of this ApiResponseCryptoBook.

        The bid prices and their respective sizes, in descending order of price.  # noqa: E501

        :param bids: The bids of this ApiResponseCryptoBook.  # noqa: E501
        :type: list[CryptoBookEntry]
        """

        self._bids = bids

    @property
    def asks(self):
        """Gets the asks of this ApiResponseCryptoBook.  # noqa: E501

        The ask prices and their respective sizes, in ascending order of price.  # noqa: E501

        :return: The asks of this ApiResponseCryptoBook.  # noqa: E501
        :rtype: list[CryptoBookEntry]
        """
        return self._asks
        
    @property
    def asks_dict(self):
        """Gets the asks of this ApiResponseCryptoBook.  # noqa: E501

        The ask prices and their respective sizes, in ascending order of price. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The asks of this ApiResponseCryptoBook.  # noqa: E501
        :rtype: list[CryptoBookEntry]
        """

        result = None

        value = self.asks
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
            result = { 'asks': value }

        
        return result
        

    @asks.setter
    def asks(self, asks):
        """Sets the asks of this ApiResponseCryptoBook.

        The ask prices and their respective sizes, in ascending order of price.  # noqa: E501

        :param asks: The asks of this ApiResponseCryptoBook.  # noqa: E501
        :type: list[CryptoBookEntry]
        """

        self._asks = asks

    @property
    def pair(self):
        """Gets the pair of this ApiResponseCryptoBook.  # noqa: E501


        :return: The pair of this ApiResponseCryptoBook.  # noqa: E501
        :rtype: CryptoPairSummary
        """
        return self._pair
        
    @property
    def pair_dict(self):
        """Gets the pair of this ApiResponseCryptoBook.  # noqa: E501


        :return: The pair of this ApiResponseCryptoBook.  # noqa: E501
        :rtype: CryptoPairSummary
        """

        result = None

        value = self.pair
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
            result = { 'pair': value }

        
        return result
        

    @pair.setter
    def pair(self, pair):
        """Sets the pair of this ApiResponseCryptoBook.


        :param pair: The pair of this ApiResponseCryptoBook.  # noqa: E501
        :type: CryptoPairSummary
        """

        self._pair = pair

    @property
    def exchange(self):
        """Gets the exchange of this ApiResponseCryptoBook.  # noqa: E501


        :return: The exchange of this ApiResponseCryptoBook.  # noqa: E501
        :rtype: CryptoExchangeSummary
        """
        return self._exchange
        
    @property
    def exchange_dict(self):
        """Gets the exchange of this ApiResponseCryptoBook.  # noqa: E501


        :return: The exchange of this ApiResponseCryptoBook.  # noqa: E501
        :rtype: CryptoExchangeSummary
        """

        result = None

        value = self.exchange
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
            result = { 'exchange': value }

        
        return result
        

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this ApiResponseCryptoBook.


        :param exchange: The exchange of this ApiResponseCryptoBook.  # noqa: E501
        :type: CryptoExchangeSummary
        """

        self._exchange = exchange

    @property
    def last_updated(self):
        """Gets the last_updated of this ApiResponseCryptoBook.  # noqa: E501

        The UTC timestamp of when the order book was last updated.  # noqa: E501

        :return: The last_updated of this ApiResponseCryptoBook.  # noqa: E501
        :rtype: str
        """
        return self._last_updated
        
    @property
    def last_updated_dict(self):
        """Gets the last_updated of this ApiResponseCryptoBook.  # noqa: E501

        The UTC timestamp of when the order book was last updated. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The last_updated of this ApiResponseCryptoBook.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.last_updated
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
            result = { 'last_updated': value }

        
        return result
        

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this ApiResponseCryptoBook.

        The UTC timestamp of when the order book was last updated.  # noqa: E501

        :param last_updated: The last_updated of this ApiResponseCryptoBook.  # noqa: E501
        :type: str
        """

        self._last_updated = last_updated

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
        if not isinstance(other, ApiResponseCryptoBook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
