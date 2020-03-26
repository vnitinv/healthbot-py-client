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

from jnpr.healthbot.swagger.models.tlivekafkaoc_schema_security import TlivekafkaocSchemaSecurity  # noqa: F401,E501


class TliveKafkaOcSchema(object):
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
        'brokers': 'list[str]',
        'collector_settings': 'object',
        'name': 'str',
        'security': 'TlivekafkaocSchemaSecurity',
        'topics': 'list[str]'
    }

    attribute_map = {
        'brokers': 'brokers',
        'collector_settings': 'collector-settings',
        'name': 'name',
        'security': 'security',
        'topics': 'topics'
    }

    def __init__(self, brokers=None, collector_settings=None, name=None, security=None, topics=None):  # noqa: E501
        """TliveKafkaOcSchema - a model defined in Swagger"""  # noqa: E501

        self._brokers = None
        self._collector_settings = None
        self._name = None
        self._security = None
        self._topics = None
        self.discriminator = None

        self.brokers = brokers
        if collector_settings is not None:
            self.collector_settings = collector_settings
        self.name = name
        if security is not None:
            self.security = security
        if topics is not None:
            self.topics = topics

    @property
    def brokers(self):
        """Gets the brokers of this TliveKafkaOcSchema.  # noqa: E501


        :return: The brokers of this TliveKafkaOcSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._brokers

    @brokers.setter
    def brokers(self, brokers):
        """Sets the brokers of this TliveKafkaOcSchema.


        :param brokers: The brokers of this TliveKafkaOcSchema.  # noqa: E501
        :type: list[str]
        """
        if brokers is None:
            raise ValueError("Invalid value for `brokers`, must not be `None`")  # noqa: E501

        self._brokers = brokers

    @property
    def collector_settings(self):
        """Gets the collector_settings of this TliveKafkaOcSchema.  # noqa: E501


        :return: The collector_settings of this TliveKafkaOcSchema.  # noqa: E501
        :rtype: object
        """
        return self._collector_settings

    @collector_settings.setter
    def collector_settings(self, collector_settings):
        """Sets the collector_settings of this TliveKafkaOcSchema.


        :param collector_settings: The collector_settings of this TliveKafkaOcSchema.  # noqa: E501
        :type: object
        """

        self._collector_settings = collector_settings

    @property
    def name(self):
        """Gets the name of this TliveKafkaOcSchema.  # noqa: E501

        Name of this instance  # noqa: E501

        :return: The name of this TliveKafkaOcSchema.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TliveKafkaOcSchema.

        Name of this instance  # noqa: E501

        :param name: The name of this TliveKafkaOcSchema.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 64:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501
        if name is not None and not re.search('^[a-zA-Z][a-zA-Z0-9_-]*$', name):  # noqa: E501
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._name = name

    @property
    def security(self):
        """Gets the security of this TliveKafkaOcSchema.  # noqa: E501


        :return: The security of this TliveKafkaOcSchema.  # noqa: E501
        :rtype: TlivekafkaocSchemaSecurity
        """
        return self._security

    @security.setter
    def security(self, security):
        """Sets the security of this TliveKafkaOcSchema.


        :param security: The security of this TliveKafkaOcSchema.  # noqa: E501
        :type: TlivekafkaocSchemaSecurity
        """

        self._security = security

    @property
    def topics(self):
        """Gets the topics of this TliveKafkaOcSchema.  # noqa: E501


        :return: The topics of this TliveKafkaOcSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        """Sets the topics of this TliveKafkaOcSchema.


        :param topics: The topics of this TliveKafkaOcSchema.  # noqa: E501
        :type: list[str]
        """

        self._topics = topics

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
        if not isinstance(other, TliveKafkaOcSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
