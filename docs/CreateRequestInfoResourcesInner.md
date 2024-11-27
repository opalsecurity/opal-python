# CreateRequestInfoResourcesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the resource requested. Should not be specified if group_id is specified. | [optional] 
**access_level_remote_id** | **str** | The ID of the access level requested on the remote system. | [optional] 
**access_level_name** | **str** | The ID of the access level requested on the remote system. | [optional] 

## Example

```python
from opal_security.models.create_request_info_resources_inner import CreateRequestInfoResourcesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRequestInfoResourcesInner from a JSON string
create_request_info_resources_inner_instance = CreateRequestInfoResourcesInner.from_json(json)
# print the JSON string representation of the object
print(CreateRequestInfoResourcesInner.to_json())

# convert the object into a dict
create_request_info_resources_inner_dict = create_request_info_resources_inner_instance.to_dict()
# create an instance of CreateRequestInfoResourcesInner from a dict
create_request_info_resources_inner_from_dict = CreateRequestInfoResourcesInner.from_dict(create_request_info_resources_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


