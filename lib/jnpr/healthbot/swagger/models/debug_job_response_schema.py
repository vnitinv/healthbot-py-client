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


class DebugJobResponseSchema(object):
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
        'job_id': 'str',
        'job_status': 'str',
        'job_details': 'str',
        'debug_data': 'str',
        'debug_type': 'str',
        'debug_name': 'str'
    }

    attribute_map = {
        'job_id': 'job-id',
        'job_status': 'job-status',
        'job_details': 'job-details',
        'debug_data': 'debug-data',
        'debug_type': 'debug-type',
        'debug_name': 'debug-name'
    }

    def __init__(self, job_id=None, job_status=None, job_details=None, debug_data=None, debug_type=None, debug_name=None):  # noqa: E501
        """DebugJobResponseSchema - a model defined in Swagger"""  # noqa: E501

        self._job_id = None
        self._job_status = None
        self._job_details = None
        self._debug_data = None
        self._debug_type = None
        self._debug_name = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if job_status is not None:
            self.job_status = job_status
        if job_details is not None:
            self.job_details = job_details
        if debug_data is not None:
            self.debug_data = debug_data
        if debug_type is not None:
            self.debug_type = debug_type
        if debug_name is not None:
            self.debug_name = debug_name

    @property
    def job_id(self):
        """Gets the job_id of this DebugJobResponseSchema.  # noqa: E501


        :return: The job_id of this DebugJobResponseSchema.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this DebugJobResponseSchema.


        :param job_id: The job_id of this DebugJobResponseSchema.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def job_status(self):
        """Gets the job_status of this DebugJobResponseSchema.  # noqa: E501


        :return: The job_status of this DebugJobResponseSchema.  # noqa: E501
        :rtype: str
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        """Sets the job_status of this DebugJobResponseSchema.


        :param job_status: The job_status of this DebugJobResponseSchema.  # noqa: E501
        :type: str
        """
        allowed_values = ["finished", "started", "error", "pending"]  # noqa: E501
        if job_status not in allowed_values:
            raise ValueError(
                "Invalid value for `job_status` ({0}), must be one of {1}"  # noqa: E501
                .format(job_status, allowed_values)
            )

        self._job_status = job_status

    @property
    def job_details(self):
        """Gets the job_details of this DebugJobResponseSchema.  # noqa: E501


        :return: The job_details of this DebugJobResponseSchema.  # noqa: E501
        :rtype: str
        """
        return self._job_details

    @job_details.setter
    def job_details(self, job_details):
        """Sets the job_details of this DebugJobResponseSchema.


        :param job_details: The job_details of this DebugJobResponseSchema.  # noqa: E501
        :type: str
        """

        self._job_details = job_details

    @property
    def debug_data(self):
        """Gets the debug_data of this DebugJobResponseSchema.  # noqa: E501


        :return: The debug_data of this DebugJobResponseSchema.  # noqa: E501
        :rtype: str
        """
        return self._debug_data

    @debug_data.setter
    def debug_data(self, debug_data):
        """Sets the debug_data of this DebugJobResponseSchema.


        :param debug_data: The debug_data of this DebugJobResponseSchema.  # noqa: E501
        :type: str
        """

        self._debug_data = debug_data

    @property
    def debug_type(self):
        """Gets the debug_type of this DebugJobResponseSchema.  # noqa: E501


        :return: The debug_type of this DebugJobResponseSchema.  # noqa: E501
        :rtype: str
        """
        return self._debug_type

    @debug_type.setter
    def debug_type(self, debug_type):
        """Sets the debug_type of this DebugJobResponseSchema.


        :param debug_type: The debug_type of this DebugJobResponseSchema.  # noqa: E501
        :type: str
        """
        allowed_values = ["scenario", "service"]  # noqa: E501
        if debug_type not in allowed_values:
            raise ValueError(
                "Invalid value for `debug_type` ({0}), must be one of {1}"  # noqa: E501
                .format(debug_type, allowed_values)
            )

        self._debug_type = debug_type

    @property
    def debug_name(self):
        """Gets the debug_name of this DebugJobResponseSchema.  # noqa: E501


        :return: The debug_name of this DebugJobResponseSchema.  # noqa: E501
        :rtype: str
        """
        return self._debug_name

    @debug_name.setter
    def debug_name(self, debug_name):
        """Sets the debug_name of this DebugJobResponseSchema.


        :param debug_name: The debug_name of this DebugJobResponseSchema.  # noqa: E501
        :type: str
        """

        self._debug_name = debug_name

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
        if not isinstance(other, DebugJobResponseSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
