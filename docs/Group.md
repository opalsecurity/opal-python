# Group

# Group Object ### Description The `Group` object is used to represent a group.  ### Usage Example Update from the `UPDATE Groups` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The ID of the group. | 
**app_id** | **str** | The ID of the group&#39;s app. | [optional] 
**name** | **str** | The name of the group. | [optional] 
**description** | **str** | A description of the group. | [optional] 
**admin_owner_id** | **str** | The ID of the owner of the group. | [optional] 
**group_leader_user_ids** | **List[str]** | A list of User IDs for the group leaders of the group | [optional] 
**remote_id** | **str** | The ID of the remote. | [optional] 
**remote_name** | **str** | The name of the remote. | [optional] 
**group_type** | [**GroupTypeEnum**](GroupTypeEnum.md) |  | [optional] 
**max_duration** | **int** | The maximum duration for which the group can be requested (in minutes). | [optional] 
**recommended_duration** | **int** | The recommended duration for which the group should be requested (in minutes). -1 represents an indefinite duration. | [optional] 
**require_manager_approval** | **bool** | A bool representing whether or not access requests to the group require manager approval. | [optional] 
**require_support_ticket** | **bool** | A bool representing whether or not access requests to the group require an access ticket. | [optional] 
**require_mfa_to_approve** | **bool** | A bool representing whether or not to require MFA for reviewers to approve requests for this group. | [optional] 
**require_mfa_to_request** | **bool** | A bool representing whether or not to require MFA for requesting access to this group. | [optional] 
**auto_approval** | **bool** | A bool representing whether or not to automatically approve requests to this group. | [optional] 
**request_template_id** | **str** | The ID of the associated request template. | [optional] 
**configuration_template_id** | **str** | The ID of the associated configuration template. | [optional] 
**group_binding_id** | **str** | The ID of the associated group binding. | [optional] 
**is_requestable** | **bool** | A bool representing whether or not to allow access requests to this group. | [optional] 
**request_configurations** | [**List[RequestConfiguration]**](RequestConfiguration.md) | A list of request configurations for this group. | [optional] 
**request_configuration_list** | [**List[RequestConfiguration]**](RequestConfiguration.md) | A list of request configurations for this group. Deprecated in favor of &#x60;request_configurations&#x60;. | [optional] 
**metadata** | **str** | JSON metadata about the remote group. Only set for items linked to remote systems. See [this guide](https://docs.opal.dev/reference/end-system-objects) for details. | [optional] 
**remote_info** | [**GroupRemoteInfo**](GroupRemoteInfo.md) |  | [optional] 
**custom_request_notification** | **str** | Custom request notification sent to the requester when the request is approved. | [optional] 
**risk_sensitivity** | [**RiskSensitivityEnum**](RiskSensitivityEnum.md) | The risk sensitivity level for the group. When an override is set, this field will match that. | [optional] [readonly] 
**risk_sensitivity_override** | [**RiskSensitivityEnum**](RiskSensitivityEnum.md) |  | [optional] 

## Example

```python
from opal_security.models.group import Group

# TODO update the JSON string below
json = "{}"
# create an instance of Group from a JSON string
group_instance = Group.from_json(json)
# print the JSON string representation of the object
print(Group.to_json())

# convert the object into a dict
group_dict = group_instance.to_dict()
# create an instance of Group from a dict
group_from_dict = Group.from_dict(group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


