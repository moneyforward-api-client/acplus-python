# coding: utf-8

"""
    マネーフォワードクラウド会計Plus API

    マネーフォワードクラウド会計PlusのAPI  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: yasuhiroota26@gmail.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from moneyforward_acplus.configuration import Configuration


class Account(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'account_financial_statements_type': 'str',
        'category_name': 'str',
        'account_id': 'int',
        'account_name': 'str',
        'tax': 'str',
        'is_enabled': 'bool'
    }

    attribute_map = {
        'account_financial_statements_type': 'accountFinancialStatementsType',
        'category_name': 'categoryName',
        'account_id': 'accountId',
        'account_name': 'accountName',
        'tax': 'tax',
        'is_enabled': 'isEnabled'
    }

    def __init__(self, account_financial_statements_type=None, category_name=None, account_id=None, account_name=None, tax=None, is_enabled=None, local_vars_configuration=None):  # noqa: E501
        """Account - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_financial_statements_type = None
        self._category_name = None
        self._account_id = None
        self._account_name = None
        self._tax = None
        self._is_enabled = None
        self.discriminator = None

        self.account_financial_statements_type = account_financial_statements_type
        self.category_name = category_name
        self.account_id = account_id
        self.account_name = account_name
        self.tax = tax
        self.is_enabled = is_enabled

    @property
    def account_financial_statements_type(self):
        """Gets the account_financial_statements_type of this Account.  # noqa: E501

        帳票  # noqa: E501

        :return: The account_financial_statements_type of this Account.  # noqa: E501
        :rtype: str
        """
        return self._account_financial_statements_type

    @account_financial_statements_type.setter
    def account_financial_statements_type(self, account_financial_statements_type):
        """Sets the account_financial_statements_type of this Account.

        帳票  # noqa: E501

        :param account_financial_statements_type: The account_financial_statements_type of this Account.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and account_financial_statements_type is None:  # noqa: E501
            raise ValueError("Invalid value for `account_financial_statements_type`, must not be `None`")  # noqa: E501

        self._account_financial_statements_type = account_financial_statements_type

    @property
    def category_name(self):
        """Gets the category_name of this Account.  # noqa: E501

        分類  # noqa: E501

        :return: The category_name of this Account.  # noqa: E501
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """Sets the category_name of this Account.

        分類  # noqa: E501

        :param category_name: The category_name of this Account.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and category_name is None:  # noqa: E501
            raise ValueError("Invalid value for `category_name`, must not be `None`")  # noqa: E501

        self._category_name = category_name

    @property
    def account_id(self):
        """Gets the account_id of this Account.  # noqa: E501

        勘定科目ID  # noqa: E501

        :return: The account_id of this Account.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Account.

        勘定科目ID  # noqa: E501

        :param account_id: The account_id of this Account.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def account_name(self):
        """Gets the account_name of this Account.  # noqa: E501

        勘定科目名  # noqa: E501

        :return: The account_name of this Account.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this Account.

        勘定科目名  # noqa: E501

        :param account_name: The account_name of this Account.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and account_name is None:  # noqa: E501
            raise ValueError("Invalid value for `account_name`, must not be `None`")  # noqa: E501

        self._account_name = account_name

    @property
    def tax(self):
        """Gets the tax of this Account.  # noqa: E501

        税区分  # noqa: E501

        :return: The tax of this Account.  # noqa: E501
        :rtype: str
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Sets the tax of this Account.

        税区分  # noqa: E501

        :param tax: The tax of this Account.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and tax is None:  # noqa: E501
            raise ValueError("Invalid value for `tax`, must not be `None`")  # noqa: E501

        self._tax = tax

    @property
    def is_enabled(self):
        """Gets the is_enabled of this Account.  # noqa: E501

        使用  # noqa: E501

        :return: The is_enabled of this Account.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this Account.

        使用  # noqa: E501

        :param is_enabled: The is_enabled of this Account.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_enabled is None:  # noqa: E501
            raise ValueError("Invalid value for `is_enabled`, must not be `None`")  # noqa: E501

        self._is_enabled = is_enabled

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, Account):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Account):
            return True

        return self.to_dict() != other.to_dict()
