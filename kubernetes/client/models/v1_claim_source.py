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


class V1ClaimSource(object):
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
        'resource_claim_name': 'str',
        'resource_claim_template_name': 'str'
    }

    attribute_map = {
        'resource_claim_name': 'resourceClaimName',
        'resource_claim_template_name': 'resourceClaimTemplateName'
    }

    def __init__(self, resource_claim_name=None, resource_claim_template_name=None, local_vars_configuration=None):  # noqa: E501
        """V1ClaimSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._resource_claim_name = None
        self._resource_claim_template_name = None
        self.discriminator = None

        if resource_claim_name is not None:
            self.resource_claim_name = resource_claim_name
        if resource_claim_template_name is not None:
            self.resource_claim_template_name = resource_claim_template_name

    @property
    def resource_claim_name(self):
        """Gets the resource_claim_name of this V1ClaimSource.  # noqa: E501

        ResourceClaimName is the name of a ResourceClaim object in the same namespace as this pod.  # noqa: E501

        :return: The resource_claim_name of this V1ClaimSource.  # noqa: E501
        :rtype: str
        """
        return self._resource_claim_name

    @resource_claim_name.setter
    def resource_claim_name(self, resource_claim_name):
        """Sets the resource_claim_name of this V1ClaimSource.

        ResourceClaimName is the name of a ResourceClaim object in the same namespace as this pod.  # noqa: E501

        :param resource_claim_name: The resource_claim_name of this V1ClaimSource.  # noqa: E501
        :type: str
        """

        self._resource_claim_name = resource_claim_name

    @property
    def resource_claim_template_name(self):
        """Gets the resource_claim_template_name of this V1ClaimSource.  # noqa: E501

        ResourceClaimTemplateName is the name of a ResourceClaimTemplate object in the same namespace as this pod.  The template will be used to create a new ResourceClaim, which will be bound to this pod. When this pod is deleted, the ResourceClaim will also be deleted. The name of the ResourceClaim will be <pod name>-<resource name>, where <resource name> is the PodResourceClaim.Name. Pod validation will reject the pod if the concatenated name is not valid for a ResourceClaim (e.g. too long).  An existing ResourceClaim with that name that is not owned by the pod will not be used for the pod to avoid using an unrelated resource by mistake. Scheduling and pod startup are then blocked until the unrelated ResourceClaim is removed.  This field is immutable and no changes will be made to the corresponding ResourceClaim by the control plane after creating the ResourceClaim.  # noqa: E501

        :return: The resource_claim_template_name of this V1ClaimSource.  # noqa: E501
        :rtype: str
        """
        return self._resource_claim_template_name

    @resource_claim_template_name.setter
    def resource_claim_template_name(self, resource_claim_template_name):
        """Sets the resource_claim_template_name of this V1ClaimSource.

        ResourceClaimTemplateName is the name of a ResourceClaimTemplate object in the same namespace as this pod.  The template will be used to create a new ResourceClaim, which will be bound to this pod. When this pod is deleted, the ResourceClaim will also be deleted. The name of the ResourceClaim will be <pod name>-<resource name>, where <resource name> is the PodResourceClaim.Name. Pod validation will reject the pod if the concatenated name is not valid for a ResourceClaim (e.g. too long).  An existing ResourceClaim with that name that is not owned by the pod will not be used for the pod to avoid using an unrelated resource by mistake. Scheduling and pod startup are then blocked until the unrelated ResourceClaim is removed.  This field is immutable and no changes will be made to the corresponding ResourceClaim by the control plane after creating the ResourceClaim.  # noqa: E501

        :param resource_claim_template_name: The resource_claim_template_name of this V1ClaimSource.  # noqa: E501
        :type: str
        """

        self._resource_claim_template_name = resource_claim_template_name

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
        if not isinstance(other, V1ClaimSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ClaimSource):
            return True

        return self.to_dict() != other.to_dict()
