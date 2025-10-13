# CreateIdpGroupMappingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | Optional alias for the group mapping | [optional] 
**hidden_from_end_user** | **bool** | Whether this mapping should be hidden from end users. - **New mappings**: If not provided, defaults to &#x60;false&#x60; - **Existing mappings**: If not provided, existing value is preserved (no change) - **Explicit values**: If provided, value is updated to the specified boolean  | [optional] 

## Example

```python
from opal_security.models.create_idp_group_mapping_request import CreateIdpGroupMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIdpGroupMappingRequest from a JSON string
create_idp_group_mapping_request_instance = CreateIdpGroupMappingRequest.from_json(json)
# print the JSON string representation of the object
print(CreateIdpGroupMappingRequest.to_json())

# convert the object into a dict
create_idp_group_mapping_request_dict = create_idp_group_mapping_request_instance.to_dict()
# create an instance of CreateIdpGroupMappingRequest from a dict
create_idp_group_mapping_request_from_dict = CreateIdpGroupMappingRequest.from_dict(create_idp_group_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


