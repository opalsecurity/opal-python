# TagSelector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**value** | **str** |  | 
**connection_id** | **str** |  | 

## Example

```python
from opal_security.models.tag_selector import TagSelector

# TODO update the JSON string below
json = "{}"
# create an instance of TagSelector from a JSON string
tag_selector_instance = TagSelector.from_json(json)
# print the JSON string representation of the object
print(TagSelector.to_json())

# convert the object into a dict
tag_selector_dict = tag_selector_instance.to_dict()
# create an instance of TagSelector from a dict
tag_selector_from_dict = TagSelector.from_dict(tag_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


