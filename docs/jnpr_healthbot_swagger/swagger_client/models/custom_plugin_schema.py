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

from swagger_client.models.customplugin_schema_parameters import CustompluginSchemaParameters  # noqa: F401,E501
from swagger_client.models.customplugin_schema_securityparameters import CustompluginSchemaSecurityparameters  # noqa: F401,E501


class CustomPluginSchema(object):
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
        'name': 'str',
        'parameters': 'list[CustompluginSchemaParameters]',
        'plugin_name': 'str',
        'security_parameters': 'CustompluginSchemaSecurityparameters',
        'service_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'parameters': 'parameters',
        'plugin_name': 'plugin-name',
        'security_parameters': 'security-parameters',
        'service_name': 'service-name'
    }

    def __init__(self, name=None, parameters=None, plugin_name=None, security_parameters=None, service_name=None):  # noqa: E501
        """CustomPluginSchema - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._parameters = None
        self._plugin_name = None
        self._security_parameters = None
        self._service_name = None
        self.discriminator = None

        self.name = name
        if parameters is not None:
            self.parameters = parameters
        if plugin_name is not None:
            self.plugin_name = plugin_name
        if security_parameters is not None:
            self.security_parameters = security_parameters
        if service_name is not None:
            self.service_name = service_name

    @property
    def name(self):
        """Gets the name of this CustomPluginSchema.  # noqa: E501

        Name is the identifier of this config, referred in sensor config under topic/rule  # noqa: E501

        :return: The name of this CustomPluginSchema.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomPluginSchema.

        Name is the identifier of this config, referred in sensor config under topic/rule  # noqa: E501

        :param name: The name of this CustomPluginSchema.  # noqa: E501
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
    def parameters(self):
        """Gets the parameters of this CustomPluginSchema.  # noqa: E501

        Plugin specific parameters (config)  # noqa: E501

        :return: The parameters of this CustomPluginSchema.  # noqa: E501
        :rtype: list[CustompluginSchemaParameters]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this CustomPluginSchema.

        Plugin specific parameters (config)  # noqa: E501

        :param parameters: The parameters of this CustomPluginSchema.  # noqa: E501
        :type: list[CustompluginSchemaParameters]
        """

        self._parameters = parameters

    @property
    def plugin_name(self):
        """Gets the plugin_name of this CustomPluginSchema.  # noqa: E501

        Name of the loaded input plugin of BYOI  # noqa: E501

        :return: The plugin_name of this CustomPluginSchema.  # noqa: E501
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """Sets the plugin_name of this CustomPluginSchema.

        Name of the loaded input plugin of BYOI  # noqa: E501

        :param plugin_name: The plugin_name of this CustomPluginSchema.  # noqa: E501
        :type: str
        """

        self._plugin_name = plugin_name

    @property
    def security_parameters(self):
        """Gets the security_parameters of this CustomPluginSchema.  # noqa: E501


        :return: The security_parameters of this CustomPluginSchema.  # noqa: E501
        :rtype: CustompluginSchemaSecurityparameters
        """
        return self._security_parameters

    @security_parameters.setter
    def security_parameters(self, security_parameters):
        """Sets the security_parameters of this CustomPluginSchema.


        :param security_parameters: The security_parameters of this CustomPluginSchema.  # noqa: E501
        :type: CustompluginSchemaSecurityparameters
        """

        self._security_parameters = security_parameters

    @property
    def service_name(self):
        """Gets the service_name of this CustomPluginSchema.  # noqa: E501

        Name of the service (docker container) which implements this plugin  # noqa: E501

        :return: The service_name of this CustomPluginSchema.  # noqa: E501
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this CustomPluginSchema.

        Name of the service (docker container) which implements this plugin  # noqa: E501

        :param service_name: The service_name of this CustomPluginSchema.  # noqa: E501
        :type: str
        """

        self._service_name = service_name

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
        if not isinstance(other, CustomPluginSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
