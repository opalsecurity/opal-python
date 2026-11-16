# CreateRequestInfo

All the information needed for creating a request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | [**List[CreateRequestInfoResourcesInner]**](CreateRequestInfoResourcesInner.md) |  | 
**groups** | [**List[CreateRequestInfoGroupsInner]**](CreateRequestInfoGroupsInner.md) |  | 
**target_user_id** | **UUID** | The ID of the user to be granted access. Should not be specified if target_group_id is specified. | [optional] 
**target_group_id** | **UUID** | The ID of the group the request is for.  Should not be specified if target_user_id is specified. | [optional] 
**initiated_by_user_id** | **UUID** | The ID of the user who asked for this access, for callers filing a request on someone else&#39;s behalf. Opal records this claim as given and does not verify it, so it never affects authorization, reviewer routing, or who may cancel the request; the authenticated caller remains the requester. Must be a user of your organization. Only accepted from a service user for which an Opal admin has enabled \&quot;Let this service user record who asked for access\&quot; under Settings on the service user&#39;s page; any other caller receives a 403 when this field is set. | [optional] 
**reason** | **str** |  | 
**support_ticket** | [**CreateRequestInfoSupportTicket**](CreateRequestInfoSupportTicket.md) |  | [optional] 
**duration_minutes** | **int** | The duration of the request in minutes. -1 represents an indefinite duration | 
**custom_metadata** | [**List[CreateRequestInfoCustomMetadataInner]**](CreateRequestInfoCustomMetadataInner.md) |  | [optional] 

## Example

```python
from opal_security.models.create_request_info import CreateRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRequestInfo from a JSON string
create_request_info_instance = CreateRequestInfo.from_json(json)
# print the JSON string representation of the object
print(CreateRequestInfo.to_json())

# convert the object into a dict
create_request_info_dict = create_request_info_instance.to_dict()
# create an instance of CreateRequestInfo from a dict
create_request_info_from_dict = CreateRequestInfo.from_dict(create_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


