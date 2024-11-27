# Resource

# Resource Object ### Description The `Resource` object is used to represent a resource.  ### Usage Example Update from the `UPDATE Resources` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The ID of the resource. | 
**app_id** | **str** | The ID of the app. | [optional] 
**name** | **str** | The name of the resource. | [optional] 
**description** | **str** | A description of the resource. | [optional] 
**admin_owner_id** | **str** | The ID of the owner of the resource. | [optional] 
**remote_resource_id** | **str** | The ID of the resource on the remote system. | [optional] 
**remote_resource_name** | **str** | The name of the resource on the remote system. | [optional] 
**resource_type** | [**ResourceTypeEnum**](ResourceTypeEnum.md) |  | [optional] 
**max_duration** | **int** | The maximum duration for which the resource can be requested (in minutes). | [optional] 
**recommended_duration** | **int** | The recommended duration for which the resource should be requested (in minutes). -1 represents an indefinite duration. | [optional] 
**require_manager_approval** | **bool** | A bool representing whether or not access requests to the resource require manager approval. | [optional] 
**require_support_ticket** | **bool** | A bool representing whether or not access requests to the resource require an access ticket. | [optional] 
**require_mfa_to_approve** | **bool** | A bool representing whether or not to require MFA for reviewers to approve requests for this resource. | [optional] 
**require_mfa_to_request** | **bool** | A bool representing whether or not to require MFA for requesting access to this resource. | [optional] 
**require_mfa_to_connect** | **bool** | A bool representing whether or not to require MFA to connect to this resource. | [optional] 
**auto_approval** | **bool** | A bool representing whether or not to automatically approve requests to this resource. | [optional] 
**request_template_id** | **str** | The ID of the associated request template. | [optional] 
**is_requestable** | **bool** | A bool representing whether or not to allow access requests to this resource. | [optional] 
**parent_resource_id** | **str** | The ID of the parent resource. | [optional] 
**configuration_template_id** | **str** | The ID of the associated configuration template. | [optional] 
**request_configurations** | [**List[RequestConfiguration]**](RequestConfiguration.md) | A list of configurations for requests to this resource. | [optional] 
**request_configuration_list** | [**List[RequestConfiguration]**](RequestConfiguration.md) | A list of configurations for requests to this resource. Deprecated in favor of &#x60;request_configurations&#x60;. | [optional] 
**ticket_propagation** | [**TicketPropagationConfiguration**](TicketPropagationConfiguration.md) |  | [optional] 
**custom_request_notification** | **str** | Custom request notification sent upon request approval. | [optional] 
**risk_sensitivity** | [**RiskSensitivityEnum**](RiskSensitivityEnum.md) | The risk sensitivity level for the resource. When an override is set, this field will match that. | [optional] [readonly] 
**risk_sensitivity_override** | [**RiskSensitivityEnum**](RiskSensitivityEnum.md) |  | [optional] 
**metadata** | **str** | JSON metadata about the remote resource. Only set for items linked to remote systems. See [this guide](https://docs.opal.dev/reference/end-system-objects) for details. | [optional] 
**remote_info** | [**ResourceRemoteInfo**](ResourceRemoteInfo.md) |  | [optional] 

## Example

```python
from opal_security.models.resource import Resource

# TODO update the JSON string below
json = "{}"
# create an instance of Resource from a JSON string
resource_instance = Resource.from_json(json)
# print the JSON string representation of the object
print(Resource.to_json())

# convert the object into a dict
resource_dict = resource_instance.to_dict()
# create an instance of Resource from a dict
resource_from_dict = Resource.from_dict(resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


