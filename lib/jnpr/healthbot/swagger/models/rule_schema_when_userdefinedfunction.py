# coding: utf-8

"""
    Healthbot APIs

    API interface for Healthbot application  # noqa: E501

    OpenAPI spec version: 3.1.0
    Contact: healthbot-feedback@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RuleSchemaWhenUserdefinedfunction(object):
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
        'all': 'list[object]',
        'any': 'list[object]',
        'argument': 'list[RuleSchemaThenArgument]',
        'function_name': 'str',
        'time_range': 'str'
    }

    attribute_map = {
        'all': 'all',
        'any': 'any',
        'argument': 'argument',
        'function_name': 'function-name',
        'time_range': 'time-range'
    }

    def __init__(self, all=None, any=None, argument=None, function_name=None, time_range=None):  # noqa: E501
        """RuleSchemaWhenUserdefinedfunction - a model defined in Swagger"""  # noqa: E501

        self._all = None
        self._any = None
        self._argument = None
        self._function_name = None
        self._time_range = None
        self.discriminator = None

        if all is not None:
            self.all = all
        if any is not None:
            self.any = any
        if argument is not None:
            self.argument = argument
        self.function_name = function_name
        if time_range is not None:
            self.time_range = time_range

    @property
    def all(self):
        """Gets the all of this RuleSchemaWhenUserdefinedfunction.  # noqa: E501

        With this flag, result is set to True only if all the data matches the given condition  # noqa: E501

        :return: The all of this RuleSchemaWhenUserdefinedfunction.  # noqa: E501
        :rtype: list[object]
        """
        return self._all

    @all.setter
    def all(self, all):
        """Sets the all of this RuleSchemaWhenUserdefinedfunction.

        With this flag, result is set to True only if all the data matches the given condition  # noqa: E501

        :param all: The all of this RuleSchemaWhenUserdefinedfunction.  # noqa: E501
        :type: list[object]
        """

        self._all = all

    @property
    def any(self):
        """Gets the any of this RuleSchemaWhenUserdefinedfunction.  # noqa: E501

        With this flag, result is set to True if any one of the data matches the condition  # noqa: E501

        :return: The any of this RuleSchemaWhenUserdefinedfunction.  # noqa: E501
        :rtype: list[object]
        """
        return self._any

    @any.setter
    def any(self, any):
        """Sets the any of this RuleSchemaWhenUserdefinedfunction.

        With this flag, result is set to True if any one of the data matches the condition  # noqa: E501

        :param any: The any of this RuleSchemaWhenUserdefinedfunction.  # noqa: E501
        :type: list[object]
        """

        self._any = any

    @property
    def argument(self):
        """Gets the argument of this RuleSchemaWhenUserdefinedfunction.  # noqa: E501


        :return: The argument of this RuleSchemaWhenUserdefinedfunction.  # noqa: E501
        :rtype: list[RuleSchemaThenArgument]
        """
        return self._argument

    @argument.setter
    def argument(self, argument):
        """Sets the argument of this RuleSchemaWhenUserdefinedfunction.


        :param argument: The argument of this RuleSchemaWhenUserdefinedfunction.  # noqa: E501
        :type: list[RuleSchemaThenArgument]
        """

        self._argument = argument

    @property
    def function_name(self):
        """Gets the function_name of this RuleSchemaWhenUserdefinedfunction.  # noqa: E501

        Function name  # noqa: E501

        :return: The function_name of this RuleSchemaWhenUserdefinedfunction.  # noqa: E501
        :rtype: str
        """
        return self._function_name

    @function_name.setter
    def function_name(self, function_name):
        """Sets the function_name of this RuleSchemaWhenUserdefinedfunction.

        Function name  # noqa: E501

        :param function_name: The function_name of this RuleSchemaWhenUserdefinedfunction.  # noqa: E501
        :type: str
        """
        if function_name is None:
            raise ValueError("Invalid value for `function_name`, must not be `None`")  # noqa: E501
        if function_name is not None and len(function_name) > 64:
            raise ValueError("Invalid value for `function_name`, length must be less than or equal to `64`")  # noqa: E501
        if function_name is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9_-]*$', function_name):  # noqa: E501
            raise ValueError(r"Invalid value for `function_name`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._function_name = function_name

    @property
    def time_range(self):
        """Gets the time_range of this RuleSchemaWhenUserdefinedfunction.  # noqa: E501

        How much back in time should we look for data. Specify positive integer followed by s/m/h/d/w/y/o representing seconds/minutes/hours/days/weeks/years/offset. Eg: 2s  # noqa: E501

        :return: The time_range of this RuleSchemaWhenUserdefinedfunction.  # noqa: E501
        :rtype: str
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """Sets the time_range of this RuleSchemaWhenUserdefinedfunction.

        How much back in time should we look for data. Specify positive integer followed by s/m/h/d/w/y/o representing seconds/minutes/hours/days/weeks/years/offset. Eg: 2s  # noqa: E501

        :param time_range: The time_range of this RuleSchemaWhenUserdefinedfunction.  # noqa: E501
        :type: str
        """
        if time_range is not None and not re.search(r'^[1-9][0-9]*(o|s|m|h|d|w|y|offset)$', time_range):  # noqa: E501
            raise ValueError(r"Invalid value for `time_range`, must be a follow pattern or equal to `/^[1-9][0-9]*(o|s|m|h|d|w|y|offset)$/`")  # noqa: E501

        self._time_range = time_range

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
        if issubclass(RuleSchemaWhenUserdefinedfunction, dict):
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
        if not isinstance(other, RuleSchemaWhenUserdefinedfunction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
