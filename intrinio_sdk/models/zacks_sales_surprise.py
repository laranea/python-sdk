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


class ZacksSalesSurprise(object):
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
        'id': 'str',
        'fiscal_year': 'float',
        'fiscal_quarter': 'str',
        'calendar_year': 'float',
        'calendar_quarter': 'str',
        'actual_reported_date': 'date',
        'actual_reported_time': 'str',
        'actual_reported_code': 'str',
        'actual_reported_desc': 'str',
        'last_rev_date': 'date',
        'sales_actual': 'float',
        'sales_actual_zacks_adj': 'float',
        'sales_actual_gaap': 'float',
        'sales_mean_estimate': 'float',
        'sales_amount_diff': 'float',
        'sales_percent_diff': 'float',
        'sales_std_dev_estimate': 'float'
    }

    attribute_map = {
        'id': 'id',
        'fiscal_year': 'fiscal_year',
        'fiscal_quarter': 'fiscal_quarter',
        'calendar_year': 'calendar_year',
        'calendar_quarter': 'calendar_quarter',
        'actual_reported_date': 'actual_reported_date',
        'actual_reported_time': 'actual_reported_time',
        'actual_reported_code': 'actual_reported_code',
        'actual_reported_desc': 'actual_reported_desc',
        'last_rev_date': 'last_rev_date',
        'sales_actual': 'sales_actual',
        'sales_actual_zacks_adj': 'sales_actual_zacks_adj',
        'sales_actual_gaap': 'sales_actual_gaap',
        'sales_mean_estimate': 'sales_mean_estimate',
        'sales_amount_diff': 'sales_amount_diff',
        'sales_percent_diff': 'sales_percent_diff',
        'sales_std_dev_estimate': 'sales_std_dev_estimate'
    }

    def __init__(self, id=None, fiscal_year=None, fiscal_quarter=None, calendar_year=None, calendar_quarter=None, actual_reported_date=None, actual_reported_time=None, actual_reported_code=None, actual_reported_desc=None, last_rev_date=None, sales_actual=None, sales_actual_zacks_adj=None, sales_actual_gaap=None, sales_mean_estimate=None, sales_amount_diff=None, sales_percent_diff=None, sales_std_dev_estimate=None):  # noqa: E501
        """ZacksSalesSurprise - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._fiscal_year = None
        self._fiscal_quarter = None
        self._calendar_year = None
        self._calendar_quarter = None
        self._actual_reported_date = None
        self._actual_reported_time = None
        self._actual_reported_code = None
        self._actual_reported_desc = None
        self._last_rev_date = None
        self._sales_actual = None
        self._sales_actual_zacks_adj = None
        self._sales_actual_gaap = None
        self._sales_mean_estimate = None
        self._sales_amount_diff = None
        self._sales_percent_diff = None
        self._sales_std_dev_estimate = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if fiscal_year is not None:
            self.fiscal_year = fiscal_year
        if fiscal_quarter is not None:
            self.fiscal_quarter = fiscal_quarter
        if calendar_year is not None:
            self.calendar_year = calendar_year
        if calendar_quarter is not None:
            self.calendar_quarter = calendar_quarter
        if actual_reported_date is not None:
            self.actual_reported_date = actual_reported_date
        if actual_reported_time is not None:
            self.actual_reported_time = actual_reported_time
        if actual_reported_code is not None:
            self.actual_reported_code = actual_reported_code
        if actual_reported_desc is not None:
            self.actual_reported_desc = actual_reported_desc
        if last_rev_date is not None:
            self.last_rev_date = last_rev_date
        if sales_actual is not None:
            self.sales_actual = sales_actual
        if sales_actual_zacks_adj is not None:
            self.sales_actual_zacks_adj = sales_actual_zacks_adj
        if sales_actual_gaap is not None:
            self.sales_actual_gaap = sales_actual_gaap
        if sales_mean_estimate is not None:
            self.sales_mean_estimate = sales_mean_estimate
        if sales_amount_diff is not None:
            self.sales_amount_diff = sales_amount_diff
        if sales_percent_diff is not None:
            self.sales_percent_diff = sales_percent_diff
        if sales_std_dev_estimate is not None:
            self.sales_std_dev_estimate = sales_std_dev_estimate

    @property
    def id(self):
        """Gets the id of this ZacksSalesSurprise.  # noqa: E501

        The Intrinio ID for the record  # noqa: E501

        :return: The id of this ZacksSalesSurprise.  # noqa: E501
        :rtype: str
        """
        return self._id
        
    @property
    def id_dict(self):
        """Gets the id of this ZacksSalesSurprise.  # noqa: E501

        The Intrinio ID for the record as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The id of this ZacksSalesSurprise.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.id
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
            result = { 'id': value }

        
        return result
        

    @id.setter
    def id(self, id):
        """Sets the id of this ZacksSalesSurprise.

        The Intrinio ID for the record  # noqa: E501

        :param id: The id of this ZacksSalesSurprise.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def fiscal_year(self):
        """Gets the fiscal_year of this ZacksSalesSurprise.  # noqa: E501

        The company’s fiscal year for the reported period  # noqa: E501

        :return: The fiscal_year of this ZacksSalesSurprise.  # noqa: E501
        :rtype: float
        """
        return self._fiscal_year
        
    @property
    def fiscal_year_dict(self):
        """Gets the fiscal_year of this ZacksSalesSurprise.  # noqa: E501

        The company’s fiscal year for the reported period as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The fiscal_year of this ZacksSalesSurprise.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.fiscal_year
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
            result = { 'fiscal_year': value }

        
        return result
        

    @fiscal_year.setter
    def fiscal_year(self, fiscal_year):
        """Sets the fiscal_year of this ZacksSalesSurprise.

        The company’s fiscal year for the reported period  # noqa: E501

        :param fiscal_year: The fiscal_year of this ZacksSalesSurprise.  # noqa: E501
        :type: float
        """

        self._fiscal_year = fiscal_year

    @property
    def fiscal_quarter(self):
        """Gets the fiscal_quarter of this ZacksSalesSurprise.  # noqa: E501

        The company’s fiscal quarter for the reported period  # noqa: E501

        :return: The fiscal_quarter of this ZacksSalesSurprise.  # noqa: E501
        :rtype: str
        """
        return self._fiscal_quarter
        
    @property
    def fiscal_quarter_dict(self):
        """Gets the fiscal_quarter of this ZacksSalesSurprise.  # noqa: E501

        The company’s fiscal quarter for the reported period as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The fiscal_quarter of this ZacksSalesSurprise.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.fiscal_quarter
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
            result = { 'fiscal_quarter': value }

        
        return result
        

    @fiscal_quarter.setter
    def fiscal_quarter(self, fiscal_quarter):
        """Sets the fiscal_quarter of this ZacksSalesSurprise.

        The company’s fiscal quarter for the reported period  # noqa: E501

        :param fiscal_quarter: The fiscal_quarter of this ZacksSalesSurprise.  # noqa: E501
        :type: str
        """

        self._fiscal_quarter = fiscal_quarter

    @property
    def calendar_year(self):
        """Gets the calendar_year of this ZacksSalesSurprise.  # noqa: E501

        The closest calendar year for the company’s fiscal year  # noqa: E501

        :return: The calendar_year of this ZacksSalesSurprise.  # noqa: E501
        :rtype: float
        """
        return self._calendar_year
        
    @property
    def calendar_year_dict(self):
        """Gets the calendar_year of this ZacksSalesSurprise.  # noqa: E501

        The closest calendar year for the company’s fiscal year as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The calendar_year of this ZacksSalesSurprise.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.calendar_year
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
            result = { 'calendar_year': value }

        
        return result
        

    @calendar_year.setter
    def calendar_year(self, calendar_year):
        """Sets the calendar_year of this ZacksSalesSurprise.

        The closest calendar year for the company’s fiscal year  # noqa: E501

        :param calendar_year: The calendar_year of this ZacksSalesSurprise.  # noqa: E501
        :type: float
        """

        self._calendar_year = calendar_year

    @property
    def calendar_quarter(self):
        """Gets the calendar_quarter of this ZacksSalesSurprise.  # noqa: E501

        The closest calendar quarter for the company’s fiscal year  # noqa: E501

        :return: The calendar_quarter of this ZacksSalesSurprise.  # noqa: E501
        :rtype: str
        """
        return self._calendar_quarter
        
    @property
    def calendar_quarter_dict(self):
        """Gets the calendar_quarter of this ZacksSalesSurprise.  # noqa: E501

        The closest calendar quarter for the company’s fiscal year as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The calendar_quarter of this ZacksSalesSurprise.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.calendar_quarter
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
            result = { 'calendar_quarter': value }

        
        return result
        

    @calendar_quarter.setter
    def calendar_quarter(self, calendar_quarter):
        """Sets the calendar_quarter of this ZacksSalesSurprise.

        The closest calendar quarter for the company’s fiscal year  # noqa: E501

        :param calendar_quarter: The calendar_quarter of this ZacksSalesSurprise.  # noqa: E501
        :type: str
        """

        self._calendar_quarter = calendar_quarter

    @property
    def actual_reported_date(self):
        """Gets the actual_reported_date of this ZacksSalesSurprise.  # noqa: E501

        The actual report date for the earnings release  # noqa: E501

        :return: The actual_reported_date of this ZacksSalesSurprise.  # noqa: E501
        :rtype: date
        """
        return self._actual_reported_date
        
    @property
    def actual_reported_date_dict(self):
        """Gets the actual_reported_date of this ZacksSalesSurprise.  # noqa: E501

        The actual report date for the earnings release as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The actual_reported_date of this ZacksSalesSurprise.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.actual_reported_date
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
            result = { 'actual_reported_date': value }

        
        return result
        

    @actual_reported_date.setter
    def actual_reported_date(self, actual_reported_date):
        """Sets the actual_reported_date of this ZacksSalesSurprise.

        The actual report date for the earnings release  # noqa: E501

        :param actual_reported_date: The actual_reported_date of this ZacksSalesSurprise.  # noqa: E501
        :type: date
        """

        self._actual_reported_date = actual_reported_date

    @property
    def actual_reported_time(self):
        """Gets the actual_reported_time of this ZacksSalesSurprise.  # noqa: E501

        The actual report time for the earnings release  # noqa: E501

        :return: The actual_reported_time of this ZacksSalesSurprise.  # noqa: E501
        :rtype: str
        """
        return self._actual_reported_time
        
    @property
    def actual_reported_time_dict(self):
        """Gets the actual_reported_time of this ZacksSalesSurprise.  # noqa: E501

        The actual report time for the earnings release as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The actual_reported_time of this ZacksSalesSurprise.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.actual_reported_time
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
            result = { 'actual_reported_time': value }

        
        return result
        

    @actual_reported_time.setter
    def actual_reported_time(self, actual_reported_time):
        """Sets the actual_reported_time of this ZacksSalesSurprise.

        The actual report time for the earnings release  # noqa: E501

        :param actual_reported_time: The actual_reported_time of this ZacksSalesSurprise.  # noqa: E501
        :type: str
        """

        self._actual_reported_time = actual_reported_time

    @property
    def actual_reported_code(self):
        """Gets the actual_reported_code of this ZacksSalesSurprise.  # noqa: E501

        The code cooresponding to the earnings release  BTO = BEFORE THE OPEN | DTM = DURING THE MARKET | AMC = AFTER MARKET CLOSE  # noqa: E501

        :return: The actual_reported_code of this ZacksSalesSurprise.  # noqa: E501
        :rtype: str
        """
        return self._actual_reported_code
        
    @property
    def actual_reported_code_dict(self):
        """Gets the actual_reported_code of this ZacksSalesSurprise.  # noqa: E501

        The code cooresponding to the earnings release  BTO = BEFORE THE OPEN | DTM = DURING THE MARKET | AMC = AFTER MARKET CLOSE as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The actual_reported_code of this ZacksSalesSurprise.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.actual_reported_code
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
            result = { 'actual_reported_code': value }

        
        return result
        

    @actual_reported_code.setter
    def actual_reported_code(self, actual_reported_code):
        """Sets the actual_reported_code of this ZacksSalesSurprise.

        The code cooresponding to the earnings release  BTO = BEFORE THE OPEN | DTM = DURING THE MARKET | AMC = AFTER MARKET CLOSE  # noqa: E501

        :param actual_reported_code: The actual_reported_code of this ZacksSalesSurprise.  # noqa: E501
        :type: str
        """

        self._actual_reported_code = actual_reported_code

    @property
    def actual_reported_desc(self):
        """Gets the actual_reported_desc of this ZacksSalesSurprise.  # noqa: E501

        The description for the type of earnings release  # noqa: E501

        :return: The actual_reported_desc of this ZacksSalesSurprise.  # noqa: E501
        :rtype: str
        """
        return self._actual_reported_desc
        
    @property
    def actual_reported_desc_dict(self):
        """Gets the actual_reported_desc of this ZacksSalesSurprise.  # noqa: E501

        The description for the type of earnings release as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The actual_reported_desc of this ZacksSalesSurprise.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.actual_reported_desc
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
            result = { 'actual_reported_desc': value }

        
        return result
        

    @actual_reported_desc.setter
    def actual_reported_desc(self, actual_reported_desc):
        """Sets the actual_reported_desc of this ZacksSalesSurprise.

        The description for the type of earnings release  # noqa: E501

        :param actual_reported_desc: The actual_reported_desc of this ZacksSalesSurprise.  # noqa: E501
        :type: str
        """

        self._actual_reported_desc = actual_reported_desc

    @property
    def last_rev_date(self):
        """Gets the last_rev_date of this ZacksSalesSurprise.  # noqa: E501

        The last revision date for the analyst estimates  # noqa: E501

        :return: The last_rev_date of this ZacksSalesSurprise.  # noqa: E501
        :rtype: date
        """
        return self._last_rev_date
        
    @property
    def last_rev_date_dict(self):
        """Gets the last_rev_date of this ZacksSalesSurprise.  # noqa: E501

        The last revision date for the analyst estimates as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The last_rev_date of this ZacksSalesSurprise.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.last_rev_date
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
            result = { 'last_rev_date': value }

        
        return result
        

    @last_rev_date.setter
    def last_rev_date(self, last_rev_date):
        """Sets the last_rev_date of this ZacksSalesSurprise.

        The last revision date for the analyst estimates  # noqa: E501

        :param last_rev_date: The last_rev_date of this ZacksSalesSurprise.  # noqa: E501
        :type: date
        """

        self._last_rev_date = last_rev_date

    @property
    def sales_actual(self):
        """Gets the sales_actual of this ZacksSalesSurprise.  # noqa: E501

        The actual Non-GAAP sales figure released by the company, interpreted by Zacks.  # noqa: E501

        :return: The sales_actual of this ZacksSalesSurprise.  # noqa: E501
        :rtype: float
        """
        return self._sales_actual
        
    @property
    def sales_actual_dict(self):
        """Gets the sales_actual of this ZacksSalesSurprise.  # noqa: E501

        The actual Non-GAAP sales figure released by the company, interpreted by Zacks. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The sales_actual of this ZacksSalesSurprise.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.sales_actual
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
            result = { 'sales_actual': value }

        
        return result
        

    @sales_actual.setter
    def sales_actual(self, sales_actual):
        """Sets the sales_actual of this ZacksSalesSurprise.

        The actual Non-GAAP sales figure released by the company, interpreted by Zacks.  # noqa: E501

        :param sales_actual: The sales_actual of this ZacksSalesSurprise.  # noqa: E501
        :type: float
        """

        self._sales_actual = sales_actual

    @property
    def sales_actual_zacks_adj(self):
        """Gets the sales_actual_zacks_adj of this ZacksSalesSurprise.  # noqa: E501

        The adjustments Zacks made to get to Non-GAAP sales to reconcile with GAAP sales.  # noqa: E501

        :return: The sales_actual_zacks_adj of this ZacksSalesSurprise.  # noqa: E501
        :rtype: float
        """
        return self._sales_actual_zacks_adj
        
    @property
    def sales_actual_zacks_adj_dict(self):
        """Gets the sales_actual_zacks_adj of this ZacksSalesSurprise.  # noqa: E501

        The adjustments Zacks made to get to Non-GAAP sales to reconcile with GAAP sales. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The sales_actual_zacks_adj of this ZacksSalesSurprise.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.sales_actual_zacks_adj
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
            result = { 'sales_actual_zacks_adj': value }

        
        return result
        

    @sales_actual_zacks_adj.setter
    def sales_actual_zacks_adj(self, sales_actual_zacks_adj):
        """Sets the sales_actual_zacks_adj of this ZacksSalesSurprise.

        The adjustments Zacks made to get to Non-GAAP sales to reconcile with GAAP sales.  # noqa: E501

        :param sales_actual_zacks_adj: The sales_actual_zacks_adj of this ZacksSalesSurprise.  # noqa: E501
        :type: float
        """

        self._sales_actual_zacks_adj = sales_actual_zacks_adj

    @property
    def sales_actual_gaap(self):
        """Gets the sales_actual_gaap of this ZacksSalesSurprise.  # noqa: E501

        The actual GAAP sales figured released by the company  # noqa: E501

        :return: The sales_actual_gaap of this ZacksSalesSurprise.  # noqa: E501
        :rtype: float
        """
        return self._sales_actual_gaap
        
    @property
    def sales_actual_gaap_dict(self):
        """Gets the sales_actual_gaap of this ZacksSalesSurprise.  # noqa: E501

        The actual GAAP sales figured released by the company as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The sales_actual_gaap of this ZacksSalesSurprise.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.sales_actual_gaap
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
            result = { 'sales_actual_gaap': value }

        
        return result
        

    @sales_actual_gaap.setter
    def sales_actual_gaap(self, sales_actual_gaap):
        """Sets the sales_actual_gaap of this ZacksSalesSurprise.

        The actual GAAP sales figured released by the company  # noqa: E501

        :param sales_actual_gaap: The sales_actual_gaap of this ZacksSalesSurprise.  # noqa: E501
        :type: float
        """

        self._sales_actual_gaap = sales_actual_gaap

    @property
    def sales_mean_estimate(self):
        """Gets the sales_mean_estimate of this ZacksSalesSurprise.  # noqa: E501

        The pre-earnings release mean sales estimate for the company sales_count_estimate; the pre-earnings release number of estimates by analysts  # noqa: E501

        :return: The sales_mean_estimate of this ZacksSalesSurprise.  # noqa: E501
        :rtype: float
        """
        return self._sales_mean_estimate
        
    @property
    def sales_mean_estimate_dict(self):
        """Gets the sales_mean_estimate of this ZacksSalesSurprise.  # noqa: E501

        The pre-earnings release mean sales estimate for the company sales_count_estimate; the pre-earnings release number of estimates by analysts as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The sales_mean_estimate of this ZacksSalesSurprise.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.sales_mean_estimate
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
            result = { 'sales_mean_estimate': value }

        
        return result
        

    @sales_mean_estimate.setter
    def sales_mean_estimate(self, sales_mean_estimate):
        """Sets the sales_mean_estimate of this ZacksSalesSurprise.

        The pre-earnings release mean sales estimate for the company sales_count_estimate; the pre-earnings release number of estimates by analysts  # noqa: E501

        :param sales_mean_estimate: The sales_mean_estimate of this ZacksSalesSurprise.  # noqa: E501
        :type: float
        """

        self._sales_mean_estimate = sales_mean_estimate

    @property
    def sales_amount_diff(self):
        """Gets the sales_amount_diff of this ZacksSalesSurprise.  # noqa: E501

        The sales surprise amount difference  # noqa: E501

        :return: The sales_amount_diff of this ZacksSalesSurprise.  # noqa: E501
        :rtype: float
        """
        return self._sales_amount_diff
        
    @property
    def sales_amount_diff_dict(self):
        """Gets the sales_amount_diff of this ZacksSalesSurprise.  # noqa: E501

        The sales surprise amount difference as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The sales_amount_diff of this ZacksSalesSurprise.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.sales_amount_diff
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
            result = { 'sales_amount_diff': value }

        
        return result
        

    @sales_amount_diff.setter
    def sales_amount_diff(self, sales_amount_diff):
        """Sets the sales_amount_diff of this ZacksSalesSurprise.

        The sales surprise amount difference  # noqa: E501

        :param sales_amount_diff: The sales_amount_diff of this ZacksSalesSurprise.  # noqa: E501
        :type: float
        """

        self._sales_amount_diff = sales_amount_diff

    @property
    def sales_percent_diff(self):
        """Gets the sales_percent_diff of this ZacksSalesSurprise.  # noqa: E501

        The sales surprise percent difference  # noqa: E501

        :return: The sales_percent_diff of this ZacksSalesSurprise.  # noqa: E501
        :rtype: float
        """
        return self._sales_percent_diff
        
    @property
    def sales_percent_diff_dict(self):
        """Gets the sales_percent_diff of this ZacksSalesSurprise.  # noqa: E501

        The sales surprise percent difference as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The sales_percent_diff of this ZacksSalesSurprise.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.sales_percent_diff
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
            result = { 'sales_percent_diff': value }

        
        return result
        

    @sales_percent_diff.setter
    def sales_percent_diff(self, sales_percent_diff):
        """Sets the sales_percent_diff of this ZacksSalesSurprise.

        The sales surprise percent difference  # noqa: E501

        :param sales_percent_diff: The sales_percent_diff of this ZacksSalesSurprise.  # noqa: E501
        :type: float
        """

        self._sales_percent_diff = sales_percent_diff

    @property
    def sales_std_dev_estimate(self):
        """Gets the sales_std_dev_estimate of this ZacksSalesSurprise.  # noqa: E501

        The pre-earnings release standard deviation of sales estimates  # noqa: E501

        :return: The sales_std_dev_estimate of this ZacksSalesSurprise.  # noqa: E501
        :rtype: float
        """
        return self._sales_std_dev_estimate
        
    @property
    def sales_std_dev_estimate_dict(self):
        """Gets the sales_std_dev_estimate of this ZacksSalesSurprise.  # noqa: E501

        The pre-earnings release standard deviation of sales estimates as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The sales_std_dev_estimate of this ZacksSalesSurprise.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.sales_std_dev_estimate
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
            result = { 'sales_std_dev_estimate': value }

        
        return result
        

    @sales_std_dev_estimate.setter
    def sales_std_dev_estimate(self, sales_std_dev_estimate):
        """Sets the sales_std_dev_estimate of this ZacksSalesSurprise.

        The pre-earnings release standard deviation of sales estimates  # noqa: E501

        :param sales_std_dev_estimate: The sales_std_dev_estimate of this ZacksSalesSurprise.  # noqa: E501
        :type: float
        """

        self._sales_std_dev_estimate = sales_std_dev_estimate

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
        if not isinstance(other, ZacksSalesSurprise):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other