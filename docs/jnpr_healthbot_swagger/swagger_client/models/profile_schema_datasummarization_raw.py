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


class ProfileSchemaDatasummarizationRaw(object):
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
        'data_type': 'list[RawSchemaDatatype]',
        'name': 'str',
        'path': 'list[RawSchemaPath]'
    }

    attribute_map = {
        'data_type': 'data-type',
        'name': 'name',
        'path': 'path'
    }

    def __init__(self, data_type=None, name=None, path=None):  # noqa: E501
        """ProfileSchemaDatasummarizationRaw - a model defined in Swagger"""  # noqa: E501

        self._data_type = None
        self._name = None
        self._path = None
        self.discriminator = None

        if data_type is not None:
            self.data_type = data_type
        self.name = name
        if path is not None:
            self.path = path

    @property
    def data_type(self):
        """Gets the data_type of this ProfileSchemaDatasummarizationRaw.  # noqa: E501


        :return: The data_type of this ProfileSchemaDatasummarizationRaw.  # noqa: E501
        :rtype: list[RawSchemaDatatype]
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this ProfileSchemaDatasummarizationRaw.


        :param data_type: The data_type of this ProfileSchemaDatasummarizationRaw.  # noqa: E501
        :type: list[RawSchemaDatatype]
        """

        self._data_type = data_type

    @property
    def name(self):
        """Gets the name of this ProfileSchemaDatasummarizationRaw.  # noqa: E501

        Name of raw-data summarization profile  # noqa: E501

        :return: The name of this ProfileSchemaDatasummarizationRaw.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProfileSchemaDatasummarizationRaw.

        Name of raw-data summarization profile  # noqa: E501

        :param name: The name of this ProfileSchemaDatasummarizationRaw.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 64:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501
        if name is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9_-]*$', name):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._name = name

    @property
    def path(self):
        """Gets the path of this ProfileSchemaDatasummarizationRaw.  # noqa: E501


        :return: The path of this ProfileSchemaDatasummarizationRaw.  # noqa: E501
        :rtype: list[RawSchemaPath]
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ProfileSchemaDatasummarizationRaw.


        :param path: The path of this ProfileSchemaDatasummarizationRaw.  # noqa: E501
        :type: list[RawSchemaPath]
        """

        self._path = path

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
        if issubclass(ProfileSchemaDatasummarizationRaw, dict):
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
        if not isinstance(other, ProfileSchemaDatasummarizationRaw):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
