# coding: utf-8

"""
    Healthbot APIs

    API interface for Healthbot application  # noqa: E501

    OpenAPI spec version: 3.1.0
    Contact: healthbot-feedback@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class FactsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def retrieve_iceberg_device_device_facts_by_id(self, device_id, **kwargs):  # noqa: E501
        """Get a device's facts.  # noqa: E501

        Get the fact details of a device by its `device-id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_iceberg_device_device_facts_by_id(device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_id: ID of device-id (required)
        :param str authorization: authentication header object
        :param bool working: true queries un-committed configuration
        :param bool update: true will first update facts from device and then return facts
        :param int timeout: timeout in seconds to wait for facts from given device id
        :return: DeviceSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_iceberg_device_device_facts_by_id_with_http_info(device_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_iceberg_device_device_facts_by_id_with_http_info(device_id, **kwargs)  # noqa: E501
            return data

    def retrieve_iceberg_device_device_facts_by_id_with_http_info(self, device_id, **kwargs):  # noqa: E501
        """Get a device's facts.  # noqa: E501

        Get the fact details of a device by its `device-id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_iceberg_device_device_facts_by_id_with_http_info(device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_id: ID of device-id (required)
        :param str authorization: authentication header object
        :param bool working: true queries un-committed configuration
        :param bool update: true will first update facts from device and then return facts
        :param int timeout: timeout in seconds to wait for facts from given device id
        :return: DeviceSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id', 'authorization', 'working', 'update', 'timeout']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_iceberg_device_device_facts_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `retrieve_iceberg_device_device_facts_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['device_id'] = params['device_id']  # noqa: E501

        query_params = []
        if 'working' in params:
            query_params.append(('working', params['working']))  # noqa: E501
        if 'update' in params:
            query_params.append(('update', params['update']))  # noqa: E501
        if 'timeout' in params:
            query_params.append(('timeout', params['timeout']))  # noqa: E501

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/config/device/{device_id}/facts/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceSchema',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_iceberg_devices_devices_facts(self, **kwargs):  # noqa: E501
        """Get devices facts.  # noqa: E501

        Get the fact details of every device  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_iceberg_devices_devices_facts(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: authentication header object
        :param bool working: true queries un-committed configuration
        :param bool update: true will first update facts from device and then return facts
        :param int timeout: timeout in seconds to wait for facts from every device
        :return: DeviceSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_iceberg_devices_devices_facts_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_iceberg_devices_devices_facts_with_http_info(**kwargs)  # noqa: E501
            return data

    def retrieve_iceberg_devices_devices_facts_with_http_info(self, **kwargs):  # noqa: E501
        """Get devices facts.  # noqa: E501

        Get the fact details of every device  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_iceberg_devices_devices_facts_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: authentication header object
        :param bool working: true queries un-committed configuration
        :param bool update: true will first update facts from device and then return facts
        :param int timeout: timeout in seconds to wait for facts from every device
        :return: DeviceSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'working', 'update', 'timeout']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_iceberg_devices_devices_facts" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'working' in params:
            query_params.append(('working', params['working']))  # noqa: E501
        if 'update' in params:
            query_params.append(('update', params['update']))  # noqa: E501
        if 'timeout' in params:
            query_params.append(('timeout', params['timeout']))  # noqa: E501

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/config/devices/facts/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceSchema',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_iceberg_devices_facts_by_group(self, device_group_name, **kwargs):  # noqa: E501
        """Get a devices facts for given group.  # noqa: E501

        Get the fact details of every device under given group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_iceberg_devices_facts_by_group(device_group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_group_name: ID of group (required)
        :param str authorization: authentication header object
        :param bool working: true queries un-committed configuration
        :param bool update: true will first update facts from device and then return facts
        :param int timeout: timeout in seconds to wait for facts from every device
        :return: DeviceSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_iceberg_devices_facts_by_group_with_http_info(device_group_name, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_iceberg_devices_facts_by_group_with_http_info(device_group_name, **kwargs)  # noqa: E501
            return data

    def retrieve_iceberg_devices_facts_by_group_with_http_info(self, device_group_name, **kwargs):  # noqa: E501
        """Get a devices facts for given group.  # noqa: E501

        Get the fact details of every device under given group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_iceberg_devices_facts_by_group_with_http_info(device_group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_group_name: ID of group (required)
        :param str authorization: authentication header object
        :param bool working: true queries un-committed configuration
        :param bool update: true will first update facts from device and then return facts
        :param int timeout: timeout in seconds to wait for facts from every device
        :return: DeviceSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_group_name', 'authorization', 'working', 'update', 'timeout']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_iceberg_devices_facts_by_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_group_name' is set
        if ('device_group_name' not in params or
                params['device_group_name'] is None):
            raise ValueError("Missing the required parameter `device_group_name` when calling `retrieve_iceberg_devices_facts_by_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_group_name' in params:
            path_params['device_group_name'] = params['device_group_name']  # noqa: E501

        query_params = []
        if 'working' in params:
            query_params.append(('working', params['working']))  # noqa: E501
        if 'update' in params:
            query_params.append(('update', params['update']))  # noqa: E501
        if 'timeout' in params:
            query_params.append(('timeout', params['timeout']))  # noqa: E501

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/config/device-group/{device_group_name}/facts/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceSchema',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
