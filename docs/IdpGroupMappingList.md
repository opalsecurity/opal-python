# IdpGroupMappingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mappings** | [**List[IdpGroupMapping]**](IdpGroupMapping.md) |  | 

## Example

```python
from opal_security.models.idp_group_mapping_list import IdpGroupMappingList

# TODO update the JSON string below
json = "{}"
# create an instance of IdpGroupMappingList from a JSON string
idp_group_mapping_list_instance = IdpGroupMappingList.from_json(json)
# print the JSON string representation of the object
print(IdpGroupMappingList.to_json())

# convert the object into a dict
idp_group_mapping_list_dict = idp_group_mapping_list_instance.to_dict()
# create an instance of IdpGroupMappingList from a dict
idp_group_mapping_list_from_dict = IdpGroupMappingList.from_dict(idp_group_mapping_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


