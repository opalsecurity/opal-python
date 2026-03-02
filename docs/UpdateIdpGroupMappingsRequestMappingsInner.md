# UpdateIdpGroupMappingsRequestMappingsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** |  | [optional] 
**alias** | **str** |  | [optional] 
**hidden_from_end_user** | **bool** |  | [optional] 

## Example

```python
from opal_security.models.update_idp_group_mappings_request_mappings_inner import UpdateIdpGroupMappingsRequestMappingsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIdpGroupMappingsRequestMappingsInner from a JSON string
update_idp_group_mappings_request_mappings_inner_instance = UpdateIdpGroupMappingsRequestMappingsInner.from_json(json)
# print the JSON string representation of the object
print(UpdateIdpGroupMappingsRequestMappingsInner.to_json())

# convert the object into a dict
update_idp_group_mappings_request_mappings_inner_dict = update_idp_group_mappings_request_mappings_inner_instance.to_dict()
# create an instance of UpdateIdpGroupMappingsRequestMappingsInner from a dict
update_idp_group_mappings_request_mappings_inner_from_dict = UpdateIdpGroupMappingsRequestMappingsInner.from_dict(update_idp_group_mappings_request_mappings_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


