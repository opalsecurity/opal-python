# UpdateIdpGroupMappingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mappings** | [**List[UpdateIdpGroupMappingsRequestMappingsInner]**](UpdateIdpGroupMappingsRequestMappingsInner.md) |  | 

## Example

```python
from opal_security.models.update_idp_group_mappings_request import UpdateIdpGroupMappingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIdpGroupMappingsRequest from a JSON string
update_idp_group_mappings_request_instance = UpdateIdpGroupMappingsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateIdpGroupMappingsRequest.to_json())

# convert the object into a dict
update_idp_group_mappings_request_dict = update_idp_group_mappings_request_instance.to_dict()
# create an instance of UpdateIdpGroupMappingsRequest from a dict
update_idp_group_mappings_request_from_dict = UpdateIdpGroupMappingsRequest.from_dict(update_idp_group_mappings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


