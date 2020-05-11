# coding: utf-8

"""
    Healthbot APIs

    API interface for Healthbot application  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: healthbot-hackers@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class LicenseFeaturesSchema(object):
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
        'license_feature': 'list[LicenseFeatureSchema]'
    }

    attribute_map = {
        'license_feature': 'license-feature'
    }

    def __init__(self, license_feature=None):  # noqa: E501
        """LicenseFeaturesSchema - a model defined in Swagger"""  # noqa: E501

        self._license_feature = None
        self.discriminator = None

        if license_feature is not None:
            self.license_feature = license_feature

    @property
    def license_feature(self):
        """Gets the license_feature of this LicenseFeaturesSchema.  # noqa: E501


        :return: The license_feature of this LicenseFeaturesSchema.  # noqa: E501
        :rtype: list[LicenseFeatureSchema]
        """
        return self._license_feature

    @license_feature.setter
    def license_feature(self, license_feature):
        """Sets the license_feature of this LicenseFeaturesSchema.


        :param license_feature: The license_feature of this LicenseFeaturesSchema.  # noqa: E501
        :type: list[LicenseFeatureSchema]
        """

        self._license_feature = license_feature

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
        if issubclass(LicenseFeaturesSchema, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LicenseFeaturesSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
