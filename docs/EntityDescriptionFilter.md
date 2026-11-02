# EntityDescriptionFilter

Filters GROUP and RESOURCE entities by a case-insensitive substring of their description (\"contains\"). USER entities have no description and never match, in either polarity. `not` inverts the match within the resource/group domain (\"does NOT contain\"), so it still returns only resources/groups rather than sweeping in users. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**string** | **str** | The substring to match against the entity description. | 
**var_not** | **bool** | Invert the match — return resources/groups whose description does NOT contain the substring. | [optional] 

## Example

```python
from opal_security.models.entity_description_filter import EntityDescriptionFilter

# TODO update the JSON string below
json = "{}"
# create an instance of EntityDescriptionFilter from a JSON string
entity_description_filter_instance = EntityDescriptionFilter.from_json(json)
# print the JSON string representation of the object
print(EntityDescriptionFilter.to_json())

# convert the object into a dict
entity_description_filter_dict = entity_description_filter_instance.to_dict()
# create an instance of EntityDescriptionFilter from a dict
entity_description_filter_from_dict = EntityDescriptionFilter.from_dict(entity_description_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


