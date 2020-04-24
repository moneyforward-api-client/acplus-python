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


class CreateJournalFileResponse(object):
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
        'request_id': 'int'
    }

    attribute_map = {
        'request_id': 'requestId'
    }

    def __init__(self, request_id=None, local_vars_configuration=None):  # noqa: E501
        """CreateJournalFileResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._request_id = None
        self.discriminator = None

        self.request_id = request_id

    @property
    def request_id(self):
        """Gets the request_id of this CreateJournalFileResponse.  # noqa: E501

        作成要求ID  # noqa: E501

        :return: The request_id of this CreateJournalFileResponse.  # noqa: E501
        :rtype: int
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this CreateJournalFileResponse.

        作成要求ID  # noqa: E501

        :param request_id: The request_id of this CreateJournalFileResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and request_id is None:  # noqa: E501
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                request_id is not None and request_id < 0):  # noqa: E501
            raise ValueError("Invalid value for `request_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._request_id = request_id

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
        if not isinstance(other, CreateJournalFileResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateJournalFileResponse):
            return True

        return self.to_dict() != other.to_dict()
