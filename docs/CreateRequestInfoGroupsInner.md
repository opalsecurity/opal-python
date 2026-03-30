# CreateRequestInfoGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the group requested. Should not be specified if resource_id is specified. | 
**access_level_remote_id** | **str** | The ID of the access level requested on the remote system. | [optional] 
**access_level_name** | **str** | The ID of the access level requested on the remote system. | [optional] 

## Example

```python
from opal_security.models.create_request_info_groups_inner import CreateRequestInfoGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRequestInfoGroupsInner from a JSON string
create_request_info_groups_inner_instance = CreateRequestInfoGroupsInner.from_json(json)
# print the JSON string representation of the object
print(CreateRequestInfoGroupsInner.to_json())

# convert the object into a dict
create_request_info_groups_inner_dict = create_request_info_groups_inner_instance.to_dict()
# create an instance of CreateRequestInfoGroupsInner from a dict
create_request_info_groups_inner_from_dict = CreateRequestInfoGroupsInner.from_dict(create_request_info_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


