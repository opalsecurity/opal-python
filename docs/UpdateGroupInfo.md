# UpdateGroupInfo

# UpdateGroupInfo Object ### Description The `UpdateGroupInfo` object is used as an input to the UpdateGroup API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The ID of the group. | 
**name** | **str** | The name of the group. | [optional] 
**description** | **str** | A description of the group. | [optional] 
**admin_owner_id** | **str** | The ID of the owner of the group. | [optional] 
**max_duration** | **int** | The maximum duration for which the group can be requested (in minutes). Use -1 to set to indefinite. Deprecated in favor of &#x60;request_configurations&#x60;. | [optional] 
**recommended_duration** | **int** | The recommended duration for which the group should be requested (in minutes). Will be the default value in a request. Use -1 to set to indefinite and 0 to unset. Deprecated in favor of &#x60;request_configurations&#x60;. | [optional] 
**require_manager_approval** | **bool** | A bool representing whether or not access requests to the group require manager approval. Deprecated in favor of &#x60;request_configurations&#x60;. | [optional] 
**require_support_ticket** | **bool** | A bool representing whether or not access requests to the group require an access ticket. Deprecated in favor of &#x60;request_configurations&#x60;. | [optional] 
**folder_id** | **str** | The ID of the folder that the group is located in. | [optional] 
**require_mfa_to_approve** | **bool** | A bool representing whether or not to require MFA for reviewers to approve requests for this group. | [optional] 
**require_mfa_to_request** | **bool** | A bool representing whether or not to require MFA for requesting access to this group. Deprecated in favor of &#x60;request_configurations&#x60;. | [optional] 
**auto_approval** | **bool** | A bool representing whether or not to automatically approve requests to this group. Deprecated in favor of &#x60;request_configurations&#x60;. | [optional] 
**configuration_template_id** | **str** | The ID of the associated configuration template. | [optional] 
**request_template_id** | **str** | The ID of the associated request template. Deprecated in favor of &#x60;request_configurations&#x60;. | [optional] 
**is_requestable** | **bool** | A bool representing whether or not to allow access requests to this group. Deprecated in favor of &#x60;request_configurations&#x60;. | [optional] 
**group_leader_user_ids** | **List[str]** | A list of User IDs for the group leaders of the group | [optional] 
**request_configurations** | [**List[RequestConfiguration]**](RequestConfiguration.md) | The request configuration list of the configuration template. If not provided, the default request configuration will be used. | [optional] 
**request_configuration_list** | [**CreateRequestConfigurationInfoList**](CreateRequestConfigurationInfoList.md) | The request configuration list of the configuration template. If not provided, the default request configuration will be used. Deprecated in favor of &#x60;request_configurations&#x60;. | [optional] 
**custom_request_notification** | **str** | Custom request notification sent to the requester when the request is approved. | [optional] 
**risk_sensitivity_override** | [**RiskSensitivityEnum**](RiskSensitivityEnum.md) |  | [optional] 

## Example

```python
from opal_security.models.update_group_info import UpdateGroupInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGroupInfo from a JSON string
update_group_info_instance = UpdateGroupInfo.from_json(json)
# print the JSON string representation of the object
print(UpdateGroupInfo.to_json())

# convert the object into a dict
update_group_info_dict = update_group_info_instance.to_dict()
# create an instance of UpdateGroupInfo from a dict
update_group_info_from_dict = UpdateGroupInfo.from_dict(update_group_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


