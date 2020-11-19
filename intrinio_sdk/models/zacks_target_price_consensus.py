# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.16.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from intrinio_sdk.models.company_summary import CompanySummary  # noqa: F401,E501


class ZacksTargetPriceConsensus(object):
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
        'ticker': 'str',
        'company_name': 'str',
        'industry_group_number': 'str',
        'high': 'float',
        'low': 'float',
        'mean': 'float',
        'standard_deviation': 'float',
        'total': 'int',
        'most_recent_date': 'date',
        'median': 'float',
        'raised': 'int',
        'lowered': 'int',
        'company': 'CompanySummary'
    }

    attribute_map = {
        'ticker': 'ticker',
        'company_name': 'company_name',
        'industry_group_number': 'industry_group_number',
        'high': 'high',
        'low': 'low',
        'mean': 'mean',
        'standard_deviation': 'standard_deviation',
        'total': 'total',
        'most_recent_date': 'most_recent_date',
        'median': 'median',
        'raised': 'raised',
        'lowered': 'lowered',
        'company': 'company'
    }

    def __init__(self, ticker=None, company_name=None, industry_group_number=None, high=None, low=None, mean=None, standard_deviation=None, total=None, most_recent_date=None, median=None, raised=None, lowered=None, company=None):  # noqa: E501
        """ZacksTargetPriceConsensus - a model defined in Swagger"""  # noqa: E501

        self._ticker = None
        self._company_name = None
        self._industry_group_number = None
        self._high = None
        self._low = None
        self._mean = None
        self._standard_deviation = None
        self._total = None
        self._most_recent_date = None
        self._median = None
        self._raised = None
        self._lowered = None
        self._company = None
        self.discriminator = None

        if ticker is not None:
            self.ticker = ticker
        if company_name is not None:
            self.company_name = company_name
        if industry_group_number is not None:
            self.industry_group_number = industry_group_number
        if high is not None:
            self.high = high
        if low is not None:
            self.low = low
        if mean is not None:
            self.mean = mean
        if standard_deviation is not None:
            self.standard_deviation = standard_deviation
        if total is not None:
            self.total = total
        if most_recent_date is not None:
            self.most_recent_date = most_recent_date
        if median is not None:
            self.median = median
        if raised is not None:
            self.raised = raised
        if lowered is not None:
            self.lowered = lowered
        if company is not None:
            self.company = company

    @property
    def ticker(self):
        """Gets the ticker of this ZacksTargetPriceConsensus.  # noqa: E501

        The Zacks common exchange ticker  # noqa: E501

        :return: The ticker of this ZacksTargetPriceConsensus.  # noqa: E501
        :rtype: str
        """
        return self._ticker
        
    @property
    def ticker_dict(self):
        """Gets the ticker of this ZacksTargetPriceConsensus.  # noqa: E501

        The Zacks common exchange ticker as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ticker of this ZacksTargetPriceConsensus.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.ticker
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
            result = { 'ticker': value }

        
        return result
        

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this ZacksTargetPriceConsensus.

        The Zacks common exchange ticker  # noqa: E501

        :param ticker: The ticker of this ZacksTargetPriceConsensus.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def company_name(self):
        """Gets the company_name of this ZacksTargetPriceConsensus.  # noqa: E501

        The company name  # noqa: E501

        :return: The company_name of this ZacksTargetPriceConsensus.  # noqa: E501
        :rtype: str
        """
        return self._company_name
        
    @property
    def company_name_dict(self):
        """Gets the company_name of this ZacksTargetPriceConsensus.  # noqa: E501

        The company name as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The company_name of this ZacksTargetPriceConsensus.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.company_name
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
            result = { 'company_name': value }

        
        return result
        

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this ZacksTargetPriceConsensus.

        The company name  # noqa: E501

        :param company_name: The company_name of this ZacksTargetPriceConsensus.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def industry_group_number(self):
        """Gets the industry_group_number of this ZacksTargetPriceConsensus.  # noqa: E501

        The Zacks industry group number  # noqa: E501

        :return: The industry_group_number of this ZacksTargetPriceConsensus.  # noqa: E501
        :rtype: str
        """
        return self._industry_group_number
        
    @property
    def industry_group_number_dict(self):
        """Gets the industry_group_number of this ZacksTargetPriceConsensus.  # noqa: E501

        The Zacks industry group number as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The industry_group_number of this ZacksTargetPriceConsensus.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.industry_group_number
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
            result = { 'industry_group_number': value }

        
        return result
        

    @industry_group_number.setter
    def industry_group_number(self, industry_group_number):
        """Sets the industry_group_number of this ZacksTargetPriceConsensus.

        The Zacks industry group number  # noqa: E501

        :param industry_group_number: The industry_group_number of this ZacksTargetPriceConsensus.  # noqa: E501
        :type: str
        """

        self._industry_group_number = industry_group_number

    @property
    def high(self):
        """Gets the high of this ZacksTargetPriceConsensus.  # noqa: E501

        The high target price estimate  # noqa: E501

        :return: The high of this ZacksTargetPriceConsensus.  # noqa: E501
        :rtype: float
        """
        return self._high
        
    @property
    def high_dict(self):
        """Gets the high of this ZacksTargetPriceConsensus.  # noqa: E501

        The high target price estimate as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The high of this ZacksTargetPriceConsensus.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.high
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
            result = { 'high': value }

        
        return result
        

    @high.setter
    def high(self, high):
        """Sets the high of this ZacksTargetPriceConsensus.

        The high target price estimate  # noqa: E501

        :param high: The high of this ZacksTargetPriceConsensus.  # noqa: E501
        :type: float
        """

        self._high = high

    @property
    def low(self):
        """Gets the low of this ZacksTargetPriceConsensus.  # noqa: E501

        The low target price estimate  # noqa: E501

        :return: The low of this ZacksTargetPriceConsensus.  # noqa: E501
        :rtype: float
        """
        return self._low
        
    @property
    def low_dict(self):
        """Gets the low of this ZacksTargetPriceConsensus.  # noqa: E501

        The low target price estimate as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The low of this ZacksTargetPriceConsensus.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.low
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
            result = { 'low': value }

        
        return result
        

    @low.setter
    def low(self, low):
        """Sets the low of this ZacksTargetPriceConsensus.

        The low target price estimate  # noqa: E501

        :param low: The low of this ZacksTargetPriceConsensus.  # noqa: E501
        :type: float
        """

        self._low = low

    @property
    def mean(self):
        """Gets the mean of this ZacksTargetPriceConsensus.  # noqa: E501

        The mean target price estimate  # noqa: E501

        :return: The mean of this ZacksTargetPriceConsensus.  # noqa: E501
        :rtype: float
        """
        return self._mean
        
    @property
    def mean_dict(self):
        """Gets the mean of this ZacksTargetPriceConsensus.  # noqa: E501

        The mean target price estimate as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The mean of this ZacksTargetPriceConsensus.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.mean
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
            result = { 'mean': value }

        
        return result
        

    @mean.setter
    def mean(self, mean):
        """Sets the mean of this ZacksTargetPriceConsensus.

        The mean target price estimate  # noqa: E501

        :param mean: The mean of this ZacksTargetPriceConsensus.  # noqa: E501
        :type: float
        """

        self._mean = mean

    @property
    def standard_deviation(self):
        """Gets the standard_deviation of this ZacksTargetPriceConsensus.  # noqa: E501

        The standard deviation of target price estimates  # noqa: E501

        :return: The standard_deviation of this ZacksTargetPriceConsensus.  # noqa: E501
        :rtype: float
        """
        return self._standard_deviation
        
    @property
    def standard_deviation_dict(self):
        """Gets the standard_deviation of this ZacksTargetPriceConsensus.  # noqa: E501

        The standard deviation of target price estimates as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The standard_deviation of this ZacksTargetPriceConsensus.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.standard_deviation
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
            result = { 'standard_deviation': value }

        
        return result
        

    @standard_deviation.setter
    def standard_deviation(self, standard_deviation):
        """Sets the standard_deviation of this ZacksTargetPriceConsensus.

        The standard deviation of target price estimates  # noqa: E501

        :param standard_deviation: The standard_deviation of this ZacksTargetPriceConsensus.  # noqa: E501
        :type: float
        """

        self._standard_deviation = standard_deviation

    @property
    def total(self):
        """Gets the total of this ZacksTargetPriceConsensus.  # noqa: E501

        The number of target price estimates in consensus  # noqa: E501

        :return: The total of this ZacksTargetPriceConsensus.  # noqa: E501
        :rtype: int
        """
        return self._total
        
    @property
    def total_dict(self):
        """Gets the total of this ZacksTargetPriceConsensus.  # noqa: E501

        The number of target price estimates in consensus as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The total of this ZacksTargetPriceConsensus.  # noqa: E501
        :rtype: int
        """

        result = None

        value = self.total
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
            result = { 'total': value }

        
        return result
        

    @total.setter
    def total(self, total):
        """Sets the total of this ZacksTargetPriceConsensus.

        The number of target price estimates in consensus  # noqa: E501

        :param total: The total of this ZacksTargetPriceConsensus.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def most_recent_date(self):
        """Gets the most_recent_date of this ZacksTargetPriceConsensus.  # noqa: E501

        The date of most recent estimate  # noqa: E501

        :return: The most_recent_date of this ZacksTargetPriceConsensus.  # noqa: E501
        :rtype: date
        """
        return self._most_recent_date
        
    @property
    def most_recent_date_dict(self):
        """Gets the most_recent_date of this ZacksTargetPriceConsensus.  # noqa: E501

        The date of most recent estimate as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The most_recent_date of this ZacksTargetPriceConsensus.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.most_recent_date
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
            result = { 'most_recent_date': value }

        
        return result
        

    @most_recent_date.setter
    def most_recent_date(self, most_recent_date):
        """Sets the most_recent_date of this ZacksTargetPriceConsensus.

        The date of most recent estimate  # noqa: E501

        :param most_recent_date: The most_recent_date of this ZacksTargetPriceConsensus.  # noqa: E501
        :type: date
        """

        self._most_recent_date = most_recent_date

    @property
    def median(self):
        """Gets the median of this ZacksTargetPriceConsensus.  # noqa: E501

        The median target price estimate  # noqa: E501

        :return: The median of this ZacksTargetPriceConsensus.  # noqa: E501
        :rtype: float
        """
        return self._median
        
    @property
    def median_dict(self):
        """Gets the median of this ZacksTargetPriceConsensus.  # noqa: E501

        The median target price estimate as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The median of this ZacksTargetPriceConsensus.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.median
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
            result = { 'median': value }

        
        return result
        

    @median.setter
    def median(self, median):
        """Sets the median of this ZacksTargetPriceConsensus.

        The median target price estimate  # noqa: E501

        :param median: The median of this ZacksTargetPriceConsensus.  # noqa: E501
        :type: float
        """

        self._median = median

    @property
    def raised(self):
        """Gets the raised of this ZacksTargetPriceConsensus.  # noqa: E501

        The number of estimates raised  # noqa: E501

        :return: The raised of this ZacksTargetPriceConsensus.  # noqa: E501
        :rtype: int
        """
        return self._raised
        
    @property
    def raised_dict(self):
        """Gets the raised of this ZacksTargetPriceConsensus.  # noqa: E501

        The number of estimates raised as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The raised of this ZacksTargetPriceConsensus.  # noqa: E501
        :rtype: int
        """

        result = None

        value = self.raised
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
            result = { 'raised': value }

        
        return result
        

    @raised.setter
    def raised(self, raised):
        """Sets the raised of this ZacksTargetPriceConsensus.

        The number of estimates raised  # noqa: E501

        :param raised: The raised of this ZacksTargetPriceConsensus.  # noqa: E501
        :type: int
        """

        self._raised = raised

    @property
    def lowered(self):
        """Gets the lowered of this ZacksTargetPriceConsensus.  # noqa: E501

        The number of estimates lowered  # noqa: E501

        :return: The lowered of this ZacksTargetPriceConsensus.  # noqa: E501
        :rtype: int
        """
        return self._lowered
        
    @property
    def lowered_dict(self):
        """Gets the lowered of this ZacksTargetPriceConsensus.  # noqa: E501

        The number of estimates lowered as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The lowered of this ZacksTargetPriceConsensus.  # noqa: E501
        :rtype: int
        """

        result = None

        value = self.lowered
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
            result = { 'lowered': value }

        
        return result
        

    @lowered.setter
    def lowered(self, lowered):
        """Sets the lowered of this ZacksTargetPriceConsensus.

        The number of estimates lowered  # noqa: E501

        :param lowered: The lowered of this ZacksTargetPriceConsensus.  # noqa: E501
        :type: int
        """

        self._lowered = lowered

    @property
    def company(self):
        """Gets the company of this ZacksTargetPriceConsensus.  # noqa: E501


        :return: The company of this ZacksTargetPriceConsensus.  # noqa: E501
        :rtype: CompanySummary
        """
        return self._company
        
    @property
    def company_dict(self):
        """Gets the company of this ZacksTargetPriceConsensus.  # noqa: E501


        :return: The company of this ZacksTargetPriceConsensus.  # noqa: E501
        :rtype: CompanySummary
        """

        result = None

        value = self.company
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
            result = { 'company': value }

        
        return result
        

    @company.setter
    def company(self, company):
        """Sets the company of this ZacksTargetPriceConsensus.


        :param company: The company of this ZacksTargetPriceConsensus.  # noqa: E501
        :type: CompanySummary
        """

        self._company = company

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
        if not isinstance(other, ZacksTargetPriceConsensus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
