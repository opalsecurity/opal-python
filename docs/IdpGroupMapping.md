# IdpGroupMapping

Information about a group mapping.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The ID of the group. | 
**alias** | **str** | The alias of the group. | [optional] 
**hidden_from_end_user** | **bool** | A bool representing whether or not the group is hidden from the end user. | 

## Example

```python
from opal_security.models.idp_group_mapping import IdpGroupMapping

# TODO update the JSON string below
json = "{}"
# create an instance of IdpGroupMapping from a JSON string
idp_group_mapping_instance = IdpGroupMapping.from_json(json)
# print the JSON string representation of the object
print(IdpGroupMapping.to_json())

# convert the object into a dict
idp_group_mapping_dict = idp_group_mapping_instance.to_dict()
# create an instance of IdpGroupMapping from a dict
idp_group_mapping_from_dict = IdpGroupMapping.from_dict(idp_group_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


