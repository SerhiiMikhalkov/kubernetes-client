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


class V1alpha1ValidatingAdmissionPolicySpec(object):
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
        'failure_policy': 'str',
        'match_constraints': 'V1alpha1MatchResources',
        'param_kind': 'V1alpha1ParamKind',
        'validations': 'list[V1alpha1Validation]'
    }

    attribute_map = {
        'failure_policy': 'failurePolicy',
        'match_constraints': 'matchConstraints',
        'param_kind': 'paramKind',
        'validations': 'validations'
    }

    def __init__(self, failure_policy=None, match_constraints=None, param_kind=None, validations=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1ValidatingAdmissionPolicySpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._failure_policy = None
        self._match_constraints = None
        self._param_kind = None
        self._validations = None
        self.discriminator = None

        if failure_policy is not None:
            self.failure_policy = failure_policy
        if match_constraints is not None:
            self.match_constraints = match_constraints
        if param_kind is not None:
            self.param_kind = param_kind
        self.validations = validations

    @property
    def failure_policy(self):
        """Gets the failure_policy of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501

        FailurePolicy defines how to handle failures for the admission policy. Failures can occur from invalid or mis-configured policy definitions or bindings. A policy is invalid if spec.paramKind refers to a non-existent Kind. A binding is invalid if spec.paramRef.name refers to a non-existent resource. Allowed values are Ignore or Fail. Defaults to Fail.  # noqa: E501

        :return: The failure_policy of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501
        :rtype: str
        """
        return self._failure_policy

    @failure_policy.setter
    def failure_policy(self, failure_policy):
        """Sets the failure_policy of this V1alpha1ValidatingAdmissionPolicySpec.

        FailurePolicy defines how to handle failures for the admission policy. Failures can occur from invalid or mis-configured policy definitions or bindings. A policy is invalid if spec.paramKind refers to a non-existent Kind. A binding is invalid if spec.paramRef.name refers to a non-existent resource. Allowed values are Ignore or Fail. Defaults to Fail.  # noqa: E501

        :param failure_policy: The failure_policy of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501
        :type: str
        """

        self._failure_policy = failure_policy

    @property
    def match_constraints(self):
        """Gets the match_constraints of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501


        :return: The match_constraints of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501
        :rtype: V1alpha1MatchResources
        """
        return self._match_constraints

    @match_constraints.setter
    def match_constraints(self, match_constraints):
        """Sets the match_constraints of this V1alpha1ValidatingAdmissionPolicySpec.


        :param match_constraints: The match_constraints of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501
        :type: V1alpha1MatchResources
        """

        self._match_constraints = match_constraints

    @property
    def param_kind(self):
        """Gets the param_kind of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501


        :return: The param_kind of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501
        :rtype: V1alpha1ParamKind
        """
        return self._param_kind

    @param_kind.setter
    def param_kind(self, param_kind):
        """Sets the param_kind of this V1alpha1ValidatingAdmissionPolicySpec.


        :param param_kind: The param_kind of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501
        :type: V1alpha1ParamKind
        """

        self._param_kind = param_kind

    @property
    def validations(self):
        """Gets the validations of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501

        Validations contain CEL expressions which is used to apply the validation. A minimum of one validation is required for a policy definition. Required.  # noqa: E501

        :return: The validations of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501
        :rtype: list[V1alpha1Validation]
        """
        return self._validations

    @validations.setter
    def validations(self, validations):
        """Sets the validations of this V1alpha1ValidatingAdmissionPolicySpec.

        Validations contain CEL expressions which is used to apply the validation. A minimum of one validation is required for a policy definition. Required.  # noqa: E501

        :param validations: The validations of this V1alpha1ValidatingAdmissionPolicySpec.  # noqa: E501
        :type: list[V1alpha1Validation]
        """
        if self.local_vars_configuration.client_side_validation and validations is None:  # noqa: E501
            raise ValueError("Invalid value for `validations`, must not be `None`")  # noqa: E501

        self._validations = validations

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
        if not isinstance(other, V1alpha1ValidatingAdmissionPolicySpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1ValidatingAdmissionPolicySpec):
            return True

        return self.to_dict() != other.to_dict()
