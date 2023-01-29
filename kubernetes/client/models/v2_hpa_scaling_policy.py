# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.26
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V2HPAScalingPolicy(object):
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
        'period_seconds': 'int',
        'type': 'str',
        'value': 'int'
    }

    attribute_map = {
        'period_seconds': 'periodSeconds',
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, period_seconds=None, type=None, value=None, local_vars_configuration=None):  # noqa: E501
        """V2HPAScalingPolicy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._period_seconds = None
        self._type = None
        self._value = None
        self.discriminator = None

        self.period_seconds = period_seconds
        self.type = type
        self.value = value

    @property
    def period_seconds(self):
        """Gets the period_seconds of this V2HPAScalingPolicy.  # noqa: E501

        PeriodSeconds specifies the window of time for which the policy should hold true. PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min).  # noqa: E501

        :return: The period_seconds of this V2HPAScalingPolicy.  # noqa: E501
        :rtype: int
        """
        return self._period_seconds

    @period_seconds.setter
    def period_seconds(self, period_seconds):
        """Sets the period_seconds of this V2HPAScalingPolicy.

        PeriodSeconds specifies the window of time for which the policy should hold true. PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min).  # noqa: E501

        :param period_seconds: The period_seconds of this V2HPAScalingPolicy.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and period_seconds is None:  # noqa: E501
            raise ValueError("Invalid value for `period_seconds`, must not be `None`")  # noqa: E501

        self._period_seconds = period_seconds

    @property
    def type(self):
        """Gets the type of this V2HPAScalingPolicy.  # noqa: E501

        Type is used to specify the scaling policy.  # noqa: E501

        :return: The type of this V2HPAScalingPolicy.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V2HPAScalingPolicy.

        Type is used to specify the scaling policy.  # noqa: E501

        :param type: The type of this V2HPAScalingPolicy.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def value(self):
        """Gets the value of this V2HPAScalingPolicy.  # noqa: E501

        Value contains the amount of change which is permitted by the policy. It must be greater than zero  # noqa: E501

        :return: The value of this V2HPAScalingPolicy.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this V2HPAScalingPolicy.

        Value contains the amount of change which is permitted by the policy. It must be greater than zero  # noqa: E501

        :param value: The value of this V2HPAScalingPolicy.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, V2HPAScalingPolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V2HPAScalingPolicy):
            return True

        return self.to_dict() != other.to_dict()
