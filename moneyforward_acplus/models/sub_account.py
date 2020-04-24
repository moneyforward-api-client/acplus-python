# coding: utf-8

"""
    マネーフォワードクラウド会計Plus API

    マネーフォワードクラウド会計PlusのAPI  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: api.acplus.support@moneyforward.co.jp
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from moneyforward_acplus.configuration import Configuration


class SubAccount(object):
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
        'account_id': 'int',
        'sub_account_name': 'str',
        'tax': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'sub_account_name': 'subAccountName',
        'tax': 'tax'
    }

    def __init__(self, account_id=None, sub_account_name=None, tax=None, local_vars_configuration=None):  # noqa: E501
        """SubAccount - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._sub_account_name = None
        self._tax = None
        self.discriminator = None

        self.account_id = account_id
        self.sub_account_name = sub_account_name
        self.tax = tax

    @property
    def account_id(self):
        """Gets the account_id of this SubAccount.  # noqa: E501

        勘定科目ID  # noqa: E501

        :return: The account_id of this SubAccount.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this SubAccount.

        勘定科目ID  # noqa: E501

        :param account_id: The account_id of this SubAccount.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def sub_account_name(self):
        """Gets the sub_account_name of this SubAccount.  # noqa: E501

        補助科目名  # noqa: E501

        :return: The sub_account_name of this SubAccount.  # noqa: E501
        :rtype: str
        """
        return self._sub_account_name

    @sub_account_name.setter
    def sub_account_name(self, sub_account_name):
        """Sets the sub_account_name of this SubAccount.

        補助科目名  # noqa: E501

        :param sub_account_name: The sub_account_name of this SubAccount.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sub_account_name is None:  # noqa: E501
            raise ValueError("Invalid value for `sub_account_name`, must not be `None`")  # noqa: E501

        self._sub_account_name = sub_account_name

    @property
    def tax(self):
        """Gets the tax of this SubAccount.  # noqa: E501

        税区分  # noqa: E501

        :return: The tax of this SubAccount.  # noqa: E501
        :rtype: str
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Sets the tax of this SubAccount.

        税区分  # noqa: E501

        :param tax: The tax of this SubAccount.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and tax is None:  # noqa: E501
            raise ValueError("Invalid value for `tax`, must not be `None`")  # noqa: E501

        self._tax = tax

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
        if not isinstance(other, SubAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubAccount):
            return True

        return self.to_dict() != other.to_dict()