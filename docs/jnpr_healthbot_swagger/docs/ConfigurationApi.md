# swagger_client.ConfigurationApi

All URIs are relative to *http://api-server/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_device_group_unsaved_configuration**](ConfigurationApi.md#check_device_group_unsaved_configuration) | **POST** /configuration/check/device-group/{device_group_name}/ | Check if the un-committed configuration of the given device group is correct
[**check_network_group_unsaved_configuration**](ConfigurationApi.md#check_network_group_unsaved_configuration) | **POST** /configuration/check/network-group/{network_group_name}/ | Check if the unsaved configuration of the given network group is correct.
[**commit_unsaved_configuration**](ConfigurationApi.md#commit_unsaved_configuration) | **POST** /configuration/ | Commit unsaved configuration.
[**create_iceberg_device_device_by_id**](ConfigurationApi.md#create_iceberg_device_device_by_id) | **POST** /device/{device_id}/ | Update or create a device.
[**create_iceberg_device_group_device_group_by_id**](ConfigurationApi.md#create_iceberg_device_group_device_group_by_id) | **POST** /device-group/{device_group_name}/ | Update or create a device-group.
[**create_iceberg_device_groups_device_groups_by_id**](ConfigurationApi.md#create_iceberg_device_groups_device_groups_by_id) | **POST** /device-groups/ | Update or create multiple device-groups.
[**create_iceberg_devices_devices_by_id**](ConfigurationApi.md#create_iceberg_devices_devices_by_id) | **POST** /devices/ | Update or create multiple devices.
[**create_iceberg_network_group_network_group_by_id**](ConfigurationApi.md#create_iceberg_network_group_network_group_by_id) | **POST** /network-group/{network_group_name}/ | Update or create a network-group.
[**create_iceberg_network_groups_network_groups_by_id**](ConfigurationApi.md#create_iceberg_network_groups_network_groups_by_id) | **POST** /network-groups/ | Update or create multiple network-groups.
[**create_iceberg_notification_notification_by_id**](ConfigurationApi.md#create_iceberg_notification_notification_by_id) | **POST** /notification/{notification_name}/ | Update or create a notification
[**create_iceberg_notifications_notifications_by_id**](ConfigurationApi.md#create_iceberg_notifications_notifications_by_id) | **POST** /notifications/ | Update or create multiple notifications.
[**create_iceberg_playbook_playbook_by_id**](ConfigurationApi.md#create_iceberg_playbook_playbook_by_id) | **POST** /playbook/{playbook_name}/ | Update or create a playbook.
[**create_iceberg_playbooks_playbooks_by_id**](ConfigurationApi.md#create_iceberg_playbooks_playbooks_by_id) | **POST** /playbooks/ | Update or create multiple playbooks.
[**create_iceberg_retention_policies_retention_policies_by_id**](ConfigurationApi.md#create_iceberg_retention_policies_retention_policies_by_id) | **POST** /retention-policies/ | Update or create multiple retention-policies.
[**create_iceberg_retention_policy_retention_policy_by_id**](ConfigurationApi.md#create_iceberg_retention_policy_retention_policy_by_id) | **POST** /retention-policy/{retention_policy_name}/ | Update or create a retention-policy.
[**create_iceberg_system_settings_destination_by_id**](ConfigurationApi.md#create_iceberg_system_settings_destination_by_id) | **POST** /system-settings/report-generation/destination/{name}/ | Create destination by name
[**create_iceberg_system_settings_destinations**](ConfigurationApi.md#create_iceberg_system_settings_destinations) | **POST** /system-settings/report-generation/destinations/ | Create destinations by name
[**create_iceberg_system_settings_report_by_id**](ConfigurationApi.md#create_iceberg_system_settings_report_by_id) | **POST** /system-settings/report-generation/report/{name}/ | Create report by name
[**create_iceberg_system_settings_reports**](ConfigurationApi.md#create_iceberg_system_settings_reports) | **POST** /system-settings/report-generation/reports/ | Create reports by name
[**create_iceberg_system_settings_scheduler_by_id**](ConfigurationApi.md#create_iceberg_system_settings_scheduler_by_id) | **POST** /system-settings/scheduler/{name}/ | Create scheduler by name
[**create_iceberg_system_settings_schedulers**](ConfigurationApi.md#create_iceberg_system_settings_schedulers) | **POST** /system-settings/schedulers/ | Create schedulers by name
[**create_iceberg_system_settings_system_settings_by_id**](ConfigurationApi.md#create_iceberg_system_settings_system_settings_by_id) | **POST** /system-settings/ | Create system-settings
[**create_iceberg_topic_rule_rule_by_id**](ConfigurationApi.md#create_iceberg_topic_rule_rule_by_id) | **POST** /topic/{topic_name}/rule/{rule_name}/ | Update or create a rule.
[**create_iceberg_topic_topic_by_id**](ConfigurationApi.md#create_iceberg_topic_topic_by_id) | **POST** /topic/{topic_name}/ | Update or create a topic.
[**create_iceberg_topics_topics_by_id**](ConfigurationApi.md#create_iceberg_topics_topics_by_id) | **POST** /topics/ | Update or create multiple topics.
[**delete_iceberg_device_device_by_id**](ConfigurationApi.md#delete_iceberg_device_device_by_id) | **DELETE** /device/{device_id}/ | Delete device.
[**delete_iceberg_device_group_device_group_by_id**](ConfigurationApi.md#delete_iceberg_device_group_device_group_by_id) | **DELETE** /device-group/{device_group_name}/ | Delete device-group.
[**delete_iceberg_device_groups_device_groups_by_id**](ConfigurationApi.md#delete_iceberg_device_groups_device_groups_by_id) | **DELETE** /device-groups/ | Delete all device-groups.
[**delete_iceberg_devices_devices_by_id**](ConfigurationApi.md#delete_iceberg_devices_devices_by_id) | **DELETE** /devices/ | Delete all devices.
[**delete_iceberg_network_group_network_group_by_id**](ConfigurationApi.md#delete_iceberg_network_group_network_group_by_id) | **DELETE** /network-group/{network_group_name}/ | Delete network-group.
[**delete_iceberg_network_groups_network_groups_by_id**](ConfigurationApi.md#delete_iceberg_network_groups_network_groups_by_id) | **DELETE** /network-groups/ | Delete all network-groups.
[**delete_iceberg_notification_notification_by_id**](ConfigurationApi.md#delete_iceberg_notification_notification_by_id) | **DELETE** /notification/{notification_name}/ | Delete a notification.
[**delete_iceberg_notifications_notifications_by_id**](ConfigurationApi.md#delete_iceberg_notifications_notifications_by_id) | **DELETE** /notifications/ | Delete all notifications.
[**delete_iceberg_playbook_playbook_by_id**](ConfigurationApi.md#delete_iceberg_playbook_playbook_by_id) | **DELETE** /playbook/{playbook_name}/ | Delete a playbook.
[**delete_iceberg_playbooks_playbooks_by_id**](ConfigurationApi.md#delete_iceberg_playbooks_playbooks_by_id) | **DELETE** /playbooks/ | Delete all playbooks.
[**delete_iceberg_retention_policies_retention_policies_by_id**](ConfigurationApi.md#delete_iceberg_retention_policies_retention_policies_by_id) | **DELETE** /retention-policies/ | Delete all retention-policies.
[**delete_iceberg_retention_policy_retention_policy_by_id**](ConfigurationApi.md#delete_iceberg_retention_policy_retention_policy_by_id) | **DELETE** /retention-policy/{retention_policy_name}/ | Delete a retention-policy.
[**delete_iceberg_system_settings_destination_by_id**](ConfigurationApi.md#delete_iceberg_system_settings_destination_by_id) | **DELETE** /system-settings/report-generation/destination/{name}/ | Delete destination by name
[**delete_iceberg_system_settings_destinations**](ConfigurationApi.md#delete_iceberg_system_settings_destinations) | **DELETE** /system-settings/report-generation/destinations/ | Delete destinations by name
[**delete_iceberg_system_settings_report_by_id**](ConfigurationApi.md#delete_iceberg_system_settings_report_by_id) | **DELETE** /system-settings/report-generation/report/{name}/ | Delete report by name
[**delete_iceberg_system_settings_reports**](ConfigurationApi.md#delete_iceberg_system_settings_reports) | **DELETE** /system-settings/report-generation/reports/ | Delete reports by name
[**delete_iceberg_system_settings_scheduler_by_id**](ConfigurationApi.md#delete_iceberg_system_settings_scheduler_by_id) | **DELETE** /system-settings/scheduler/{name}/ | Delete scheduler by name
[**delete_iceberg_system_settings_schedulers**](ConfigurationApi.md#delete_iceberg_system_settings_schedulers) | **DELETE** /system-settings/schedulers/ | Delete schedulers by name
[**delete_iceberg_system_settings_system_settings_by_id**](ConfigurationApi.md#delete_iceberg_system_settings_system_settings_by_id) | **DELETE** /system-settings/ | Delete system-settings
[**delete_iceberg_topic_rule_rule_by_id**](ConfigurationApi.md#delete_iceberg_topic_rule_rule_by_id) | **DELETE** /topic/{topic_name}/rule/{rule_name}/ | Delete a rule.
[**delete_iceberg_topic_topic_by_id**](ConfigurationApi.md#delete_iceberg_topic_topic_by_id) | **DELETE** /topic/{topic_name}/ | Delete a topic.
[**delete_iceberg_topics_topics_by_id**](ConfigurationApi.md#delete_iceberg_topics_topics_by_id) | **DELETE** /topics/ | Delete all topics.
[**retrieve_affected_groups**](ConfigurationApi.md#retrieve_affected_groups) | **GET** /configuration/ | Get all groups affected by un-committed configuration changes.
[**retrieve_device_group_status**](ConfigurationApi.md#retrieve_device_group_status) | **GET** /device-group/{device_group_name}/status/ | Get device-group&#39;s status.
[**retrieve_iceberg_device_device**](ConfigurationApi.md#retrieve_iceberg_device_device) | **GET** /device/ | List all device-ids.
[**retrieve_iceberg_device_device_by_id**](ConfigurationApi.md#retrieve_iceberg_device_device_by_id) | **GET** /device/{device_id}/ | Get a device&#39;s configuration.
[**retrieve_iceberg_device_group_device_group**](ConfigurationApi.md#retrieve_iceberg_device_group_device_group) | **GET** /device-group/ | List all device-group names.
[**retrieve_iceberg_device_group_device_group_by_id**](ConfigurationApi.md#retrieve_iceberg_device_group_device_group_by_id) | **GET** /device-group/{device_group_name}/ | Get device-group&#39;s configuration.
[**retrieve_iceberg_device_groups_device_groups**](ConfigurationApi.md#retrieve_iceberg_device_groups_device_groups) | **GET** /device-groups/ | Get all device-groups&#39; configuration.
[**retrieve_iceberg_devices_devices**](ConfigurationApi.md#retrieve_iceberg_devices_devices) | **GET** /devices/ | Get all devices&#39; configuration.
[**retrieve_iceberg_network_group_network_group**](ConfigurationApi.md#retrieve_iceberg_network_group_network_group) | **GET** /network-group/ | List all network-group names.
[**retrieve_iceberg_network_group_network_group_by_id**](ConfigurationApi.md#retrieve_iceberg_network_group_network_group_by_id) | **GET** /network-group/{network_group_name}/ | Get network-group&#39;s configuration.
[**retrieve_iceberg_network_groups_network_groups**](ConfigurationApi.md#retrieve_iceberg_network_groups_network_groups) | **GET** /network-groups/ | Get all network-groups&#39; configuration.
[**retrieve_iceberg_notification_notification**](ConfigurationApi.md#retrieve_iceberg_notification_notification) | **GET** /notification/ | List all notification-names.
[**retrieve_iceberg_notification_notification_by_id**](ConfigurationApi.md#retrieve_iceberg_notification_notification_by_id) | **GET** /notification/{notification_name}/ | Get a notification&#39;s configuration.
[**retrieve_iceberg_notifications_notifications_by_id**](ConfigurationApi.md#retrieve_iceberg_notifications_notifications_by_id) | **GET** /notifications/ | Get all notifications&#39; configuration.
[**retrieve_iceberg_playbook_playbook**](ConfigurationApi.md#retrieve_iceberg_playbook_playbook) | **GET** /playbook/ | List all playbook-names.
[**retrieve_iceberg_playbook_playbook_by_id**](ConfigurationApi.md#retrieve_iceberg_playbook_playbook_by_id) | **GET** /playbook/{playbook_name}/ | Get a playbook&#39;s configuration.
[**retrieve_iceberg_playbooks_playbooks_by_id**](ConfigurationApi.md#retrieve_iceberg_playbooks_playbooks_by_id) | **GET** /playbooks/ | Get all playbooks&#39; configuration.
[**retrieve_iceberg_retention_policies_retention_policies_by_id**](ConfigurationApi.md#retrieve_iceberg_retention_policies_retention_policies_by_id) | **GET** /retention-policies/ | Get all retention-policies&#39; configuration.
[**retrieve_iceberg_retention_policy_retention_policy**](ConfigurationApi.md#retrieve_iceberg_retention_policy_retention_policy) | **GET** /retention-policy/ | List all retention-policy-names.
[**retrieve_iceberg_retention_policy_retention_policy_by_id**](ConfigurationApi.md#retrieve_iceberg_retention_policy_retention_policy_by_id) | **GET** /retention-policy/{retention_policy_name}/ | Get a retention-policy&#39;s configuration.
[**retrieve_iceberg_system_settings_destination_by_id**](ConfigurationApi.md#retrieve_iceberg_system_settings_destination_by_id) | **GET** /system-settings/report-generation/destination/{name}/ | Retrieve destination by name
[**retrieve_iceberg_system_settings_destinations**](ConfigurationApi.md#retrieve_iceberg_system_settings_destinations) | **GET** /system-settings/report-generation/destinations/ | Retrieve destinations by name
[**retrieve_iceberg_system_settings_report_by_id**](ConfigurationApi.md#retrieve_iceberg_system_settings_report_by_id) | **GET** /system-settings/report-generation/report/{name}/ | Retrieve report by name
[**retrieve_iceberg_system_settings_reports**](ConfigurationApi.md#retrieve_iceberg_system_settings_reports) | **GET** /system-settings/report-generation/reports/ | Retrieve reports by name
[**retrieve_iceberg_system_settings_scheduler_by_id**](ConfigurationApi.md#retrieve_iceberg_system_settings_scheduler_by_id) | **GET** /system-settings/scheduler/{name}/ | Retrieve scheduler by name
[**retrieve_iceberg_system_settings_schedulers**](ConfigurationApi.md#retrieve_iceberg_system_settings_schedulers) | **GET** /system-settings/schedulers/ | Retrieve schedulers by name
[**retrieve_iceberg_system_settings_system_settings**](ConfigurationApi.md#retrieve_iceberg_system_settings_system_settings) | **GET** /system-settings/ | Retrieve system-settings
[**retrieve_iceberg_topic_rule_rule**](ConfigurationApi.md#retrieve_iceberg_topic_rule_rule) | **GET** /topic/{topic_name}/rule/ | List all rule-names in a topic.
[**retrieve_iceberg_topic_rule_rule_by_id**](ConfigurationApi.md#retrieve_iceberg_topic_rule_rule_by_id) | **GET** /topic/{topic_name}/rule/{rule_name}/ | Get a rule&#39;s configuration.
[**retrieve_iceberg_topic_topic**](ConfigurationApi.md#retrieve_iceberg_topic_topic) | **GET** /topic/ | List all topic-names.
[**retrieve_iceberg_topic_topic_by_id**](ConfigurationApi.md#retrieve_iceberg_topic_topic_by_id) | **GET** /topic/{topic_name}/ | Get a topic&#39;s configuration.
[**retrieve_iceberg_topics_topics**](ConfigurationApi.md#retrieve_iceberg_topics_topics) | **GET** /topics/ | Get all topics&#39; configuration.
[**retrieve_network_group_status**](ConfigurationApi.md#retrieve_network_group_status) | **GET** /network-group/{network_group_name}/status/ | Get network-group&#39;s status.
[**rollback_unsaved_configuration**](ConfigurationApi.md#rollback_unsaved_configuration) | **DELETE** /configuration/ | Delete the un-committed configuration.
[**update_iceberg_device_device_by_id**](ConfigurationApi.md#update_iceberg_device_device_by_id) | **PUT** /device/{device_id}/ | Overwrite a device.
[**update_iceberg_device_group_device_group_by_id**](ConfigurationApi.md#update_iceberg_device_group_device_group_by_id) | **PUT** /device-group/{device_group_name}/ | Overwrite a device-group.
[**update_iceberg_device_groups_device_groups_by_id**](ConfigurationApi.md#update_iceberg_device_groups_device_groups_by_id) | **PUT** /device-groups/ | Overwrite device-groups.
[**update_iceberg_devices_devices_by_id**](ConfigurationApi.md#update_iceberg_devices_devices_by_id) | **PUT** /devices/ | Overwrite devices.
[**update_iceberg_network_group_network_group_by_id**](ConfigurationApi.md#update_iceberg_network_group_network_group_by_id) | **PUT** /network-group/{network_group_name}/ | Overwrite a network-group.
[**update_iceberg_network_groups_network_groups_by_id**](ConfigurationApi.md#update_iceberg_network_groups_network_groups_by_id) | **PUT** /network-groups/ | Overwrite network-groups.
[**update_iceberg_notification_notification_by_id**](ConfigurationApi.md#update_iceberg_notification_notification_by_id) | **PUT** /notification/{notification_name}/ | Overwrite a notification.
[**update_iceberg_notifications_notifications_by_id**](ConfigurationApi.md#update_iceberg_notifications_notifications_by_id) | **PUT** /notifications/ | Overwrite notifications.
[**update_iceberg_playbook_playbook_by_id**](ConfigurationApi.md#update_iceberg_playbook_playbook_by_id) | **PUT** /playbook/{playbook_name}/ | Overwrite a playbook.
[**update_iceberg_playbooks_playbooks_by_id**](ConfigurationApi.md#update_iceberg_playbooks_playbooks_by_id) | **PUT** /playbooks/ | Overwrite all playbooks.
[**update_iceberg_retention_policies_retention_policies_id**](ConfigurationApi.md#update_iceberg_retention_policies_retention_policies_id) | **PUT** /retention-policies/ | Overwrite all retention-policies.
[**update_iceberg_retention_policy_retention_policy_by_id**](ConfigurationApi.md#update_iceberg_retention_policy_retention_policy_by_id) | **PUT** /retention-policy/{retention_policy_name}/ | Overwrite a retention-policy.
[**update_iceberg_system_settings_destination_by_id**](ConfigurationApi.md#update_iceberg_system_settings_destination_by_id) | **PUT** /system-settings/report-generation/destination/{name}/ | Update destination by name
[**update_iceberg_system_settings_destinations**](ConfigurationApi.md#update_iceberg_system_settings_destinations) | **PUT** /system-settings/report-generation/destinations/ | Update destinations by name
[**update_iceberg_system_settings_report_by_id**](ConfigurationApi.md#update_iceberg_system_settings_report_by_id) | **PUT** /system-settings/report-generation/report/{name}/ | Update report by name
[**update_iceberg_system_settings_reports**](ConfigurationApi.md#update_iceberg_system_settings_reports) | **PUT** /system-settings/report-generation/reports/ | Update reports by name
[**update_iceberg_system_settings_scheduler_by_id**](ConfigurationApi.md#update_iceberg_system_settings_scheduler_by_id) | **PUT** /system-settings/scheduler/{name}/ | Update scheduler by name
[**update_iceberg_system_settings_schedulers**](ConfigurationApi.md#update_iceberg_system_settings_schedulers) | **PUT** /system-settings/schedulers/ | Update schedulers by name
[**update_iceberg_system_settings_system_settings_by_id**](ConfigurationApi.md#update_iceberg_system_settings_system_settings_by_id) | **PUT** /system-settings/ | Update system-settings by ID
[**update_iceberg_topic_rule_rule_by_id**](ConfigurationApi.md#update_iceberg_topic_rule_rule_by_id) | **PUT** /topic/{topic_name}/rule/{rule_name}/ | Overwrite a rule.
[**update_iceberg_topic_topic_by_id**](ConfigurationApi.md#update_iceberg_topic_topic_by_id) | **PUT** /topic/{topic_name}/ | Overwrite a topic.
[**update_iceberg_topics_topics_by_id**](ConfigurationApi.md#update_iceberg_topics_topics_by_id) | **PUT** /topics/ | Overwrite topics.


# **check_device_group_unsaved_configuration**
> check_device_group_unsaved_configuration(device_group_name)

Check if the un-committed configuration of the given device group is correct

Checks if the un-committed configuration of a device-group is correct. The un-committed changes are merged with the committed configuration and the complete configuration required for the supplied device-group is validated.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
device_group_name = 'device_group_name_example' # str | Name of device group

try:
    # Check if the un-committed configuration of the given device group is correct
    api_instance.check_device_group_unsaved_configuration(device_group_name)
except ApiException as e:
    print("Exception when calling ConfigurationApi->check_device_group_unsaved_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_name** | **str**| Name of device group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_network_group_unsaved_configuration**
> check_network_group_unsaved_configuration(network_group_name)

Check if the unsaved configuration of the given network group is correct.

Checks if the un-committed configuration of a network-group is correct. The un-committed changes are merged with the committed configuration and the complete configuration required for the supplied network-group is validated.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
network_group_name = 'network_group_name_example' # str | Name of network group

try:
    # Check if the unsaved configuration of the given network group is correct.
    api_instance.check_network_group_unsaved_configuration(network_group_name)
except ApiException as e:
    print("Exception when calling ConfigurationApi->check_network_group_unsaved_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_group_name** | **str**| Name of network group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commit_unsaved_configuration**
> commit_unsaved_configuration(sync=sync)

Commit unsaved configuration.

Commit the configuration in configuration database. Services of all the affected groups are started or restarted. If there is an error in the configuration, changes would not be saved into the database. If there is some system error, changes would be saved into the database.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
sync = true # bool | Boolean variable is set to false allow the commit to go asynchronously, default value is true which means commit will go synchronously (optional) (default to true)

try:
    # Commit unsaved configuration.
    api_instance.commit_unsaved_configuration(sync=sync)
except ApiException as e:
    print("Exception when calling ConfigurationApi->commit_unsaved_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync** | **bool**| Boolean variable is set to false allow the commit to go asynchronously, default value is true which means commit will go synchronously | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_device_device_by_id**
> create_iceberg_device_device_by_id(device_id, device)

Update or create a device.

Create/Update a device by `device-id`. The `device-id` specified in URL and the request body must match. If the device already exists then, old content will be updated with the new content.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
device_id = 'device_id_example' # str | ID of device-id
device = swagger_client.DeviceSchema() # DeviceSchema | devicebody object

try:
    # Update or create a device.
    api_instance.create_iceberg_device_device_by_id(device_id, device)
except ApiException as e:
    print("Exception when calling ConfigurationApi->create_iceberg_device_device_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| ID of device-id | 
 **device** | [**DeviceSchema**](DeviceSchema.md)| devicebody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_device_group_device_group_by_id**
> create_iceberg_device_group_device_group_by_id(device_group_name, device_group)

Update or create a device-group.

Create/Update a device-group by `device-group-name`. The `device-group-name` specified in URL and the request body must match. If the device-group already exists then, old content will be updated with the new content

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
device_group_name = 'device_group_name_example' # str | ID of device-group-name
device_group = swagger_client.DeviceGroupSchema() # DeviceGroupSchema | device_groupbody object

try:
    # Update or create a device-group.
    api_instance.create_iceberg_device_group_device_group_by_id(device_group_name, device_group)
except ApiException as e:
    print("Exception when calling ConfigurationApi->create_iceberg_device_group_device_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_name** | **str**| ID of device-group-name | 
 **device_group** | [**DeviceGroupSchema**](DeviceGroupSchema.md)| device_groupbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_device_groups_device_groups_by_id**
> create_iceberg_device_groups_device_groups_by_id(device_groups)

Update or create multiple device-groups.

Create/Update multiple device-groups. The new content for the existing device-groups updates the existing content and new device-groups are created.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
device_groups = swagger_client.DeviceGroupsSchema() # DeviceGroupsSchema | device-groupsbody object

try:
    # Update or create multiple device-groups.
    api_instance.create_iceberg_device_groups_device_groups_by_id(device_groups)
except ApiException as e:
    print("Exception when calling ConfigurationApi->create_iceberg_device_groups_device_groups_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_groups** | [**DeviceGroupsSchema**](DeviceGroupsSchema.md)| device-groupsbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_devices_devices_by_id**
> create_iceberg_devices_devices_by_id(devices)

Update or create multiple devices.

Create/Update multiple devices. The new content for the existing devices updates the existing content and the new devices are created.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
devices = swagger_client.DevicesSchema() # DevicesSchema | devicesbody object

try:
    # Update or create multiple devices.
    api_instance.create_iceberg_devices_devices_by_id(devices)
except ApiException as e:
    print("Exception when calling ConfigurationApi->create_iceberg_devices_devices_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **devices** | [**DevicesSchema**](DevicesSchema.md)| devicesbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_network_group_network_group_by_id**
> create_iceberg_network_group_network_group_by_id(network_group_name, network_group)

Update or create a network-group.

Create/Update a network-group by `network-group-name`. The `network-group-name` parameter specified in URL and the request body must match. If the network-group already exists then, the existing network-group's configuration will be updated with the new content.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
network_group_name = 'network_group_name_example' # str | ID of network-group-name
network_group = swagger_client.NetworkGroupSchema() # NetworkGroupSchema | network_groupbody object

try:
    # Update or create a network-group.
    api_instance.create_iceberg_network_group_network_group_by_id(network_group_name, network_group)
except ApiException as e:
    print("Exception when calling ConfigurationApi->create_iceberg_network_group_network_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_group_name** | **str**| ID of network-group-name | 
 **network_group** | [**NetworkGroupSchema**](NetworkGroupSchema.md)| network_groupbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_network_groups_network_groups_by_id**
> create_iceberg_network_groups_network_groups_by_id(network_groups)

Update or create multiple network-groups.

Create/Update multiple network-groups. The new content for the existing network-groups updates the existing content and the new network-groups are created.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
network_groups = swagger_client.NetworkGroupsSchema() # NetworkGroupsSchema | network-groupsbody object

try:
    # Update or create multiple network-groups.
    api_instance.create_iceberg_network_groups_network_groups_by_id(network_groups)
except ApiException as e:
    print("Exception when calling ConfigurationApi->create_iceberg_network_groups_network_groups_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_groups** | [**NetworkGroupsSchema**](NetworkGroupsSchema.md)| network-groupsbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_notification_notification_by_id**
> create_iceberg_notification_notification_by_id(notification_name, notification)

Update or create a notification

Create/Update a notification by `notification-name`. The `notification-name` specified in URL and the request body must match. If the notification already exists then, the existing notification's configuration will be updated with the new content.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
notification_name = 'notification_name_example' # str | ID of notification-name
notification = swagger_client.NotificationSchema() # NotificationSchema | notificationbody object

try:
    # Update or create a notification
    api_instance.create_iceberg_notification_notification_by_id(notification_name, notification)
except ApiException as e:
    print("Exception when calling ConfigurationApi->create_iceberg_notification_notification_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_name** | **str**| ID of notification-name | 
 **notification** | [**NotificationSchema**](NotificationSchema.md)| notificationbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_notifications_notifications_by_id**
> create_iceberg_notifications_notifications_by_id(notifications)

Update or create multiple notifications.

Create/Update multiple notifications. The new content for the existing notifications updates the existing content and the new notifications are created.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
notifications = swagger_client.NotificationsSchema() # NotificationsSchema | notificationsbody object

try:
    # Update or create multiple notifications.
    api_instance.create_iceberg_notifications_notifications_by_id(notifications)
except ApiException as e:
    print("Exception when calling ConfigurationApi->create_iceberg_notifications_notifications_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notifications** | [**NotificationsSchema**](NotificationsSchema.md)| notificationsbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_playbook_playbook_by_id**
> create_iceberg_playbook_playbook_by_id(playbook_name, playbook)

Update or create a playbook.

Create/Update a playbook by `playbook-name`. The `playbook-name` specified in URL and the request body must match. If the playbook already exists then, the existing playbook's configuration will be updated with the new content.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
playbook_name = 'playbook_name_example' # str | ID of playbook-name
playbook = swagger_client.PlaybookSchema() # PlaybookSchema | playbookbody object

try:
    # Update or create a playbook.
    api_instance.create_iceberg_playbook_playbook_by_id(playbook_name, playbook)
except ApiException as e:
    print("Exception when calling ConfigurationApi->create_iceberg_playbook_playbook_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playbook_name** | **str**| ID of playbook-name | 
 **playbook** | [**PlaybookSchema**](PlaybookSchema.md)| playbookbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_playbooks_playbooks_by_id**
> create_iceberg_playbooks_playbooks_by_id(playbooks)

Update or create multiple playbooks.

Create/Update multiple playbooks. The new content for the existing playbooks updates the existing content and the new playbooks are created.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
playbooks = swagger_client.PlaybooksSchema() # PlaybooksSchema | playbooksbody object

try:
    # Update or create multiple playbooks.
    api_instance.create_iceberg_playbooks_playbooks_by_id(playbooks)
except ApiException as e:
    print("Exception when calling ConfigurationApi->create_iceberg_playbooks_playbooks_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playbooks** | [**PlaybooksSchema**](PlaybooksSchema.md)| playbooksbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_retention_policies_retention_policies_by_id**
> create_iceberg_retention_policies_retention_policies_by_id(retention_policies)

Update or create multiple retention-policies.

Create/Update multiple retention-policies. The new content for the existing retention-policies update the existing content and the new retention-policies are created.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
retention_policies = swagger_client.RetentionPoliciesSchema() # RetentionPoliciesSchema | retention-policiesbody object object

try:
    # Update or create multiple retention-policies.
    api_instance.create_iceberg_retention_policies_retention_policies_by_id(retention_policies)
except ApiException as e:
    print("Exception when calling ConfigurationApi->create_iceberg_retention_policies_retention_policies_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retention_policies** | [**RetentionPoliciesSchema**](RetentionPoliciesSchema.md)| retention-policiesbody object object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_retention_policy_retention_policy_by_id**
> create_iceberg_retention_policy_retention_policy_by_id(retention_policy_name, retention_policy)

Update or create a retention-policy.

Create/Update a retention-policy by `retention-policy-name`. The `retention-policy-name` specified in URL and the request body must match. If the retention-policy exists then, the existing retention-policy's configuration will be updated by the new content.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
retention_policy_name = 'retention_policy_name_example' # str | ID of retention-policy-name
retention_policy = swagger_client.RetentionPolicySchema() # RetentionPolicySchema | retention_policybody object

try:
    # Update or create a retention-policy.
    api_instance.create_iceberg_retention_policy_retention_policy_by_id(retention_policy_name, retention_policy)
except ApiException as e:
    print("Exception when calling ConfigurationApi->create_iceberg_retention_policy_retention_policy_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retention_policy_name** | **str**| ID of retention-policy-name | 
 **retention_policy** | [**RetentionPolicySchema**](RetentionPolicySchema.md)| retention_policybody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_system_settings_destination_by_id**
> create_iceberg_system_settings_destination_by_id(name, destination)

Create destination by name

Create/Update a destination by `name`. The `name` specified in URL and the request body must match. If the destination exists then, the existing destination's configuration will be updated by the new content.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
name = 'name_example' # str | ID of name
destination = swagger_client.DestinationSchema() # DestinationSchema | destinationsbody object

try:
    # Create destination by name
    api_instance.create_iceberg_system_settings_destination_by_id(name, destination)
except ApiException as e:
    print("Exception when calling ConfigurationApi->create_iceberg_system_settings_destination_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **destination** | [**DestinationSchema**](DestinationSchema.md)| destinationsbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_system_settings_destinations**
> create_iceberg_system_settings_destinations(destinations)

Create destinations by name

Create/Update multiple destinations. The new content for the existing destinations updates the existing content and the new destinations are created.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
destinations = swagger_client.DestinationsSchema() # DestinationsSchema | destinationsbody object

try:
    # Create destinations by name
    api_instance.create_iceberg_system_settings_destinations(destinations)
except ApiException as e:
    print("Exception when calling ConfigurationApi->create_iceberg_system_settings_destinations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destinations** | [**DestinationsSchema**](DestinationsSchema.md)| destinationsbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_system_settings_report_by_id**
> create_iceberg_system_settings_report_by_id(name, report)

Create report by name

Create/Update a report by `name`. The `name` specified in URL and the request body must match. If the report exists then, the existing report's configuration will be updated by the new content.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
name = 'name_example' # str | ID of name
report = swagger_client.ReportSchema() # ReportSchema | reportsbody object

try:
    # Create report by name
    api_instance.create_iceberg_system_settings_report_by_id(name, report)
except ApiException as e:
    print("Exception when calling ConfigurationApi->create_iceberg_system_settings_report_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **report** | [**ReportSchema**](ReportSchema.md)| reportsbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_system_settings_reports**
> create_iceberg_system_settings_reports(reports)

Create reports by name

Create/Update multiple reports. The new content for the existing reports updates the existing content and the new reports are created.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
reports = swagger_client.ReportsSchema() # ReportsSchema | reportsbody object

try:
    # Create reports by name
    api_instance.create_iceberg_system_settings_reports(reports)
except ApiException as e:
    print("Exception when calling ConfigurationApi->create_iceberg_system_settings_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reports** | [**ReportsSchema**](ReportsSchema.md)| reportsbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_system_settings_scheduler_by_id**
> create_iceberg_system_settings_scheduler_by_id(name, scheduler)

Create scheduler by name

Create/Update a scheduler by `name`. The `name` specified in URL and the request body must match. If the scheduler exists then, the existing scheduler's configuration will be updated by the new content.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
name = 'name_example' # str | ID of name
scheduler = swagger_client.SchedulerSchema() # SchedulerSchema | schedulerbody object

try:
    # Create scheduler by name
    api_instance.create_iceberg_system_settings_scheduler_by_id(name, scheduler)
except ApiException as e:
    print("Exception when calling ConfigurationApi->create_iceberg_system_settings_scheduler_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **scheduler** | [**SchedulerSchema**](SchedulerSchema.md)| schedulerbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_system_settings_schedulers**
> create_iceberg_system_settings_schedulers(schedulers)

Create schedulers by name

Create/Update multiple schdeulers. The new content for the existing schedulers updates the existing content and the new schedulers are created.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
schedulers = swagger_client.SchedulersSchema() # SchedulersSchema | schedulersbody object

try:
    # Create schedulers by name
    api_instance.create_iceberg_system_settings_schedulers(schedulers)
except ApiException as e:
    print("Exception when calling ConfigurationApi->create_iceberg_system_settings_schedulers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedulers** | [**SchedulersSchema**](SchedulersSchema.md)| schedulersbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_system_settings_system_settings_by_id**
> create_iceberg_system_settings_system_settings_by_id(system_settings)

Create system-settings

Create/Update system-settings to populate persis-raw-data, schedulers, destinations and reports.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
system_settings = swagger_client.SystemSettingsSchema() # SystemSettingsSchema | system_settings body object

try:
    # Create system-settings
    api_instance.create_iceberg_system_settings_system_settings_by_id(system_settings)
except ApiException as e:
    print("Exception when calling ConfigurationApi->create_iceberg_system_settings_system_settings_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_settings** | [**SystemSettingsSchema**](SystemSettingsSchema.md)| system_settings body object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_topic_rule_rule_by_id**
> create_iceberg_topic_rule_rule_by_id(topic_name, rule_name, rule)

Update or create a rule.

Create/Update a rule by `rule-name`. The `rule-name` specified in URL and the request body must match. If the rule already exists then, the existing rule's configuration will be updated with the new content

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
topic_name = 'topic_name_example' # str | ID of topic-name
rule_name = 'rule_name_example' # str | ID of rule-name
rule = swagger_client.RuleSchema() # RuleSchema | rulebody object

try:
    # Update or create a rule.
    api_instance.create_iceberg_topic_rule_rule_by_id(topic_name, rule_name, rule)
except ApiException as e:
    print("Exception when calling ConfigurationApi->create_iceberg_topic_rule_rule_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_name** | **str**| ID of topic-name | 
 **rule_name** | **str**| ID of rule-name | 
 **rule** | [**RuleSchema**](RuleSchema.md)| rulebody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_topic_topic_by_id**
> create_iceberg_topic_topic_by_id(topic_name, topic)

Update or create a topic.

Create/Update a topic by `topic-name`. The `topic-name` specified in URL and the request body must match. If the topic already exists then, the existing topic's configuration will be updated with the new content.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
topic_name = 'topic_name_example' # str | ID of topic-name
topic = swagger_client.TopicSchema() # TopicSchema | topicbody object

try:
    # Update or create a topic.
    api_instance.create_iceberg_topic_topic_by_id(topic_name, topic)
except ApiException as e:
    print("Exception when calling ConfigurationApi->create_iceberg_topic_topic_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_name** | **str**| ID of topic-name | 
 **topic** | [**TopicSchema**](TopicSchema.md)| topicbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iceberg_topics_topics_by_id**
> create_iceberg_topics_topics_by_id(topics)

Update or create multiple topics.

Create/Update multiple topics. The new content for the existing topics updates the existing content and the new topics are created.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
topics = swagger_client.TopicsSchema() # TopicsSchema | topicsbody object

try:
    # Update or create multiple topics.
    api_instance.create_iceberg_topics_topics_by_id(topics)
except ApiException as e:
    print("Exception when calling ConfigurationApi->create_iceberg_topics_topics_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topics** | [**TopicsSchema**](TopicsSchema.md)| topicsbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_device_device_by_id**
> delete_iceberg_device_device_by_id(device_id)

Delete device.

Delete a device by `device-id`. Delete will fail if the device is being referenced by a device-group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
device_id = 'device_id_example' # str | ID of device-id

try:
    # Delete device.
    api_instance.delete_iceberg_device_device_by_id(device_id)
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_iceberg_device_device_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| ID of device-id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_device_group_device_group_by_id**
> delete_iceberg_device_group_device_group_by_id(device_group_name)

Delete device-group.

Delete a device-group by `device-group-name`. Delete will fail if the device-group's services are running.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
device_group_name = 'device_group_name_example' # str | ID of device-group-name

try:
    # Delete device-group.
    api_instance.delete_iceberg_device_group_device_group_by_id(device_group_name)
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_iceberg_device_group_device_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_name** | **str**| ID of device-group-name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_device_groups_device_groups_by_id**
> delete_iceberg_device_groups_device_groups_by_id()

Delete all device-groups.

Delete all device-groups. Delete fails if services are still running for the device groups.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()

try:
    # Delete all device-groups.
    api_instance.delete_iceberg_device_groups_device_groups_by_id()
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_iceberg_device_groups_device_groups_by_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_devices_devices_by_id**
> delete_iceberg_devices_devices_by_id()

Delete all devices.

Delete all devices. This will fail if any device is referenced in any device-group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()

try:
    # Delete all devices.
    api_instance.delete_iceberg_devices_devices_by_id()
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_iceberg_devices_devices_by_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_network_group_network_group_by_id**
> delete_iceberg_network_group_network_group_by_id(network_group_name)

Delete network-group.

Delete a network-group by `network-group-name`. Delete will fail if the network-group's services are running.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
network_group_name = 'network_group_name_example' # str | ID of network-group-name

try:
    # Delete network-group.
    api_instance.delete_iceberg_network_group_network_group_by_id(network_group_name)
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_iceberg_network_group_network_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_group_name** | **str**| ID of network-group-name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_network_groups_network_groups_by_id**
> delete_iceberg_network_groups_network_groups_by_id()

Delete all network-groups.

Delete all network-groups. Delete will fail if services are still running for the network groups.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()

try:
    # Delete all network-groups.
    api_instance.delete_iceberg_network_groups_network_groups_by_id()
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_iceberg_network_groups_network_groups_by_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_notification_notification_by_id**
> delete_iceberg_notification_notification_by_id(notification_name)

Delete a notification.

Delete a notification by `notification-name`. Delete will fail if the notification is referenced by a device-group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
notification_name = 'notification_name_example' # str | ID of notification-name

try:
    # Delete a notification.
    api_instance.delete_iceberg_notification_notification_by_id(notification_name)
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_iceberg_notification_notification_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_name** | **str**| ID of notification-name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_notifications_notifications_by_id**
> delete_iceberg_notifications_notifications_by_id()

Delete all notifications.

Delete all notifications. This will fail if any notification is referenced in any device-group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()

try:
    # Delete all notifications.
    api_instance.delete_iceberg_notifications_notifications_by_id()
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_iceberg_notifications_notifications_by_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_playbook_playbook_by_id**
> delete_iceberg_playbook_playbook_by_id(playbook_name)

Delete a playbook.

Delete a playbook by `playbook-name`. Delete will fail if the playbook is referenced by a device-group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
playbook_name = 'playbook_name_example' # str | ID of playbook-name

try:
    # Delete a playbook.
    api_instance.delete_iceberg_playbook_playbook_by_id(playbook_name)
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_iceberg_playbook_playbook_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playbook_name** | **str**| ID of playbook-name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_playbooks_playbooks_by_id**
> delete_iceberg_playbooks_playbooks_by_id()

Delete all playbooks.

Delete all playbooks. This will fail if any playbook is referenced in any device-group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()

try:
    # Delete all playbooks.
    api_instance.delete_iceberg_playbooks_playbooks_by_id()
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_iceberg_playbooks_playbooks_by_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_retention_policies_retention_policies_by_id**
> delete_iceberg_retention_policies_retention_policies_by_id()

Delete all retention-policies.

Delete all the retention policies. This will fail if any retention-policy is referenced in any device-group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()

try:
    # Delete all retention-policies.
    api_instance.delete_iceberg_retention_policies_retention_policies_by_id()
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_iceberg_retention_policies_retention_policies_by_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_retention_policy_retention_policy_by_id**
> delete_iceberg_retention_policy_retention_policy_by_id(retention_policy_name)

Delete a retention-policy.

Delete a retention-policy by `retention-policy-name`. Delete will fail if the retention-policy is referenced by a device-group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
retention_policy_name = 'retention_policy_name_example' # str | ID of retention-policy-name

try:
    # Delete a retention-policy.
    api_instance.delete_iceberg_retention_policy_retention_policy_by_id(retention_policy_name)
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_iceberg_retention_policy_retention_policy_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retention_policy_name** | **str**| ID of retention-policy-name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_system_settings_destination_by_id**
> delete_iceberg_system_settings_destination_by_id(name)

Delete destination by name

Delete a destination by `name`. Delete will fail if the destination is being referenced by a report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
name = 'name_example' # str | ID of name

try:
    # Delete destination by name
    api_instance.delete_iceberg_system_settings_destination_by_id(name)
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_iceberg_system_settings_destination_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_system_settings_destinations**
> delete_iceberg_system_settings_destinations()

Delete destinations by name

Delete all destinations. This will fail if any destination is referenced in any report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()

try:
    # Delete destinations by name
    api_instance.delete_iceberg_system_settings_destinations()
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_iceberg_system_settings_destinations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_system_settings_report_by_id**
> delete_iceberg_system_settings_report_by_id(name)

Delete report by name

Delete a report by `name`. Delete will fail if the report is being referenced by a device-group or network-group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
name = 'name_example' # str | ID of name

try:
    # Delete report by name
    api_instance.delete_iceberg_system_settings_report_by_id(name)
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_iceberg_system_settings_report_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_system_settings_reports**
> delete_iceberg_system_settings_reports()

Delete reports by name

Delete all reports. This will fail if any report is referenced in any device-group or network-group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()

try:
    # Delete reports by name
    api_instance.delete_iceberg_system_settings_reports()
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_iceberg_system_settings_reports: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_system_settings_scheduler_by_id**
> delete_iceberg_system_settings_scheduler_by_id(name)

Delete scheduler by name

Delete a scheduler by `name`. Delete will fail if the scheduler is being referenced by a report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
name = 'name_example' # str | ID of name

try:
    # Delete scheduler by name
    api_instance.delete_iceberg_system_settings_scheduler_by_id(name)
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_iceberg_system_settings_scheduler_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_system_settings_schedulers**
> delete_iceberg_system_settings_schedulers()

Delete schedulers by name

Delete all schedulers. This will fail if any scheduler is referenced in any report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()

try:
    # Delete schedulers by name
    api_instance.delete_iceberg_system_settings_schedulers()
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_iceberg_system_settings_schedulers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_system_settings_system_settings_by_id**
> delete_iceberg_system_settings_system_settings_by_id()

Delete system-settings

Delete system-settings. This will delete all the reports, destinations and schedulers. The request will fail of any of the reports is being referenced by a device-group or network-group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()

try:
    # Delete system-settings
    api_instance.delete_iceberg_system_settings_system_settings_by_id()
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_iceberg_system_settings_system_settings_by_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_topic_rule_rule_by_id**
> delete_iceberg_topic_rule_rule_by_id(topic_name, rule_name)

Delete a rule.

Delete a rule by `rule-name`. Delete will fail if the rule is referenced by any other playbook.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
topic_name = 'topic_name_example' # str | ID of topic-name
rule_name = 'rule_name_example' # str | ID of rule-name

try:
    # Delete a rule.
    api_instance.delete_iceberg_topic_rule_rule_by_id(topic_name, rule_name)
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_iceberg_topic_rule_rule_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_name** | **str**| ID of topic-name | 
 **rule_name** | **str**| ID of rule-name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_topic_topic_by_id**
> delete_iceberg_topic_topic_by_id(topic_name)

Delete a topic.

Delete a topic by `topic-name`. Delete will fail if the topic is referenced by any other playbook.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
topic_name = 'topic_name_example' # str | ID of topic-name

try:
    # Delete a topic.
    api_instance.delete_iceberg_topic_topic_by_id(topic_name)
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_iceberg_topic_topic_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_name** | **str**| ID of topic-name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iceberg_topics_topics_by_id**
> delete_iceberg_topics_topics_by_id()

Delete all topics.

Delete all topics. This will fail if any topic is referenced in any playbook.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()

try:
    # Delete all topics.
    api_instance.delete_iceberg_topics_topics_by_id()
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_iceberg_topics_topics_by_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_affected_groups**
> AffectedGroups retrieve_affected_groups()

Get all groups affected by un-committed configuration changes.

Get all groups that are affected by the un-committed configuration changes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()

try:
    # Get all groups affected by un-committed configuration changes.
    api_response = api_instance.retrieve_affected_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_affected_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AffectedGroups**](AffectedGroups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_device_group_status**
> ServiceStatus retrieve_device_group_status(device_group_name)

Get device-group's status.

Get information about the status of a device-group's services.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
device_group_name = 'device_group_name_example' # str | Name of device-group

try:
    # Get device-group's status.
    api_response = api_instance.retrieve_device_group_status(device_group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_device_group_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_name** | **str**| Name of device-group | 

### Return type

[**ServiceStatus**](ServiceStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_device_device**
> list[str] retrieve_iceberg_device_device(working=working)

List all device-ids.

Get a list of all the device IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
working = true # bool | true queries un-committed configuration (optional)

try:
    # List all device-ids.
    api_response = api_instance.retrieve_iceberg_device_device(working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_device_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working** | **bool**| true queries un-committed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_device_device_by_id**
> DeviceSchema retrieve_iceberg_device_device_by_id(device_id, working=working)

Get a device's configuration.

Get the configuration details of a device by its `device-id`.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
device_id = 'device_id_example' # str | ID of device-id
working = true # bool | true queries un-committed configuration (optional)

try:
    # Get a device's configuration.
    api_response = api_instance.retrieve_iceberg_device_device_by_id(device_id, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_device_device_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| ID of device-id | 
 **working** | **bool**| true queries un-committed configuration | [optional] 

### Return type

[**DeviceSchema**](DeviceSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_device_group_device_group**
> list[str] retrieve_iceberg_device_group_device_group(working=working)

List all device-group names.

Get a list of all the device-group names.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
working = true # bool | true queries un-committed configuration (optional)

try:
    # List all device-group names.
    api_response = api_instance.retrieve_iceberg_device_group_device_group(working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_device_group_device_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working** | **bool**| true queries un-committed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_device_group_device_group_by_id**
> DeviceGroupSchema retrieve_iceberg_device_group_device_group_by_id(device_group_name, working=working)

Get device-group's configuration.

Get configuration details of a device group by the device group name.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
device_group_name = 'device_group_name_example' # str | ID of device-group-name
working = true # bool | true queries un-committed configuration (optional)

try:
    # Get device-group's configuration.
    api_response = api_instance.retrieve_iceberg_device_group_device_group_by_id(device_group_name, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_device_group_device_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_name** | **str**| ID of device-group-name | 
 **working** | **bool**| true queries un-committed configuration | [optional] 

### Return type

[**DeviceGroupSchema**](DeviceGroupSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_device_groups_device_groups**
> DeviceGroupsSchema retrieve_iceberg_device_groups_device_groups(working=working)

Get all device-groups' configuration.

Get configuration details of all the device-groups.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
working = true # bool | true queries un-committed configuration (optional)

try:
    # Get all device-groups' configuration.
    api_response = api_instance.retrieve_iceberg_device_groups_device_groups(working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_device_groups_device_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working** | **bool**| true queries un-committed configuration | [optional] 

### Return type

[**DeviceGroupsSchema**](DeviceGroupsSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_devices_devices**
> DevicesSchema retrieve_iceberg_devices_devices(working=working)

Get all devices' configuration.

Get the configuration details of all devices.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
working = true # bool | true queries un-committed configuration (optional)

try:
    # Get all devices' configuration.
    api_response = api_instance.retrieve_iceberg_devices_devices(working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_devices_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working** | **bool**| true queries un-committed configuration | [optional] 

### Return type

[**DevicesSchema**](DevicesSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_network_group_network_group**
> list[str] retrieve_iceberg_network_group_network_group(working=working)

List all network-group names.

Get a list of all the `network-group-name`s.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
working = true # bool | true queries un-committed configuration (optional)

try:
    # List all network-group names.
    api_response = api_instance.retrieve_iceberg_network_group_network_group(working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_network_group_network_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working** | **bool**| true queries un-committed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_network_group_network_group_by_id**
> NetworkGroupSchema retrieve_iceberg_network_group_network_group_by_id(network_group_name, working=working)

Get network-group's configuration.

Get the configuration details of a network group by its network group name.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
network_group_name = 'network_group_name_example' # str | ID of network-group-name
working = true # bool | true queries un-committed configuration (optional)

try:
    # Get network-group's configuration.
    api_response = api_instance.retrieve_iceberg_network_group_network_group_by_id(network_group_name, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_network_group_network_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_group_name** | **str**| ID of network-group-name | 
 **working** | **bool**| true queries un-committed configuration | [optional] 

### Return type

[**NetworkGroupSchema**](NetworkGroupSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_network_groups_network_groups**
> NetworkGroupsSchema retrieve_iceberg_network_groups_network_groups(working=working)

Get all network-groups' configuration.

Get configuration of all network-groups.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
working = true # bool | true queries un-committed configuration (optional)

try:
    # Get all network-groups' configuration.
    api_response = api_instance.retrieve_iceberg_network_groups_network_groups(working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_network_groups_network_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working** | **bool**| true queries un-committed configuration | [optional] 

### Return type

[**NetworkGroupsSchema**](NetworkGroupsSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_notification_notification**
> list[str] retrieve_iceberg_notification_notification(working=working)

List all notification-names.

Get a list of all the `notification-name`s.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
working = true # bool | true queries un-committed configuration (optional)

try:
    # List all notification-names.
    api_response = api_instance.retrieve_iceberg_notification_notification(working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_notification_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working** | **bool**| true queries un-committed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_notification_notification_by_id**
> NotificationSchema retrieve_iceberg_notification_notification_by_id(notification_name, working=working)

Get a notification's configuration.

Get the configuration details of a notification by `notification-name`.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
notification_name = 'notification_name_example' # str | ID of notification-name
working = true # bool | true queries un-committed configuration (optional)

try:
    # Get a notification's configuration.
    api_response = api_instance.retrieve_iceberg_notification_notification_by_id(notification_name, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_notification_notification_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_name** | **str**| ID of notification-name | 
 **working** | **bool**| true queries un-committed configuration | [optional] 

### Return type

[**NotificationSchema**](NotificationSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_notifications_notifications_by_id**
> NotificationsSchema retrieve_iceberg_notifications_notifications_by_id(working=working)

Get all notifications' configuration.

Get the configuration details of all notifications.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
working = true # bool | true queries un-committed configuration (optional)

try:
    # Get all notifications' configuration.
    api_response = api_instance.retrieve_iceberg_notifications_notifications_by_id(working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_notifications_notifications_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working** | **bool**| true queries un-committed configuration | [optional] 

### Return type

[**NotificationsSchema**](NotificationsSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_playbook_playbook**
> list[str] retrieve_iceberg_playbook_playbook(working=working)

List all playbook-names.

Get a list of all the `playbook-name`s.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
working = true # bool | true queries un-committed configuration (optional)

try:
    # List all playbook-names.
    api_response = api_instance.retrieve_iceberg_playbook_playbook(working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_playbook_playbook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working** | **bool**| true queries un-committed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_playbook_playbook_by_id**
> PlaybookSchema retrieve_iceberg_playbook_playbook_by_id(playbook_name, working=working)

Get a playbook's configuration.

Get the configuration details of a playbook by `playbook-name`.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
playbook_name = 'playbook_name_example' # str | ID of playbook-name
working = true # bool | true queries un-committed configuration (optional)

try:
    # Get a playbook's configuration.
    api_response = api_instance.retrieve_iceberg_playbook_playbook_by_id(playbook_name, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_playbook_playbook_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playbook_name** | **str**| ID of playbook-name | 
 **working** | **bool**| true queries un-committed configuration | [optional] 

### Return type

[**PlaybookSchema**](PlaybookSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_playbooks_playbooks_by_id**
> PlaybooksSchema retrieve_iceberg_playbooks_playbooks_by_id(working=working)

Get all playbooks' configuration.

Get the configuration of all playbooks.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
working = true # bool | true queries un-committed configuration (optional)

try:
    # Get all playbooks' configuration.
    api_response = api_instance.retrieve_iceberg_playbooks_playbooks_by_id(working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_playbooks_playbooks_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working** | **bool**| true queries un-committed configuration | [optional] 

### Return type

[**PlaybooksSchema**](PlaybooksSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_retention_policies_retention_policies_by_id**
> RetentionPoliciesSchema retrieve_iceberg_retention_policies_retention_policies_by_id(working=working)

Get all retention-policies' configuration.

Get the configuration of all the retention-policies.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
working = true # bool | true queries un-committed configuration (optional)

try:
    # Get all retention-policies' configuration.
    api_response = api_instance.retrieve_iceberg_retention_policies_retention_policies_by_id(working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_retention_policies_retention_policies_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working** | **bool**| true queries un-committed configuration | [optional] 

### Return type

[**RetentionPoliciesSchema**](RetentionPoliciesSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_retention_policy_retention_policy**
> list[str] retrieve_iceberg_retention_policy_retention_policy(working=working)

List all retention-policy-names.

Get a list of all the `retention-policy-name`s.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
working = true # bool | true queries un-committed configuration (optional)

try:
    # List all retention-policy-names.
    api_response = api_instance.retrieve_iceberg_retention_policy_retention_policy(working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_retention_policy_retention_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working** | **bool**| true queries un-committed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_retention_policy_retention_policy_by_id**
> RetentionPolicySchema retrieve_iceberg_retention_policy_retention_policy_by_id(retention_policy_name, working=working)

Get a retention-policy's configuration.

Get the configuration details of a retention policy by `retention-policy-name`.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
retention_policy_name = 'retention_policy_name_example' # str | ID of retention-policy-name
working = true # bool | true queries un-committed configuration (optional)

try:
    # Get a retention-policy's configuration.
    api_response = api_instance.retrieve_iceberg_retention_policy_retention_policy_by_id(retention_policy_name, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_retention_policy_retention_policy_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retention_policy_name** | **str**| ID of retention-policy-name | 
 **working** | **bool**| true queries un-committed configuration | [optional] 

### Return type

[**RetentionPolicySchema**](RetentionPolicySchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_system_settings_destination_by_id**
> DestinationSchema retrieve_iceberg_system_settings_destination_by_id(name, working=working)

Retrieve destination by name

Get the configuration details of a destination by its `name`.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
name = 'name_example' # str | ID of name
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve destination by name
    api_response = api_instance.retrieve_iceberg_system_settings_destination_by_id(name, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_system_settings_destination_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**DestinationSchema**](DestinationSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_system_settings_destinations**
> DestinationsSchema retrieve_iceberg_system_settings_destinations(working=working)

Retrieve destinations by name

Get the configuration details of all destinations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve destinations by name
    api_response = api_instance.retrieve_iceberg_system_settings_destinations(working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_system_settings_destinations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**DestinationsSchema**](DestinationsSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_system_settings_report_by_id**
> ReportSchema retrieve_iceberg_system_settings_report_by_id(name, working=working)

Retrieve report by name

Get the configuration details of a report by its `name`.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
name = 'name_example' # str | ID of name
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve report by name
    api_response = api_instance.retrieve_iceberg_system_settings_report_by_id(name, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_system_settings_report_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**ReportSchema**](ReportSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_system_settings_reports**
> ReportsSchema retrieve_iceberg_system_settings_reports(working=working)

Retrieve reports by name

Get the configuration details of all reports.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve reports by name
    api_response = api_instance.retrieve_iceberg_system_settings_reports(working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_system_settings_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**ReportsSchema**](ReportsSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_system_settings_scheduler_by_id**
> SchedulerSchema retrieve_iceberg_system_settings_scheduler_by_id(name, working=working)

Retrieve scheduler by name

Get the configuration details of a scheduler by its `name`.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
name = 'name_example' # str | ID of name
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve scheduler by name
    api_response = api_instance.retrieve_iceberg_system_settings_scheduler_by_id(name, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_system_settings_scheduler_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**SchedulerSchema**](SchedulerSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_system_settings_schedulers**
> SchedulersSchema retrieve_iceberg_system_settings_schedulers(working=working)

Retrieve schedulers by name

Get the configuration details of all schedulers.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve schedulers by name
    api_response = api_instance.retrieve_iceberg_system_settings_schedulers(working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_system_settings_schedulers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**SchedulersSchema**](SchedulersSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_system_settings_system_settings**
> SystemSettingsSchema retrieve_iceberg_system_settings_system_settings(working=working)

Retrieve system-settings

Retrieve system-settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
working = true # bool | true queries undeployed configuration (optional)

try:
    # Retrieve system-settings
    api_response = api_instance.retrieve_iceberg_system_settings_system_settings(working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_system_settings_system_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working** | **bool**| true queries undeployed configuration | [optional] 

### Return type

[**SystemSettingsSchema**](SystemSettingsSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_topic_rule_rule**
> list[str] retrieve_iceberg_topic_rule_rule(topic_name, working=working)

List all rule-names in a topic.

Get a list of all the `rule-name`s in a topic.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
topic_name = 'topic_name_example' # str | ID of topic-name
working = true # bool | true queries un-committed configuration (optional)

try:
    # List all rule-names in a topic.
    api_response = api_instance.retrieve_iceberg_topic_rule_rule(topic_name, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_topic_rule_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_name** | **str**| ID of topic-name | 
 **working** | **bool**| true queries un-committed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_topic_rule_rule_by_id**
> RuleSchema retrieve_iceberg_topic_rule_rule_by_id(topic_name, rule_name, working=working)

Get a rule's configuration.

Get the configuration details of a rule by `rule-name`.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
topic_name = 'topic_name_example' # str | ID of topic-name
rule_name = 'rule_name_example' # str | ID of rule-name
working = true # bool | true queries un-committed configuration (optional)

try:
    # Get a rule's configuration.
    api_response = api_instance.retrieve_iceberg_topic_rule_rule_by_id(topic_name, rule_name, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_topic_rule_rule_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_name** | **str**| ID of topic-name | 
 **rule_name** | **str**| ID of rule-name | 
 **working** | **bool**| true queries un-committed configuration | [optional] 

### Return type

[**RuleSchema**](RuleSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_topic_topic**
> list[str] retrieve_iceberg_topic_topic(working=working)

List all topic-names.

Get a list of all the `topic-name`s.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
working = true # bool | true queries un-committed configuration (optional)

try:
    # List all topic-names.
    api_response = api_instance.retrieve_iceberg_topic_topic(working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_topic_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working** | **bool**| true queries un-committed configuration | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_topic_topic_by_id**
> TopicSchema retrieve_iceberg_topic_topic_by_id(topic_name, working=working)

Get a topic's configuration.

Get the configuration details of a topic by the `topic-name`.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
topic_name = 'topic_name_example' # str | ID of topic-name
working = true # bool | true queries un-committed configuration (optional)

try:
    # Get a topic's configuration.
    api_response = api_instance.retrieve_iceberg_topic_topic_by_id(topic_name, working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_topic_topic_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_name** | **str**| ID of topic-name | 
 **working** | **bool**| true queries un-committed configuration | [optional] 

### Return type

[**TopicSchema**](TopicSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_iceberg_topics_topics**
> TopicsSchema retrieve_iceberg_topics_topics(working=working)

Get all topics' configuration.

Get the configuration details of all topics.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
working = true # bool | true queries un-committed configuration (optional)

try:
    # Get all topics' configuration.
    api_response = api_instance.retrieve_iceberg_topics_topics(working=working)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_iceberg_topics_topics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working** | **bool**| true queries un-committed configuration | [optional] 

### Return type

[**TopicsSchema**](TopicsSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_network_group_status**
> ServiceStatus retrieve_network_group_status(network_group_name)

Get network-group's status.

Get information about the status of a network-group's services.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
network_group_name = 'network_group_name_example' # str | Name of network-group

try:
    # Get network-group's status.
    api_response = api_instance.retrieve_network_group_status(network_group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->retrieve_network_group_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_group_name** | **str**| Name of network-group | 

### Return type

[**ServiceStatus**](ServiceStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rollback_unsaved_configuration**
> rollback_unsaved_configuration()

Delete the un-committed configuration.

The API server follows a commit model. Unsaved configuration is called a working configuration. This API call deletes the working configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()

try:
    # Delete the un-committed configuration.
    api_instance.rollback_unsaved_configuration()
except ApiException as e:
    print("Exception when calling ConfigurationApi->rollback_unsaved_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_device_device_by_id**
> update_iceberg_device_device_by_id(device_id, device)

Overwrite a device.

Overwrite a device by device ID. The device ID specified in the URL and the request body must match.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
device_id = 'device_id_example' # str | ID of device-id
device = swagger_client.DeviceSchema() # DeviceSchema | devicebody object

try:
    # Overwrite a device.
    api_instance.update_iceberg_device_device_by_id(device_id, device)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_iceberg_device_device_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| ID of device-id | 
 **device** | [**DeviceSchema**](DeviceSchema.md)| devicebody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_device_group_device_group_by_id**
> update_iceberg_device_group_device_group_by_id(device_group_name, device_group)

Overwrite a device-group.

Overwrite a device-group by its `device-group-name`. The `device-group-name` specified in the URL and the request body must match.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
device_group_name = 'device_group_name_example' # str | ID of device-group-name
device_group = swagger_client.DeviceGroupSchema() # DeviceGroupSchema | device_groupbody object

try:
    # Overwrite a device-group.
    api_instance.update_iceberg_device_group_device_group_by_id(device_group_name, device_group)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_iceberg_device_group_device_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_name** | **str**| ID of device-group-name | 
 **device_group** | [**DeviceGroupSchema**](DeviceGroupSchema.md)| device_groupbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_device_groups_device_groups_by_id**
> update_iceberg_device_groups_device_groups_by_id(device_groups)

Overwrite device-groups.

Overwrite the existing configuration of device-groups. New device-groups are created and the existing device-groups are overwritten with new content. If some existing device-groups are not present in the payload, such device-groups are deleted. This will fail if any of the device-groups that are not present in the payload have running services.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
device_groups = swagger_client.DeviceGroupsSchema() # DeviceGroupsSchema | device-groupsbody object

try:
    # Overwrite device-groups.
    api_instance.update_iceberg_device_groups_device_groups_by_id(device_groups)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_iceberg_device_groups_device_groups_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_groups** | [**DeviceGroupsSchema**](DeviceGroupsSchema.md)| device-groupsbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_devices_devices_by_id**
> update_iceberg_devices_devices_by_id(devices)

Overwrite devices.

Overwrite the existing configuration of devices. New devices are created and the existing devices are overwritten with new content. If some existing devices are not present in the payload, such devices are deleted. This will fail if any of the devices that are not present in the payload are referenced by a device-group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
devices = swagger_client.DevicesSchema() # DevicesSchema | devicesbody object

try:
    # Overwrite devices.
    api_instance.update_iceberg_devices_devices_by_id(devices)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_iceberg_devices_devices_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **devices** | [**DevicesSchema**](DevicesSchema.md)| devicesbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_network_group_network_group_by_id**
> update_iceberg_network_group_network_group_by_id(network_group_name, network_group)

Overwrite a network-group.

Overwrite a network-group by the `network-group-name`. The `network-group-name` specified in the URL and the request body must match.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
network_group_name = 'network_group_name_example' # str | ID of network-group-name
network_group = swagger_client.NetworkGroupSchema() # NetworkGroupSchema | network_groupbody object

try:
    # Overwrite a network-group.
    api_instance.update_iceberg_network_group_network_group_by_id(network_group_name, network_group)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_iceberg_network_group_network_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_group_name** | **str**| ID of network-group-name | 
 **network_group** | [**NetworkGroupSchema**](NetworkGroupSchema.md)| network_groupbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_network_groups_network_groups_by_id**
> update_iceberg_network_groups_network_groups_by_id(network_groups)

Overwrite network-groups.

Overwrite the existing network-group configuration. New network-groups are created and the existing network-groups are overwritten with new content. If some of the existing network-groups are not present in the payload, such network-groups are deleted. This will fail if any of the network-groups that are not present in the payload have running services.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
network_groups = swagger_client.NetworkGroupsSchema() # NetworkGroupsSchema | network-groupsbody object

try:
    # Overwrite network-groups.
    api_instance.update_iceberg_network_groups_network_groups_by_id(network_groups)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_iceberg_network_groups_network_groups_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_groups** | [**NetworkGroupsSchema**](NetworkGroupsSchema.md)| network-groupsbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_notification_notification_by_id**
> update_iceberg_notification_notification_by_id(notification_name, notification)

Overwrite a notification.

Overwrite a notification by the `notification-name`. The `notification-name` specified in URL and the request body must match.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
notification_name = 'notification_name_example' # str | ID of notification-name
notification = swagger_client.NotificationSchema() # NotificationSchema | notificationbody object

try:
    # Overwrite a notification.
    api_instance.update_iceberg_notification_notification_by_id(notification_name, notification)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_iceberg_notification_notification_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_name** | **str**| ID of notification-name | 
 **notification** | [**NotificationSchema**](NotificationSchema.md)| notificationbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_notifications_notifications_by_id**
> update_iceberg_notifications_notifications_by_id(notifications)

Overwrite notifications.

Overwrite the existing notifications configuration. New notifications are created and existing notifications are overwritten with new content. If some of the existing notifications are not present in the payload, such notifications are deleted. This will fail if any of the notifications that are not present in the payload are referenced by a device-group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
notifications = swagger_client.NotificationsSchema() # NotificationsSchema | notificationsbody object

try:
    # Overwrite notifications.
    api_instance.update_iceberg_notifications_notifications_by_id(notifications)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_iceberg_notifications_notifications_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notifications** | [**NotificationsSchema**](NotificationsSchema.md)| notificationsbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_playbook_playbook_by_id**
> update_iceberg_playbook_playbook_by_id(playbook_name, playbook)

Overwrite a playbook.

Overwrite a playbook by the `playbook-name`. The `playbook-name` specified in the URL and the request body must match.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
playbook_name = 'playbook_name_example' # str | ID of playbook-name
playbook = swagger_client.PlaybookSchema() # PlaybookSchema | playbookbody object

try:
    # Overwrite a playbook.
    api_instance.update_iceberg_playbook_playbook_by_id(playbook_name, playbook)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_iceberg_playbook_playbook_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playbook_name** | **str**| ID of playbook-name | 
 **playbook** | [**PlaybookSchema**](PlaybookSchema.md)| playbookbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_playbooks_playbooks_by_id**
> update_iceberg_playbooks_playbooks_by_id(playbooks)

Overwrite all playbooks.

Overwrite the existing playbooks configuration. New playbooks are created and existing playbooks are overwritten with new content. If some of the existing playbooks are not present in the payload, such playbooks are deleted. This will fail if any of the playbooks that are not present in the payload are referenced by a device-group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
playbooks = swagger_client.PlaybooksSchema() # PlaybooksSchema | playbooksbody object

try:
    # Overwrite all playbooks.
    api_instance.update_iceberg_playbooks_playbooks_by_id(playbooks)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_iceberg_playbooks_playbooks_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playbooks** | [**PlaybooksSchema**](PlaybooksSchema.md)| playbooksbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_retention_policies_retention_policies_id**
> update_iceberg_retention_policies_retention_policies_id(retention_policies)

Overwrite all retention-policies.

Overwrite the existing retention-policies configuration. New retention-policies are created and existing retention-policies are overwritten with new content. If some existing retention-policies are not present in the payload, such retention-policies are deleted. This will fail if any of the retention-policies that are not present in the payload are referenced by a device-group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
retention_policies = swagger_client.RetentionPoliciesSchema() # RetentionPoliciesSchema | retention-policies body object

try:
    # Overwrite all retention-policies.
    api_instance.update_iceberg_retention_policies_retention_policies_id(retention_policies)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_iceberg_retention_policies_retention_policies_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retention_policies** | [**RetentionPoliciesSchema**](RetentionPoliciesSchema.md)| retention-policies body object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_retention_policy_retention_policy_by_id**
> update_iceberg_retention_policy_retention_policy_by_id(retention_policy_name, retention_policy)

Overwrite a retention-policy.

Overwrite a retention-policy by the `retention-policy-name`. The `retention-policy-name` specified in URL and the request body must match.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
retention_policy_name = 'retention_policy_name_example' # str | ID of retention-policy-name
retention_policy = swagger_client.RetentionPolicySchema() # RetentionPolicySchema | retention_policybody object

try:
    # Overwrite a retention-policy.
    api_instance.update_iceberg_retention_policy_retention_policy_by_id(retention_policy_name, retention_policy)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_iceberg_retention_policy_retention_policy_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retention_policy_name** | **str**| ID of retention-policy-name | 
 **retention_policy** | [**RetentionPolicySchema**](RetentionPolicySchema.md)| retention_policybody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_system_settings_destination_by_id**
> update_iceberg_system_settings_destination_by_id(name, destination)

Update destination by name

Overwrite a destination by destination name. The destination name specified in the URL and the request body must match.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
name = 'name_example' # str | ID of name
destination = swagger_client.DestinationSchema() # DestinationSchema | destinationsbody object

try:
    # Update destination by name
    api_instance.update_iceberg_system_settings_destination_by_id(name, destination)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_iceberg_system_settings_destination_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **destination** | [**DestinationSchema**](DestinationSchema.md)| destinationsbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_system_settings_destinations**
> update_iceberg_system_settings_destinations(destinations)

Update destinations by name

Overwrite the existing configuration of destinations. New destinations are created and the existing destinations are overwritten with new content. If some existing destinations are not present in the payload, such destinations are deleted. This will fail if any of the destinations that are not present in the payload are referenced by a report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
destinations = swagger_client.DestinationsSchema() # DestinationsSchema | destinationsbody object

try:
    # Update destinations by name
    api_instance.update_iceberg_system_settings_destinations(destinations)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_iceberg_system_settings_destinations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destinations** | [**DestinationsSchema**](DestinationsSchema.md)| destinationsbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_system_settings_report_by_id**
> update_iceberg_system_settings_report_by_id(name, report)

Update report by name

Overwrite a report by report name. The report name specified in the URL and the request body must match.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
name = 'name_example' # str | ID of name
report = swagger_client.ReportSchema() # ReportSchema | reportsbody object

try:
    # Update report by name
    api_instance.update_iceberg_system_settings_report_by_id(name, report)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_iceberg_system_settings_report_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **report** | [**ReportSchema**](ReportSchema.md)| reportsbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_system_settings_reports**
> update_iceberg_system_settings_reports(reports)

Update reports by name

Overwrite the existing configuration of reports. New reports are created and the existing reports are overwritten with new content. If some existing reports are not present in the payload, such reports are deleted. This will fail if any of the reports that are not present in the payload are referenced by a device-group or network-group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
reports = swagger_client.ReportsSchema() # ReportsSchema | reportsbody object

try:
    # Update reports by name
    api_instance.update_iceberg_system_settings_reports(reports)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_iceberg_system_settings_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reports** | [**ReportsSchema**](ReportsSchema.md)| reportsbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_system_settings_scheduler_by_id**
> update_iceberg_system_settings_scheduler_by_id(name, scheduler)

Update scheduler by name

Overwrite a scheduler by scheduler name. The scheduler name specified in the URL and the request body must match.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
name = 'name_example' # str | ID of name
scheduler = swagger_client.SchedulerSchema() # SchedulerSchema | schedulerbody object

try:
    # Update scheduler by name
    api_instance.update_iceberg_system_settings_scheduler_by_id(name, scheduler)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_iceberg_system_settings_scheduler_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| ID of name | 
 **scheduler** | [**SchedulerSchema**](SchedulerSchema.md)| schedulerbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_system_settings_schedulers**
> update_iceberg_system_settings_schedulers(schedulers)

Update schedulers by name

Update operation of resource: schedulers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
schedulers = swagger_client.SchedulersSchema() # SchedulersSchema | schedulersbody object

try:
    # Update schedulers by name
    api_instance.update_iceberg_system_settings_schedulers(schedulers)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_iceberg_system_settings_schedulers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedulers** | [**SchedulersSchema**](SchedulersSchema.md)| schedulersbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_system_settings_system_settings_by_id**
> update_iceberg_system_settings_system_settings_by_id(system_settings)

Update system-settings by ID

Overwrite the existing configuration of system-settings. New system-settings are created and existing system-settings are overwritten with new content. If some existing system-settings are not present in the payload, such system-settings are deleted. This will fail if any of the reports in system-settings that are not present in the payload are referenced by a device-group or network-group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
system_settings = swagger_client.SystemSettingsSchema() # SystemSettingsSchema | system_settingsbody object

try:
    # Update system-settings by ID
    api_instance.update_iceberg_system_settings_system_settings_by_id(system_settings)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_iceberg_system_settings_system_settings_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_settings** | [**SystemSettingsSchema**](SystemSettingsSchema.md)| system_settingsbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_topic_rule_rule_by_id**
> update_iceberg_topic_rule_rule_by_id(topic_name, rule_name, rule)

Overwrite a rule.

Overwrite a rule by the `rule-name`. The `rule-name` specified in URL and the request body must match.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
topic_name = 'topic_name_example' # str | ID of topic-name
rule_name = 'rule_name_example' # str | ID of rule-name
rule = swagger_client.RuleSchema() # RuleSchema | rulebody object

try:
    # Overwrite a rule.
    api_instance.update_iceberg_topic_rule_rule_by_id(topic_name, rule_name, rule)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_iceberg_topic_rule_rule_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_name** | **str**| ID of topic-name | 
 **rule_name** | **str**| ID of rule-name | 
 **rule** | [**RuleSchema**](RuleSchema.md)| rulebody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_topic_topic_by_id**
> update_iceberg_topic_topic_by_id(topic_name, topic)

Overwrite a topic.

Overwrite a topic by the `topic-name`. The `topic-name` specified in URL and the request body must match.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
topic_name = 'topic_name_example' # str | ID of topic-name
topic = swagger_client.TopicSchema() # TopicSchema | topicbody object

try:
    # Overwrite a topic.
    api_instance.update_iceberg_topic_topic_by_id(topic_name, topic)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_iceberg_topic_topic_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_name** | **str**| ID of topic-name | 
 **topic** | [**TopicSchema**](TopicSchema.md)| topicbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iceberg_topics_topics_by_id**
> update_iceberg_topics_topics_by_id(topics)

Overwrite topics.

Overwrite the existing topics configuration. New topics are created and existing topics are overwritten with new content. If some existing topics are not present in the payload, such topics are deleted. This will fail if any of the topics that are not present in the payload are referenced by a playbook.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationApi()
topics = swagger_client.TopicsSchema() # TopicsSchema | topicsbody object

try:
    # Overwrite topics.
    api_instance.update_iceberg_topics_topics_by_id(topics)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_iceberg_topics_topics_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topics** | [**TopicsSchema**](TopicsSchema.md)| topicsbody object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

