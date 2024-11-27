# UpdateResourceInfo

# UpdateResourceInfo Object ### Description The `UpdateResourceInfo` object is used as an input to the UpdateResource API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The ID of the resource. | 
**name** | **str** | The name of the resource. | [optional] 
**description** | **str** | A description of the resource. | [optional] 
**admin_owner_id** | **str** | The ID of the owner of the resource. | [optional] 
**max_duration** | **int** | The maximum duration for which the resource can be requested (in minutes). Use -1 to set to indefinite. Deprecated in favor of &#x60;request_configurations&#x60;. | [optional] 
**recommended_duration** | **int** | The recommended duration for which the resource should be requested (in minutes). Will be the default value in a request. Use -1 to set to indefinite and 0 to unset. Deprecated in favor of &#x60;request_configurations&#x60;. | [optional] 
**require_manager_approval** | **bool** | A bool representing whether or not access requests to the resource require manager approval. | [optional] 
**require_support_ticket** | **bool** | A bool representing whether or not access requests to the resource require an access ticket. Deprecated in favor of &#x60;request_configurations&#x60;. | [optional] 
**folder_id** | **str** | The ID of the folder that the resource is located in. | [optional] 
**require_mfa_to_approve** | **bool** | A bool representing whether or not to require MFA for reviewers to approve requests for this resource. | [optional] 
**require_mfa_to_request** | **bool** | A bool representing whether or not to require MFA for requesting access to this resource. Deprecated in favor of &#x60;request_configurations&#x60;. | [optional] 
**require_mfa_to_connect** | **bool** | A bool representing whether or not to require MFA to connect to this resource. | [optional] 
**auto_approval** | **bool** | A bool representing whether or not to automatically approve requests to this resource. Deprecated in favor of &#x60;request_configurations&#x60;. | [optional] 
**ticket_propagation** | [**TicketPropagationConfiguration**](TicketPropagationConfiguration.md) |  | [optional] 
**custom_request_notification** | **str** | Custom request notification sent upon request approval. | [optional] 
**risk_sensitivity_override** | [**RiskSensitivityEnum**](RiskSensitivityEnum.md) |  | [optional] 
**configuration_template_id** | **str** | The ID of the associated configuration template. | [optional] 
**request_template_id** | **str** | The ID of the associated request template. Deprecated in favor of &#x60;request_configurations&#x60;. | [optional] 
**is_requestable** | **bool** | A bool representing whether or not to allow access requests to this resource. Deprecated in favor of &#x60;request_configurations&#x60;. | [optional] 
**request_configurations** | [**List[RequestConfiguration]**](RequestConfiguration.md) | A list of configurations for requests to this resource. If not provided, the default request configuration will be used. | [optional] 
**request_configuration_list** | [**CreateRequestConfigurationInfoList**](CreateRequestConfigurationInfoList.md) | A list of configurations for requests to this resource. If not provided, the default request configuration will be used. Deprecated in favor of &#x60;request_configurations&#x60;. | [optional] 

## Example

```python
from opal_security.models.update_resource_info import UpdateResourceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateResourceInfo from a JSON string
update_resource_info_instance = UpdateResourceInfo.from_json(json)
# print the JSON string representation of the object
print(UpdateResourceInfo.to_json())

# convert the object into a dict
update_resource_info_dict = update_resource_info_instance.to_dict()
# create an instance of UpdateResourceInfo from a dict
update_resource_info_from_dict = UpdateResourceInfo.from_dict(update_resource_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


