# EntityNameFilter

Filters entities by name using a string match strategy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**string_match_type** | [**StringMatchType**](StringMatchType.md) |  | 
**string** | **str** | The string value to match against the entity name. | 

## Example

```python
from opal_security.models.entity_name_filter import EntityNameFilter

# TODO update the JSON string below
json = "{}"
# create an instance of EntityNameFilter from a JSON string
entity_name_filter_instance = EntityNameFilter.from_json(json)
# print the JSON string representation of the object
print(EntityNameFilter.to_json())

# convert the object into a dict
entity_name_filter_dict = entity_name_filter_instance.to_dict()
# create an instance of EntityNameFilter from a dict
entity_name_filter_from_dict = EntityNameFilter.from_dict(entity_name_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


