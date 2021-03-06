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


class JournalFileStatus(object):
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
        'request_id': 'int',
        'requested_at': 'datetime',
        'request_params': 'CreateJournalFileRequest',
        'status': 'str',
        'created_at': 'datetime'
    }

    attribute_map = {
        'request_id': 'requestId',
        'requested_at': 'requestedAt',
        'request_params': 'requestParams',
        'status': 'status',
        'created_at': 'createdAt'
    }

    def __init__(self, request_id=None, requested_at=None, request_params=None, status=None, created_at=None, local_vars_configuration=None):  # noqa: E501
        """JournalFileStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._request_id = None
        self._requested_at = None
        self._request_params = None
        self._status = None
        self._created_at = None
        self.discriminator = None

        self.request_id = request_id
        self.requested_at = requested_at
        self.request_params = request_params
        self.status = status
        if created_at is not None:
            self.created_at = created_at

    @property
    def request_id(self):
        """Gets the request_id of this JournalFileStatus.  # noqa: E501

        作成要求ID  # noqa: E501

        :return: The request_id of this JournalFileStatus.  # noqa: E501
        :rtype: int
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this JournalFileStatus.

        作成要求ID  # noqa: E501

        :param request_id: The request_id of this JournalFileStatus.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and request_id is None:  # noqa: E501
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                request_id is not None and request_id < 0):  # noqa: E501
            raise ValueError("Invalid value for `request_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._request_id = request_id

    @property
    def requested_at(self):
        """Gets the requested_at of this JournalFileStatus.  # noqa: E501

        作成要求日時  # noqa: E501

        :return: The requested_at of this JournalFileStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._requested_at

    @requested_at.setter
    def requested_at(self, requested_at):
        """Sets the requested_at of this JournalFileStatus.

        作成要求日時  # noqa: E501

        :param requested_at: The requested_at of this JournalFileStatus.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and requested_at is None:  # noqa: E501
            raise ValueError("Invalid value for `requested_at`, must not be `None`")  # noqa: E501

        self._requested_at = requested_at

    @property
    def request_params(self):
        """Gets the request_params of this JournalFileStatus.  # noqa: E501


        :return: The request_params of this JournalFileStatus.  # noqa: E501
        :rtype: CreateJournalFileRequest
        """
        return self._request_params

    @request_params.setter
    def request_params(self, request_params):
        """Sets the request_params of this JournalFileStatus.


        :param request_params: The request_params of this JournalFileStatus.  # noqa: E501
        :type: CreateJournalFileRequest
        """
        if self.local_vars_configuration.client_side_validation and request_params is None:  # noqa: E501
            raise ValueError("Invalid value for `request_params`, must not be `None`")  # noqa: E501

        self._request_params = request_params

    @property
    def status(self):
        """Gets the status of this JournalFileStatus.  # noqa: E501

        作成状況  # noqa: E501

        :return: The status of this JournalFileStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JournalFileStatus.

        作成状況  # noqa: E501

        :param status: The status of this JournalFileStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["pending", "in_progress", "created", "failed"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this JournalFileStatus.  # noqa: E501

        作成日時  # noqa: E501

        :return: The created_at of this JournalFileStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this JournalFileStatus.

        作成日時  # noqa: E501

        :param created_at: The created_at of this JournalFileStatus.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

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
        if not isinstance(other, JournalFileStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JournalFileStatus):
            return True

        return self.to_dict() != other.to_dict()
