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

from jnpr.healthbot.swagger.models.rule_schema_byoi import RuleSchemaByoi  # noqa: F401,E501
from jnpr.healthbot.swagger.models.rule_schema_flow import RuleSchemaFlow  # noqa: F401,E501
from jnpr.healthbot.swagger.models.rule_schema_i_agent import RuleSchemaIAgent  # noqa: F401,E501
from jnpr.healthbot.swagger.models.rule_schema_nativegpb import RuleSchemaNativegpb  # noqa: F401,E501
from jnpr.healthbot.swagger.models.rule_schema_openconfig import RuleSchemaOpenconfig  # noqa: F401,E501
from jnpr.healthbot.swagger.models.rule_schema_snmp import RuleSchemaSnmp  # noqa: F401,E501
from jnpr.healthbot.swagger.models.rule_schema_syslog import RuleSchemaSyslog  # noqa: F401,E501


class RuleSchemaSensor1(object):
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
        'description': 'str',
        'flow': 'RuleSchemaFlow',
        'i_agent': 'RuleSchemaIAgent',
        'native_gpb': 'RuleSchemaNativegpb',
        'open_config': 'RuleSchemaOpenconfig',
        'sensor_name': 'str',
        'snmp': 'RuleSchemaSnmp',
        'syslog': 'RuleSchemaSyslog',
        'synopsis': 'str',
        'byoi': 'RuleSchemaByoi'
    }

    attribute_map = {
        'description': 'description',
        'flow': 'flow',
        'i_agent': 'iAgent',
        'native_gpb': 'native-gpb',
        'open_config': 'open-config',
        'sensor_name': 'sensor-name',
        'snmp': 'snmp',
        'syslog': 'syslog',
        'synopsis': 'synopsis',
        'byoi': 'byoi'
    }

    def __init__(self, description=None, flow=None, i_agent=None, native_gpb=None, open_config=None, sensor_name=None, snmp=None, syslog=None, synopsis=None, byoi=None):  # noqa: E501
        """RuleSchemaSensor1 - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._flow = None
        self._i_agent = None
        self._native_gpb = None
        self._open_config = None
        self._sensor_name = None
        self._snmp = None
        self._syslog = None
        self._synopsis = None
        self._byoi = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if flow is not None:
            self.flow = flow
        if i_agent is not None:
            self.i_agent = i_agent
        if native_gpb is not None:
            self.native_gpb = native_gpb
        if open_config is not None:
            self.open_config = open_config
        self.sensor_name = sensor_name
        if snmp is not None:
            self.snmp = snmp
        if syslog is not None:
            self.syslog = syslog
        if synopsis is not None:
            self.synopsis = synopsis
        if byoi is not None:
            self.byoi = byoi

    @property
    def description(self):
        """Gets the description of this RuleSchemaSensor1.  # noqa: E501

        Description about the sensor  # noqa: E501

        :return: The description of this RuleSchemaSensor1.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RuleSchemaSensor1.

        Description about the sensor  # noqa: E501

        :param description: The description of this RuleSchemaSensor1.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def flow(self):
        """Gets the flow of this RuleSchemaSensor1.  # noqa: E501


        :return: The flow of this RuleSchemaSensor1.  # noqa: E501
        :rtype: RuleSchemaFlow
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        """Sets the flow of this RuleSchemaSensor1.


        :param flow: The flow of this RuleSchemaSensor1.  # noqa: E501
        :type: RuleSchemaFlow
        """

        self._flow = flow

    @property
    def i_agent(self):
        """Gets the i_agent of this RuleSchemaSensor1.  # noqa: E501


        :return: The i_agent of this RuleSchemaSensor1.  # noqa: E501
        :rtype: RuleSchemaIAgent
        """
        return self._i_agent

    @i_agent.setter
    def i_agent(self, i_agent):
        """Sets the i_agent of this RuleSchemaSensor1.


        :param i_agent: The i_agent of this RuleSchemaSensor1.  # noqa: E501
        :type: RuleSchemaIAgent
        """

        self._i_agent = i_agent

    @property
    def native_gpb(self):
        """Gets the native_gpb of this RuleSchemaSensor1.  # noqa: E501


        :return: The native_gpb of this RuleSchemaSensor1.  # noqa: E501
        :rtype: RuleSchemaNativegpb
        """
        return self._native_gpb

    @native_gpb.setter
    def native_gpb(self, native_gpb):
        """Sets the native_gpb of this RuleSchemaSensor1.


        :param native_gpb: The native_gpb of this RuleSchemaSensor1.  # noqa: E501
        :type: RuleSchemaNativegpb
        """

        self._native_gpb = native_gpb

    @property
    def open_config(self):
        """Gets the open_config of this RuleSchemaSensor1.  # noqa: E501


        :return: The open_config of this RuleSchemaSensor1.  # noqa: E501
        :rtype: RuleSchemaOpenconfig
        """
        return self._open_config

    @open_config.setter
    def open_config(self, open_config):
        """Sets the open_config of this RuleSchemaSensor1.


        :param open_config: The open_config of this RuleSchemaSensor1.  # noqa: E501
        :type: RuleSchemaOpenconfig
        """

        self._open_config = open_config

    @property
    def sensor_name(self):
        """Gets the sensor_name of this RuleSchemaSensor1.  # noqa: E501

        Name of sensor. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :return: The sensor_name of this RuleSchemaSensor1.  # noqa: E501
        :rtype: str
        """
        return self._sensor_name

    @sensor_name.setter
    def sensor_name(self, sensor_name):
        """Sets the sensor_name of this RuleSchemaSensor1.

        Name of sensor. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :param sensor_name: The sensor_name of this RuleSchemaSensor1.  # noqa: E501
        :type: str
        """
        if sensor_name is None:
            raise ValueError("Invalid value for `sensor_name`, must not be `None`")  # noqa: E501
        if sensor_name is not None and len(sensor_name) > 64:
            raise ValueError("Invalid value for `sensor_name`, length must be less than or equal to `64`")  # noqa: E501
        if sensor_name is not None and not re.search('^[a-zA-Z][a-zA-Z0-9_-]*$', sensor_name):  # noqa: E501
            raise ValueError("Invalid value for `sensor_name`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._sensor_name = sensor_name

    @property
    def snmp(self):
        """Gets the snmp of this RuleSchemaSensor1.  # noqa: E501


        :return: The snmp of this RuleSchemaSensor1.  # noqa: E501
        :rtype: RuleSchemaSnmp
        """
        return self._snmp

    @snmp.setter
    def snmp(self, snmp):
        """Sets the snmp of this RuleSchemaSensor1.


        :param snmp: The snmp of this RuleSchemaSensor1.  # noqa: E501
        :type: RuleSchemaSnmp
        """

        self._snmp = snmp

    @property
    def syslog(self):
        """Gets the syslog of this RuleSchemaSensor1.  # noqa: E501


        :return: The syslog of this RuleSchemaSensor1.  # noqa: E501
        :rtype: RuleSchemaSyslog
        """
        return self._syslog

    @syslog.setter
    def syslog(self, syslog):
        """Sets the syslog of this RuleSchemaSensor1.


        :param syslog: The syslog of this RuleSchemaSensor1.  # noqa: E501
        :type: RuleSchemaSyslog
        """

        self._syslog = syslog

    @property
    def synopsis(self):
        """Gets the synopsis of this RuleSchemaSensor1.  # noqa: E501

        Synopsis about the sensor  # noqa: E501

        :return: The synopsis of this RuleSchemaSensor1.  # noqa: E501
        :rtype: str
        """
        return self._synopsis

    @synopsis.setter
    def synopsis(self, synopsis):
        """Sets the synopsis of this RuleSchemaSensor1.

        Synopsis about the sensor  # noqa: E501

        :param synopsis: The synopsis of this RuleSchemaSensor1.  # noqa: E501
        :type: str
        """

        self._synopsis = synopsis

    @property
    def byoi(self):
        """Gets the byoi of this RuleSchemaSensor1.  # noqa: E501


        :return: The byoi of this RuleSchemaSensor1.  # noqa: E501
        :rtype: RuleSchemaByoi
        """
        return self._byoi

    @byoi.setter
    def byoi(self, byoi):
        """Sets the byoi of this RuleSchemaSensor1.


        :param byoi: The byoi of this RuleSchemaSensor1.  # noqa: E501
        :type: RuleSchemaByoi
        """

        self._byoi = byoi

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
        if not isinstance(other, RuleSchemaSensor1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
