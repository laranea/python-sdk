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


class CryptoStat(object):
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
        'name': 'str',
        'code': 'str',
        'symbol': 'str',
        'market_cap_usd': 'float',
        'available_supply': 'float',
        'total_supply': 'float',
        'max_supply': 'float',
        'last_updated': 'str'
    }

    attribute_map = {
        'name': 'name',
        'code': 'code',
        'symbol': 'symbol',
        'market_cap_usd': 'market_cap_usd',
        'available_supply': 'available_supply',
        'total_supply': 'total_supply',
        'max_supply': 'max_supply',
        'last_updated': 'last_updated'
    }

    def __init__(self, name=None, code=None, symbol=None, market_cap_usd=None, available_supply=None, total_supply=None, max_supply=None, last_updated=None):  # noqa: E501
        """CryptoStat - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._code = None
        self._symbol = None
        self._market_cap_usd = None
        self._available_supply = None
        self._total_supply = None
        self._max_supply = None
        self._last_updated = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if code is not None:
            self.code = code
        if symbol is not None:
            self.symbol = symbol
        if market_cap_usd is not None:
            self.market_cap_usd = market_cap_usd
        if available_supply is not None:
            self.available_supply = available_supply
        if total_supply is not None:
            self.total_supply = total_supply
        if max_supply is not None:
            self.max_supply = max_supply
        if last_updated is not None:
            self.last_updated = last_updated

    @property
    def name(self):
        """Gets the name of this CryptoStat.  # noqa: E501

        The common name of the crypto currency.  # noqa: E501

        :return: The name of this CryptoStat.  # noqa: E501
        :rtype: str
        """
        return self._name
        
    @property
    def name_dict(self):
        """Gets the name of this CryptoStat.  # noqa: E501

        The common name of the crypto currency. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The name of this CryptoStat.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.name
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
            result = { 'name': value }

        
        return result
        

    @name.setter
    def name(self, name):
        """Sets the name of this CryptoStat.

        The common name of the crypto currency.  # noqa: E501

        :param name: The name of this CryptoStat.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def code(self):
        """Gets the code of this CryptoStat.  # noqa: E501

        A code representing the crypto currency.  # noqa: E501

        :return: The code of this CryptoStat.  # noqa: E501
        :rtype: str
        """
        return self._code
        
    @property
    def code_dict(self):
        """Gets the code of this CryptoStat.  # noqa: E501

        A code representing the crypto currency. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The code of this CryptoStat.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.code
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
            result = { 'code': value }

        
        return result
        

    @code.setter
    def code(self, code):
        """Sets the code of this CryptoStat.

        A code representing the crypto currency.  # noqa: E501

        :param code: The code of this CryptoStat.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def symbol(self):
        """Gets the symbol of this CryptoStat.  # noqa: E501

        The symbol of the Crypto Currency.  # noqa: E501

        :return: The symbol of this CryptoStat.  # noqa: E501
        :rtype: str
        """
        return self._symbol
        
    @property
    def symbol_dict(self):
        """Gets the symbol of this CryptoStat.  # noqa: E501

        The symbol of the Crypto Currency. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The symbol of this CryptoStat.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.symbol
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
            result = { 'symbol': value }

        
        return result
        

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this CryptoStat.

        The symbol of the Crypto Currency.  # noqa: E501

        :param symbol: The symbol of this CryptoStat.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def market_cap_usd(self):
        """Gets the market_cap_usd of this CryptoStat.  # noqa: E501

        The market cap of the Crypto Currency in USD.  # noqa: E501

        :return: The market_cap_usd of this CryptoStat.  # noqa: E501
        :rtype: float
        """
        return self._market_cap_usd
        
    @property
    def market_cap_usd_dict(self):
        """Gets the market_cap_usd of this CryptoStat.  # noqa: E501

        The market cap of the Crypto Currency in USD. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The market_cap_usd of this CryptoStat.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.market_cap_usd
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
            result = { 'market_cap_usd': value }

        
        return result
        

    @market_cap_usd.setter
    def market_cap_usd(self, market_cap_usd):
        """Sets the market_cap_usd of this CryptoStat.

        The market cap of the Crypto Currency in USD.  # noqa: E501

        :param market_cap_usd: The market_cap_usd of this CryptoStat.  # noqa: E501
        :type: float
        """

        self._market_cap_usd = market_cap_usd

    @property
    def available_supply(self):
        """Gets the available_supply of this CryptoStat.  # noqa: E501

        The available supply of the Crypto Currency.  # noqa: E501

        :return: The available_supply of this CryptoStat.  # noqa: E501
        :rtype: float
        """
        return self._available_supply
        
    @property
    def available_supply_dict(self):
        """Gets the available_supply of this CryptoStat.  # noqa: E501

        The available supply of the Crypto Currency. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The available_supply of this CryptoStat.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.available_supply
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
            result = { 'available_supply': value }

        
        return result
        

    @available_supply.setter
    def available_supply(self, available_supply):
        """Sets the available_supply of this CryptoStat.

        The available supply of the Crypto Currency.  # noqa: E501

        :param available_supply: The available_supply of this CryptoStat.  # noqa: E501
        :type: float
        """

        self._available_supply = available_supply

    @property
    def total_supply(self):
        """Gets the total_supply of this CryptoStat.  # noqa: E501

        The total supply of the Crypto Currency.  # noqa: E501

        :return: The total_supply of this CryptoStat.  # noqa: E501
        :rtype: float
        """
        return self._total_supply
        
    @property
    def total_supply_dict(self):
        """Gets the total_supply of this CryptoStat.  # noqa: E501

        The total supply of the Crypto Currency. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The total_supply of this CryptoStat.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.total_supply
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
            result = { 'total_supply': value }

        
        return result
        

    @total_supply.setter
    def total_supply(self, total_supply):
        """Sets the total_supply of this CryptoStat.

        The total supply of the Crypto Currency.  # noqa: E501

        :param total_supply: The total_supply of this CryptoStat.  # noqa: E501
        :type: float
        """

        self._total_supply = total_supply

    @property
    def max_supply(self):
        """Gets the max_supply of this CryptoStat.  # noqa: E501

        The maxmium supply of coins available to mine.  # noqa: E501

        :return: The max_supply of this CryptoStat.  # noqa: E501
        :rtype: float
        """
        return self._max_supply
        
    @property
    def max_supply_dict(self):
        """Gets the max_supply of this CryptoStat.  # noqa: E501

        The maxmium supply of coins available to mine. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The max_supply of this CryptoStat.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.max_supply
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
            result = { 'max_supply': value }

        
        return result
        

    @max_supply.setter
    def max_supply(self, max_supply):
        """Sets the max_supply of this CryptoStat.

        The maxmium supply of coins available to mine.  # noqa: E501

        :param max_supply: The max_supply of this CryptoStat.  # noqa: E501
        :type: float
        """

        self._max_supply = max_supply

    @property
    def last_updated(self):
        """Gets the last_updated of this CryptoStat.  # noqa: E501

        UTC timestamp of when the data was last updated.  # noqa: E501

        :return: The last_updated of this CryptoStat.  # noqa: E501
        :rtype: str
        """
        return self._last_updated
        
    @property
    def last_updated_dict(self):
        """Gets the last_updated of this CryptoStat.  # noqa: E501

        UTC timestamp of when the data was last updated. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The last_updated of this CryptoStat.  # noqa: E501
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
        """Sets the last_updated of this CryptoStat.

        UTC timestamp of when the data was last updated.  # noqa: E501

        :param last_updated: The last_updated of this CryptoStat.  # noqa: E501
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
        if not isinstance(other, CryptoStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
