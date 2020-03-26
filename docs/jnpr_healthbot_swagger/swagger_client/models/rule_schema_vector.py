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

from swagger_client.models.rule_schema_formula1 import RuleSchemaFormula1  # noqa: F401,E501


class RuleSchemaVector(object):
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
        'formula': 'RuleSchemaFormula1',
        'path': 'list[str]',
        'time_range': 'str',
        'vector_name': 'str'
    }

    attribute_map = {
        'formula': 'formula',
        'path': 'path',
        'time_range': 'time-range',
        'vector_name': 'vector-name'
    }

    def __init__(self, formula=None, path=None, time_range=None, vector_name=None):  # noqa: E501
        """RuleSchemaVector - a model defined in Swagger"""  # noqa: E501

        self._formula = None
        self._path = None
        self._time_range = None
        self._vector_name = None
        self.discriminator = None

        if formula is not None:
            self.formula = formula
        if path is not None:
            self.path = path
        if time_range is not None:
            self.time_range = time_range
        self.vector_name = vector_name

    @property
    def formula(self):
        """Gets the formula of this RuleSchemaVector.  # noqa: E501


        :return: The formula of this RuleSchemaVector.  # noqa: E501
        :rtype: RuleSchemaFormula1
        """
        return self._formula

    @formula.setter
    def formula(self, formula):
        """Sets the formula of this RuleSchemaVector.


        :param formula: The formula of this RuleSchemaVector.  # noqa: E501
        :type: RuleSchemaFormula1
        """

        self._formula = formula

    @property
    def path(self):
        """Gets the path of this RuleSchemaVector.  # noqa: E501


        :return: The path of this RuleSchemaVector.  # noqa: E501
        :rtype: list[str]
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this RuleSchemaVector.


        :param path: The path of this RuleSchemaVector.  # noqa: E501
        :type: list[str]
        """

        self._path = path

    @property
    def time_range(self):
        """Gets the time_range of this RuleSchemaVector.  # noqa: E501

        How much back in time should we look for data. Specify positive integer followed by s/m/h/d/w/y/o representing seconds/minutes/hours/days/weeks/years/offset. Eg: 2s  # noqa: E501

        :return: The time_range of this RuleSchemaVector.  # noqa: E501
        :rtype: str
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """Sets the time_range of this RuleSchemaVector.

        How much back in time should we look for data. Specify positive integer followed by s/m/h/d/w/y/o representing seconds/minutes/hours/days/weeks/years/offset. Eg: 2s  # noqa: E501

        :param time_range: The time_range of this RuleSchemaVector.  # noqa: E501
        :type: str
        """
        if time_range is not None and not re.search('^[1-9][0-9]*(o|s|m|h|d|w|y|offset)$', time_range):  # noqa: E501
            raise ValueError("Invalid value for `time_range`, must be a follow pattern or equal to `/^[1-9][0-9]*(o|s|m|h|d|w|y|offset)$/`")  # noqa: E501

        self._time_range = time_range

    @property
    def vector_name(self):
        """Gets the vector_name of this RuleSchemaVector.  # noqa: E501

        Name of the vector. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :return: The vector_name of this RuleSchemaVector.  # noqa: E501
        :rtype: str
        """
        return self._vector_name

    @vector_name.setter
    def vector_name(self, vector_name):
        """Sets the vector_name of this RuleSchemaVector.

        Name of the vector. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :param vector_name: The vector_name of this RuleSchemaVector.  # noqa: E501
        :type: str
        """
        if vector_name is None:
            raise ValueError("Invalid value for `vector_name`, must not be `None`")  # noqa: E501
        if vector_name is not None and len(vector_name) > 64:
            raise ValueError("Invalid value for `vector_name`, length must be less than or equal to `64`")  # noqa: E501
        if vector_name is not None and not re.search('^[a-zA-Z][a-zA-Z0-9_-]*$', vector_name):  # noqa: E501
            raise ValueError("Invalid value for `vector_name`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._vector_name = vector_name

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
        if not isinstance(other, RuleSchemaVector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
