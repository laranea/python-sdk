# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.6.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ZacksAnalystRatingSnapshot(object):
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
        'type': 'str',
        'snapshot_date': 'date',
        'rating_date': 'date',
        'mean': 'float',
        'percentile': 'float',
        'strong_buys': 'int',
        'buys': 'int',
        'holds': 'int',
        'sells': 'int',
        'strong_sells': 'int',
        'total': 'int'
    }

    attribute_map = {
        'type': 'type',
        'snapshot_date': 'snapshot_date',
        'rating_date': 'rating_date',
        'mean': 'mean',
        'percentile': 'percentile',
        'strong_buys': 'strong_buys',
        'buys': 'buys',
        'holds': 'holds',
        'sells': 'sells',
        'strong_sells': 'strong_sells',
        'total': 'total'
    }

    def __init__(self, type=None, snapshot_date=None, rating_date=None, mean=None, percentile=None, strong_buys=None, buys=None, holds=None, sells=None, strong_sells=None, total=None):  # noqa: E501
        """ZacksAnalystRatingSnapshot - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._snapshot_date = None
        self._rating_date = None
        self._mean = None
        self._percentile = None
        self._strong_buys = None
        self._buys = None
        self._holds = None
        self._sells = None
        self._strong_sells = None
        self._total = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if snapshot_date is not None:
            self.snapshot_date = snapshot_date
        if rating_date is not None:
            self.rating_date = rating_date
        if mean is not None:
            self.mean = mean
        if percentile is not None:
            self.percentile = percentile
        if strong_buys is not None:
            self.strong_buys = strong_buys
        if buys is not None:
            self.buys = buys
        if holds is not None:
            self.holds = holds
        if sells is not None:
            self.sells = sells
        if strong_sells is not None:
            self.strong_sells = strong_sells
        if total is not None:
            self.total = total

    @property
    def type(self):
        """Gets the type of this ZacksAnalystRatingSnapshot.  # noqa: E501

        The snapshot type, signifying the age of the ratings data from the snapshot date.  # noqa: E501

        :return: The type of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._type
        
    @property
    def type_dict(self):
        """Gets the type of this ZacksAnalystRatingSnapshot.  # noqa: E501

        The snapshot type, signifying the age of the ratings data from the snapshot date. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The type of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.type
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
            result = { 'type': value }

        
        return result
        

    @type.setter
    def type(self, type):
        """Sets the type of this ZacksAnalystRatingSnapshot.

        The snapshot type, signifying the age of the ratings data from the snapshot date.  # noqa: E501

        :param type: The type of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def snapshot_date(self):
        """Gets the snapshot_date of this ZacksAnalystRatingSnapshot.  # noqa: E501

        The date of the snapshot, when data was recorded.  # noqa: E501

        :return: The snapshot_date of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :rtype: date
        """
        return self._snapshot_date
        
    @property
    def snapshot_date_dict(self):
        """Gets the snapshot_date of this ZacksAnalystRatingSnapshot.  # noqa: E501

        The date of the snapshot, when data was recorded. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The snapshot_date of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.snapshot_date
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
            result = { 'snapshot_date': value }

        
        return result
        

    @snapshot_date.setter
    def snapshot_date(self, snapshot_date):
        """Sets the snapshot_date of this ZacksAnalystRatingSnapshot.

        The date of the snapshot, when data was recorded.  # noqa: E501

        :param snapshot_date: The snapshot_date of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :type: date
        """

        self._snapshot_date = snapshot_date

    @property
    def rating_date(self):
        """Gets the rating_date of this ZacksAnalystRatingSnapshot.  # noqa: E501

        The date of the latest rating for the snapshot timeframe. This is the effective date of the ratings data.  # noqa: E501

        :return: The rating_date of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :rtype: date
        """
        return self._rating_date
        
    @property
    def rating_date_dict(self):
        """Gets the rating_date of this ZacksAnalystRatingSnapshot.  # noqa: E501

        The date of the latest rating for the snapshot timeframe. This is the effective date of the ratings data. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The rating_date of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.rating_date
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
            result = { 'rating_date': value }

        
        return result
        

    @rating_date.setter
    def rating_date(self, rating_date):
        """Sets the rating_date of this ZacksAnalystRatingSnapshot.

        The date of the latest rating for the snapshot timeframe. This is the effective date of the ratings data.  # noqa: E501

        :param rating_date: The rating_date of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :type: date
        """

        self._rating_date = rating_date

    @property
    def mean(self):
        """Gets the mean of this ZacksAnalystRatingSnapshot.  # noqa: E501

        The mean (average) weighing of analyst recommendations, from 1 (strong buy) to 5 (strong sell).  # noqa: E501

        :return: The mean of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :rtype: float
        """
        return self._mean
        
    @property
    def mean_dict(self):
        """Gets the mean of this ZacksAnalystRatingSnapshot.  # noqa: E501

        The mean (average) weighing of analyst recommendations, from 1 (strong buy) to 5 (strong sell). as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The mean of this ZacksAnalystRatingSnapshot.  # noqa: E501
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
        """Sets the mean of this ZacksAnalystRatingSnapshot.

        The mean (average) weighing of analyst recommendations, from 1 (strong buy) to 5 (strong sell).  # noqa: E501

        :param mean: The mean of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :type: float
        """

        self._mean = mean

    @property
    def percentile(self):
        """Gets the percentile of this ZacksAnalystRatingSnapshot.  # noqa: E501

        The percentile of the mean, derived by comparing to all securities rated by analysts as of the rating date, ranging 0.0 (strong buy) to 1.0 (strong sell).  # noqa: E501

        :return: The percentile of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :rtype: float
        """
        return self._percentile
        
    @property
    def percentile_dict(self):
        """Gets the percentile of this ZacksAnalystRatingSnapshot.  # noqa: E501

        The percentile of the mean, derived by comparing to all securities rated by analysts as of the rating date, ranging 0.0 (strong buy) to 1.0 (strong sell). as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The percentile of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.percentile
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
            result = { 'percentile': value }

        
        return result
        

    @percentile.setter
    def percentile(self, percentile):
        """Sets the percentile of this ZacksAnalystRatingSnapshot.

        The percentile of the mean, derived by comparing to all securities rated by analysts as of the rating date, ranging 0.0 (strong buy) to 1.0 (strong sell).  # noqa: E501

        :param percentile: The percentile of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :type: float
        """

        self._percentile = percentile

    @property
    def strong_buys(self):
        """Gets the strong_buys of this ZacksAnalystRatingSnapshot.  # noqa: E501

        The number of analysts recommending Strong Buy.  # noqa: E501

        :return: The strong_buys of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :rtype: int
        """
        return self._strong_buys
        
    @property
    def strong_buys_dict(self):
        """Gets the strong_buys of this ZacksAnalystRatingSnapshot.  # noqa: E501

        The number of analysts recommending Strong Buy. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The strong_buys of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :rtype: int
        """

        result = None

        value = self.strong_buys
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
            result = { 'strong_buys': value }

        
        return result
        

    @strong_buys.setter
    def strong_buys(self, strong_buys):
        """Sets the strong_buys of this ZacksAnalystRatingSnapshot.

        The number of analysts recommending Strong Buy.  # noqa: E501

        :param strong_buys: The strong_buys of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :type: int
        """

        self._strong_buys = strong_buys

    @property
    def buys(self):
        """Gets the buys of this ZacksAnalystRatingSnapshot.  # noqa: E501

        The number of analysts recommending Buy.  # noqa: E501

        :return: The buys of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :rtype: int
        """
        return self._buys
        
    @property
    def buys_dict(self):
        """Gets the buys of this ZacksAnalystRatingSnapshot.  # noqa: E501

        The number of analysts recommending Buy. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The buys of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :rtype: int
        """

        result = None

        value = self.buys
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
            result = { 'buys': value }

        
        return result
        

    @buys.setter
    def buys(self, buys):
        """Sets the buys of this ZacksAnalystRatingSnapshot.

        The number of analysts recommending Buy.  # noqa: E501

        :param buys: The buys of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :type: int
        """

        self._buys = buys

    @property
    def holds(self):
        """Gets the holds of this ZacksAnalystRatingSnapshot.  # noqa: E501

        The number of analysts recommending Hold.  # noqa: E501

        :return: The holds of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :rtype: int
        """
        return self._holds
        
    @property
    def holds_dict(self):
        """Gets the holds of this ZacksAnalystRatingSnapshot.  # noqa: E501

        The number of analysts recommending Hold. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The holds of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :rtype: int
        """

        result = None

        value = self.holds
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
            result = { 'holds': value }

        
        return result
        

    @holds.setter
    def holds(self, holds):
        """Sets the holds of this ZacksAnalystRatingSnapshot.

        The number of analysts recommending Hold.  # noqa: E501

        :param holds: The holds of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :type: int
        """

        self._holds = holds

    @property
    def sells(self):
        """Gets the sells of this ZacksAnalystRatingSnapshot.  # noqa: E501

        The number of analysts recommending Sell.  # noqa: E501

        :return: The sells of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :rtype: int
        """
        return self._sells
        
    @property
    def sells_dict(self):
        """Gets the sells of this ZacksAnalystRatingSnapshot.  # noqa: E501

        The number of analysts recommending Sell. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The sells of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :rtype: int
        """

        result = None

        value = self.sells
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
            result = { 'sells': value }

        
        return result
        

    @sells.setter
    def sells(self, sells):
        """Sets the sells of this ZacksAnalystRatingSnapshot.

        The number of analysts recommending Sell.  # noqa: E501

        :param sells: The sells of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :type: int
        """

        self._sells = sells

    @property
    def strong_sells(self):
        """Gets the strong_sells of this ZacksAnalystRatingSnapshot.  # noqa: E501

        The number of analysts recommending Strong Sell.  # noqa: E501

        :return: The strong_sells of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :rtype: int
        """
        return self._strong_sells
        
    @property
    def strong_sells_dict(self):
        """Gets the strong_sells of this ZacksAnalystRatingSnapshot.  # noqa: E501

        The number of analysts recommending Strong Sell. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The strong_sells of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :rtype: int
        """

        result = None

        value = self.strong_sells
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
            result = { 'strong_sells': value }

        
        return result
        

    @strong_sells.setter
    def strong_sells(self, strong_sells):
        """Sets the strong_sells of this ZacksAnalystRatingSnapshot.

        The number of analysts recommending Strong Sell.  # noqa: E501

        :param strong_sells: The strong_sells of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :type: int
        """

        self._strong_sells = strong_sells

    @property
    def total(self):
        """Gets the total of this ZacksAnalystRatingSnapshot.  # noqa: E501

        The total number of analysts recommendations.  # noqa: E501

        :return: The total of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :rtype: int
        """
        return self._total
        
    @property
    def total_dict(self):
        """Gets the total of this ZacksAnalystRatingSnapshot.  # noqa: E501

        The total number of analysts recommendations. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The total of this ZacksAnalystRatingSnapshot.  # noqa: E501
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
        """Sets the total of this ZacksAnalystRatingSnapshot.

        The total number of analysts recommendations.  # noqa: E501

        :param total: The total of this ZacksAnalystRatingSnapshot.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if not isinstance(other, ZacksAnalystRatingSnapshot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
