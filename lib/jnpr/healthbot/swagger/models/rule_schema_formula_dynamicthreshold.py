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


class RuleSchemaFormulaDynamicthreshold(object):
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
        'algorithm': 'str',
        'field_name': 'str',
        'learning_period': 'str',
        'pattern_periodicity': 'str'
    }

    attribute_map = {
        'algorithm': 'algorithm',
        'field_name': 'field-name',
        'learning_period': 'learning-period',
        'pattern_periodicity': 'pattern-periodicity'
    }

    def __init__(self, algorithm=None, field_name=None, learning_period=None, pattern_periodicity=None):  # noqa: E501
        """RuleSchemaFormulaDynamicthreshold - a model defined in Swagger"""  # noqa: E501

        self._algorithm = None
        self._field_name = None
        self._learning_period = None
        self._pattern_periodicity = None
        self.discriminator = None

        self.algorithm = algorithm
        self.field_name = field_name
        self.learning_period = learning_period
        self.pattern_periodicity = pattern_periodicity

    @property
    def algorithm(self):
        """Gets the algorithm of this RuleSchemaFormulaDynamicthreshold.  # noqa: E501

        Algorithm used to learn the dynamic threshold value  # noqa: E501

        :return: The algorithm of this RuleSchemaFormulaDynamicthreshold.  # noqa: E501
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this RuleSchemaFormulaDynamicthreshold.

        Algorithm used to learn the dynamic threshold value  # noqa: E501

        :param algorithm: The algorithm of this RuleSchemaFormulaDynamicthreshold.  # noqa: E501
        :type: str
        """
        if algorithm is None:
            raise ValueError("Invalid value for `algorithm`, must not be `None`")  # noqa: E501
        allowed_values = ["3sigma", "k-means"]  # noqa: E501
        if algorithm not in allowed_values:
            raise ValueError(
                "Invalid value for `algorithm` ({0}), must be one of {1}"  # noqa: E501
                .format(algorithm, allowed_values)
            )

        self._algorithm = algorithm

    @property
    def field_name(self):
        """Gets the field_name of this RuleSchemaFormulaDynamicthreshold.  # noqa: E501

        Field name on which dynamic threshold needs to be applied  # noqa: E501

        :return: The field_name of this RuleSchemaFormulaDynamicthreshold.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this RuleSchemaFormulaDynamicthreshold.

        Field name on which dynamic threshold needs to be applied  # noqa: E501

        :param field_name: The field_name of this RuleSchemaFormulaDynamicthreshold.  # noqa: E501
        :type: str
        """
        if field_name is None:
            raise ValueError("Invalid value for `field_name`, must not be `None`")  # noqa: E501

        self._field_name = field_name

    @property
    def learning_period(self):
        """Gets the learning_period of this RuleSchemaFormulaDynamicthreshold.  # noqa: E501

        Learning period to learn the dynamic threshold. Should be of pattern [1-9][0-9]*(seconds|minutes|hours|days|weeks|years|offset)  # noqa: E501

        :return: The learning_period of this RuleSchemaFormulaDynamicthreshold.  # noqa: E501
        :rtype: str
        """
        return self._learning_period

    @learning_period.setter
    def learning_period(self, learning_period):
        """Sets the learning_period of this RuleSchemaFormulaDynamicthreshold.

        Learning period to learn the dynamic threshold. Should be of pattern [1-9][0-9]*(seconds|minutes|hours|days|weeks|years|offset)  # noqa: E501

        :param learning_period: The learning_period of this RuleSchemaFormulaDynamicthreshold.  # noqa: E501
        :type: str
        """
        if learning_period is None:
            raise ValueError("Invalid value for `learning_period`, must not be `None`")  # noqa: E501
        if learning_period is not None and not re.search('^[1-9][0-9]*(offset|seconds|minutes|hours|days|weeks|years|o|s|m|h|d|w|y)$', learning_period):  # noqa: E501
            raise ValueError("Invalid value for `learning_period`, must be a follow pattern or equal to `/^[1-9][0-9]*(offset|seconds|minutes|hours|days|weeks|years|o|s|m|h|d|w|y)$/`")  # noqa: E501

        self._learning_period = learning_period

    @property
    def pattern_periodicity(self):
        """Gets the pattern_periodicity of this RuleSchemaFormulaDynamicthreshold.  # noqa: E501

        Pattern periodicity. Should be of pattern [1-9][0-9]*(minutes|hours|days|weeks|months)(,[1-9][0-9]*(minutes|hours|days|weeks|months))*  # noqa: E501

        :return: The pattern_periodicity of this RuleSchemaFormulaDynamicthreshold.  # noqa: E501
        :rtype: str
        """
        return self._pattern_periodicity

    @pattern_periodicity.setter
    def pattern_periodicity(self, pattern_periodicity):
        """Sets the pattern_periodicity of this RuleSchemaFormulaDynamicthreshold.

        Pattern periodicity. Should be of pattern [1-9][0-9]*(minutes|hours|days|weeks|months)(,[1-9][0-9]*(minutes|hours|days|weeks|months))*  # noqa: E501

        :param pattern_periodicity: The pattern_periodicity of this RuleSchemaFormulaDynamicthreshold.  # noqa: E501
        :type: str
        """
        if pattern_periodicity is None:
            raise ValueError("Invalid value for `pattern_periodicity`, must not be `None`")  # noqa: E501
        if pattern_periodicity is not None and not re.search('^[1-9][0-9]*(minutes|hours|days|weeks|months|t|h|d|w|m|T|H|D|W|M)(,[1-9][0-9]*(minutes|hours|days|weeks|months|t|h|d|w|m|T|H|D|W|M))*$', pattern_periodicity):  # noqa: E501
            raise ValueError("Invalid value for `pattern_periodicity`, must be a follow pattern or equal to `/^[1-9][0-9]*(minutes|hours|days|weeks|months|t|h|d|w|m|T|H|D|W|M)(,[1-9][0-9]*(minutes|hours|days|weeks|months|t|h|d|w|m|T|H|D|W|M))*$/`")  # noqa: E501

        self._pattern_periodicity = pattern_periodicity

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
        if not isinstance(other, RuleSchemaFormulaDynamicthreshold):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
