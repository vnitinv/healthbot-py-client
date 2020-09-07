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


class SchedulerSchemaRunfor(object):
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
        'days': 'int',
        'hours': 'int',
        'minutes': 'int'
    }

    attribute_map = {
        'days': 'days',
        'hours': 'hours',
        'minutes': 'minutes'
    }

    def __init__(self, days=None, hours=None, minutes=None):  # noqa: E501
        """SchedulerSchemaRunfor - a model defined in Swagger"""  # noqa: E501

        self._days = None
        self._hours = None
        self._minutes = None
        self.discriminator = None

        if days is not None:
            self.days = days
        if hours is not None:
            self.hours = hours
        if minutes is not None:
            self.minutes = minutes

    @property
    def days(self):
        """Gets the days of this SchedulerSchemaRunfor.  # noqa: E501

        Duration of time in days  # noqa: E501

        :return: The days of this SchedulerSchemaRunfor.  # noqa: E501
        :rtype: int
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this SchedulerSchemaRunfor.

        Duration of time in days  # noqa: E501

        :param days: The days of this SchedulerSchemaRunfor.  # noqa: E501
        :type: int
        """
        if days is not None and days > 65535:  # noqa: E501
            raise ValueError("Invalid value for `days`, must be a value less than or equal to `65535`")  # noqa: E501
        if days is not None and days < 1:  # noqa: E501
            raise ValueError("Invalid value for `days`, must be a value greater than or equal to `1`")  # noqa: E501

        self._days = days

    @property
    def hours(self):
        """Gets the hours of this SchedulerSchemaRunfor.  # noqa: E501

        Duration of time in hours  # noqa: E501

        :return: The hours of this SchedulerSchemaRunfor.  # noqa: E501
        :rtype: int
        """
        return self._hours

    @hours.setter
    def hours(self, hours):
        """Sets the hours of this SchedulerSchemaRunfor.

        Duration of time in hours  # noqa: E501

        :param hours: The hours of this SchedulerSchemaRunfor.  # noqa: E501
        :type: int
        """
        if hours is not None and hours > 65535:  # noqa: E501
            raise ValueError("Invalid value for `hours`, must be a value less than or equal to `65535`")  # noqa: E501
        if hours is not None and hours < 1:  # noqa: E501
            raise ValueError("Invalid value for `hours`, must be a value greater than or equal to `1`")  # noqa: E501

        self._hours = hours

    @property
    def minutes(self):
        """Gets the minutes of this SchedulerSchemaRunfor.  # noqa: E501

        Duration of time in minutes  # noqa: E501

        :return: The minutes of this SchedulerSchemaRunfor.  # noqa: E501
        :rtype: int
        """
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        """Sets the minutes of this SchedulerSchemaRunfor.

        Duration of time in minutes  # noqa: E501

        :param minutes: The minutes of this SchedulerSchemaRunfor.  # noqa: E501
        :type: int
        """
        if minutes is not None and minutes > 65535:  # noqa: E501
            raise ValueError("Invalid value for `minutes`, must be a value less than or equal to `65535`")  # noqa: E501
        if minutes is not None and minutes < 1:  # noqa: E501
            raise ValueError("Invalid value for `minutes`, must be a value greater than or equal to `1`")  # noqa: E501

        self._minutes = minutes

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
        if issubclass(SchedulerSchemaRunfor, dict):
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
        if not isinstance(other, SchedulerSchemaRunfor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
